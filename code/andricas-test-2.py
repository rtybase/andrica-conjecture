import math
import primetest
import matplotlib.pyplot as plt

primes = []

def calculate_log(sqrt_p1, sqrt_p2):
    sqrt_1_p2 = 1.0 + sqrt_p2
    r = math.log(sqrt_1_p2/(1.0 + sqrt_p1))
    return r * sqrt_1_p2

N = 1500000

print "Populate primes ..."
for i in xrange(2, N):
    if primetest.is_prime(i):
        primes.append(i);

print "Calculating ..."
sqrt_diff = [] # sqrt diffs
diff = []      # simple diffs
log_calcs = [] # log calcs
x = []
for i in xrange(1, len(primes)):
    sqrt_p2 = math.sqrt(primes[i])
    sqrt_p1 = math.sqrt(primes[i-1])
    sqrt_diff.append(sqrt_p2 - sqrt_p1)
    diff.append(primes[i] - primes[i-1])
    log_calcs.append(calculate_log(sqrt_p1, sqrt_p2))
    x.append(i)

#for i in xrange(len(sqrt_diff)):
#    print sqrt_diff[i]," = s(",primes[i+1],") - s(",primes[i],")"

print "Plotting ..."
plt.subplot(311)
plt.plot(x, sqrt_diff)
plt.subplot(312)
plt.plot(x, log_calcs)
plt.subplot(313)
plt.hist(diff, 1000)
plt.show()