import csv
import math

def load_data(filename):
  with open(filename) as csvfile:
    lines = csv.reader(csvfile)
    dataset = list(lines)
    header = dataset.pop(0)
    return dataset,header

class Node:
  def __init__(self,attribute):
    self.attribute = attribute
    self.child =[]
    self.answer = ""

def entropy(S):
  attr = list(set(S))
  if len(attr)==1:
    return 0
  counts = [0,0]
  for i in range(2):
    counts[i] = sum([1 for x in S if attr[i]==x])/(len(S)*1.0) 
  sums = 0
  for cnt in counts:
    sums += (-1)*cnt*math.log(cnt,2)
  return sums

def sub_table(data,col,delete):
  coldata = [row[col] for row in data]
  attr =   list(set(coldata))
  counts = [0]*len(attr)
  r = len(data)
  c = len(data[0])
  for x in range(len(attr)):
    for y in range(r):
      if data[y][col] == attr[x]:
        counts[x]+=1
  dic = {}      
  for x in range(len(attr)):
    dic[attr[x]] = [[0 for i in range(c)] for j in range(counts[x])]
    pos =0
    for y in range(r):
      if data[y][col] == attr[x]:
        if delete:
          del data[y][col]
        dic[attr[x]][pos] = data[y]
        pos+=1
  return attr,dic
  
def compute_gain(data,col):
  attr,dic = sub_table(data,col,delete=False)
  size = len(data)
  entr = [0]*len(attr)
  ratio = [0]*len(attr)
  total = entropy([row[-1] for row in data])
  for i in range(len(attr)):
    entr[i] = entropy([row[-1] for row in dic[attr[i]]])
    ratio[i] = len(dic[attr[i]])/(size*1.0)
    total -= ratio[i]*entr[i]
  return total

def build_tree(data,feature):
  lastcol = [row[-1] for row in data]
  if(len(set(lastcol))==1):
    node = Node("")
    node.answer = lastcol[0]
    return node
  n = len(data[0])-1
  gains = [0]*n
  for col in range(n):
    gains[col] = compute_gain(data,col)
  split = gains.index(max(gains))
  fea = feature[:split]+feature[split+1:]
  node = Node(feature[split])
  attr,dic = sub_table(data,split,delete=True)
  
  for x in range(len(attr)):
    child = build_tree(dic[attr[x]],fea)
    node.child.append((attr[x],child))
  return node
  
def print_tree(node,level):
  if node.answer != "":
    print("  "*level,node.answer)
    return
  print("  "*level,node.attribute)
  for val,n in node.child:
    print("  "*(level+1),val)
    print_tree(n,level+2)
     
def classify(node,x_test,feature):
  if node.answer != "":
    print(node.answer)
    return
  pos = feature.index(node.attribute)
  for val,n in node.child:
    if x_test[pos]==val:
      classify(n,x_test,feature)
      
      
dataset,header = load_data('data3.csv')
nodel = build_tree(dataset,header)
print_tree(nodel,0)

test,header = load_data('data3_test.csv')
for t in test:
  classify(nodel,t,header)
     
    
  
        
   
  
