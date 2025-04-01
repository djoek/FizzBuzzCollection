def fizzbuzz(i: int) -> str:
    _ = i
    try:
        1 / (i % 15), str(chr(35) * (i % 5))[0], bytearray((i % 3) - 1)
    except ValueError as f:
        _ = "Fizz"
    except IndexError as b:
        _ = "Buzz"
    except ZeroDivisionError as fb:
        _ = "FizzBuzz"
    else:
        _ = i
    finally:
        return _


print(*(fizzbuzz(x) for x in range(1, 101)), sep='\n')
