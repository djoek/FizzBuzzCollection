fizz, buzz = range(0, 101, 3), range(0, 101, 5)
rest = set(range(1, 101)) - set(fizz) - set(buzz)


def fizzbuzz(i: int) -> str:
    return str(["FizzBuzz"][:i in fizz and i in buzz] or
               ["Fizz"][:i in fizz] or
               ["Buzz"][:i in buzz] or
               [i][:i in rest])


print(*map(fizzbuzz, range(1, 101)), sep="\n")
