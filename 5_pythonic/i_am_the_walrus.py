def fizzbuzz(i: int) -> str:
    fizz = not (fb := '') and (i % 3 or (fb := 'Fizz'))
    buzz = (i % 5 or (fb := f'{fb}Buzz'))
    return fizz and buzz and (fb or f'{i!s}')


print(*map(fizzbuzz, range(1, 101)), sep="\n")
