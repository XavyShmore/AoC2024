import re

def read_file(path) -> str:
    with open(path, 'r') as f:
        return f.read()

mul_regex = r'mul\(\d{1,3},\d{1,3}\)'
do_regex = r'do\(\)'
dont_regex = r"don't\(\)"

def find_mul(text: str) -> list[str]:
    result = re.findall(mul_regex, text)
    return result if result else []

def exec_mul(text: str) -> int:
    numbers = re.findall(r'\d+', text)

    return int(numbers[0]) * int(numbers[1])

#Challenge 1
def calc_sum_of_mul(txt:str) -> int:
    mult = find_mul(txt)

    total = 0
    for m in mult:
        total += exec_mul(m)

    return total

def find_token(text:str) -> list[str]:
    result = re.findall(f"{mul_regex}|{do_regex}|{dont_regex}", text)
    return result if result else []

def is_mul(token:str):
    match = re.search(mul_regex, token)
    if match:
        return True
    return False
def is_do(token:str):
    match = re.search(do_regex, token)
    if match:
        return True
    return False
def is_dont(token:str):
    match = re.search(dont_regex, token)
    if match:
        return True
    return False

#Challenge 2
def calc_sum_of_mul_with_control(txt:str) -> int:
    tokens = find_token(txt)

    total = 0
    enabled = True

    for token in tokens:
        if is_mul(token) and enabled:
            total += exec_mul(token)
        elif is_do(token):enabled = True
        elif is_dont(token):enabled = False

    return total

def main():
    memory = read_file("./input.txt")

    print(f'Sum of multiplication (Challenge 1): {calc_sum_of_mul(memory)}')
    print(f'Sum of multiplication (Challenge 2): {calc_sum_of_mul_with_control(memory)}')


if __name__ == '__main__':
    main()