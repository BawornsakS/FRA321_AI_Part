from Graph import Graph
from implementation import Queue
from implementation import PriorityQueue

#List

#Creating a list - You can put different data type in one list.
l = ['A',0,'C']
#print(l)

#You can have tuples in a list
l2 = [(0,0),(0,1),(1,2)]

#Access an element in a list
#print(l2[0])       #Print the first element of the list
#print(l2[0][0])    #Print the first number of the first element of the list


#Add to a list - You can add the same element into a list
l.append(4)
l.append(4000)
l.append(4)
#print(l)

#Remove from a list - There are 2 4s in the list. Observe what happen here.
l.remove(4)
#print(l)



#Queue - from implementation.py

q = Queue()

#Add to a queue
q.put('A')          # queue = A
q.put('B')          # queue = A -> B

#Pop from a queue
#print(q.get())      # After getting, queue = B
#print(q.get())      # After getting, queue = Null



#Priority Queue

pq = PriorityQueue()

#Add to a priority queue
pq.put('A',10)      # queue = A
pq.put('B', 20)     # queue = A -> B
pq.put('C', 15)     # queue = A -> C -> B

#print(pq.get())
#print(pq.get())
#print(pq.get())



#Dictionary

graphA = Graph()
graphA.edges = {
    'A': ['B'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['E'],
    'E': ['B']
}

#Get keys
map = graphA.edges
keys = map.keys()
#print(keys)             #Dictionary will print in a random order

#Change from a dictionary to a list
listOfKeys = list(keys)
#print(listOfKeys)


#Dictionary is not sorted. We can sort it with:
sort = sorted(map)
#print(sort)




#for loop of a list - You can change from a list to a queue or a stack

for element in l:
    print (element)