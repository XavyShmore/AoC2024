

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
    return 1 <= diff <= 3

def is_increasing(e1:int, e2:int) ->bool:
    return e1 < e2

def list_without_index(l: list[int], index) -> list[int]:
    return [e for i, e in enumerate(l) if i != index]

def check_level_basic(level: list[int]) -> bool:

    is_level_increasing = is_increasing(level[0], level[1])
    is_safe_enough = True

    for i in range(len(level)-1):
        if is_level_increasing != is_increasing(level[i], level[i+1]): is_safe_enough = False
        if not is_adjacent_diff_safe(level[i], level[i+1]): is_safe_enough = False

    return is_safe_enough


def check_level_tolerate_error(level: list[int], max_error = 0, error_count = 0) -> bool:
    if check_level_basic(level): return True
    if max_error == error_count: return False

    for i in range(len(level)):
        if check_level_tolerate_error(list_without_index(level, i), max_error, error_count + 1) : return True

    return False

#Challenge 1 and 2
def safe_report_count(reports, tolerated_unsafe_levels):
    total = 0
    for report in reports:
        if check_level_tolerate_error(report, tolerated_unsafe_levels): total += 1
    return total


def main():
    reports = parse('./input.txt')

    print(f'Safe Reports (Challenge 1): {safe_report_count(reports, 0)}')
    print(f'Safe Reports (Challenge 2): {safe_report_count(reports, 1)}')


if __name__ == '__main__':
    main()