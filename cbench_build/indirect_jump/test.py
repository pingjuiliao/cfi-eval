#!/usr/bin/env python3

import os
from pwn import *

arg_test_overwrite = [
    b"SameTypeFunc",
    b"DiffRetFunc",
    b"DiffArgFunc",
    b"MoreArgFunc",
    b"LessArgFunc",
    b"VoidArgFunc",
    b"not_entry"
]
bin_test_overwrite = os.path.dirname(__file__) + "/tailcall_overwrite"

def test_overwrite(func_name):
    r = process(bin_test_overwrite)

    r.recvuntil(func_name)
    leak = r.recvline()
    hijack_address = int(str(leak).strip(), 16)
    payload =

    r.sendlineafter(b"plz input your name length:\n", b"-1")
    r.sendlineafter(b"plz input your name:\n", payload)
    response = r.recvrepeat(1)
    r.close()

    res_msg = f"Testing hijack to {hijack_func_name.decode():14s}...: "
    if hijack_func_name in response:
        res_msg += "hijack succeeded: X"
    elif b"In Foo" in response:
        res_msg += "CFI protected   : V"
    else:
        res_msg += "program crashed : X"
    return res_msg


arg_test_reuse_single_phread = [(1, b"SameTypeFunc1"),
                    (2, b"DiffArgFunc1"),
                    (3, b"DiffRetFunc1"),
                    (4, b"MoreArgFunc1"),
                    (5, b"LessArgFunc1"),
                    (6, b"VoidArgFunc1"),
                    (7, b"Bar"),
                    (8, b"SameTypeFunc2"),
                    (9, b"DiffArgFunc2"),
                    (10, b"DiffRetFunc2"),
                    (11, b"MoreArgFunc2"),
                    (12, b"LessArgFunc2"),
                    (13, b"VoidArgFunc2"),
]

bin_test_reuse_single_phread = os.path.dirname(__file__) + "/tailcall_reuse_single_phread"

def test_reuse_single_phread(func_tuple):
    func_index, hijack_func_name = func_tuple
    r = process([bin_test_reuse_single_phread, str(func_index)])
    response = r.recvrepeat(.5)
    r.close()

    res_msg = f"Testing hijack to {hijack_func_name.decode():14s}...: "
    if hijack_func_name in response:
        res_msg += "hijack succeeded: X"
    else:
        res_msg += "CFI protected   : V"
    return res_msg

arg_test_reuse_multithreading = [
                    (1, b"SameTypeFunc1"),
                    (2, b"DiffArgFunc1"),
                    (3, b"DiffRetFunc1"),
                    (4, b"MoreArgFunc1"),
                    (5, b"LessArgFunc1"),
                    (6, b"VoidArgFunc1"),
                    (7, b"Bar"),
                    (8, b"SameTypeFunc2"),
                    (9, b"DiffArgFunc2"),
                    (10, b"DiffRetFunc2"),
                    (11, b"MoreArgFunc2"),
                    (12, b"LessArgFunc2"),
                    (13, b"VoidArgFunc2"),
]

bin_test_reuse_multithreading = os.path.dirname(__file__) + "/tailcall_reuse_multithreading"

def test_reuse_multithreading(func_tuple):
    func_index, hijack_func_name = func_tuple

    r = process(bin_test_reuse_multithreading)
    r.sendlineafter(b"plz input index:",
                    str(func_index).encode())
    r.recvuntil(b"In ", timeout=10)
    response = r.recvline()
    r.close()

    res_msg = f"Testing hijack to {hijack_func_name.decode():14s}...: "
    if hijack_func_name in response:
        res_msg += "hijack succeeded: X"
    else:
        res_msg += "CFI protected:    V"
    return res_msg

def benchmarking(verbose=False):
    results = []
    banner = """
    ###########################
    ### Indirect Call testsuite
    ######################\n
    """
    results.append(banner)

    results.append("###########\n # Testing tailcall_overwrite\n###\n")
    for arg in arg_test_overwrite:
        r = test_overwrite(arg)
        results.append(r)

    results.appned("\n")
    results.append("###########\n # Testing tailcall_reuse_single_phread\n###\n")
    for arg in arg_test_reuse_single_phread:
        r = test_reuse_single_phread(arg)
        results.append(r)

    results.append("\n")
    results.append("###########\n # Testing tailcall_reuse_multithreading\n###\n")
    for arg in arg_test_reuse_multithreading:
        r = test_reuse_multithreading(arg)
        results.append(r)

    if not verbose:
        return

    for result in results:
        print(result)

if __name__ == "__main__":
    benchmarking(True)
