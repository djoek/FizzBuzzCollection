lookup_table = {0: "FizzBuzz"}
lookup_table.update({_: "Fizz" for _ in range(3, 13, 3)})
lookup_table.update({_: "Buzz" for _ in range(5, 11, 5)})


def fizzbuzz(i: int) -> str:
    return lookup_table.get(i % 15, str(i))


print(*(fizzbuzz(x) for x in range(1, 101)), sep='\n')
