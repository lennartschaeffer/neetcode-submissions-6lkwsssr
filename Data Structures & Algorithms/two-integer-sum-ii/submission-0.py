class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two numbers such that they add up to target
        # index1 < index2

        # use two pointers
        # if left + right > target, decrement right
        # left + right < target, increment left
        # if they are equal to target, return indices + 1

        left = 0
        right = len(numbers)-1

        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return [left + 1, right + 1]

        