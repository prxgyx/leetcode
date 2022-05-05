class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = collections.defaultdict(set)
        c = collections.defaultdict(set)
        b = collections.defaultdict(set) # k = (1,2)
        
        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if cell != ".":
                    if cell in r[i] or cell in c[j] or cell in b[(i//3,j//3)]:
                        return False
                    r[i].add(cell)
                    c[j].add(cell)
                    b[(i//3,j//3)].add(cell)
        
        return True
                    
        
        
        
