def fizzbuzz(i):
    try:
        1/(i%15), str(chr(35)*(i%5))[0], bytearray((i%3)-1)   
    except ValueError as fizz:
        _ = "Fizz"
    except IndexError as buzz:
        _ = "Buzz"
    except ZeroDivisionError as fizzbuzz:
        _ = "FizzBuzz"
    else:
        _ = i
    finally:
        return _
    
fb = map(fizzbuzz, range(1, 101))
print(*fb, sep="\n")


# more compact
def fizzbuzz(i):
    try: bytearray(bool(([(i%3)/(i%15)]*(i%5))[0])-1)  
    except ValueError: i = "Fizz"
    except IndexError: i = "Buzz"
    except ZeroDivisionError: i = "FizzBuzz"
    return i

fb = map(fizzbuzz, range(1, 101))
print(*fb, sep="\n")