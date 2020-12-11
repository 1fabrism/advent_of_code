"""

"""

# PART 1:
def get_adjacents(old_map, i, k):


def update_map(old_map):
    for i,line in enumerate(old_map):
        for k,seat in enumerate(line):
            if seat == 'L':
                #check 8 surrounding seats
                adjacents = [old_map[i-1][k-1], old_map[i-1][k], old_map[i-1][k+1],
                             old_map[i][k-1], old_map[i][k+1],
                             old_map[i+1][k-1], old_map[i+1][k], old_map[i+1][k+1]]
            if seat == '#':


with open("day11_input.txt", 'r') as file:
    input = file.readlines()
    input = [line.rstrip('\n') for line in input]
    old_map = input.copy()
    new_map = input.copy()
    # go through map, update seats accordingly
    while True:
        new_map = update_map(old_map)
        if new_map == old_map:
            break
        old_map = new_map.copy()

    # go through current map to count number of '#'
    occupied = 0
    for line in new_map:
        occupied += line.count('#')
    print(occupied)



"""

"""

# PART 2:
# with open("day11_input.txt", 'r') as file:
#     input = file.readlines()
#     input = [line.rstrip('\n') for line in input]

