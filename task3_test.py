#!python3

import task3

def test1():
    assert task3.title("*") == "*********\n* Title *\n*********"

def test2():
    assert task3.title() == "=========\n= Title =\n========="