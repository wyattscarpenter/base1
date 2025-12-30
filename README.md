# base1 (python implementation)

This is a python implementation of Base1 encoding, as detailed in https://github.com/ferno/base1. It follows that API. I implemented this largely on 2025-12-29, for fun.

It is a python library, not a command-line program.

qntm's base1 works with javascript concepts, which have analogues in python. So, we use `bytes` instead of UInt8Array or whatever, and `int` instead of BigInt. The names of functions uses snakecase instead of camelcase.

The algorithm to encode and decode base1, especially in closed form, is not entirely trivial if you just read qntm's readme. You can derive, with some analytical work. It's all there, but you have to think about it a little. (What does it mean, mathematically to, eg, "sort all possible buffers by length and then lexicographically"? that seems like it would take a lot of time for the CPU to execute).

I lost interest in this project before testing it very well.
