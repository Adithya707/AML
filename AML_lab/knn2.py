from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.metrics import confusion_matrix,classification_report
from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris()
x = iris.data
y = iris.target

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)

classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(x_train,y_train)
y_pred = classifier.predict(x_test)

print('Accuracy',confusion_matrix(y_pred,y_test))
print('Classification_report',classification_report(y_test,y_pred))
