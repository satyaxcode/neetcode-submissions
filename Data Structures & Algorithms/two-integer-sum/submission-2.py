class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenMap = {}

        for idx, num in enumerate(nums):
            req = target - num
            if req in seenMap:
                return [seenMap[req], idx]

            seenMap[num] = idx
            

        