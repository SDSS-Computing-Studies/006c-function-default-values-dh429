#!python3
"""
Create a function called multiplication that takes 2 input paremeters:
number: integer.  
end: integer. It should have a default value of 12.

The function will create a list that stores the multiplication tables for the number, and ends at end.

return value:
list.  The multiplication tables starting at a multiple of 1 and ending at whatever the default value is.

example assertion:
assert multiplication(5) == [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
assert multiplication(2,5) == [2, 4, 6, 8, 10]
"""

def multiplication(number, end = 12):
    multi = 1
    output = []
    mnum = number
    for i in range(0, end + 1):
        mnum = number * multi
        output.append(mnum)
        multi = multi + 1
        if multi == end:
            mnum = number * multi
            output.append(mnum)
            break
    return output
