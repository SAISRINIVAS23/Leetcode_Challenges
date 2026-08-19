class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        ex=n*(n+1)//2
        actual=sum(nums)
        return ex-actual
        