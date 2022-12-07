def task():
    def string_checker(my_line):
        for index, value in enumerate(my_line):
            if len(set(my_line[index: index + 4])) == 4:
                return index + 4

    def string_checker_second(my_line):
        for index, value in enumerate(my_line):
            if len(set(my_line[index: index + 14])) == 14:
                return index + 14

    with open("input.txt") as f:
        while True:
            line = f.readline()
            if not line:
                break
            print(string_checker(line.rstrip()))
            print(string_checker_second(line.rstrip()))


if __name__ == "__main__":
    task()
