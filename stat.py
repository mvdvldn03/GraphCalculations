import matplotlib.pyplot as plt
import math

data = []
y_values = []
x_values = []
for line in open('DATA'):
   if line.strip():           
       n = int(line) 
       data.append(n)
for digit in range(1,max(data)+1):
  y_values.append(data.count(digit))
  x_values.append(digit)
bins = input("Bins? ")
plt.hist(data,bins=int(bins))
plt.xlabel('Data')
plt.ylabel('Frequency')
plt.savefig('graph.png')
plt.show

data.sort()

def mean(data):
  sum = 0
  for digit in data:
    sum += digit
  return float(sum)/len(data)

def median(data):
 average = float(len(data)+1)/2 
 if (len(data)+1) % 2 == 0:
   return data[int(average)-1]
 if (len(data)+1) % 2 == 1:
   y = (data[int(float(average)-0.5)])
   z = (data[int(float(average)-1.5)])
   return float(y+z)/2

def mode(y_values):
  mode = []
  for position, item in enumerate(y_values):
    if item == max(y_values):
      mode.append(position+1)
  return mode

def standard_deviation_s(data,mean):
  total = 0
  n=len(data)
  for digit in data:
    total += ((digit-mean)**2)
  t = total/(n-1)
  return math.sqrt(t)
def standard_deviation_p(data,mean):
  total = 0
  n=len(data)
  for digit in data:
    total += ((digit-mean)**2)
  t = total/(n)
  return math.sqrt(t)

sample_or_population = input("Is the data a sample or a population? ")
if(sample_or_population == "s"):
  stdev = standard_deviation_s(data,mean(data))
if(sample_or_population == "p"):
  stdev = standard_deviation_p(data,mean(data))

def data_range(data):
  return(max(data) - min(data))

print("Center:")
print("     Mean: " + str(mean(data)))
print("     Median: " + str(median(data)))
print("     Mode/s: " + str(mode(y_values)) + "\n")
print("Spread")
print("     Range: " + str(data_range(data)))
print("     Standard Devation for " + sample_or_population + ": " + str(stdev))

print(data)
