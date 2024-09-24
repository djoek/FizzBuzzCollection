import json
from openai import OpenAI

client = OpenAI()  # You should have OPENAI_API_KEY set

system_prompt = """You are FizzBuzz. 
You output the numbers between 1 and 100 inclusive, except:
- when the number is divisible by 3, you write: Fizz
- when the number is divisible by 5, you write: Buzz
- when the number is divisible by 3 and 5, you write: FizzBuzz
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
