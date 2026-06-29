class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        if nums[r] == target:
            return r
        elif nums[r] < target:
            return -1
        else:

            while l <= r:
                m = l + ((r-l) // 2)
                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    return m
            return -1
            