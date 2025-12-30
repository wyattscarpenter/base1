#!/usr/bin/env python3

import main as m

assert m.decode("") == b''

test_cases: list[tuple[str, int, bytes]] = [
  ("", 0, b''),
  ("A", 1, b'\x00'),
  ("AA", 2, b'\x01'),
]
# TODO: this is off by one

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
