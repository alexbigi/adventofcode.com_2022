def first_task(i, j):
    if all(data[i][j] > data[k][j] for k in range(i)):
        return True
    if all(data[i][j] > data[i][k] for k in range(j)):
        return True
    if all(data[i][j] > data[k][j] for k in range(i + 1, len(data))):
        return True
    if all(data[i][j] > data[i][k] for k in range(j + 1, len(data))):
        return True
    return False


def second_task(i, j):
    checker = 1
    trees = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for (di, dj) in trees:
        ix, jx = i, j
        col = 0
        while True:
            ix += di
            jx += dj
            if ix < 0 or ix >= len(data) or jx < 0 or jx >= len(data):
                break
            elif data[ix][jx] < data[i][j]:
                col += 1
            else:
                col += 1
                break
        checker *= col
    return checker


if __name__ == "__main__":
    data = [list(line) for line in open("input.txt").read().splitlines()]
    print(sum([first_task(i, j) for i in range(len(data)) for j in range(len(data))]))
    print(max([second_task(i, j) for i in range(len(data)) for j in range(len(data))]))
