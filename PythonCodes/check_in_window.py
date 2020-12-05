a = [1,2,3,5,6,2,34,5,10,2]
k = 3
target = 3
alltargets = []
for i in range(len(a)-k+1):
    window = a[i : i+k]
    if target in window:
        alltargets.append(window)

print(alltargets)
