from itertools import combinations
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return [list(x) for x in combinations(range(1,10), k) if sum(x) == n]
