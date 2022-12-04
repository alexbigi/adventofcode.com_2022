def find_char_value(first_part, second_part):
    for char in first_part:
        if second_part.find(char) != -1:
            return ord(char) - (96 if char.islower() else 38)
    return 0


def first_task():
    total_sum = 0
    with open('input.txt') as f:
        while True:
            line: str = f.readline()
            if not line:
                break
            first_part = line.strip()[:len(line.strip()) // 2]
            second_part = line.strip()[len(line.strip()) // 2:]
            total_sum += find_char_value(first_part, second_part)
    print(total_sum)


def lines_bruteforce(three_lines_list):
    for char in three_lines_list[0]:
        if three_lines_list[1].find(char) != -1 and three_lines_list[2].find(char) != -1:
            return ord(char) - (96 if char.islower() else 38)
    return 0


def second_task():
    total_sum = 0
    three_lines_counter = 1
    three_lines_list = []
    with open('input.txt') as f:
        while True:
            line: str = f.readline()
            if not line:
                break
            three_lines_list.append(line.strip())
            three_lines_counter += 1
            if three_lines_counter > 3:
                total_sum += lines_bruteforce(three_lines_list)
                three_lines_counter = 1
                three_lines_list = []
    print(total_sum)


if __name__ == "__main__":
    first_task()
    second_task()
