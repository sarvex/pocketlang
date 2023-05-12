from time import process_time as clock

def is_prime(n):
	return False if n < 2 else all(n % i != 0 for i in range(2, n))

start = clock()

N = 30000
primes = [i for i in range(N) if is_prime(i)]
print("elapsed:", clock() - start, "s")
