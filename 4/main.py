def first_task():
    total_sum = 0
    with open("input.txt") as f:
        while True:
            line = f.readline()
            if not line:
                break
            range_check = set((range(int(line.strip().split(",")[0].split("-")[0]),
                                     int(line.strip().split(",")[0].split("-")[1]) + 1))).issubset(
                range(int(line.strip().split(",")[1].split("-")[0]),
                      int(line.strip().split(",")[1].split("-")[1]) + 1))
            range_check_reverse = set((range(int(line.strip().split(",")[1].split("-")[0]),
                                             int(line.strip().split(",")[1].split("-")[1]) + 1))).issubset(
                range(int(line.strip().split(",")[0].split("-")[0]),
                      int(line.strip().split(",")[0].split("-")[1]) + 1))
            if range_check or range_check_reverse:
                total_sum += 1
    print(total_sum)


def second_task():
    def range_checker(linez):
        for i in range(int(linez.strip().split(",")[0].split("-")[0]),
                       int(linez.strip().split(",")[0].split("-")[1]) + 1):
            for j in range(int(linez.strip().split(",")[1].split("-")[0]),
                           int(linez.strip().split(",")[1].split("-")[1]) + 1):
                if i == j:
                    return True
        return False
    total_sum = 0
    with open("input.txt") as f:
        while True:
            line = f.readline()
            if not line:
                break
            if range_checker(line):
                total_sum += 1
    print(total_sum)


if __name__ == "__main__":
    first_task()
    second_task()
