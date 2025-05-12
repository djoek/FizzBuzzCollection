from typing import Annotated
from fastapi import FastAPI, Path

app = FastAPI(title="FizzBuzz API")

@app.get("/fizzbuzz/{i}")
async def fizzbuzz(i: Annotated[int, Path(title="integer to fizzbuzz", gt=0, le=100)]) -> str:
    fizz = 'Fizz' if i % 3 == 0 else ''
    buzz = 'Buzz' if i % 5 == 0 else ''
    return f'{fizz}{buzz}' or str(i)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=0xfbfb)
