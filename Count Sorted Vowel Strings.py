class Solution:
    def countVowelStrings(self, n: int) -> int:
        arr=[1,1,1,1,1]
        s=5
        for i in range(n-1):
            s=1
            for j in range(1,5):
                arr[j]+=arr[j-1]
                s+=arr[j]
        return s
