nums = [2, 7, 3, 1, 5, 2, 6 ,2]
dq = []
k = 4
max_numbers = []
for i in range(len(nums)):
    while dq and nums[i] >= nums[dq[-1]]:
        dq.pop()
    dq.append(i)
    if i >= k and dq and dq[0] <= i - k:
        dq.pop(0)
    if i >= k - 1:
        max_numbers.append(nums[dq[0]])

print(max_numbers)