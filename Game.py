import random

class CrosswordGame:
    def __init__(self, words):
        self.words = words
        self.board = [[' ' for _ in range(10)] for _ in range(10)]
    
    def generate_board(self):
        for word in self.words:
            placed = False
            while not placed:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                direction = random.choice(['horizontal', 'vertical'])
                if self.can_place_word(word, x, y, direction):
                    self.place_word(word, x, y, direction)
                    placed = True
    
    def can_place_word(self, word, x, y, direction):
        if direction == 'horizontal':
            if y + len(word) > 10:
                return False
            for i in range(len(word)):
                if self.board[x][y+i] != ' ' and self.board[x][y+i] != word[i]:
                    return False
        elif direction == 'vertical':
            if x + len(word) > 10:
                return False
            for i in range(len(word)):
                if self.board[x+i][y] != ' ' and self.board[x+i][y] != word[i]:
                    return False
        return True
    
    def place_word(self, word, x, y, direction):
        if direction == 'horizontal':
            for i in range(len(word)):
                self.board[x][y+i] = word[i]
        elif direction == 'vertical':
            for i in range(len(word)):
                self.board[x+i][y] = word[i]
    
    def print_board(self):
        for row in self.board:
            print(' '.join(row))

# Example usage
words = ['python', 'code', 'programming', 'crossword']
game = CrosswordGame(words)
game.generate_board()
game.print_board()
