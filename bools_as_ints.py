def fizzbuzz(i):
    return f"{'Fizz'*(1-i%3)}{'Buzz'*(1-i%5)}" or i

fb = map(fizzbuzz, range(1,101))
print(*fb, sep="\n")