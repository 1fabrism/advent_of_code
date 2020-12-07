with open('input.txt') as f:
    wires = [line.rstrip().split(',') for line in f.readlines()]

"""
#Smaller input for quicker prototyping:

# wires1 output = 159 distance, 610 steps
wires1 = ['R75,D30,R83,U83,L12,D49,R71,U7,L72',
         'U62,R66,U55,R34,D71,R55,D58,R83']

# wires2 output = 135 distance, 410 steps
wires2 = ['R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51',
         'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7']
wires=wires2
wires = [x.split(',') for x in wires]
"""

# Part 1
#
# THIS CODE IS REALLY SLOW!!!
#
commands = {'R':(1,0),'L':(-1,0),'U':(0,1),'D':(0,-1)}
print("Creating paths:")
paths = []
for w,wire in enumerate(wires):
    coords = (0,0)
    path = []
    for segment in wire:
        for i in range(0,int(segment[1:])):
            coords = tuple(map(lambda x,y:x+y, coords,commands[segment[0:1]]))
            path.append(coords)
            
    print("Wire {} done.".format(w+1))
    paths.append(path)

print("Calculating wire crossings:")
crossings = []
for i,path_outer in enumerate(paths):
    for k,path_inner in enumerate(paths):
        if k <= i:
            continue        # We already checked this combination of wires
        else:
            for n, pos in enumerate(path_inner):
                if pos in path_outer and pos not in [c.get('Coordinates')
                                                         for c in crossings]:
                    steps = path_outer.index(pos) + n +2 #+2 due to 1st step having index 0
                    crossings.append({'Wires':[i, k],'Coordinates':pos,
                                     'Steps':steps})
            
        print("Wire {} checked.".format(k))

print(80*"~")
man_dists = [abs(c['Coordinates'][0])+abs(c['Coordinates'][1]) for c in
             crossings]
print("Manhattan distance of closest crossing: {}".format(min(man_dists)))



# Part 2

min_steps = min([c['Steps'] for c in crossings])
print("Minimum steps: {}".format(min_steps))






