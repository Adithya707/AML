import csv
a=[]

with open('enjoysport.csv') as csvfile:
  for row in csv.reader(csvfile):
    a.append(row)
    
num_attr = len(a[0])-1
hypo = ['0']*num_attr

for i in range(0,len(a)):
  if a[i][num_attr] == 'yes':
    for j in range(num_attr):
      if hypo[j] == '0' or hypo[j] == a[i][j]:
        hypo[j] = a[i][j]
      else:
        hypo[j] = '?'
print(hypo)
