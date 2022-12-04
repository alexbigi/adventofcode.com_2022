def first():
    max_value: int = 0
    now_value: int = 0
    with open('input.txt') as f:
        while True:
            line = f.readline()
            if not line:
                break
            if line != "\n":
                now_value += int(line.strip())
            else:
                max_value = now_value if now_value > max_value else max_value
                now_value = 0
    print(max_value)


def second():
    leaders_list = [0, 0, 0]
    now_value: int = 0
    with open('input.txt') as f:
        while True:
            line = f.readline()
            if not line:
                if min(leaders_list) < now_value:
                    leaders_list[leaders_list.index(min(leaders_list))] = now_value
                break
            if line != "\n":
                now_value += int(line.strip())
            else:
                if min(leaders_list) < now_value:
                    leaders_list[leaders_list.index(min(leaders_list))] = now_value
                now_value = 0
    print(sum(leaders_list))


if __name__ == "__main__":
    first()
    second()
