lookup_table = dict()
lookup_table[0] = "FizzBuzz"
lookup_table[3] = lookup_table[6] = lookup_table[9] = lookup_table[12] = "Fizz"
lookup_table[5] = lookup_table[10] = "Buzz"


def fizzbuzz(i: int) -> str:
    return lookup_table.get(i % 15, str(i))


print(*(fizzbuzz(x) for x in range(1, 101)), sep='\n')
