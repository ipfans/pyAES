pyAES
=====

AES algorithm with pure Python 3 implementation. Small modify based on [https://bitbucket.org/intgr/pyaes/](https://bitbucket.org/intgr/pyaes/) to compatible with PEP-8.

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
Even though pyAES is an optimized Python implementation, Python itself is still slow. It should be capable of around 300 kB/s on modern hardware; __that's 1000x slower than pure C implementations__.

This is a test in My Macbook Air M1 (CPython and PyPy):

```
$ python3 bench.py --all
AES-CBC-128 short encrypt: 0.3024  8723 cpb 335.9 kB/s
AES-CBC-128 short decrypt: 0.3330  9605 cpb 305.0 kB/s
AES-CBC-192 short encrypt: 0.3644  10512 cpb 278.7 kB/s
AES-CBC-192 short decrypt: 0.4015  11581 cpb 253.0 kB/s
AES-CBC-256 short encrypt: 0.4249  12256 cpb 239.0 kB/s
AES-CBC-256 short decrypt: 0.4644  13397 cpb 218.7 kB/s
AES-CBC-128  long encrypt: 0.3107  8796 cpb 333.1 kB/s
AES-CBC-128  long decrypt: 0.3385  9583 cpb 305.7 kB/s
AES-CBC-192  long encrypt: 0.3709  10498 cpb 279.1 kB/s
AES-CBC-192  long decrypt: 0.4061  11496 cpb 254.8 kB/s
AES-CBC-256  long encrypt: 0.4319  12224 cpb 239.7 kB/s
AES-CBC-256  long decrypt: 0.4746  13433 cpb 218.1 kB/s
AES-ECB-128 short encrypt: 0.2982  8601 cpb 340.6 kB/s
AES-ECB-128 short decrypt: 0.3252  9381 cpb 312.3 kB/s
AES-ECB-192 short encrypt: 0.3570  10299 cpb 284.5 kB/s
AES-ECB-192 short decrypt: 0.3940  11365 cpb 257.8 kB/s
AES-ECB-256 short encrypt: 0.4180  12058 cpb 243.0 kB/s
AES-ECB-256 short decrypt: 0.4570  13183 cpb 222.2 kB/s
AES-ECB-128  long encrypt: 0.3044  8617 cpb 340.0 kB/s
AES-ECB-128  long decrypt: 0.3334  9437 cpb 310.4 kB/s
AES-ECB-192  long encrypt: 0.3664  10373 cpb 282.4 kB/s
AES-ECB-192  long decrypt: 0.3980  11265 cpb 260.1 kB/s
AES-ECB-256  long encrypt: 0.4276  12103 cpb 242.1 kB/s
AES-ECB-256  long decrypt: 0.4663  13199 cpb 222.0 kB/s

$ pypy3 bench.py --all
AES-CBC-128 short encrypt: 0.0452  1305 cpb 2245.7 kB/s
AES-CBC-128 short decrypt: 0.0425  1225 cpb 2392.4 kB/s
AES-CBC-192 short encrypt: 0.0299  861 cpb 3401.1 kB/s
AES-CBC-192 short decrypt: 0.0340  981 cpb 2985.4 kB/s
AES-CBC-256 short encrypt: 0.0321  925 cpb 3168.8 kB/s
AES-CBC-256 short decrypt: 0.0343  989 cpb 2961.1 kB/s
AES-CBC-128  long encrypt: 0.0230  651 cpb 4501.6 kB/s
AES-CBC-128  long decrypt: 0.0238  675 cpb 4341.5 kB/s
AES-CBC-192  long encrypt: 0.0282  797 cpb 3674.2 kB/s
AES-CBC-192  long decrypt: 0.0282  799 cpb 3665.8 kB/s
AES-CBC-256  long encrypt: 0.0324  916 cpb 3196.8 kB/s
AES-CBC-256  long decrypt: 0.0329  932 cpb 3144.0 kB/s
AES-ECB-128 short encrypt: 0.0371  1070 cpb 2738.0 kB/s
AES-ECB-128 short decrypt: 0.0323  932 cpb 3143.7 kB/s
AES-ECB-192 short encrypt: 0.0278  802 cpb 3652.7 kB/s
AES-ECB-192 short decrypt: 0.0272  783 cpb 3740.5 kB/s
AES-ECB-256 short encrypt: 0.0321  925 cpb 3167.8 kB/s
AES-ECB-256 short decrypt: 0.0318  917 cpb 3195.9 kB/s
AES-ECB-128  long encrypt: 0.0227  643 cpb 4558.5 kB/s
AES-ECB-128  long decrypt: 0.0237  672 cpb 4362.8 kB/s
AES-ECB-192  long encrypt: 0.0270  764 cpb 3835.0 kB/s
AES-ECB-192  long decrypt: 0.0284  805 cpb 3638.4 kB/s
AES-ECB-256  long encrypt: 0.0317  898 cpb 3262.3 kB/s
AES-ECB-256  long decrypt: 0.0329  933 cpb 3141.3 kB/s

$ openssl speed -evp aes-128-cbc aes-192-cbc aes-256-cbc -elapsed
You have chosen to measure elapsed time instead of user CPU time.

......(pass some info)

type             16 bytes     64 bytes    256 bytes   1024 bytes   8192 bytes
aes-192 cbc     258761.09k   271434.35k   274407.33k   273140.34k   271047.29k
aes-256 cbc     232336.64k   237868.93k   234162.85k   238381.57k   239210.50k
aes-128-cbc     303575.80k   316688.83k   320358.54k   318650.80k   320910.45k
```

Why pyAES
---
Some app engine environment don't allow to upload package with C implementation and don't supply a workable C ext wrapper. So in this situation, I just need pure python implementation.

This module also can use in PyPy environment.

In other case, just use C implementation plz.
