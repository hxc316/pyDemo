
import json

#写数据
def dump1():
    numbers = [1,2,3,4,5];
    fn = "a.json"
    with open(fn,"w") as f:
        json.dump(numbers,f)

#加载数据
def load1():
    b=[]
    with open("a.json") as f:
        b=json.load(f)
    print(b)

dump1()
load1()
