class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #loop through the lists and check the range,
        #if target falls in between list[0] and list[-1]
        #then we know we have to search that list
        #from there we can perform binary search?????

        for l in matrix:
            if l[0] <= target <= l[-1]:
                lo,hi = 0, len(l)-1
                while lo <= hi:
                    mid = (lo+hi) // 2
                    if l[mid] < target:
                        lo = mid + 1
                    elif l[mid] > target:
                        hi = mid - 1
                    else:
                        return True

        return False