import numpy as np

# essentially the same idea as list_and_slice.py
fb = np.arange(101, dtype='object')
fb[::3], fb[::5], fb[::15] = 'Fizz', 'Buzz', 'FizzBuzz'

print(*fb[1:], sep='\n')
