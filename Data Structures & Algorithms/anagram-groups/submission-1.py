class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for str in strs:
            count = [0] * 26
            for chr in str:
                count[ord(chr) - ord("a")] += 1

            res[tuple(count)].append(str)

        return list(res.values())