def get_primes_with_hashes(n):
    sieve = [True] * (n+1)
    for p in range(2,n+1):
        if sieve[p]:
            for m in range(p*p, n+1, p):
                sieve[m] = False
    return [(x, randint(1,2**32-1)) for x in range(2,n+1) if sieve[x]]