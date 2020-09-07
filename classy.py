class FizzBuzz(int):
    
    fb = ['Fizz', '', '', '', '', '', 'Buzz']
    
    def __str__(self):
        return FizzBuzz.fb[self%3]+FizzBuzz.fb[::-1][self%5] or super().__str__()


fb = map(FizzBuzz, range(1, 101))
print(*fb, sep="\n")