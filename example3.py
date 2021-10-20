#!python3

"""
You can actually specify your variables in any order if you use the = assignment
operator in your function call.
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


x = sample(a=10,c="Fish")
print(x)

# All of a sudden the print statement makes some sense.
print("hello!" , end="ending")
print("hello!" , flush=True, end="*")
# the print statement is a function that has some optional input parameters
# it requires some specific output to be displayed, but can also take some
# optional parameters for end and flush
