b = [None, 1,2,3,4,5,6,7,8,9,10]
#This is the representation of a heap
a = b[1:]
from math import ceil, log
from collections import defaultdict

r = defaultdict(list)
i = 0
j = 0
h = 1
heap = []
while i < ceil(log(len(a), 2)):
  l = pow(2,i) + j
  p = a[j:l]
  heap.append(p)
  j = l
  i += 1
print(heap)

for i in heap[1:]:
  for j in i:
    g = b.index(j)
    r[b[g//2]].append(j)
    #print(b[g//2] , j , " ")
  
  print("")

for i,j in r.items():
  print(i , j)

res = dict(reversed(list(r.items())))
for i,j  in r.items():
  for k in range(len(j)):
    if i > j[k]:
      i,j[k] = j[k],i

 
print(res)

#setup the representation of a heap
