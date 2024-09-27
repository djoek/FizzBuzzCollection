def fizzbuzz(i):
    fizz = not (fb := '') and (i % 3 or (fb := 'Fizz'))
    buzz = (i % 5 or (fb := f'{fb}Buzz'))
    return fizz and buzz and (fb or f'{i!s}')


print(*(fizzbuzz(x) for x in range(1, 101)), sep='\n')
