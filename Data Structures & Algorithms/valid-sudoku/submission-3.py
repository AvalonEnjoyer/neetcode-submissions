class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        unique_elements_rows = {}
        unique_elements_cols = {}
        unique_elements_boxes = {}
        for i, row in enumerate(board):
            unique_elements_rows.setdefault(i, [])
            for j in range(len(row)):
                unique_elements_cols.setdefault(j, [])
                box_index = (i // 3) * 3 + j // 3
                unique_elements_boxes.setdefault(box_index, [])
                if row[j] != ".":
                    if row[j] not in unique_elements_rows[i]:
                        unique_elements_rows[i].append(row[j])
                    else:
                        return False
                    if row[j] not in unique_elements_cols[j]:
                        unique_elements_cols[j].append(row[j])
                    else:
                        return False
                    if row[j] not in unique_elements_boxes[box_index]:
                        unique_elements_boxes[box_index].append(row[j])
                    else:
                        return False
        return True