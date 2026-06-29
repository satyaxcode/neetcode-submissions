class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        emp = set()
        for i in nums:
            if i in emp:
                return True
            emp.add(i)
        return False