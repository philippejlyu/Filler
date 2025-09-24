
class Filler:
    rows = 8
    cols = 8
    colors = ['🟥', '🟩', '🟨', '🟦', '🟪', '⬛️']
    board = []
    player1Turn = True
    player2Turn = False
    player1Area = [] # Array of 2d coordinates
    player2Area = [] # Array of 2d coordinates
    player1Color = ''
    player2Color = ''

    def __init__(self):
        self.board = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]
        self.player1Turn = True
        self.randomly_fill_board()
        self.player1Area = [(0, 7)]
        self.player2Area = [(7, 0)]

    def print_board(self):
        print("  " + " ".join(str(i) for i in range(self.cols)))
        for idx, row in enumerate(self.board):
            print(f"{idx} " + " ".join(row))
        print()

    def is_game_over(self):
        total_area = len(self.player1Area) + len(self.player2Area)
        return total_area == self.rows * self.cols
    
    def calculate_winner(self):
        if len(self.player1Area) > len(self.player2Area):
            return "Player 1 wins!"
        elif len(self.player2Area) > len(self.player1Area):
            return "Player 2 wins!"
        else:
            return "It's a tie!"

    def randomly_fill_board(self):
        import random
        for r in range(self.rows):
            for c in range(self.cols):
                available_colors = self.colors[:]
                if r > 0 and self.board[r - 1][c] in available_colors:
                    available_colors.remove(self.board[r - 1][c])
                if c > 0 and self.board[r][c - 1] in available_colors:
                    available_colors.remove(self.board[r][c - 1])
                self.board[r][c] = random.choice(available_colors)
        # Ensure that the 2 starting postions are different colors
        if self.board[0][7] == self.board[7][0]:
            available_colors = self.colors[:]
            if self.board[0][6] in available_colors:
                available_colors.remove(self.board[0][6])
            if self.board[1][7] in available_colors:
                available_colors.remove(self.board[1][7])
            if self.board[6][0] in available_colors:
                available_colors.remove(self.board[6][0])
            if self.board[7][1] in available_colors:
                available_colors.remove(self.board[7][1])
            if available_colors:
                self.board[7][0] = random.choice(available_colors)
        self.print_board()

    def emoji_color_to_string(self, emoji):
        color_map = {
            '🟥': 'Red',
            '🟩': 'Green',
            '🟨': 'Yellow',
            '🟦': 'Blue',
            '🟪': 'Purple',
            '⬛️': 'Black'
        }
        return color_map.get(emoji, 'Unknown')
    
    def expand_area(self, area, color):
        # First set all the current area to the new color
        for r, c in area:
            self.board[r][c] = color
        # BFS
        from collections import deque
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set(area)
        queue = deque(area)
        while queue:
            r, c = queue.popleft()
            for x, y in directions:
                nr, nc = r + x, c + y
                if 0 <= nr < self.rows and 0 <= nc < self.cols and self.board[nr][nc] == color:
                    if (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
        return list(visited)
    
    def player1_move(self, color):
        if color == self.player2Color:
            print("Invalid move: Cannot choose opponent's color.")
            return False
        self.player1Color = color
        self.player1Area = self.expand_area(self.player1Area, color)
        self.player1Turn = False
        self.player2Turn = True
        if self.is_game_over():
            # print(self.calculate_winner())
            pass
        return True
    
    def player2_move(self, color):
        if color == self.player1Color:
            print("Invalid move: Cannot choose opponent's color.")
            return False
        self.player2Color = color
        self.player2Area = self.expand_area(self.player2Area, color)
        self.player2Turn = False
        self.player1Turn = True
        if self.is_game_over():
            # print(self.calculate_winner())
            pass
        return True

if __name__ == '__main__':
    game = Filler()

    while True:
        if game.player1Turn:
            print("Player 1's turn.")
            color = input(f"Choose a color {game.colors}: ")
            if color in game.colors:
                if game.player1_move(color):
                    game.player1Turn = False
                    game.player2Turn = True
            else:
                print("Invalid color. Try again.")
        elif game.player2Turn:
            print("Player 2's turn.")
            color = input(f"Choose a color {game.colors}: ")
            if color in game.colors:
                if game.player2_move(color):
                    game.player2Turn = False
                    game.player1Turn = True
            else:
                print("Invalid color. Try again.")

