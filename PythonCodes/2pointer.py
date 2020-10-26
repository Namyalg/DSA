a = [1,2,3,4,5,9,10,83,383]
f = 0
l = len(a)-1

#use hash map or the 2 pointers method
def hash_2_sum():
    d = dict()
    s = 9
    store_sum = []
    for i in a:
        if (s-i) in d:
            store_sum.append(i)
            store_sum.append(s-i)
            break
        else:
            d[i] = 1
    return(store_sum)

def two_ptr():
    #works only for a sorted array, so there is an overhead of ) O(nlogn)
    #best might be to use the hash map technique as lookup takes constant time for a hashmap
    a = [1,2,3,4,5,9,10,83,383]
    s = 10
    a = sorted(a)
    p1 = 0
    p2 = len(a) - 1
    while(p2 >= p1):
        if a[p1] + a[p2] == s:
            return([a[p1], a[p2]])
        elif a[p1] + a[p2] > s:
            p2 = p2 - 1
        else:
            p1 = p1 + 1
    return("None")
print(hash_2_sum())
print(two_ptr())
