#!/usr/bin/env python3
import os
from pwn import *

bin_cfi_function = os.path.dirname(__file__) + "/cfi_function"

def test_cfi_function():
    p = process(bin_cfi_function)
    response = p.recvrepeat(1)
    p.close()
    if b"=" in response and b"the number is" in response:
        return "Confusion     compatible: Secure X, Compatiblity V"
    return "Does not allow confusion: Secure V, Compatibility X"

bin_cfi_object = os.path.dirname(__file__) + "/cfi_object"

def test_cfi_object():
    p = process(bin_cfi_object)
    response = p.recvrepeat(1)
    p.close()
    if b"I will execute the \"/bin/sh\" command" in response:
        return "Confusion     compatible: Secure X, Compatiblity V"
    return "Does not allow confusion: Secure V, Compatibility X"

bin_cfi_object_function = os.path.dirname(__file__) + "/cfi_object_function"

def test_cfi_object_function():
    p = process(bin_cfi_object_function)
    response = p.recvrepeat(1)
    p.close()
    if b"I am admin" in response:
        return "Confusion     compatible: Secure X, Compatiblity V"
    return "Does not allow confusion: Secure V, Compatibility X"

def benchmarking(verbose=False):
    results = []
    banner = """
    \n###########################\n### type confuse testsuite\n#####################\n
    """
    results.append(banner)

    results.append("###########\n # Testing cfi_function\n###\n")
    results.append(test_cfi_function())

    results.append("\n")
    results.append("###########\n # Testing cfi_object\n###\n")
    results.append(test_cfi_object())

    results.append("\n")
    results.append("###########\n # Testing cfi_object_function\n###\n")
    results.append(test_cfi_object_function())

    if not verbose:
        return

    for result in results:
        print(result)

if __name__ == "__main__":
    benchmarking(True)
