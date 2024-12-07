def parse(path:str) -> list[(int, list[int])]:
    problem_data=[]

    with open(path) as f:
        for line in f:
            line = line.strip()
            if len(line) == 0: continue

            splited = line.split(':')
            solution = int(splited[0].strip())

            numbers = splited[1].strip().split(' ')
            numbers = [int(number) for number in numbers ]

            problem_data.append((solution, numbers))

    return problem_data

def add(a, b): return a+b
def mul(a, b): return a*b
def concat(a,b): return int(str(a)+str(b))

def calculate(solution:int, remaining_numbers:list[int], current_total, operators) -> int:
    if current_total > solution: return 0
    if len(remaining_numbers) == 0: return current_total if current_total == solution else 0

    for operator in operators:
        result = calculate(solution, remaining_numbers[1:], operator(current_total ,remaining_numbers[0]), operators)
        if result != 0:
            return result

    return 0

def main():
    problems = parse("./input.txt")

    total = 0

    for solution, numbers in problems:
        total += calculate(solution, numbers, 0, [add, mul])

    print(f'Challenge 1: {total}')

    #Add a concatenation operator for challenge 2
    total = 0
    for solution, numbers in problems:
        total += calculate(solution, numbers, 0, [add, mul, concat])
    print(f'Challenge 2: {total}')

if __name__ == '__main__':
    main()




