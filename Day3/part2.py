

with open('Day3\input.txt') as f:
    lines = f.readlines()

def parts_engine(array):
    starting_index = 0
    ending_index = 0
    total = 0
    values = []
    on_number = False
    numbers = set()

    for i, line in enumerate(array):
        for j, char in enumerate(line):
            if on_number:
                if char.isdigit():
                    values.append(char)
                else:
                    on_number = False
                    ending_index = j-1
                    total += (check_adjacent(array, values, starting_index, ending_index, i))
                    values = []

            else:
                if char.isdigit():
                    starting_index = j
                    values.append(char)
                    on_number = True

    # print(numbers)
    # numbers.remove(0)
    # for num in numbers:
    #     total *= num
    total /= 2
    print(total)
                

def check_adjacent(array, values, start, end, row):
    star_x, star_y = 0, 0
    """Checks the adjacent values for symbols"""
    hasStar = False
    product = 0

    start_point = [[-1,0],[-1, -1], [0, -1], [1, -1], [1, 0]]
    end_point = [[-1,0], [-1, 1], [0, 1], [1, 1], [1, 0]]
                   
    for point in start_point:
        if array[row + point[0]][start + point[1]] == "*":
            hasStar = True
            star_x = row + point[0]
            star_y = start + point[1]

    for i in range (start, end):
        if array[row-1][i] != '.' and not array[row-1][i].isdigit():
            hasStar = True
            star_x = row - 1
            star_y = i
        if array[row+1][i] != '.' and not array[row+1][i].isdigit():
            hasStar = True
            star_x = row + 1
            star_y = i

    for point in end_point:
        if array[row + point[0]][end + point[1]] != '.' and not array[row + point[0]][end + point[1]].isdigit():
            hasStar = True
            star_x = row + point[0]
            star_y = end + point[1]

    


    
    
    return gear_product(array, star_x, star_y)

def gear_product(array, x, y):
    """Returns the product of the two numbers around the star"""
    numbers = set()
    nums = []

    check_spots = [[-1,-1], [-1, 0], [-1, 1], 
                     [0, -1], [0, 1],
                     [1, -1], [1, 0], [1, 1]]

    for spot in check_spots:
        if array[x + spot[0]][y + spot[1]].isdigit():
            nums.append(array[x + spot[0]][y + spot[1]])
            # check the left and right of the number until no more digits
            i = 1
            while array[x + spot[0]][y + spot[1] - i].isdigit():
                nums.insert(0, array[x + spot[0]][y + spot[1] - i])
                i += 1
            i = 1
            while array[x + spot[0]][y + spot[1] + i].isdigit():
                nums.append(array[x + spot[0]][y + spot[1] + i])
                i += 1
            numbers.add(int(''.join(nums)))
            nums = []


    # return product of all numbers in numbers
    total = 1
    if len(numbers) < 2:
        return 0
    else:
        for num in numbers:
            total *= num
            print(num, end=" ")
        print(total)
        return total
        


def pad_and_split_array(array):
    """Pads the array with '.' and splits each line into a list of characters"""
    padded_array = []
    i = 0
    j = 0

    for i, line in enumerate(array):
        if i == 0:
            padded_array.append(["."] * (len(line) + 1))
        padded_array.append([])
        

        for j, char in enumerate(line):
            if j == 0:
                padded_array[i + 1].append(".")
            padded_array[i + 1].append(char)
            if j == len(line) - 1:
                padded_array[i + 1][j+1] = "."

        if i == len(array) - 1:
            padded_array[i+1].append(".")
            padded_array.append(["."] * (len(line) + 2))

    # print
    # for line in padded_array:
    #     print(line)


    return padded_array


parts_engine(pad_and_split_array(lines))




