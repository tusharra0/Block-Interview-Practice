from collections import deque

class ConnectFour:
    def __init__(self, rows, cols, toWin):
        self.rows, self.cols, self.toWin = rows, cols, toWin
        self.grid = [['-' for _ in range(cols)] for _ in range(rows)]

    def display(self):
        for row in self.grid:
            print(' '.join(row))
        print()

    def play(self, col, color):
        for r in range(self.rows - 1, -1, -1):
            if self.grid[r][col] == '-':
                self.grid[r][col] = color
                return (r, col)
        return None  # column full

    def check_winner(self, row, col, color):
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]  # up, down, left, right
        for dr, dc in dirs:
            count = 1
            for sign in [1, -1]:  # check both directions
                r, c = row, col
                while True:
                    r += dr * sign
                    c += dc * sign
                    if 0 <= r < self.rows and 0 <= c < self.cols and self.grid[r][c] == color:
                        count += 1
                    else:
                        break
            if count >= self.toWin:
                return True
        return False


# Example
game = ConnectFour(3, 6, 5)
game.play(0, 'R')
game.play(1, 'R')
game.play(2, 'R')
game.play(3, 'R')
game.play(4, 'R')
game.display()

r, c = 0, 4
if game.check_winner(r, c, 'R'):
    print("R wins!")
else:
    print("No winner yet.")
