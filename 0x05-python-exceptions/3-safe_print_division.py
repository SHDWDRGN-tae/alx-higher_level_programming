#!/usr/bin/python3

def safe_print_division(a, b):
    result = 0

    try:
        results = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print('Inside result: {}'.format(result))
        return result
