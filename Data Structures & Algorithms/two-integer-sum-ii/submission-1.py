class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l, r = 0, len(numbers) - 1

        while l<r:
            cumsum = numbers[l] + numbers[r]
            if cumsum>target:
                r-=1
            if cumsum<target:
                l+=1
            if cumsum==target:
                return [l+1,r+1]
        return []

