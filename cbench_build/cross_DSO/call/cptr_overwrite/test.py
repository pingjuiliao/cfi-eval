#!/usr/bin/env python3

import os
from pwn import *
arg_cptr_overwrite = [
    b"SameTypeFunc",
    b"DiffRetFunc",
    b"DiffArgFunc",
    b"MoreArgFunc",
    b"LessArgFunc",
    b"VoidArgFunc",
    b"Not Entry"
]

bin_cptr_overwrite = os.path.dirname(__file__) + "/cptr_overwrite"

def test_cptr_overwrite(hijack_func_name):

    p = process(bin_cptr_overwrite)

    p.recvuntil(b"ptr address is:")
    leak_stack = p.recvline()
    stack_address = int(leak_stack.decode().strip(), 16)

    p.recvuntil(hijack_func_name + b": ")
    leak_func = p.recvline()
    hijack_address = int(leak_func.decode().strip(), 16)


    p.sendlineafter(b"plz input the value of anyptr:",
                    hex(stack_address).encode())

    p.sendlineafter(b"plz change the value of *anyptr:",
                    hex(hijack_address).encode())

    response = p.recvrepeat(1)
    p.close()

    res_msg = f"Testing hijack to {hijack_func_name.decode():14s}...: "
    if hijack_func_name in response:
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
    results.append("###########\n # Testing ptr_overwite\n###\n")
    for arg in arg_cptr_overwrite:
        r = test_cptr_overwrite(arg)
        results.append(r)

    if not verbose:
        return

    for result in results:
        print(result)

if __name__ == "__main__":
    benchmarking(True)
