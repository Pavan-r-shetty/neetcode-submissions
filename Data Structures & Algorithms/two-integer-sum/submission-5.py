class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        smap = {}

        for i, num in enumerate(nums):
            diff =  target- num
            if diff in smap:
                return [smap[diff], i]
            smap[num] = i 



