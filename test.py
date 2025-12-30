#!/usr/bin/env python3

import main as m

# Easily check for type errors and other instant failures:
assert m.decode("") == b''
assert m.encode(b'') == ""

def dprint(*args):
  DEBUG = True
  if DEBUG:
    print(*args)

def trunc(s: str) -> str:
  if len(s) > 5:
    return s[:5] + "…"
  else:
    return s

test_cases: list[tuple[str, int, bytes]] = [
  ("", 0, b''),
  ("A", 1, b'\x00'),
  ("AA", 2, b'\x01'),
  ("AAA", 3, b'\x02'),
  ("A"*256, 256, b'\xFF'),
  ("A"*257, 257, b'\x00\x00'),
  ("A"*258, 258, b'\x00\x01'),
  ("A"*1217, 1217, bytes([3,192])),
  # This test case is suggested by https://github.com/girst/base1-mirror-of-git.gir.st ; unlike that repo, I could do "Hello World", since python has bigints by default, and also my "Hallo" is instant so IDK what was wrong with his algorithm. (tbh that does make his program funnier)
  ("A"*18794, 18794, b"Hi")
]

for test_case in test_cases:
  t = test_case
  s = test_case[0]
  n = test_case[1]
  b = test_case[2]
  dprint("CASE:", trunc(s), n, b)
  dprint("DE:", m.decode(s), m.decode_l(n), b)
  assert m.decode(s) == m.decode_l(n) == b
  dprint("EN:", trunc(m.encode(b)), m.encode_l(b), b)
  assert m.encode_l(b) == n and m.encode(b) == s
  dprint("-"*20)

print(f"All {len(test_cases)} tests passed ok!")
