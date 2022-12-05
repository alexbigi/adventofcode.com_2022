def task(reverse: bool):
    def remove_sublist_from_list(sub_list, in_list):
        return in_list[0:len(in_list)-len(sub_list)]

    raw_stacks: list[list[str]] = []
    stacks_map: dict[int, list[str]] = {}
    stack_indexes: list[int] = []
    commands_list: list[str] = []
    read_stacks: bool = True
    read_stacks_indexes: bool = False
    read_commands: bool = False
    stack_tops: str = ""
    with open('input.txt') as f:
        while True:
            line: str = f.readline()
            if not line:
                break
            if read_commands:
                commands_list.append(line.rstrip()) if line.rstrip() != "" else None
            if read_stacks:
                if line.find("[") != -1:
                    raw_stacks.append([line.rstrip()[i:i + 3] for i in range(0, len(line.rstrip()), 4)])
                else:
                    read_stacks = False
                    read_stacks_indexes = True
            if read_stacks_indexes:
                stack_indexes = stack_indexes + [int(line.rstrip()[i:i + 3]) for i in range(0, len(line.rstrip()), 4)]
                read_commands = True
                read_stacks_indexes = False

    for stack_index in stack_indexes:
        stacks_map[stack_index] = list()
    for index in range(raw_stacks.__len__() - 1, -1, -1):
        for raw_index, raw_value in enumerate(raw_stacks[index]):
            stacks_map[raw_index + 1].append(raw_value) if raw_value != '   ' else None
    # commands logic
    for command in commands_list:
        how = int(command.split(" ")[1])
        from_stack = int(command.split(" ")[3])
        to_stack = int(command.split(" ")[5])
        reversed_part = stacks_map[from_stack][(len(stacks_map[from_stack])) - how: len(stacks_map[from_stack])]
        stacks_map[to_stack] = stacks_map[to_stack] + (reversed_part[::-1] if reverse else reversed_part)
        stacks_map[from_stack] = remove_sublist_from_list(stacks_map[from_stack][
                                                      (len(stacks_map[from_stack])) - how: len(stacks_map[from_stack])],
                                                          stacks_map[from_stack])
    # print stack tops
    for key in stacks_map.keys():
        stack_tops += stacks_map[key][len(stacks_map[key])-1][1]
    print(stack_tops)


if __name__ == "__main__":
    task(reverse=True)
    task(reverse=False)
