class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[0]*9
        column=[0]*9
        sub=[0]*9
        for i in range(9):
            for j in range(9):
                char=board[i][j]
                if char=='.':
                    continue
                num=int(char)
                box=(i//3)*3+(j//3)
                if (row[i]&(1<<num)) or (column[j]&(1<<num)) or (sub[box]&(1<<num)):
                    return False
                row[i]=row[i]|(1<<num)
                column[j]=column[j]|(1<<num)
                sub[box]=sub[box]|(1<<num)
        return True
