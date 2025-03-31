from itertools import cycle, islice


first_15 = cycle(('', '', 'Fizz', '', 'Buzz', 'Fizz', '', '', 'Fizz', 'Buzz', '', 'Fizz', '', '', 'FizzBuzz'))

fb = islice((f_b or i for i, f_b in enumerate(first_15, 1)), 0, 101)
print(*fb, sep="\n")