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

def main():
    position, level_map = parse('input.txt')

    guard = Guard(position, (-1, 0), level_map)

    print(f'Visited squares (Challenge 1): {guard.calculate_visited_squares()}')



if __name__ == '__main__':
    main()