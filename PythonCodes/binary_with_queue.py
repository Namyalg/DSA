res = []
q = ["1"]

n = 10
for i in range(10):
    w = q.pop(0)
    res.append(w)
    q.append(w+"0")
    q.append(w+"1")

print(res)