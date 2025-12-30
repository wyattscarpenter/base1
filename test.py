#!/usr/bin/env python3

import main as m

assert m.decode("") == b''

# TODO: this is off by one
print(
m.decode("A"),
m.decode("AA")
)

assert m.decode("A") == b'\00'

print("All tests ok!")
