from pathlib import Path

root = Path(__file__).parent
source = root / 'fizzbuzz.txt'

with source.open(mode='r', encoding='utf8') as fp:
    for line in fp:
        print(line)
