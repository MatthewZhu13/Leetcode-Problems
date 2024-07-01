class Solution(object):
    def topKFrequent(self, nums, k):
        
        #Create a dictionary to find how many times each number occurs
        occurences = {}
        for i in nums:
            if i in occurences:
                occurences[i] += 1
            
            else:
                occurences[i] = 1

        
        #Create a 2D array where each index represents how many times each number in nums occurs:
        #nums = [1, 1, 1, 2, 2, 3]
        #arr = 1   2   3   4  5 (1 based indexing that represents how many times each number occurs)
        #.    [[3] [2] [3] [] []]
        arr = [[] for i in range(len(nums))]
        for x, y in occurences.items():
            arr[y - 1].append(x)
        
        #Iterate from the end of arr and add k elements starting from the last subarray to ans 
        ans = []
        for i in range(len(arr), 0, -1):
            for j in arr[i - 1]:
                if k == 0:
                    break

                ans.append(j)
                k -= 1
        
        return ans
