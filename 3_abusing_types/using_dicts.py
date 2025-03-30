lookup_table_1 = dict()
for _ in range(15):
    lookup_table_1.setdefault(
        _ % 15,
        # True / False gets cast to 1 / 0
        'Fizz' * (_ / 3).is_integer() + 'Buzz' * (_ / 5).is_integer()
    )


def fizzbuzz_1(i: int) -> str:
    return lookup_table_1.get(i % 15, str(i))


lookup_table_2 = dict()
lookup_table_2[0] = "FizzBuzz"
lookup_table_2[3] = lookup_table_2[6] = lookup_table_2[9] = lookup_table_2[12] = "Fizz"
lookup_table_2[5] = lookup_table_2[10] = "Buzz"


def fizzbuzz_2(i: int) -> str:
    return lookup_table_2.get(i % 15, str(i))


# prefilled 2 
lookup_table_3 = {0: "FizzBuzz"}
lookup_table_3.update({_: "Fizz" for _ in range(3, 13, 3)})
lookup_table_3.update({_: "Buzz" for _ in range(5, 11, 5)})


def fizzbuzz_3(i: int) -> str:
    return lookup_table_3.get(i % 15, str(i))


# using tuples as keys
lookup_table_4 = {
    (True, False): "Fizz",
    (False, True): "Buzz",
    (True, True): "FizzBuzz",
}


def fizzbuzz_4(i: int) -> str:
    return lookup_table_4.get(((i / 3).is_integer(), (i / 5).is_integer()), str(i))


# same as above, but using bit-bashing
lookup_table_5 = {1: "Buzz", 2: "Fizz", 3: "FizzBuzz"}


def fizzbuzz_5(i: int) -> str:
    return lookup_table_5.get((i / 5).is_integer() + ((i / 3).is_integer() << 1), str(i))
