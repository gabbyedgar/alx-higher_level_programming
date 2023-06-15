#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    def extract(x: tuple, i: int) -> int:
        return x[i] if len(x) >= i + 1 else 0

    return (extract(tuple_a, 0) + extract(tuple_b, 0),
            extract(tuple_a, 1) + extract(tuple_b, 1))
