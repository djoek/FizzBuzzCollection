def fizzbuzz_prime(i: int) -> str:
    # For reference
    fizz = i % 3 == 0
    buzz = i % 5 == 0

    if fizz and buzz:
        return "FizzBuzz"
    elif fizz:
        return "Fizz"
    elif buzz:
        return "Buzz"
    else:
        return str(i)


# Lots of elifs are ugly, so write it like this
def fizzbuzz(i: int) -> str:
    fizz = 'Fizz' if i % 3 == 0 else ''
    buzz = 'Buzz' if i % 5 == 0 else ''
    return f'{fizz}{buzz}' or str(i)


# print(*map(fizzbuzz, range(1, 101)), sep="\n")
