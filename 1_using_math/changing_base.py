from numpy import base_repr

def fizzbuzz(i: int) -> str:
    fizz = "Fizz" if base_repr(i, base=3).endswith("0") else ""
    buzz = "Buzz" if base_repr(i, base=5).endswith("0") else ""
    return f'{fizz}{buzz}' or str(i)


print(*map(fizzbuzz, range(1, 101)), sep="\n")
