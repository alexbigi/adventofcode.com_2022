def task():
    data = open("input.txt").read().strip()
    sizes: dict = {}
    paths: list = []
    for line in data.split("\n"):
        if line.startswith("$ cd"):
            cmd = line.split()[2]
            if cmd == "/":
                paths.append("/")
            elif cmd == "..":
                paths.pop()
            else:
                paths.append(f"{paths[-1]}{'/' if paths[-1] != '/' else ''}{cmd}")
        if line[0].isnumeric():
            for path in paths:
                try:
                    sizes[path] += int(line.split()[0])
                except KeyError:
                    sizes[path] = int(line.split()[0])

    print(sum(s for s in sizes.values() if s <= 100000))
    print(min(s for s in sizes.values() if s >= 30000000 - (70000000 - sizes['/'])))


if __name__ == "__main__":
    task()
