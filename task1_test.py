#!python3

import task1

def test1():
    assert task1.sentence("Hello") == "Hello Benjamin. How are you"

def test2():
    assert task1.sentence("Hiya","Casey","Have you enjoyed your meal") == "Hiya Casey. Have you enjoyed your meal"
