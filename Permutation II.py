class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        def dfs(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            for i in counter:
                if counter[i] != 0:
                    curr.append(i)
                    counter[i] -= 1
                    dfs(curr)
                    j = curr.pop()
                    counter[j] += 1
        dfs([])
        return res
        
