class FizzBuzzProperty:
    
    def __init__(self, divisor: int, name: str = None):
        self.divisor = divisor
        self.name = name
        
    def __get__(self, instance, owner) -> str:
        return self.name if instance % self.divisor == 0 else ''
    
    def __set_name__(self, owner, name: str):
        if self.name is None:
            self.name = name.capitalize()

            
class FizzBuzz(int):
    
    fizz = FizzBuzzProperty(3)
    buzz = FizzBuzzProperty(5)
    
    def __str__(self):
        return self.fizz + self.buzz or super().__str__()
    
    
fb = map(FizzBuzz, range(1, 101))
print(*fb, sep="\n")