import csv
import random
import math

def loadcsv(filename):
    lines = csv.reader(open(filename,"r"))
    dataset = list(lines)
    for i in range(len(dataset)):
        dataset[i] = [float(x) for x in dataset[i]]
    return dataset
    
def splitdataset(dataset,splitratio):
    trainsize = int(len(dataset)* splitratio);
    trainset = []
    copy = list(dataset);
    while len(trainset)< trainsize:
          index = random.randrange(len(copy));
          trainset.append(copy.pop(index))
    return [trainset,copy]

def separatebyclass(dataset):
    separated = {}
    for i in range(len(dataset)):
         vector = dataset[i]
         if(vector[-1] not in separated):
            separated[vector[-1]] = []
         separated[vector[-1]].append(vector)
    return separated
    
def mean(numbers):
    return sum(number)/float(len(numbers)) 

def stdev(numbers):
    avg = mean(numbers)
    var = sum([pow(x-avg,2) for x in numbers])
    return math.sqrt(var)

def summerize(dataset):
    summeries = [(mean(attribute),stdev(attribute)) for attribute in zip(*dataset)];
    del summeries[-1]
    return summeries
   
def summerizebyclass(dataset):
    separated = separatebyclass(dataset);
    summeries = {}
    for classvalue,instances in separated.items():
        summeries[classvalue] = summeries(instances)
        return summeries
        
def calculateclassprobabilities(summeries,inputvector):
    probabilities = {}
    for classvalue,classsummeries in summeries.item():
        probabilites[classvalue] = 1
        for i in range(len(classsummeries)):
            mean,stdev = classsummeries[i]
            x = inputvector[i]
            probability[classvalue] *= calculateprobability(x,mean,stdev)
    return probabilities
    
def predict(summeries,inputvector):
    probabilities = calculateclassprobabilities(sumeries,inputvector)
    bestLabel,bestProb  = None,-1
    for classvalue,probability in probabilites.items()
        if bestLabel is None or probability>bestProb:
           bestProb = probability
           bestLabel = classvalue
    return bestLabel

def getPredictions(summeries,testset):
    predictions = []
    for i in range(len(testset)):
         result = predict(summeries,testset[i])
         predictions.append(result)    
    return predictions
    
def getAccuracy(testset,predictions):
    correct = 0
    for i in range(len(testset)):
        if testset[i][-1] == predictions[i]:
           correct +=1
    return (correct/float(len(testset))) * 100.0

def main():
    filename = 'naivedata.csv'
    splitratio = 0.67
    dataset = loadcsv(filename);
    trainingset,testset = splitdataset(dataset,splitratio)
    print('Split {0} into train={1} and test={2} rows'.format(len(dataset),len(trainingset),len(testset)))
    summeries = summerizebyclass(trainingset);
    predictions = getpredictions(summeries,testset)
    accuracy = getAccuracy(testset,predictions)
    print('Accuracy of the classifier is: {0}%'.format(accuracy))

main()      
