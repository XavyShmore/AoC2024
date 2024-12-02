import sys


def parse(path) ->  list[list[int]]:
    data = []

    with open(path) as file:
        for line in file:
            numbers = line.strip().split(' ')
            if numbers is not None:
                level = []
                for number in numbers:
                    number = int(number)
                    level.append(number)

                data.append(level)

    return data

def is_adjacent_diff_safe(e1:int, e2:int) ->bool:
    diff = abs(e1 - e2)

    if 1 <= diff <= 3:
        return True

    return False

def is_increasing(e1:int, e2:int) ->bool:
    return e1 < e2

def check_level(level: list[int]) -> bool:

    is_level_increasing = is_increasing(level[0], level[1])

    for i in range(len(level)-1):
        if is_level_increasing != is_increasing(level[i], level[i+1]): return False
        if not is_adjacent_diff_safe(level[i], level[i+1]): return False

    return True

#Challenge 1
def safe_report_count(levels):
    total = 0

    for level in levels:
        if check_level(level): total += 1
    return total


def main():
    reports = parse('./input.txt')

    print(f'Safe Reports (Challenge 1): {safe_report_count(reports)}')


if __name__ == '__main__':
    main()