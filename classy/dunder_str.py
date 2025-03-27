class FizzBuzz(int):
    # Lookup table
    fb = ['Fizz', '', '', '', '', '', 'Buzz']

    def __str__(self):
        # Fizz goes forward, Buzz goes reverse
        return FizzBuzz.fb[self % 3] + FizzBuzz.fb[::-1][self % 5] or super().__str__()


def fizzbuzz(i: int) -> str:
    return str(FizzBuzz(i))
