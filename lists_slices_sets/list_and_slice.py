# native
fb = list(range(0, 101))

fb[::3] = ['Fizz']*len(fb[::3])
fb[::5] = ['Buzz']*len(fb[::5])
fb[::15] = ['FizzBuzz']*len(fb[::15])

print(*fb[1:], sep='\n')
