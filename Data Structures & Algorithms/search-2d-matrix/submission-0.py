class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target<matrix[0][0] or target>matrix[-1][-1]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        l1, l2 = 0, 0
        while l1<=m:
            mid1 = (m+l1)//2
            if matrix[mid1][0]<=target<=matrix[mid1][-1]:
                while l2<=n:
                    mid2 = (n+l2)//2
                    if matrix[mid1][mid2]<target:
                        l2 = mid2+1
                    elif matrix[mid1][mid2]>target:
                        n = mid2-1
                    else:
                        return True
                break
            elif matrix[mid1][-1]<target:
                l1 = mid1+1
            else:
                m = mid1-1

        return False
            
