#!python3
import task2
def test1():
    assert task2.multiplication(5) == [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]

def test2():
    assert task2.multiplication(3,5) == [3,6,9,12,15]