# same as tuples_as_keys.py, but using bit-shifting
lookup_table_5 = {1: "Buzz", 2: "Fizz", 3: "FizzBuzz"}


def fizzbuzz(i: int) -> str:
    return lookup_table_5.get((i / 5).is_integer() + ((i / 3).is_integer() << 1), str(i))


print(*(fizzbuzz(x) for x in range(1, 101)), sep='\n')
