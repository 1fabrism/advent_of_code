"""
--- Day 7: Handy Haversacks ---

You land at the regional airport in time for your next flight. In fact, it looks like you'll even have time to grab some food: all flights are currently delayed due to issues in luggage processing.

Due to recent aviation regulations, many rules (your puzzle input) are being enforced about bags and their contents; bags must be color-coded and must contain specific quantities of other color-coded bags. Apparently, nobody responsible for these regulations considered how long they would take to enforce!

For example, consider the following rules:

light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.

These rules specify the required contents for 9 bag types. In this example, every faded blue bag is empty, every vibrant plum bag contains 11 bags (5 faded blue and 6 dotted black), and so on.

You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different bag colors would be valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one shiny gold bag?)

In the above rules, the following options would be available to you:

    A bright white bag, which can hold your shiny gold bag directly.
    A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
    A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
    A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.

So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.

How many bag colors can eventually contain at least one shiny gold bag? (The list of rules is quite long; make sure you get all of it.)

Your puzzle answer was 185.
"""

# PART 1:
with open("day7_input.txt", 'r') as file:
    rules = dict()
    for line in file.readlines():
        breakdown = line.partition("bags")
        rules[breakdown[0]] = breakdown[2]
    bags = []
    search = ["shiny gold"]
    while search:
        for bag in search:
            for item in rules.items():
                if (bag in item[1]) and (item not in bags):
                    bags.append(item)
                    search.append(item[0])
            search.remove(bag)
    print(len(bags))



"""

"""

# PART 2:
class Bag(object):
    def __init__(self, name):
        self.name = name
        self.quantity = 0
        self.children = []
    
    def addChild(self, child):
        self.children.append(child)


def count_bags(bag):
    counter = 0
    for child in bag.children:
        counter += count_bags(child)
    return counter * bag.quantity + bag.quantity


def parse_rule(bag, input):
    rule = search_rules(bag.name, input)
    if " no " not in rule:
        for index,word in enumerate(rule.split()):
            if word.isdigit():
                child_bag = Bag(rule.split()[index+1]+' '+rule.split()[index+2])
                child_bag.quantity = int(word)
                bag.addChild(child_bag)


def search_rules(bag_name, input):
    for line in input:
        if line.startswith(bag_name):
            return line


with open("day7_input.txt", 'r') as file:
    input = file.readlines()
    shiny_gold = Bag("shiny gold")
    shiny_gold.quantity = 1
    parse_rule(shiny_gold, input)
    all_children = shiny_gold.children.copy()
    while all_children:
        for child in all_children:
            parse_rule(child, input)
            if child.children:
                all_children += child.children
            all_children.remove(child)
                    
    counter = count_bags(shiny_gold)
    print(counter-1)

