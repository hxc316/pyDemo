from numpy import *

# print(zeros((2,1024),float))


# print(arange(15))
b=arange(15)
a=arange(20).reshape(10,2)
# a.iteritems()

# print(a)

m = mat(random.rand(4,4))
# 矩阵求逆的运算。
# print(m.I)

def file():
    f=open("d:/test/11.txt")    #读取文件
    lines=f.readlines()
    for line in lines:
        print(line.strip()) #去掉换行

# file()
#将所有的数据都变成 0 到1 之间的数
def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m,1))
    normDataSet = normDataSet/tile(ranges, (m, 1)) #❶ 特征值 相除
    print(ranges)
    return normDataSet, ranges, minVals


# m1=arange(10)
# autoNorm(m1)

#22000 到60000之间的浮点数
# print(random.uniform(22000, 60000))
for i in range(20):
    print(random.standard_normal(10))






