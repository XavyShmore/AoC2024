import re

rules_regex = r'\d{1,2}\|\d{1,2}'
updates_regex = r'(\d{2}){0,1}(,\d{2})+'


#
rules:dict[str:set[str]] = {}

updates:list[list[int]] = []

def parse(path:str):
    with open(path) as file:
        for line in file:
            for match in re.findall(rules_regex, line):
                elements = match.strip().split("|")

                current_rule = rules.get(int(elements[0]), set())

                current_rule.add(int(elements[1]))
                rules[int(elements[0])] = current_rule

            if re.match(updates_regex, line):
                values = line.strip().split(",")
                values = [int(value) for value in values]
                updates.append(values)

def calculate_middle_of_correctly_ordered():

    total = 0

    for update in updates:
        update_is_valid = True
        seen_pages = set()
        for page in update:
            seen_pages.add(page)

            pages_that_cant_be_seen_before = rules.get(page, set())

            intersection = seen_pages.intersection(pages_that_cant_be_seen_before)

            if len(intersection):
                update_is_valid = False

        if update_is_valid:
            total += update[int((len(update)-1)/2)]
        else:
            pass

    return total


def main():
    parse("input.txt")

    print(f'Challenge 1: {calculate_middle_of_correctly_ordered()}')

if __name__ == "__main__":
    main()