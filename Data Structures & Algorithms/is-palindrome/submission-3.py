class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # use two pointers, one starting at the start and one at the end
        # now, if left or right is a non-alphanumeric, move it right or left
        # otherwise, if s[left] != s[right], return false
        # make sure to convert to lower case

        # "Was it a car or a cat I saw?"
        
        left = 0
        right = len(s)-1

        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            else:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1

        return True
                

        
        