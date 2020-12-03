'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
oddCount = 0
evenCount = 0
array = [1,2,3,4,5,6]
possible = False
if len(array) & 1:
    for i in range(len(array)):
        if array[i] & 1:
            oddCount += 1 
        else:
            evenCount += 1 
    if oddCount == evenCount - 1:
        possible = True
else:
    for i in range(len(array)):
        if array[i] & 1:
            oddCount += 1 
        else:
            evenCount += 1 
    if oddCount == evenCount:
        possible = True

if possible:
    for i in range(len(array)):
        index = 0
        if i & 1 and array[i] % 2 == 0:
            for j in range(i+1, len(array)):
                if array[j] & 1:
                    index = j 
                    break 
            array[i], array[index] = array[index], array[i]
        elif i % 2 == 0 and array[i] & 1:
            for j in range(i+1, len(array)):
                if array[j] % 2 == 0:
                    index = j 
                    break 
            array[i], array[index] = array[index], array[i]
    print(array)
else:
    print("Not possible to satisfy the requirement")
