class Sudoku:
    def solveSudoku(grid, row, col, N):
        if row == N - 1 and col == N:
            return True
        if col == N:
            row += 1
            col = 0
        if grid[row][col] != 0:
            return Sudoku.solveSudoku(grid, row, col + 1, N)
        for num in range(1, N + 1):
            if Sudoku.isSafe(grid, row, col, num, N):
                grid[row][col] = num
                if Sudoku.solveSudoku(grid, row, col + 1, N):
                    return True
            grid[row][col] = 0
        return False
    
    
    def print_grid(grid, N):
        for i in range(N):
            for j in range(N):
                print(grid[i][j], end=" ")
            print()


    def isSafe(grid, row, col, num, N):
        for x in range(N):
            if grid[row][x] == num:
                return False
        for x in range(N):
            if grid[x][col] == num:
                return False

        startRow = row - (row % 3)
        startCol = col - (col % 3)
        for i in range(3):
            for j in range(3):
                if grid[i + startRow][j + startCol] == num:
                    return False
        return True
    

if __name__ == "__main__":
    N = 9  # Sudoku grid size
    grid = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]
    ]
    if Sudoku.solveSudoku(grid, 0, 0, N):
        Sudoku.print_grid(grid, N)
    else:
        print("No solutions :(")