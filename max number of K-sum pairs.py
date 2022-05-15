class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dic = {}
        ans = 0
        for i in nums:
            if k - i in dic and dic[k - i] > 0:
                ans += 1
                dic[k - i] -= 1  
            elif i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        
        return ans
                
                
            
        
