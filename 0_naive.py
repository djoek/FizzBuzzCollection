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

# but lots of elifs are ugly so you would write it more like

def fizzbuzz(i):
    fizz = 'Fizz' if i%3 == 0 else ''
    buzz = 'Buzz' if i%5 == 0 else ''
    return f'{fizz}{buzz}' or str(i)


fb = (fizzbuzz(i) for i in range(1, 101))
print(*fb, sep='\n')