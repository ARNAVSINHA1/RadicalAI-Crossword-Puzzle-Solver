import numpy as np

def solve_crossword(puzzle, words):
    rows, cols = len(puzzle), len(puzzle[0])
    word_lengths = [len(word) for word in words]
    max_length = max(word_lengths)
    puzzle = np.array(puzzle)
    solved_puzzle = np.full((rows, cols), ' ')
    
    for i in range(rows):
        for j in range(cols):
            if puzzle[i][j] == '#':
                solved_puzzle[i][j] = '#'
            else:
                for length in range(1, max_length + 1):
                    if j + length <= cols and all(solved_puzzle[i][j+k] == ' ' or solved_puzzle[i][j+k] == word[k] for k in range(length)):
                        solved_puzzle[i][j:j+length] = list(word[:length])
                        break
    
    for i in range(cols):
        for j in range(rows):
            if puzzle[j][i] == '#':
                solved_puzzle[j][i] = '#'
            else:
                for length in range(1, max_length + 1):
                    if j + length <= rows and all(solved_puzzle[j+k][i] == ' ' or solved_puzzle[j+k][i] == word[k] for k in range(length)):
                        solved_puzzle[j:j+length, i] = list(word[:length])
                        break
    
    return solved_puzzle.tolist()
