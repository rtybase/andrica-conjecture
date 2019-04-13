import math

cache_prime = {}
cache_prime[1] = False
cache_prime[2] = True
cache_prime[3] = True
cache_prime[5] = True
cache_prime[7] = True
cache_prime[11] = True
cache_prime[13] = True
cache_prime[17] = True
cache_prime[19] = True

def is_prime(n):
    if n in cache_prime:
        return cache_prime[n]

    # this is fast, no need to cache
    if (n & 1 == 0):
        return False

    l = int(math.sqrt(n)) + 1
    for i in xrange(2,l):
        if (n % i) == 0:
            cache_prime[n] = False
            return False
    cache_prime[n] = True
    return True
