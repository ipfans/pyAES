#!/usr/bin/env python
# -*- coding: utf-8 -*-

#!/usr/bin/env python
"""
Simple benchmark for pyaes

Run with no arguments to do quick benchmark or --all to test everything.

For best effect, run with 'sudo nice -n-19 python ./bench.py'
"""

import sys
import os
import time

# Some magic to locate the 'pyaes' module relative to tests
path = os.path.dirname(__file__)
if path == '.' or not path:
    path = os.getcwd()
sys.path.append(os.path.dirname(path))

import pyaes

cleartext = "This is a test. What could possibly go wrong? " * 50 + '\0' * 4

keys = (
    ('128', bytes.fromhex('3afca8488ce0d5136aba87953fbd986e')),
    ('192', bytes.fromhex('35f8b4f0edcee9999d6cc995409e1d506fa8e269c2b795e6')),
    ('256', bytes.fromhex('e6cb51df8394cd2c78055c92a55fdb44202034fdabd765feeb12b7ad61554972')),
)
texts = (
    # 500 x 52 x 4 bytes = 104000
    ('short', 500, "This is a short test. What could possibly go wrong? " * 4),
    # 1 x 69 x 1536 bytes = 105984
    ('long', 1, "This is a very long test. What could possibly go wrong? More text... " * 1536),
)
modes = (
    ('CBC', pyaes.MODE_CBC),
    ('ECB', pyaes.MODE_ECB),
)
funcs = ('encrypt', 'decrypt')

iv = bytes.fromhex('b9de523d1e1588bf46f9084cb796684f')


def benchmark(key, mode, runs, func, text):
    # IV is ignored for ECB mode
    aes = pyaes.new(key, mode, IV=iv)

    f = getattr(aes, func)
    for i in range(runs):
        f(text)


def run(key, mode, runs, func, text):
    t0 = time.time()
    benchmark(key, mode, runs, func, text)
    dur = time.time() - t0

    bytes = len(text) * runs
    cpb = (3000000000 / (bytes / dur))
    kbs = ((bytes / dur) / 1024)
    return '%0.4f  %0.0f cpb %0.1f kB/s' % (dur, cpb, kbs)


def alltests():
    for modedesc, mode in modes:
        for textdesc, runs, text in texts:
            for keydesc, key in keys:
                for func in funcs:
                    result = run(key, mode, runs, func, text)
                    print ('AES-%s-%s %5s %s: %s' % (
                        modedesc,
                        keydesc,
                        textdesc,
                        func,
                        result
                    ))


def quicktest():
    # AES-CBC-128  long encrypt
    modedesc, mode = modes[0]
    keydesc, key = keys[0]
    textdesc, runs, text = texts[1]
    func = 'encrypt'

    #runs *= 2

    result = run(key, mode, runs, func, text)
    print ('AES-%s-%s %5s %s: %s' % (modedesc, keydesc, textdesc, func, result))

    # AES-CBC-256  long encrypt
    keydesc, key = keys[2]

    result = run(key, mode, runs, func, text)
    print ('AES-%s-%s %5s %s: %s' % (modedesc, keydesc, textdesc, func, result))


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--all':
        alltests()
    else:
        quicktest()
