def task():
    def check_string(line_striped: str):
        for index, char in enumerate(line_striped):
            if set(line_striped[index:index + 4]).__len__() == 4:
                return index + 4

    def check_string_second(line_striped: str):
        for index, char in enumerate(line_striped):
            if set(line_striped[index:index + 14]).__len__() == 14:
                return index + 14

    with open('input.txt') as f:
        while True:
            line: str = f.readline()
            if not line:
                break
            print(check_string(line.rstrip()))
            print(check_string_second(line.rstrip()))

if __name__ == "__main__":
    task()
