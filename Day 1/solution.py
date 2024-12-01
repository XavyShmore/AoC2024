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

#Challenge 1
def distance(list1, list2):

    total = 0

    for i in range(len(list1)):
        dist_value = abs(list1[i] - list2[i])
        total += dist_value

    return total

def create_value_count_dict(values:list) -> dict[int, int]:
    value_count_dict = {}

    for value in values:
        value_count_dict[value] = value_count_dict.get(value, 0) + 1

    return value_count_dict

#Challenge 2
def similarity(list1, list2):
    value_count_dict1 = create_value_count_dict(list1)
    value_count_dict2 = create_value_count_dict(list2)

    similarity_score = 0

    for key, value in value_count_dict1.items():
        similarity_score += key * value * value_count_dict2.get(key, 0)

    return similarity_score


def main():
    list1, list2 = parse('./input.txt')

    list1.sort()
    list2.sort()

    print(f'Distance(Challenge 1): {distance(list1, list2)}')
    print(f'Similarity(Challenge 2): {similarity(list1, list2)}')


if __name__ == '__main__':
    main()