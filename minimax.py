import copy
import math

class Minimax:
    def __init__(self, game, player, depth=30):
        self.game = game
        self.player = player  # 'player1' or 'player2'
        self.depth = depth
        self.opponent = 'player2' if player == 'player1' else 'player1'

    def evaluate(self, game_state):
        """Evaluate the board state based on area controlled by the player."""
        player1_area = len(game_state.player1Area)
        player2_area = len(game_state.player2Area)
        if self.player == 'player1':
            return player1_area - player2_area
        else:
            return player2_area - player1_area
        
    def is_game_over(self, game_state):
        """Check if the game is over."""
        total_area = len(game_state.player1Area) + len(game_state.player2Area)
        return total_area >= game_state.rows * game_state.cols

    def get_valid_colors(self, game_state):
        """Return list of colors that allow the player to expand their area."""
        opponent_color = game_state.player2Color if game_state.player1Turn else game_state.player1Color
        valid_colors = []
        player_area = game_state.player1Area if game_state.player1Turn else game_state.player2Area
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for color in game_state.colors:
            if color == opponent_color:
                continue
            # Check if the color allows expansion
            can_expand = False
            for r, c in player_area:
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < game_state.rows and 0 <= nc < game_state.cols:
                        if game_state.board[nr][nc] == color and (nr, nc) not in player_area:
                            can_expand = True
                            break
                if can_expand:
                    break
            if can_expand:
                valid_colors.append(color)

        return valid_colors

    def simulate_move(self, game_state, color):
        """Simulate a move for the current player and return the new game state."""
        game_copy = copy.deepcopy(game_state)
        if game_copy.player1Turn:
            game_copy.player1_move(color)
        else:
            game_copy.player2_move(color)
        return game_copy

    def minimax(self, game_state, depth, alpha, beta, maximizing):

        if self.is_game_over(game_state):
            return self.evaluate(game_state), None
        
        if depth == 0:
            return self.evaluate(game_state), None
        
        valid_colors = self.get_valid_colors(game_state)
        if not valid_colors:
            # We want to select the color that minimizes the opponent's options
            maximizing = not maximizing
            # This should be all colors except p1 and p2 colors
            valid_colors = [color for color in game_state.colors if color != game_state.player1Color and color != game_state.player2Color]

        if maximizing:
            max_eval = -math.inf
            best_color = None
            for color in valid_colors:
                new_state = self.simulate_move(game_state, color)
                eval_score, _ = self.minimax(new_state, depth - 1, alpha, beta, False)
                if eval_score > max_eval:
                    max_eval = eval_score
                    best_color = color
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break
            return max_eval, best_color
        else:
            min_eval = math.inf
            best_color = None
            for color in valid_colors:
                new_state = self.simulate_move(game_state, color)
                eval_score, _ = self.minimax(new_state, depth - 1, alpha, beta, True)
                if eval_score < min_eval:
                    min_eval = eval_score
                    best_color = color
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break
            return min_eval, best_color

    def best_move(self):
        """Return the best color for the current player's turn."""
        _, best_color = self.minimax(self.game, self.depth, -math.inf, math.inf, True)
        print(f"Best move for {self.player}: {best_color}")
        return best_color
    
if __name__ == '__main__':
    # Example usage with a hypothetical Filler game instance
    from Filler import Filler  # Assuming Filler class is defined in Filler.py

    game = Filler()
    ai_player = Minimax(game, 'player1', depth=12)
    ai_player2 = Minimax(game, 'player2', depth=12)

    while True:
        if game.is_game_over():
            print("Game Over!")
            print(game.calculate_winner())
            break
        if game.player1Turn:
            print("AI Player 1's turn.")
            best_color = ai_player.best_move()
            if best_color:
                print(f"AI chooses color: {best_color}")
                game.player1_move(best_color)
                game.player1Turn = False
                game.player2Turn = True
                game.print_board()
            else:
                print("No valid moves available for AI.")
                exit()
                break
        elif game.player2Turn:
            print("Player 2's turn.")
            best_color = ai_player2.best_move()
            if best_color:
                game.player2_move(best_color)
                game.player2Turn = False
                game.player1Turn = True
                game.print_board()
            else:
                print("Invalid color. Try again.")
                exit()