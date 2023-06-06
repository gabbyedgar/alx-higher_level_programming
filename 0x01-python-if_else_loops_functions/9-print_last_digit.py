#!/usr/bin/python3
def print_last_digit(number):
    print(f"{(abs(number) % 10):d}", end="")
    return abs(number) % 10
