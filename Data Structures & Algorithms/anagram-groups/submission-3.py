class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strs:
            chars = [0] * 26
            for c in s:
                idx = ord(c) - ord('a')
                chars[idx] += 1
            d[tuple(chars)].append(s)

        return list(d.values())