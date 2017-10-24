
import pynum.KNN

group,labels = pynum.KNN.createDataSet()

# print(group)

print(pynum.KNN.classify2([2,2],group,labels,3))

