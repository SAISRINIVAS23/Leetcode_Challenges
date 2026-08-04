class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash={}
        res=majority=0
        for n in nums:
            hash[n]=hash.get(n,0)+1
            if  hash[n]>majority:
                res=n
                majority=hash[n]

        return res