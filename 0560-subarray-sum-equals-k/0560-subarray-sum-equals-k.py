class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap={0:1}
        total=count=0
        for n in nums:
            total+=n
            if total-k in hashmap:
                count+=hashmap[total-k]

            hashmap[total]=1+hashmap.get(total,0)
        
        return count
