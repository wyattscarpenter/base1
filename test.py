#!/usr/bin/env python3

import main as m

# Easily check for type errors and other instant failures:
assert m.decode("") == b''
#assert m.encode(b'') == ""

test_cases: list[tuple[str, int, bytes]] = [
  ("", 0, b''),
  ("A", 1, b'\x00'),
  ("AA", 2, b'\x01'),
  ("AAA", 3, b'\x02'),
  ("A"*256, 256, b'\xFF'),
  ("A"*257, 257, b'\x00\x00'),
  ("A"*258, 258, b'\x00\x01'),
  ("A"*1217, 1217, bytes([3,192]))
]

for test_case in test_cases:
  t = test_case
  s = test_case[0]
  n = test_case[1]
  b = test_case[2]
  print(t)
  print(m.decode(s), "|", m.decode_l(n), "|", b)
  assert m.decode(s) == m.decode_l(n) == b
  print("-"*20)
print("All tests ok!")
