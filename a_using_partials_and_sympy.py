from functools import partial
import sympy


def is_p_a_prime_factor_of_j(j, p):
    return p in sympy.primefactors(j)


fizz = partial(is_p_a_prime_factor_of_j, p=3)
buzz = partial(is_p_a_prime_factor_of_j, p=5)


def fizzbuzz(i: int) -> str:
    return f'{"Fizz" if fizz(i) else ""}{"Buzz" if buzz(i) else ""}' or str(i)


print(*map(fizzbuzz, range(1, 101)), sep="\n")
