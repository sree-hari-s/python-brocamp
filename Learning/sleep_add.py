from time import sleep, time

def add(num1, num2):
    start =time()
    sleep(num1)
    sleep(num2)
    return int(time()-start)

print(add(1.5,0))