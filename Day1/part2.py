
# import text file
with open('Day1\input.txt') as f:
    lines = f.readlines()

total = 0


for line in lines:
    numbers = {}
    numwords = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six': 6, 'seven':7, 'eight':8, 'nine':9, 'ten':10}
    # try to convert char to int and add if int otherwise pass
    i = 0
    for char in line:
        try:
            numbers[i] = int(char)
        except ValueError:
            pass
        i += 1
    
    for number in numwords.keys():
        # find all starting indexes of number word
        indexes = [i for i in range(len(line)) if line.startswith(number, i)]
        for i in indexes:
            numbers[i] = numwords[number]

    nums = sorted(numbers.keys())
    total += int(numbers[nums[0]] * 10 + numbers[nums[-1]])

        
    
    # total += int(numbers[0]*10 + numbers[-1])

print(total)
        
