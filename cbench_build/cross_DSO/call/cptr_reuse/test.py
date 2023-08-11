#!/usr/bin/env python3

import os
from pwn import *
arg_cptr_reuse = [
    (1, b"SameTypeFunc"),
    (2, b"DiffArgFunc"),
    (3, b"DiffRetFunc"),
    (4, b"MoreArgFunc"),
    (5, b"LessArgFunc"),
    (6, b"VoidArgFunc"),
]

bin_cptr_reuse = os.path.dirname(__file__) + "/cptr_reuse"

def test_cptr_reuse(func_tuple):
    func_index, hijack_func_name = func_tuple

    p = process([bin_cptr_reuse, str(func_index)])
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
    results.append("###########\n # Testing cptr_reuse\n###\n")
    for arg in arg_cptr_reuse:
        r = test_cptr_reuse(arg)
        results.append(r)

    if not verbose:
        return

    for result in results:
        print(result)

if __name__ == "__main__":
    benchmarking(True)
