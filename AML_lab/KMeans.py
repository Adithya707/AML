import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix,accuracy_score

iris = datasets.load_iris()
X = pd.DataFrame(iris.data)
X.columns = ['Sepal_length','Sepal_width','Petal_length','Petal_width']
Y = pd.DataFrame(iris.target)
Y.columns = ['Target']

model = KMeans(n_clusters=3)
model.fit(X)
model.labels_
plt.figure(figsize=(14,7))
colormap = np.array(['red','lime','black'])

plt.subplot(1,2,1)
plt.scatter(X.Petal_length,X.Petal_width,c=colormap[Y.Target],s=40)
plt.title('Real Classification Petal')

plt.subplot(1,2,1)
plt.scatter(X.Sepal_length,X.Sepal_width,c=colormap[Y.Target],s=40)
plt.title('Real Classification Sepal')

plt.subplot(1,2,1)
plt.scatter(X.Petal_length,X.Petal_width,c=colormap[model.labels_],s=40)
plt.title('Real Classification')

predy = np.choose(model.labels_,[0,1,2]).astype(np.int64)
print('Accuracy Score',accuracy_score(Y.Target,predy))
print('Confusion Matrix',confusion_matrix(Y.Target,predy))

from sklearn import preprocessing

scalar = preprocessing.StandardScaler()
scalar.fit(X)
xsa = scalar.transform(X)
x = pd.DataFrame(xsa,columns=X.columns)

from sklearn.mixture import GaussianMixture

gmm = GaussianMixture(n_components=3)
gmm.fit(x)
pred = gmm.predict(x)

plt.subplot(1,2,1)
plt.scatter(X.Petal_length,X.Petal_width,c=colormap[pred],s=40)
plt.title('Real Classification')

print('Accuracy Score',accuracy_score(Y.Target,pred))
print('Confusion Matrix',confusion_matrix(Y.Target,pred))

