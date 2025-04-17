lookup_table = dict()
for _ in range(15):
    lookup_table.setdefault(
        _ % 15,
        # True / False gets cast to 1 / 0
        'Fizz' * (_ / 3).is_integer() + 'Buzz' * (_ / 5).is_integer()
    )


def fizzbuzz(i: int) -> str:
    return lookup_table.get(i % 15, str(i))


print(*(fizzbuzz(x) for x in range(1, 101)), sep='\n')
