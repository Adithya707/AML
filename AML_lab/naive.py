import csv
import math
import random
from sklearn.metrics import classification_report,confusion_matrix

def load_data(filename):
  with open(filename) as csvfile:
    lines = csv.reader(csvfile)
    dataset = list(lines)
    for i in range(len(dataset)):
      dataset[i] = [float(x) for x in dataset[i]]
    return dataset
    
def split_data(dataset,split):
  train_set = []
  train_size = int(len(dataset))*split
  copy = list(dataset)
  while len(train_set)<train_size:
    index = copy.pop(random.randrange(len(copy)))
    train_set.append(index)
  return [train_set,copy]

def mean(numbers):
  return (sum(numbers)/float(len(numbers)))

def std_dev(numbers):
  avg = mean(numbers)
  var = sum([pow(x-avg,2) for x in numbers])/(len(numbers)-1)
  return math.sqrt(var)
  
def separatedByclass(dataset):
  sepa={}
  for i in range(len(dataset)):
    vector = dataset[i]
    if vector[-1] not in sepa:
      sepa[vector[-1]]= []
    sepa[vector[-1]].append(vector)
  return sepa

def calprob(x,mean,std):
  expo = math.exp(-(pow(x-mean,2))/(2*pow(std,2)))
  prob = (1/(math.sqrt(2*math.pi*std)))*expo
  return prob

def summerize(dataset):
  summerise = {}
  summerise = [(mean(attribute),std_dev(attribute)) for attribute in zip(*dataset)]
  del summerise[-1]
  return summerise
  
def summerizeByclass(dataset):
  sep = separatedByclass(dataset)
  summerise = {}
  for classval,instance in sep.items():
    summerise[classval] = summerize(instance)
  return summerise
  
def calclassprob(summerise,inputvector):
  prob = {}
  for classval,classsummer in summerise.items():
    prob[classval] = 1
    for i in range(len(classsummer)):
      mean,std = classsummer[i]
      x = inputvector[i]
      prob[classval] *= calprob(x,mean,std)
  return prob
  
def prediction(summerise,inputvector):
  prob = calclassprob(summerise,inputvector)
  bestLabel,bestProb= None,-1
  for classval,pr in prob.items():
    if bestLabel is None or bestProb<pr:
      bestLabel = classval
      bestProb = pr
  return bestLabel
  
def getPrediction(summerise,testset):
  pred = []
  for i in range(len(testset)):
    result = prediction(summerise,testset[i])
    pred.append(result)
  return pred

def getAccuracy(prediction,testset):
  correct = 0
  for i in range(len(testset)):
    if prediction[i] == testset[i][-1]:
      correct +=1
  return (correct/len(testset))*100.0
  
def main():
  split = 0.67
  filename = 'naivedata.csv'
  dataset = load_data(filename)
  train_set,test_set = split_data(dataset,split)
  summerise  = summerizeByclass(train_set)
  prediction = getPrediction(summerise,test_set)
  y_pred = []
  for i in range(len(test_set)):
    y_pred.append(test_set[i][-1])
  accuracy = getAccuracy(prediction,test_set)
  print('classification report',classification_report(prediction,y_pred))
  print('confusion matrix',confusion_matrix(prediction,y_pred))

main()
