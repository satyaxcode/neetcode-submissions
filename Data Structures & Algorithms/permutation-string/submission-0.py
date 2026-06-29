#from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = defaultdict(int)
        window_count = defaultdict(int)

        for ch in s1:
            s1_count[ch] += 1
        
        k = len(s1)

        for i in range(k):
            window_count[s2[i]] += 1
        
        if window_count == s1_count:
            return True
        
        for right in range(k, len(s2)):
            left = right - k
            window_count[s2[right]] += 1

            window_count[s2[left]] -= 1
            if window_count[s2[left]] == 0:
                del window_count[s2[left]]
            
            if window_count == s1_count:
                return True
        return False