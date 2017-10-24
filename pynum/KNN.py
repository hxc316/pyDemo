from numpy import *
import operator

def createDataSet():
    group = array([[ 2.0, 2.1],[ 2.3, 2.4],[ 2, 2],
                   [ 2, 2],[ 2, 2.1],[ 2, 2.0]])
    labels = ['A',' A','A',' B',' B','B']
    return group, labels


# group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
# print(tile(group,2))

def classify0( inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    #❶（ 以下 三行） 距离 计算
    diffMat = tile( inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount={}
    #❷ （以下 两行） 选择 距离最小 的 k 个 点
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
        sortedClassCount = sorted(classCount.items(),key= operator.itemgetter(1),reverse= True)
        print("sortedClassCount=",sortedClassCount)
        return sortedClassCount[0][0]


def classify2(inx,dataSet,lables,k):
    dataSetSize = dataSet.shape[0]  #读取矩阵的长度 4
    print("dataSetSize=",dataSetSize)
    #距离计算
    print("tile(inx,(dataSetSize,1))=",tile(inx,(dataSetSize,1)))
    diffMat = tile(inx,(dataSetSize,1)) - dataSet
    print("diffMat=",diffMat)
    sqDiffMat = diffMat**2
    print("diffMat**2=",diffMat**2 )
    sqDistances = sqDiffMat.sum(axis=1)
    print("sqDiffMat.sum(axis=1)=",sqDiffMat.sum(axis=1))
    distances = sqDistances**0.5
    print("sqDistances**0.5=",sqDistances**0.5)
    sortedDistIndicies = distances.argsort()
    print("sortedDistIndicies=",sortedDistIndicies)
    classCount = {}
    for i in range(k):
        voteIlabel = lables[sortedDistIndicies[i]]
        # print("classCount:",classCount)
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
        print(classCount)
    print(classCount.iteritems())
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    print("sortedClassCount=",sortedClassCount)
    return sortedClassCount[0][0]
