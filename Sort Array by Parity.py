class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l=[]
        l1=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                l.append(nums[i])
            else:
                l1.append(nums[i])
        return l+l1
            
        
