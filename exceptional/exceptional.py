def fizzbuzz_1(i: int) -> str:
    _ = i
    try:
        1 / (i % 15), str(chr(35) * (i % 5))[0], bytearray((i % 3) - 1)
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


# more compact
def fizzbuzz_2(i: int) -> str:
    try:
        bytearray(bool(([(i % 3) / (i % 15)] * (i % 5))[0]) - 1)
    except ValueError:
        i = "Fizz"
    except IndexError:
        i = "Buzz"
    except ZeroDivisionError:
        i = "FizzBuzz"
    return i

