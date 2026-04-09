class Solution:
    def isValid(self, s: str) -> bool:
        """
            if we read an opening bracket, append corresponding closing bracket to the stack
            once we read a closing bracket, it should match the bracket on top of the stack
            if not, return false
            if we finish the loop, return len(stack) == 0
        """

        mapping = {
            '{': '}',
            '(': ')',
            '[': ']'
        }

        stack = []

        for c in s:
            if c in mapping.keys():
                stack.append(mapping[c])
            else:
                if len(stack):
                    top = stack.pop()
                    if top != c:
                        return False
                else:
                    return False
        
        return len(stack) == 0