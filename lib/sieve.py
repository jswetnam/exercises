# Prime number determination using the sieve of eratosthenes

def cross_off(p, sieve):
    for i in range(p*p, len(sieve)):
        if i % p == 0:
            sieve[i] = False


def next_prime(p, sieve):
    for i in range(p + 1, len(sieve)):
        if sieve[i]:
            return i


def is_prime(n):
    assert n >= 2
    sieve = [True for  _ in range(n + 1)]
    p = 2
    while p < n and sieve[n]:
        cross_off(p, sieve)
        p = next_prime(p, sieve)

    return sieve[n]
