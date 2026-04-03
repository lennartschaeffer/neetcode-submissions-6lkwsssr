class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        what determines when you slide the window?
            as long as we dont have all the characters, expand
            once we do, shrink
            OUZODYXAZXY    XYZ
            once we shrunk and there is a new min, update the left pointer to point at
            the right, then start moving the right one again
        """

        l = 0
        longest_len = float('inf')
        longest = ""
        t_chars = {}
        window = {}
        match_count = 0
        for c in t:
            t_chars[c] = t_chars.get(c, 0) + 1
        unique_t = len(t_chars.keys())
        # OUZODYXAZV   XYZ
             
        for r in range(len(s)):
            curr = s[r]
            window[curr] = window.get(curr, 0) + 1
            if curr in t_chars and t_chars[curr] == window[curr]:
                match_count += 1
            print(match_count)
            while match_count == unique_t and l <= r:
                sub = s[l:r+1]
                if len(sub) < longest_len:
                    longest = s[l:r+1]
                    print(longest)
                    longest_len = len(sub)
                window[s[l]] -= 1
                if s[l] in t_chars and window[s[l]] < t_chars[s[l]]:
                    match_count -= 1
                l += 1
        
        return longest
        



