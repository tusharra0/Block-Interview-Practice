# -----------------------------
# Object-Oriented Tic-Tac-Toe
# -----------------------------

class Board:
    def __init__(self):
        self.grid = []
        for r in range(3):
            row = []
            for c in range(3):
                row.append(" ")
            self.grid.append(row)

    def show(self):
        for row in self.grid:
            print("|".join(row))
            print("-" * 5)

    def make_move(self, row, col, symbol):
        if not (0 <= row < 3 and 0 <= col < 3):
            raise ValueError("Invalid position.")
        if self.grid[row][col] != " ":
            raise ValueError("Cell already occupied.")
        self.grid[row][col] = symbol

    def is_full(self):
        for row in self.grid:
            for cell in row:
                if cell == " ":
                    return False
        return True

    def check_winner(self, symbol):
        # Check rows
        for r in range(3):
            if all(self.grid[r][c] == symbol for c in range(3)):
                return True
        # Check columns
        for c in range(3):
            if all(self.grid[r][c] == symbol for r in range(3)):
                return True
        # Check diagonals
        if all(self.grid[i][i] == symbol for i in range(3)):
            return True
        if all(self.grid[i][2 - i] == symbol for i in range(3)):
            return True
        return False


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]
        self.current = 0  # index in players list
        self.winner = None

    def switch_turn(self):
        self.current = 1 - self.current

    def play_turn(self, row, col):
        player = self.players[self.current]
        self.board.make_move(row, col, player.symbol)

        # Check for winner
        if self.board.check_winner(player.symbol):
            self.winner = player
            return

        # Check for draw
        if self.board.is_full():
            self.winner = "Draw"
            return

        # No win or draw → switch turn
        self.switch_turn()

    def play(self):
        print("Welcome to Tic-Tac-Toe!")
        while self.winner is None:
            self.board.show()
            player = self.players[self.current]
            print(f"{player.name}'s turn ({player.symbol})")

            try:
                row = int(input("Enter row (0–2): "))
                col = int(input("Enter col (0–2): "))
                self.play_turn(row, col)
            except ValueError as e:
                print(e)
                continue

        # Game ended
        self.board.show()
        if self.winner == "Draw":
            print("Game ended in a draw!")
        else:
            print(f"🎉 {self.winner.name} wins! 🎉")


if __name__ == "__main__":
    p1 = Player("Tushar", "X")
    p2 = Player("Guru", "O")
    game = Game(p1, p2)
    game.play()
