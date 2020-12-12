"""
--- Day 12: Rain Risk ---

Your ferry made decent progress toward the island, but the storm came in faster than anyone expected. The ferry needs to take evasive actions!

Unfortunately, the ship's navigation computer seems to be malfunctioning; rather than giving a route directly to safety, it produced extremely circuitous instructions. When the captain uses the PA system to ask if anyone can help, you quickly volunteer.

The navigation instructions (your puzzle input) consists of a sequence of single-character actions paired with integer input values. After staring at them for a few minutes, you work out what they probably mean:

    Action N means to move north by the given value.
    Action S means to move south by the given value.
    Action E means to move east by the given value.
    Action W means to move west by the given value.
    Action L means to turn left the given number of degrees.
    Action R means to turn right the given number of degrees.
    Action F means to move forward by the given value in the direction the ship is currently facing.

The ship starts by facing east. Only the L and R actions change the direction the ship is facing. (That is, if the ship is facing east and the next instruction is N10, the ship would move north 10 units, but would still move east if the following action were F.)

For example:

F10
N3
F7
R90
F11

These instructions would be handled as follows:

    F10 would move the ship 10 units east (because the ship starts by facing east) to east 10, north 0.
    N3 would move the ship 3 units north to east 10, north 3.
    F7 would move the ship another 7 units east (because the ship is still facing east) to east 17, north 3.
    R90 would cause the ship to turn right by 90 degrees and face south; it remains at east 17, north 3.
    F11 would move the ship 11 units south to east 17, south 8.

At the end of these instructions, the ship's Manhattan distance (sum of the absolute values of its east/west position and its north/south position) from its starting position is 17 + 8 = 25.

Figure out where the navigation instructions lead. What is the Manhattan distance between that location and the ship's starting position?

Your puzzle answer was 757.
"""

# PART 1:
import numpy as np

with open("day12_input.txt", 'r') as file:
    input = file.readlines()
    input = [(line[:1], int(line[1:])) for line in input]
    directions = {"N":(0,1), "E":(1,0), "S":(0,-1), "W":(-1,0)}
    coordinates = (0,0)
    direction = 'E'
    for line in input:
        if line[0] in ['L', 'R']:
            d = ['N','E','S','W']
            n = line[1] // 90
            i = d.index(direction)
            if line[0] == 'L':
                direction = d[(i-n)%len(d)]
            if line[0] == 'R':
                direction = d[(i+n)%len(d)]
        elif line[0] == 'F':
            coordinates += np.multiply(line[1], directions[direction])
        elif line[0] in directions.keys():
            coordinates += np.multiply(line[1], directions[line[0]])
    print(f"Manhattan distance: {coordinates[0]}E, {coordinates[1]}N = {sum(abs(coordinates))}")



"""

"""

# PART 2:


