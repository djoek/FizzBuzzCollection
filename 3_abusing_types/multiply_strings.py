def fizzbuzz(i: int) -> str:
    # Multiplying a str with i < 1 returns ''
    return f"{'Fizz' * (1 - i % 3)}{'Buzz' * (1 - i % 5)}" or i

print(*map(fizzbuzz, range(1, 101)), sep="\n")
