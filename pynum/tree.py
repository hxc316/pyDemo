
from math import log

def calcShannonEnt( dataSet):
    numEntries = len( dataSet)
    labelCounts = {}
    #❶ （以下 五行） 为所 有可能 分类 创建 字典
    for featVec in dataSet:
        currentLabel = featVec[- 1]
        if currentLabel not in labelCounts. keys():
            labelCounts[ currentLabel] = 0
            labelCounts[ currentLabel] += 1
            shannonEnt = 0.0
            for key in labelCounts:
                prob = float(labelCounts[key])/numEntries
                shannonEnt -= prob * log( prob, 2)
                #❷ 以 2 为 底 求 对数 return shannonEnt
                return shannonEnt

def createDataSet():
    dataSet = [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
    labels = ['no surfacing',' flippers']
    return dataSet, labels


myDat, labels= createDataSet()
print(calcShannonEnt(myDat))
