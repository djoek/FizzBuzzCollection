from pydantic import BaseModel
from openai import OpenAI

client = OpenAI()


class FizzBuzz(BaseModel):
    results: list[str]


completion = client.beta.chat.completions.parse(
    model="gpt-4o-mini",
    messages=[
        {"role": "system",
         "content": "You are FizzBuzz. "
                    "You output the numbers between 1 and 100 inclusive, except:"
                    "- when the number is divisible by 3, you write: Fizz"
                    "- when the number is divisible by 5, you write: Buzz"
                    "- when the number is divisible by 3 and 5, you write: FizzBuzz"
         },
    ],
    response_format=FizzBuzz,
)

message = completion.choices[0].message
if message.parsed:
    for entry in message.parsed.results:
        print(entry)
else:
    print(message.refusal)
