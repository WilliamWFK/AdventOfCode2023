with open('Day3\input.txt') as f:
    lines = f.readlines()

def parts_engine(array):
    starting_index = 0
    ending_index = 0
    total = 0
    values = []
    on_number = False

    for i, line in enumerate(array):
        for j, char in enumerate(line):
            if on_number:
                if char.isdigit():
                    values.append(char)
                else:
                    on_number = False
                    ending_index = j-1
                    if check_adjacent(array, values, starting_index, ending_index, i):
                        total += int(''.join(values))
                        print(int(''.join(values)))
                    values = []

            else:
                if char.isdigit():
                    starting_index = j
                    values.append(char)
                    on_number = True
    print(total)
                

def check_adjacent(array, values, start, end, row):
    """Checks the adjacent values for symbols"""
    isValid = False

    start_point = [[-1,0],[-1, -1], [0, -1], [1, -1], [1, 0]]
    end_point = [[-1,0], [-1, 1], [0, 1], [1, 1], [1, 0]]
                   
    for point in start_point:
        if array[row + point[0]][start + point[1]] != '.' and not array[row + point[0]][start + point[1]].isdigit():
            isValid = True
            break

    for i in range (start, end):
        if array[row-1][i] != '.' and not array[row-1][i].isdigit():
            isValid = True
            break
        if array[row+1][i] != '.' and not array[row+1][i].isdigit():
            isValid = True
            break

    for point in end_point:
        if array[row + point[0]][end + point[1]] != '.' and not array[row + point[0]][end + point[1]].isdigit():
            isValid = True
            break
    
    return isValid
        


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
    for line in padded_array:
        print(line)


    return padded_array


parts_engine(pad_and_split_array(lines))




