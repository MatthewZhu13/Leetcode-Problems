class Solution(object):
    def intersect(self, nums1, nums2):
        ans = []
        nums1Freq = {}
        for i in nums1:
            if i in nums1Freq:
                nums1Freq[i] += 1
            
            else:
                nums1Freq[i] = 1
        
        for i in nums2:
            if i in nums1Freq and nums1Freq[i] > 0:
                ans.append(i)
                nums1Freq[i] -= 1
            
        return ans


        
