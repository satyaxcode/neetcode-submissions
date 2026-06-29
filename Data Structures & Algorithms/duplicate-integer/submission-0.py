class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        emp = []
        for i in nums:
            if i not in emp:
                emp.append(i)
            else:
                return True
        return False