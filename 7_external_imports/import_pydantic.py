from typing import Literal, Union
from pydantic import BaseModel, model_validator, Field


class FizzBuzz(BaseModel):
    number: int = Field(..., gt=0, le=100)
    fizz: Union[Literal['Fizz'], Literal['']] = 'Fizz'
    buzz: Union[Literal['Buzz'], Literal['']] = 'Buzz'

    @model_validator(mode='after')
    def fizzbuzz_validator(self):
        if self.number % 3 != 0 and self.fizz:
            self.fizz = ''

        if self.number % 5 != 0 and self.buzz:
            self.buzz = ''

        return self

    def __str__(self):
        return f"{self.fizz}{self.buzz}" or self.number.__str__()


for i in range(1, 101):
    print(FizzBuzz(number=i))
