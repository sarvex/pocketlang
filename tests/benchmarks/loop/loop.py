from time import process_time as clock

start = clock()

list = list(range(10000000))
sum = 0
for i in list: sum += i
print(sum)

print("elapsed:", clock() - start, 's')
