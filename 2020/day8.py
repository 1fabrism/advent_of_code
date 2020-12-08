"""

"""

# PART 1:
with open("day8_input.txt", 'r') as file:
    input = file.readlines()
    acc = 0
    visited = []
    index = 0
    while True:
        if index in visited:
            break
        visited.append(index)
        line = input[index].split()
        if line[0] == "acc":
            acc += int(line[1])
            index +=1
        elif line[0] == "jmp":
            index += int(line[1])
        elif line[0] == "nop":
            index += 1
        else:
            print(f"OP code not recognized: {line[0]}")
    print(acc)



"""

"""

# PART 2:
def find_last_jmp(input):
    for index,line in enumerate(input[::-1]):
        line = line.split()
        if (line[0] == "jmp") and (int(line[1]) < 0):
            break
    return len(input)-index


with open("day8_input.txt", 'r') as file:
    og_input = file.readlines()
    input = og_input.copy()
    acc = 0
    visited = []
    acc_before_change = 0
    visited_before_change = []
    changed = False
    index = 0
    while True:
        if index >= len(input):
            break
        if index in visited:
            input = og_input.copy()
            if not changed:
                visited_before_change = visited.copy()
                acc_before_change = acc
            index = visited_before_change[-1]
            while input[index].split()[0] not in ["jmp", "nop"]:
                index = visited_before_change[visited_before_change.index(index)-1]
            if input[index].split()[0] == "jmp":
                input[index] = input[index].replace("jmp", "nop")
            elif input[index].split()[0] == "nop":
                input[index] = input[index].replace("nop", "jmp")
            for i in range(0, len(visited_before_change) - visited_before_change.index(index)):
                if "acc" in input[visited_before_change[-1]]:
                    acc_before_change -= int(input[visited_before_change[-1]].split()[1])
            visited_before_change = visited_before_change[:visited_before_change.index(index)]
            visited = visited_before_change.copy()
            acc = acc_before_change
            changed = True
        visited.append(index)
        line = input[index].split()
        if line[0] == "acc":
            acc += int(line[1])
            index +=1
        elif line[0] == "jmp":
            index += int(line[1])
        elif line[0] == "nop":
            index += 1
        else:
            print(f"OP code not recognized: {line[0]}")
    print(acc)

