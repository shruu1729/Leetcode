class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums2=sorted(nums)
        start=-1
        end=-1
        for i in range(len(nums)):
            if nums2[i]!=nums[i]:
                start=i
                break
        for i in range(len(nums)-1,-1,-1):
            if nums2[i]!=nums[i]:
                end=i
                break
        if end-start>0:
            return end-start+1 
        return 0
        
