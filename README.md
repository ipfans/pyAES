pyAES
=====

AES algorithm with pure python implementation. Small modify based on [https://bitbucket.org/intgr/pyaes/](https://bitbucket.org/intgr/pyaes/) to compatible with PEP-8.

Intro
---
an implementation of AES (Advanced Encryption Standard) cipher in pure Python, including ECB & CBC modes.

* __easy to use__: it has a simple PEP 272 cipher API, like PyCrypto
* __not too slow__: it's as fast as Python permits without obfuscating the code
* __well-tested__: it includes a test runner to check the operation against NIST published test vectors
* __raw cipher only__: it does not do padding/verification/key derivation -- any secure crypto protocol should
* __liberal__: Licensed under the permissive MIT license

How to use?
---

```
>>> import pyaes
>>> cryptor = pyaes.new('secret_secretkey', pyaes.MODE_CBC, IV='_some_random_iv_')
>>> ciphertext = cryptor.encrypt('This is a test! What could possibly go wrong?___')
>>> ciphertext
'S8\n\x81\xee3\x86\xd6\t\xf8\xc6\xde~\xdc\x14H#\xd2\xe1\xda\xd79\x81\xb7'
'>\xdd\xed\xaa\xed\xcfp\xee\xc6\x8f(\xdc\xb1A"\xe9[\x9f{\x8e\xa6F\xfbQ'
>>> decryptor = pyaes.new('secret_secretkey', pyaes.MODE_CBC, IV='_some_random_iv_')
>>> decryptor.decrypt(ciphertext)
'This is a test! What could possibly go wrong?___'
```
Speed
---
Even though pyaes is an optimized Python implementation, Python itself is still slow. It should be capable of around 80 kB/s on modern hardware; __that's 1000x slower than pure C implementations__.

This is a test in My Macbook Air(CPython and PyPy):

```
$ python bench.py --all
AES-CBC-128 short encrypt: 2.3228  67004 cpb 43.7 kB/s
AES-CBC-128 short decrypt: 2.4256  69969 cpb 41.9 kB/s
AES-CBC-192 short encrypt: 2.7715  79947 cpb 36.6 kB/s
AES-CBC-192 short decrypt: 2.8919  83419 cpb 35.1 kB/s
AES-CBC-256 short encrypt: 3.2400  93462 cpb 31.3 kB/s
AES-CBC-256 short decrypt: 3.3679  97151 cpb 30.2 kB/s
AES-CBC-128  long encrypt: 2.3564  66700 cpb 43.9 kB/s
AES-CBC-128  long decrypt: 2.4683  69869 cpb 41.9 kB/s
AES-CBC-192  long encrypt: 2.8118  79591 cpb 36.8 kB/s
AES-CBC-192  long decrypt: 2.9336  83038 cpb 35.3 kB/s
AES-CBC-256  long encrypt: 3.3641  95226 cpb 30.8 kB/s
AES-CBC-256  long decrypt: 3.4369  97286 cpb 30.1 kB/s
AES-ECB-128 short encrypt: 2.3100  66634 cpb 44.0 kB/s
AES-ECB-128 short decrypt: 2.4134  69618 cpb 42.1 kB/s
AES-ECB-192 short encrypt: 2.8941  83483 cpb 35.1 kB/s
AES-ECB-192 short decrypt: 2.9094  83926 cpb 34.9 kB/s
AES-ECB-256 short encrypt: 3.2390  93432 cpb 31.4 kB/s
AES-ECB-256 short decrypt: 3.3983  98029 cpb 29.9 kB/s
AES-ECB-128  long encrypt: 2.4414  69107 cpb 42.4 kB/s
AES-ECB-128  long decrypt: 2.5723  72811 cpb 40.2 kB/s
AES-ECB-192  long encrypt: 2.9348  83073 cpb 35.3 kB/s
AES-ECB-192  long decrypt: 3.1270  88512 cpb 33.1 kB/s
AES-ECB-256  long encrypt: 3.7037  104839 cpb 27.9 kB/s
AES-ECB-256  long decrypt: 6.5956  186695 cpb 15.7 kB/s

$ pypy bench.py --all
AES-CBC-128 short encrypt: 0.3558  10263 cpb 285.5 kB/s
AES-CBC-128 short decrypt: 0.4569  13179 cpb 222.3 kB/s
AES-CBC-192 short encrypt: 0.2565  7400 cpb 395.9 kB/s
AES-CBC-192 short decrypt: 0.2916  8411 cpb 348.3 kB/s
AES-CBC-256 short encrypt: 0.2569  7410 cpb 395.4 kB/s
AES-CBC-256 short decrypt: 0.3692  10650 cpb 275.1 kB/s
AES-CBC-128  long encrypt: 0.2114  5985 cpb 489.5 kB/s
AES-CBC-128  long decrypt: 0.2103  5952 cpb 492.2 kB/s
AES-CBC-192  long encrypt: 0.2235  6325 cpb 463.2 kB/s
AES-CBC-192  long decrypt: 0.2317  6559 cpb 446.7 kB/s
AES-CBC-256  long encrypt: 0.2517  7125 cpb 411.2 kB/s
AES-CBC-256  long decrypt: 0.2549  7215 cpb 406.1 kB/s
AES-ECB-128 short encrypt: 0.3762  10852 cpb 270.0 kB/s
AES-ECB-128 short decrypt: 0.3265  9418 cpb 311.1 kB/s
AES-ECB-192 short encrypt: 0.2321  6695 cpb 437.6 kB/s
AES-ECB-192 short decrypt: 0.2962  8543 cpb 342.9 kB/s
AES-ECB-256 short encrypt: 0.2416  6970 cpb 420.3 kB/s
AES-ECB-256 short decrypt: 0.2562  7391 cpb 396.4 kB/s
AES-ECB-128  long encrypt: 0.1960  5547 cpb 528.2 kB/s
AES-ECB-128  long decrypt: 0.2123  6011 cpb 487.4 kB/s
AES-ECB-192  long encrypt: 0.2413  6829 cpb 429.0 kB/s
AES-ECB-192  long decrypt: 0.2380  6736 cpb 434.9 kB/s
AES-ECB-256  long encrypt: 0.2560  7245 cpb 404.4 kB/s
AES-ECB-256  long decrypt: 0.2638  7468 cpb 392.3 kB/s
```

Why pyAES
---
Some app engine environment don't allow to upload package with C implementation and don't supply a workable C ext wrapper. So in this situation, I just need pure python implementation.

This module also can use in PyPy environment.

In other case, just use C implementation plz.
