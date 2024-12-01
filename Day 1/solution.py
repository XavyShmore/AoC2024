import sys


def parse(path) -> (list[int], list[int]):
    list1 = []
    list2 = []

    with open(path) as file:
        for line in file:
            numbers = line.strip().split('   ')
            if numbers is not None:
                list1.append(int(numbers[0]))
                list2.append(int(numbers[1]))

    return list1, list2




def main():
    list1, list2 = parse('./input.txt')

    list1.sort()
    list2.sort()

    total = 0

    for i in range(len(list1)):
        dist_value = abs(list1[i] - list2[i])
        total += dist_value

    print(total)




if __name__ == '__main__':
    main()