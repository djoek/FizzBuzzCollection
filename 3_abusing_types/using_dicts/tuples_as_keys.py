lookup_table = {
    (True, False): "Fizz",
    (False, True): "Buzz",
    (True, True): "FizzBuzz",
}


def fizzbuzz(i: int) -> str:
    return lookup_table.get(((i / 3).is_integer(), (i / 5).is_integer()), str(i))


print(*(fizzbuzz(x) for x in range(1, 101)), sep='\n')
