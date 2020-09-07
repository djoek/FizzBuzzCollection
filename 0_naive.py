def fizzbuzz(i):
    fizz = i%3 == 0
    buzz = i%5 == 0
    if fizz and buzz:
        return "FizzBuzz"
    elif fizz:
        return "Fizz"
    elif buzz:
        return "Buzz"
    else:
        return i
    
fb = (fizzbuzz(i) for i in range(1, 101))
print(*fb, sep='\n')