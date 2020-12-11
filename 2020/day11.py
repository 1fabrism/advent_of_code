"""
--- Day 11: Seating System ---

Your plane lands with plenty of time to spare. The final leg of your journey is a ferry that goes directly to the tropical island where you can finally start your vacation. As you reach the waiting area to board the ferry, you realize you're so early, nobody else has even arrived yet!

By modeling the process people use to choose (or abandon) their seat in the waiting area, you're pretty sure you can predict the best place to sit. You make a quick map of the seat layout (your puzzle input).

The seat layout fits neatly on a grid. Each position is either floor (.), an empty seat (L), or an occupied seat (#). For example, the initial seat layout might look like this:

L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL

Now, you just need to model the people who will be arriving shortly. Fortunately, people are entirely predictable and always follow a simple set of rules. All decisions are based on the number of occupied seats adjacent to a given seat (one of the eight positions immediately up, down, left, right, or diagonal from the seat). The following rules are applied to every seat simultaneously:

    If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    Otherwise, the seat's state does not change.

Floor (.) never changes; seats don't move, and nobody sits on the floor.

After one round of these rules, every seat in the example layout becomes occupied:

#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##

After a second round, the seats with four or more occupied adjacent seats become empty again:

#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##

This process continues for three more rounds:

#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##

#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##

#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##

At this point, something interesting happens: the chaos stabilizes and further applications of these rules cause no seats to change state! Once people stop moving around, you count 37 occupied seats.

Simulate your seating area by applying the seating rules repeatedly until no seats change state. How many seats end up occupied?

Your puzzle answer was 2470.
"""

# PART 1:
def get_adjacents(map, i, k):
    adjacents = []
    for y in range(k-1, k+2):
        for x in range(i-1, i+2):
            if (x!=i or y!=k) and 0 <= x < len(map) and 0 <= y <= len(map[x])-1:
                adjacents.append(map[x][y])
    return adjacents


def update_map(old_map):
    for i,line in enumerate(old_map):
        for k,seat in enumerate(line):
            if seat == 'L':
                adjacents = get_adjacents(old_map, i, k)
                if '#' not in adjacents:
                    new_map[i] = new_map[i][0:k] + '#' + new_map[i][k+1: ]
            elif seat == '#':
                adjacents = get_adjacents(old_map, i, k)
                if adjacents.count('#') >= 4:
                    new_map[i] = new_map[i][0:k] + 'L' + new_map[i][k+1: ]


with open("day11_input.txt", 'r') as file:
    input = file.readlines()
    input = [line.rstrip('\n') for line in input]
    old_map = input.copy()
    new_map = input.copy()
    counter = 0
    # go through map, update seats accordingly
    while True:
        update_map(old_map)
        if new_map == old_map:
            break
        old_map = new_map.copy()
        counter += 1

    # go through current map to count number of '#'
    occupied = 0
    for line in new_map:
        occupied += line.count('#')
    print(occupied)
    print(counter)



"""
--- Part Two ---

As soon as people start to arrive, you realize your mistake. People don't just care about adjacent seats - they care about the first seat they can see in each of those eight directions!

Now, instead of considering just the eight immediately adjacent seats, consider the first seat in each of those eight directions. For example, the empty seat below would see eight occupied seats:

.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#.....

The leftmost empty seat below would only see one empty seat, but cannot see any of the occupied ones:

.............
.L.L.#.#.#.#.
.............

The empty seat below would see no occupied seats:

.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##.

Also, people seem to be more tolerant than you expected: it now takes five or more visible occupied seats for an occupied seat to become empty (rather than four or more from the previous rules). The other rules still apply: empty seats that see no occupied seats become occupied, seats matching no rule don't change, and floor never changes.

Given the same starting layout as above, these new rules cause the seating area to shift around as follows:

L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL

#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##

#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#

#.L#.##.L#
#L#####.LL
L.#.#..#..
##L#.##.##
#.##.#L.##
#.#####.#L
..#.#.....
LLL####LL#
#.L#####.L
#.L####.L#

#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##LL.LL.L#
L.LL.LL.L#
#.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLL#.L
#.L#LL#.L#

#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.#L.L#
#.L####.LL
..#.#.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#

#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.LL.L#
#.LLLL#.LL
..#.L.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#

Again, at this point, people stop shifting around and the seating area reaches equilibrium. Once this occurs, you count 26 occupied seats.

Given the new visibility method and the rule change for occupied seats becoming empty, once equilibrium is reached, how many seats end up occupied?

Your puzzle answer was 2259.
"""

# PART 2:
def get_adjacents2(map, i, k):
    directions = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1)]
    adjacents = []
    x = i
    y = k
    for direction in directions:
        x += direction[0]
        y += direction[1]
        while 0 <= x < len(input) and 0 <= y < len(input[i]):
            if map[x][y] in ['L', '#']:
                adjacents.append(map[x][y])
                break
            x += direction[0]
            y += direction[1]
        x = i
        y = k
    return adjacents


def update_map2(old_map):
    for i,line in enumerate(old_map):
        for k,seat in enumerate(line):
            if seat == 'L':
                adjacents = get_adjacents2(old_map, i, k)
                if '#' not in adjacents:
                    new_map[i] = new_map[i][0:k] + '#' + new_map[i][k+1: ]
            elif seat == '#':
                adjacents = get_adjacents2(old_map, i, k)
                if adjacents.count('#') >= 5:
                    new_map[i] = new_map[i][0:k] + 'L' + new_map[i][k+1: ]


with open("day11_input.txt", 'r') as file:
    input = file.readlines()
    input = [line.rstrip('\n') for line in input]
    old_map = input.copy()
    new_map = input.copy()
    counter = 0
    # go through map, update seats accordingly
    while True:
        update_map2(old_map)
        if new_map == old_map:
            break
        old_map = new_map.copy()
        counter += 1

    # go through current map to count number of '#'
    occupied = 0
    for line in new_map:
        occupied += line.count('#')
    print(occupied)
    print(counter)

