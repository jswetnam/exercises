# http://challenge.cueup.com/
# To get the password for level 3, write code to find the first prime
# fibonacci number larger than a given minimum.  For example, the first
# prime fibonacci number larger than 10 is 13.


fib_numbers = [0, 1]

def _fib(n):
    if not fib_numbers[n]:
        fib_numbers[n] = _fib(n - 1) + _fib(n - 2)

    return fib_numbers[n]

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n / 2):
        if n % i == 0:
            return False
    return True

def largest_prime_fib_gt(n):
    while fib_numbers[-1] <= n:
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])

    while not is_prime(fib_numbers[-1]):
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])


    return fib_numbers[-1]

largest_gt = largest_prime_fib_gt(227000)

prime_divisors = []

largest_gt = largest_gt + 1
for i in range(2, largest_gt):
    if largest_gt % i == 0 and is_prime(i):
        prime_divisors.append(i)

print sum(prime_divisors)

