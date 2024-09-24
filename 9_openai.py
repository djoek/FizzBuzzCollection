import json
from openai import OpenAI

client = OpenAI()  # You should have OPENAI_API_KEY set

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system",
         "content": """You are FizzBuzz. 
You output the numbers between 1 and 100 inclusive, except:
- when the number is divisible by 3, you write: Fizz
- when the number is divisible by 5, you write: Buzz
- when the number is divisible by 3 and 5, you write: FizzBuzz
"""
         },
    ],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "strict": True,
            "name": "FizzBuzz",
            "schema": {
                "properties": {"output": {"items": {"type": "string"}, "title": "Output", "type": "array"}},
                "additionalProperties": False,
                "required": ["output"], "title": "FizzBuzz", "type": "object"}}
    },
)

message = completion.choices[0].message
for entry in json.loads(message.content).get('output', []):
    print(entry)
