#This is the brute force approach
'''a = [1,3,8,6,5,4,20,9]
st =[a[0]]
q = []
for i in range(len(a)):
    fl = 0
    #the complexity here will soley depend on this inner loop
    #it will be the sum of all the n + n-1 + n-2 + n-3 ....and so on
    for j in range(i, len(a)):
        if a[j] > a[i]:
            fl = 1
            q.append(a[j])
            break
    if fl == 0:
        q.append(-1)

print(q) '''

a = [2, 4, 7, 1, 6, 8, 11, 5, 14, 12]
st = [a[0]]
nm = []
for i in range(1 ,len(a)):
   //u have to pop only till the elements in the stack are greater than it 
    while(st and a[i] > st[-1]):
           st.pop()
           nm.append(a[i])
       
    st.append(a[i])

while(st):
    st.pop()
    nm.append(-1)
print(nm)

########IMPORTANT THIS IS#################
''' while(st and a[i] > st[-1]):
           st.pop()
           nm.append(a[i])'''