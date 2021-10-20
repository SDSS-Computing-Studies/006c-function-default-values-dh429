#!python3

"""
Sometimes you need to have some required inputs, but you might want to have optional inputs.
You should specify your required inputs first, and then any optional inputs can come
afterwards
"""

def sample(a, b=4, c="Test"):
  # This program takes 1 required input: a
  # The program also takes an optional inputs:
  # b: integer value
  # c: string
  # program will repeat c a number of times specified by b
  # and add them all to the same line.
  # return:
  # the output string
  
  output = ""
  for i in range(0,4):
    output = output + c
  return output

sample(3)
sample(2,5,"cat")
sample(5,3)

# Note that with this structure, you can't specify to use the default value of b
# and enter your own value for c.  See how this can be done in example3.py
