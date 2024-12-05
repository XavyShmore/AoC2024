import numpy as np

def parse(path:str):
    data = []
    with open(path) as file:
        for line in file:
            characters = list(line.strip())
            if len(characters) > 0:
                data.append(characters)
    return np.array(data)

def coord_in_grid(position:(int, int), grid:np.ndarray):
    return 0 <= position[0] < grid.shape[0] and 0 <= position[1] < grid.shape[1]

def detect_word(word, grid, position: (int, int), direction:(int, int)):
    for i, letter in enumerate(word):
        new_coords = (position[0] + direction[0] * i, position[1] + direction[1] * i)
        if not coord_in_grid(new_coords, grid): return False
        if not letter == grid[new_coords]: return False
    return True

def count_word(word, grid, directions):
    total = 0
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            for direction in directions:
                is_word = detect_word(word, grid, (i, j), direction)
                total += is_word

    return total

def search_xmas(grid):
    searched_word = "XMAS"
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    return count_word(searched_word, grid, directions)

def detect_x_mas(grid):
    searched_word = "MAS"
    directions = [(1, 1), (-1, -1)]

    total = 0

    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            for direction in directions:
                if detect_word(searched_word, grid, (i, j), direction):
                    if detect_word(searched_word, grid, ( i + direction[0] * (len(searched_word) - 1), j ), (-1 * direction[0], 1 * direction[0])): total += 1
                    elif detect_word(searched_word, grid, (i, j + direction[1] * (len(searched_word) - 1)), (1 * direction[0], -1 * direction[0])): total += 1

    return total


def main():
    grid = parse("input.txt")

    print(f'Challenge 1: {search_xmas(grid)}')
    print(f'Challenge 2: {detect_x_mas(grid)}')

if __name__ == "__main__":
    main()
