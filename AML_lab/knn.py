import random
import csv
import operator
import math

def load_dataset(filename,split,train_set=[],test_set=[]):
  with open(filename) as csvfile:
    line = csv.reader(csvfile)
    dataset = list(line)
    for x in range(len(dataset)-1):
      for y in range(4):
        dataset[x][y] = float(dataset[x][y])
        if(random.random()<split):
          train_set.append(dataset[x])
        else:
          test_set.append(dataset[x])
    
def euclidean_dist(instance1,instance2,length):
  distance = 0
  for x in range(length):
    distance += pow((instance1[x]-instance2[x]),2)
  return math.sqrt(distance)
  
def getNeighbors(train_set,test_instance,k):
  distances = []
  length = len(test_instance)-1
  for x in range(len(train_set)):
    dist = euclidean_dist(train_set[x],test_instance,length)
    distances.append((train_set[x],dist))
  distances.sort(key=operator.itemgetter(1))
  neighbors = []
  for x in range(k):
    neighbors.append(distances[x][0])
  return neighbors
  
def getResponse(neighbors):
  classVotes={}
  for x in range(len(neighbors)):
    response = neighbors[x][-1]
    if response in classVotes:
      classVotes[response] +=1
    else:
      classVotes[response] = 1
  sortedvotes = sorted(classVotes.items(),key=operator.itemgetter(1),reverse=True)
  return sortedvotes[0][0]
  
def getAccuracy(test_set,prediction):
  correct=0
  for x in range(len(test_set)):
    if prediction[x] == test_set[x][-1]:
      correct +=1
  return float(correct/len(test_set))*100.0
  
def main():
  train_set = []
  test_set = []
  split = 0.67
  prediction = []
  load_dataset('KNN-input.csv',split,train_set,test_set)
  for x in range(len(test_set)):
    neighbors = getNeighbors(train_set,test_set[x],3)
    result = getResponse(neighbors)
    prediction.append(result)
  print('Accuracy',getAccuracy(test_set,prediction))
  
main()
    
        
