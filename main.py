def min_length_of_base1(buffer_size: int) -> int:
  """Equation from qntm readme."""
  # TODO: wait, does this have to be //?
  return (256**buffer_size - 1) / (256 - 1)

def max_length_of_base1(buffer_size: int) -> int:
  """Equation from qntm readme."""
  # TODO: wait, does this have to be //?
  # TODO: this - 1 is accurately placed outside of the expression, like in the readme, but this seems like a plausible place where someone could make an error, so better double-check that it's not supposed to be, effectively, inside the bottom parens.
  return (256**(buffer_size+1) - 1) / (256 - 1) - 1

def find_size_of_buffer_from_n(n: int) -> int:
  """ Given an n (the length of a base1 string),
  we must compute how long the buffer must be,
  before we fill said buffer."""
  # There's certainly a closed-form solution here that I just haven't thought about.
  # But, given that I haven't thought about it, let's do it the dumb way instead.
  i: int = 0
  while True:
    if min_length_of_base1(i) <= n <= max_length_of_base1(i):
      return i
    i+=1

def encode_l(input_buffer: bytes) -> int:
  pass

def encode(input_buffer: bytes) -> str:
  return "A" * encode_l(input_buffer)

def decode_l(base1_string_length: int) -> bytes:
  size: int = find_size_of_buffer_from_n(base1_string_length)
  offset: int = min_length_of_base1(size)
  remainder: int = base1_string_length - offset
  return bytes(int(remainder)) # TODO: Does this work?

def decode(base1_string: str) -> bytes:
  return decode_l(len(base1_string))
