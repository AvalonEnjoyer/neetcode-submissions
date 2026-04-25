class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target<matrix[0][0] or target>matrix[-1][-1]:
            return False
        l, r = 0, len(matrix)-1
        found = False
        while l<=r:
            mid1 = (r+l)//2
            if matrix[mid1][0]<=target<=matrix[mid1][-1]:
                found = True
                break
            elif matrix[mid1][-1]<target:
                l = mid1+1
            else:
                r = mid1-1
        if found:
            l, r = 0, len(matrix[0])-1
            while l<=r:
                mid = (r+l)//2
                if matrix[mid1][mid]<target:
                    l = mid+1
                elif matrix[mid1][mid]>target:
                    r = mid-1
                else:
                    return True
        return False
            
