import numpy as np
from Guard import Guard

def parse(path:str) -> ((int, int), np.array):
    data = []
    position = (0,0)
    with open(path) as file:
        for i, line in enumerate(file):
            characters = list(line.strip())
            if len(characters) > 0:
                for j, char in enumerate(characters):
                    if  char  == '^':
                        position = (i, j)
                        characters[j] = '.'
                data.append(characters)
    return position, np.array(data)

def calculate_number_of_loop(position, direction, level_map, visited_squares:np.array):
    total = 0

    for e in visited_squares:
        char = level_map[e[0]][e[1]]
        if char == '.':
            level_map[e[0]][e[1]] = '#'
            guard = Guard(position, direction, level_map)

            number_of_visited_squares, is_looping = guard.calculate_visited_squares()
            if is_looping:
                total+=1

            level_map[e[0]][e[1]] = '.'

    return total


def main():
    position, level_map = parse('input.txt')

    direction = (-1, 0)

    guard = Guard(position, direction, level_map)

    print(f'Visited squares (Challenge 1): {guard.calculate_visited_squares()[0]}')

    visited_squares = guard.visited_squares
    print(f'Number of loops (Challenge 2): {calculate_number_of_loop(position, direction, level_map, visited_squares)}')



if __name__ == '__main__':
    main()