#!/usr/bin/env python3

import os
from pwn import *

arg_obj_inject = []
bin_obj_inject = os.path.dirname(__file__) + "/obj_inject"

def test_obj_inject():

    p = process(bin_obj_inject)


    p.recvuntil(b"the victim object: ")
    leak = p.recvline()
    victim_obj = int(leak.decode().strip(), 16)
    p.recvuntil(b"the sprayed fake vtable is:")
    leak = p.recvline()
    fake_vtable = int(leak.decode().strip(), 16)

    # navigate
    user_a_name = b"1"
    p.sendlineafter(b"Admin registration", b"0")
    p.sendlineafter(b"UserA registration", user_a_name)
    p.sendlineafter(b"UserB registration", b"2")

    # admin secret
    p.sendlineafter(b"Rename admin:", b"Bob\x00")

    # arbitrary write
    p.sendlineafter(b" ptr:", hex(victim_obj).encode())
    p.sendlineafter(b"*ptr:", hex(fake_vtable).encode())
    response = p.recvrepeat(1)
    p.close()

    res_msg = "Testing hijack to getshell with fake vtable: "
    if b"you get shell!!" in response:
        res_msg = "hijack succeeds : X"
    elif b"Hi,I am " + user_a_name in response:
        res_msg = "CFI protected   : V"
    else:
        res_msg = "Jmp to elsewhere: X"
    return res_msg

def benchmarking(verbose=False):
    results = []
    banner = """
    \n###########################\n### Callback-object injection testsuite\n######################\n
    """
    results.append(banner)
    results.append("###########\n # Testing obj_inject\n###\n")
    r = test_obj_inject()
    results.append(r)

    if not verbose:
        return

    for result in results:
        print(result)

if __name__ == "__main__":
    benchmarking(True)
