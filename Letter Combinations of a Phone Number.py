class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
               '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
            
        if len(digits) == 0:
            return []

        comb = ['']
        for i in digits:
            tmp = []
            for j in comb:
                for k in mapping[i]:
                    tmp.append(j + k)
            comb = tmp
        return comb
