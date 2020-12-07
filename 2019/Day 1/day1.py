# Part 1
from functools import reduce
from math import floor

with open('input.txt') as f:
    mass_list = [int(line.rstrip()) for line in f.readlines()]

fuels = [floor(x/3)-2 for x in mass_list]
total_fuel = reduce(lambda x,y: x+y, fuels)
print(total_fuel)



# Part 2:
def fuel_adder(mass):
    fuel = floor(mass/3)-2
    if fuel > 0:
        fuel += fuel_adder(fuel)
    else:
        fuel = 0
    return fuel
fuels = [fuel_adder(x) for x in mass_list]
total_fuel = reduce(lambda x,y: x+y, fuels)
print(total_fuel)
