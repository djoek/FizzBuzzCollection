# djoek's FizzBuzz Collection

A collection of FizzBuzz implementations in python I've written and/or collected over the years. 
No need to comment that most of these are silly, I'm well aware and this is intentional. 

## Approach

Most solutions are organized like this:

```python
def fizzbuzz(i: int) -> str: 
    ...

print(*map(fizzbuzz, range(1, 101)), sep="\n")
```

So you can run the file and validate the output itself.
However, there are a few exceptions to this, since they operate in a way that doesn't interpret single numbers


