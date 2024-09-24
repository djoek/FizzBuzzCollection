import json
from openai import OpenAI

client = OpenAI()  # You should have OPENAI_API_KEY set

system_prompt = """You are FizzBuzz. 
Write the numbers from 1 to 100 (including 100), except:
- when the number is divisible by 3 don't write the number but instead write: Fizz
- when the number is divisible by 5 don't write the number but instead write: Buzz
- when the number is divisible by 3 and 5 don't write the number but instead write: FizzBuzz
"""

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "system", "content": system_prompt}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "strict": True,
            "name": "FizzBuzz",
            "schema": {
                "type": "object",
                "title": "FizzBuzz",
                "required": ["output"],
                "properties": {
                    "output": {
                        "type": "array",
                        "title": "Output",
                        "items": {"type": "string"},
                    }
                },
                "additionalProperties": False,
            }
        }
    },
)

message = completion.choices[0].message
for item in json.loads(message.content).get('output', []):
    print(item)
    

# But it's cleaner to do this with Pydantic
from pydantic import BaseModel


class FizzBuzz(BaseModel):
    output: list[str]


completion = client.beta.chat.completions.parse(
    model="gpt-4o-mini",
    messages=[{"role": "system", "content": system_prompt}],
    response_format=FizzBuzz
)

message = completion.choices[0].message
for item in message.parsed.output:
    print(item)
