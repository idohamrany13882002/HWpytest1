import math
import sqlite3

def add(a, b):
    return a + b

def minus(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def make_error():
    raise IndexError()

def create_table(query):
    raise sqlite3.IntegrityError

def say_hello():
    name = input("enter name? ")
    return f"hello {name}"

def power(a, b):
    return a**b

def sqrt (a):
    if a <0:
        raise ValueError
    else:
        return math.sqrt(a)

def factorial (a):
    if a == -1:
        raise ValueError
    elif a==0:
        return 1
    else:
        return math.factorial(a)