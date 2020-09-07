from itertools import cycle, islice

# variation 1
fizz = cycle(('', '', 'Fizz'))
buzz = cycle(('', '', '', '', 'Buzz'))

fb = (f+b or i for f, b, i in zip(fizz, buzz, range(1,101)))
print(*fb, sep="\n")

# variation 2 - infinite fizzbuzz limited by islice
fizzbuzz = cycle(('', '', 'Fizz', '', 'Buzz', 'Fizz', '', '', 'Fizz', 'Buzz', '', 'Fizz', '', '', 'FizzBuzz'))

fb = islice((f_b or i for i, f_b in enumerate(fizzbuzz, 1)), 0, 101)
print(*fb, sep="\n")