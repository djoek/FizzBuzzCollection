def fizzbuzz(i: int) -> str:
    # Order of Operations Ordeal
    # (((i ** 2) % 3) * 4)
    # (8 - ((-i ** 4) % 5))
    return 'FizzBuzz'[i ** 2 % 3 * 4:8 - -i ** 4 % 5] or i


print(*map(fizzbuzz, range(1, 101)), sep="\n")
