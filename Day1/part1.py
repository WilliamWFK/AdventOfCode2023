
# import text file
with open('Day1\input.txt') as f:
    lines = f.readlines()

total = 0


for line in lines:
    numbers = []
    # try to convert char to int and add if int otherwise pass
    for char in line:
        try:
            numbers.append(int(char))
        except ValueError:
            pass

    total += int(numbers[0]*10 + numbers[-1])

print(total)
        
