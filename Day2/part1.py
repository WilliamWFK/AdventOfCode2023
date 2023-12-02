import re

# import text file
with open('Day2\input.txt') as f:
    lines = f.readlines()


red_cubes = 12
green_cubes = 13
blue_cubes = 14
total = 0

pattern = r'[^0-9:;,dbg]'

# d is red, b is blue g is green

for line in lines:
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
                    if int(bag[:-1]) > red_cubes: eligible = False
                case 'b':
                    if int(bag[:-1]) > blue_cubes: eligible = False
                case 'g':
                    if int(bag[:-1]) > green_cubes: eligible = False

    print(id, eligible)
    if eligible:
        total += int(id)

print(total)
