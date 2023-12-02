import re

# import text file
with open('Day2\input.txt') as f:
    lines = f.readlines()

total = 0
pattern = r'[^0-9:;,dbg]'

# d is red, b is blue g is green

for line in lines:

    red_cubes = 0
    green_cubes = 0
    blue_cubes = 0
    

    eligible = True
    cleaned_line = re.sub(pattern, '', line)
    array = cleaned_line.split(':')
    id = array.pop(0)
    games = ''.join(array).split(';')
    for game in games:
        bags = ''.join(game).split(',')
        for bag in bags:
            bag = ''.join(bag)
            print(bag[:-1])
            match bag[-1]:
                case 'd':
                    if int(bag[:-1]) > red_cubes: red_cubes = int(bag[:-1])
                case 'b':
                    if int(bag[:-1]) > blue_cubes: blue_cubes = int(bag[:-1])
                case 'g':
                    if int(bag[:-1]) > green_cubes: green_cubes = int(bag[:-1])

    print(id, eligible)
    if eligible:
        total += red_cubes * green_cubes * blue_cubes

print(total)
