import json
from openai import OpenAI

client = OpenAI()  # You should have OPENAI_API_KEY set

system_prompt = """You are FizzBuzz. 
You output the numbers in the interval [1..100], except:
- when the number is divisible by 3, don't write the number, instead write: Fizz
- when the number is divisible by 5, don't write the number, instead write: Buzz
- when the number is divisible by 3 and 5, don't write the number, instead write: FizzBuzz
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
for entry in json.loads(message.content).get('output', []):
    print(entry)
