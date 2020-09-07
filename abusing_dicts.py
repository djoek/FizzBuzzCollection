# using setdefault()
fizzbuzz = dict()
fb = (
    fizzbuzz.setdefault(
        i%15, 
        'Fizz'*(i/3).is_integer() + 'Buzz'*(i/5).is_integer()
    ) or i for i in range(1, 101)
)

print(*fb, sep="\n")

# prefilled 1
fizzbuzz = dict()
fizzbuzz[0] = "FizzBuzz"
fizzbuzz[3] = fizzbuzz[6] = fizzbuzz[9] = fizzbuzz[12] = "Fizz"
fizzbuzz[5] = fizzbuzz[10] = "Buzz" 


fb = (fizzbuzz.get(i%15, i) for i in range(1, 101))
print(*fb, sep="\n")

# prefilled 2 
fizzbuzz = {0: "FizzBuzz"}
fizzbuzz.update({_: "Fizz" for _ in range(3, 13, 3)})
fizzbuzz.update({_: "Buzz" for _ in range(5, 11, 5)})

fb = (fizzbuzz.get(i%15, i) for i in range(1, 101))
print(*fb, sep="\n")

# using tuple keys
fizzbuzz = {
    (True, False): "Fizz",
    (False, True): "Buzz",
    (True, True): "FizzBuzz",
}

fb = (fizzbuzz.get(((i/3).is_integer(), (i/5).is_integer()), i) for i in range(1, 101))
print(*fb, sep="\n")

# using bitbashing
fizzbuzz = {1: "Buzz", 2: "Fizz", 3: "FizzBuzz"}
    
fb = (fizzbuzz.get((i/5).is_integer() + ((i/3).is_integer() << 1), i) for i in range(1, 101))
print(*fb, sep="\n")