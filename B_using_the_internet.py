import httpx

result = httpx.get('https://gist.githubusercontent.com/djoek/c57e86f3bd137c9b2bab995ebbd45278/raw/4f9c8280fdc6704cc5c53e8567df533f3f1a26b8/fizzbuzz.txt')
print(result.text)
