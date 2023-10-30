import time

while True:
    result = 0
    for i in range(1000000):
        result += i
    time.sleep(1)
