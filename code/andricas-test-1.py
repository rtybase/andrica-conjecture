import math
import primetest
import matplotlib.pyplot as plt

def pi(x):
    ret = 0
    i = 2
    while i <= x:
        if primetest.is_prime(i):
            ret += 1
        i += 1
    return ret

def f(x):
    no_of_primes = pi(x)
    # indexing is as per the article
    f3 = no_of_primes - x/math.log(x)
    f4 = no_of_primes - math.sqrt(x)
    return f3, f4

START = 0
N = 40000
step = 0.25
x = []
y3 = []
x31 = []
y31 = []
y4 = []

print "Calculating ..."
n = START + 1.5
for i in xrange(START, N):
    f3, f4 = f(n)
    x.append(n)
    y3.append(f3)
    y4.append(f4)
    
    n_n = int(n)
    if (abs(n_n - n) <= 0.0001) and primetest.is_prime(n_n):
        x31.append(n_n)
        y31.append(f3)
    
    n += step

print "Plotting ..."
plt.subplot(211)
plt.plot(x, y3)
plt.plot(x31, y31)
plt.subplot(212)
plt.plot(x, y4)
plt.show()
