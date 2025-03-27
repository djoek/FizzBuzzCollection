fizz, buzz = range(0, 101, 3), range(0, 101, 5)
rest = set(range(1, 101)) - set(fizz) - set(buzz)

fb_lists = (
    ["FizzBuzz"][:i in fizz and i in buzz] or
    ["Fizz"][:i in fizz] or
    ["Buzz"][:i in buzz] or
    [i][:i in rest]
    for i in range(1, 101))

fb = sum(fb_lists, [])
print(*fb, sep="\n")
