#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        q = a / b
    except ZeroDivisionError:
        q = None
    finally:
        print("Inside result:", q)
    return q
