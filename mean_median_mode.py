N = int(input())        #input the number of data elements
data = []
data = list(map(int, input().split()))      #input the data
mu = 0
for i in data:
    mu += i
mu /= N

data.sort()
if (N%2 == 0):
    median = (data[N//2 - 1] + data[N//2])/2
else:
    median = data[N//2 + 1]

list1 = [(i, data.count(i)) for i in data]          #making a list of tuples with each tuple having a data element and the count of its occurence
list1.sort(key = lambda x:x[1], reverse = True)     #arranging data according to descending order in count value

print('Mean is",mu)
print('Median is',median)
print('Mode is',list1[0][0])
    
