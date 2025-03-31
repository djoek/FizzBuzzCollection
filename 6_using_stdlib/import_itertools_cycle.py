from itertools import cycle

fizz = cycle(('', '', 'Fizz'))
buzz = cycle(('', '', '', '', 'Buzz'))

fb = (f+b or i for f, b, i in zip(fizz, buzz, range(1,101)))
print(*fb, sep="\n")

