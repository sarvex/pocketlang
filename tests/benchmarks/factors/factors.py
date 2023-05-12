from time import process_time as clock

start = clock()

N = 50000000
factors = [i for i in range(1, N+1) if N % i == 0]
print("elapsed:", clock() - start, 's')
