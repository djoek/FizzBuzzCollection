import httpx

result = httpx.get(
    'https://gist.githubusercontent.com/djoek/c57e86f3bd137c9b2bab995ebbd45278/'
    'raw/4f9c8280fdc6704cc5c53e8567df533f3f1a26b8/fizzbuzz.txt')

# [None] to offset zero starting list
lookup_list = [None] + result.text.split('\n')


def fizzbuzz(i: int) -> str:
    return lookup_list[i]


print(*(fizzbuzz(x) for x in range(1, 101)), sep='\n')

