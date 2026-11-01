class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nummap = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in nummap:
                return [nummap[need], i]
            nummap[num] = i

        