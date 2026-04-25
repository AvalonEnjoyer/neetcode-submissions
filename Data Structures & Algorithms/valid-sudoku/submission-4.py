class Solution:
    # Solution 2 - 
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i:set() for i in range(9)}
        cols = {i:set() for i in range(9)}
        boxes = {i:set() for i in range(9)}
        for row in range(9):
            for col in range(9):
                value = board[row][col]
                if value == ".":
                    continue
                box_index = (row//3) * 3 + col//3
                if value in rows[row] or value in cols[col] or value in boxes[box_index]:
                    return False
                rows[row].add(value)
                cols[col].add(value)
                boxes[box_index].add(value)
        return True
    # # Solution 1 - 100% runtime and 94.33% memory
    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    #     unique_elements_rows = {}
    #     unique_elements_cols = {}
    #     unique_elements_boxes = {}
    #     for i, row in enumerate(board):
    #         unique_elements_rows.setdefault(i, [])
    #         for j in range(len(row)):
    #             unique_elements_cols.setdefault(j, [])
    #             box_index = (i // 3) * 3 + j // 3
    #             unique_elements_boxes.setdefault(box_index, [])
    #             if row[j] != ".":
    #                 if row[j] not in unique_elements_rows[i]:
    #                     unique_elements_rows[i].append(row[j])
    #                 else:
    #                     return False
    #                 if row[j] not in unique_elements_cols[j]:
    #                     unique_elements_cols[j].append(row[j])
    #                 else:
    #                     return False
    #                 if row[j] not in unique_elements_boxes[box_index]:
    #                     unique_elements_boxes[box_index].append(row[j])
    #                 else:
    #                     return False
    #     return True