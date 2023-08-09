#!/usr/bin/env python3

import os
from pwn import *

arg_test_ptr_OOB = [(1, b"SameTypeFunc1"),
                    (2, b"DiffArgFunc1"),
                    (3, b"DiffRetFunc1"),
                    (4, b"MoreArgFunc1"),
                    (5, b"LessArgFunc1"),
                    (6, b"VoidArgFunc1"),
                    ]
bin_test_ptr_OOB = os.path.dirname(__file__) + "/ptr_OOB"
def test_ptr_OOB(func_tuple):
    func_index, hijack_func_name = func_tuple
    r = process([bin_test_ptr_OOB, str(func_index)])
    response = r.recvrepeat(.5)
    r.close()

    res_msg = f"Testing hijack to {hijack_func_name.decode():14s}...: "
    if hijack_func_name in response:
        res_msg += "hijack succeeded: X"
    else:
        res_msg += "CFI protected   : V"
    return res_msg


arg_test_ptr_overwrite = [b"SameTypeFunc",
                          b"DiffRetFunc",
                          b"DiffArgFunc",
                          b"MoreArgFunc",
                          b"LessArgFunc",
                          b"VoidArgFunc",
                          b"not_entry"]
bin_test_ptr_overwrite = os.path.dirname(__file__) + "/ptr_overwrite"
def test_ptr_overwrite(test_func):

    def get_hijack_address(func_name: bytes, r):
        r.recvuntil(func_name + b": ")
        leak = r.recvline()
        print(leak)
        return int(leak.decode().strip(), 16)

    r = process(bin_test_ptr_overwrite)
    func_addr = get_hijack_address(test_func, r)
    vul_addr=b'a'*8 + p64(func_addr)
    r.recvuntil(b"plz input your name:\n")
    r.sendline(vul_addr)
    response = r.recvrepeat(1)
    r.close()

    res_msg = f"Testing hijack to {test_func.decode():14s}...: "
    if test_func in response:
        res_msg += "hijack succeeds : X"
    elif b"In Foo" in response:
        res_msg += "CFI Protected   : V"
    else:
        res_msg += "program crashed : X"
    return res_msg

def benchmarking(verbose=False):
    results = []
    banner = """
    ###########################
    ### Indirect Call testsuite
    ######################\n
    """
    results.append(banner)

    results.append("###########\n # Testing ptr_OOB\n###\n")
    for arg in arg_test_ptr_OOB:
        r = test_ptr_OOB(arg)
        results.append(r)

    results.append("###########\n # Testing ptr_overwite\n###\n")
    for arg in arg_test_ptr_overwrite:
        r = test_ptr_overwrite(arg)
        results.append(r)

    if not verbose:
        return

    for result in results:
        print(result)

if __name__ == "__main__":
    benchmarking(True)
