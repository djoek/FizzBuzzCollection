def fizzbuzz(i):
    yield 'FizzBuzz'[i**2%3*4:8--i**4%5] or i
        
fb = map(fizzbuzz, range(1,101))
print(*fb, sep="\n")