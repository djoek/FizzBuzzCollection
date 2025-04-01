import numpy as np

# essentially the same idea as list_slices_sets/list_and_slice.py
lookup_table = np.arange(101, dtype='object')
lookup_table[::3], lookup_table[::5], lookup_table[::15] = 'Fizz', 'Buzz', 'FizzBuzz'


def fizzbuzz(i: int) -> str:
    return lookup_table.get(i % 15, str(i))


print(*(fizzbuzz(x) for x in range(1, 101)), sep='\n')
