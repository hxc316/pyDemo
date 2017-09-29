import time


for i in range(10):
    print(i)

print(time.strftime('%M',time.localtime(time.time())))
