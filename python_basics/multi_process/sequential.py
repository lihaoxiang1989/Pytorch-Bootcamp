import time

def countdown(n):
    while n > 0:
        n -= 1

COUNT = 50000000

start = time.time()
countdown(COUNT)
end = time.time()
print(end - start)
