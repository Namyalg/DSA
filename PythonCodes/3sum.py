class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''This is an O(n**2) solution'''
        d = dict()
        l = []
        '''for i in range(len(nums)):
            s = -1*nums[i]
            for k in range(i+1, len(nums)):
                if (s - nums[k]) in d:
                    p = sorted([nums[i],nums[k], s - nums[k]])
                    if p not in l:
                        l.append(p)
                else:
                    d[nums[k]] = 1'''
        
        '''This is the login anyways, set this and use 2pointer method'''
        for i in range(len(nums)):
            s = nums[i]*-1
            num = sorted(nums)
            f = 0
            e = len(nums) - 1
            print(l)
            while f < e:
                if num[f] + num[e] == s:
                    d = sorted([num[f], num[e], s])
                    if d not in l:
                        l.append(d)
                        break
                elif num[f] + num[e] < s:
                    f += 1
                elif num[f] + num[e] > s:
                    e = e - 1
        return(l)
        
                    
        
