from time import process_time as clock

def fib(n):
  return n if n < 2 else fib(n - 1) + fib(n - 2)

start = clock()
for _ in range(0, 10):
  print(fib(30))
print("elapsed: ", clock() - start, 's')
