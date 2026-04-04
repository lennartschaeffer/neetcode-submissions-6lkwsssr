class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        note: its a permutation, not a substring, so the whole thing has to match
        so the logic would be:
            store current window chars in hashmap
            as long as all chars in current window are in s1 we can expand
            if we read a char thats not in s1 we shrink, or if a char count in the 
            window is greater than s1 char count for that character
        """

        window = {}
        s1_chars = {}

        for c in s1:
            s1_chars[c] = s1_chars.get(c,0) + 1
        
        l = 0

        for r in range(len(s2)):
            char = s2[r]
            window[char] = window.get(char,0) + 1
            prev = s2[l]
            while l < r and (prev not in s1_chars or window[prev] > s1_chars[prev]):
                if window[prev] > 1:
                    window[prev] -= 1
                else:
                    del window[prev]
                l += 1
                prev = s2[l]
                
            if window == s1_chars: #at some point this would be true
                return True
        
        return False