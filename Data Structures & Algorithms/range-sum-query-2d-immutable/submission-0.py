class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for i, row in enumerate(self.matrix):
            if (i< row1) or (i>row2):
                continue
            else:
                for j, columns in enumerate(row):
                    if (j<col1) or (j>col2):
                        continue
                    else:
                        sum += columns
        return sum
            
            

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)