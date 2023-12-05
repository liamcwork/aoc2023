def check_number_surroundings(y, x, size):
    for i in range (-1, 2):
        for j in range (-1, 1+size):
            if i == 0 and (j > -1 and j < size):
                continue
            if y+i > 139 or x+j > 139 or y+i < 0 or x+j < 0:
                continue
            if (y+i, x+j) in symbol_locations:
                return True
    return False

def check_gears_and_get_ratio(y, x):
    first_value = 0
    for i in range (-1, 2):
        for j in range (-1, 2):
            if i == 0 and j == 0:
                continue
            if y+i > 139 or x+j > 139 or y+i < 0 or x+j < 0:
                continue
            if (y+i, x+j) in number_locations:
                value = number_locations[(y+i, x+j)][0]
                if first_value != 0 and first_value != value:
                    return first_value * value
                first_value = value
    return 0

            

def build_graphs_v1(lines):
    y = 0
    for line in lines:
        x = 0
        tmp = ""
        length = 0
        for char in line:
            if char.isdigit():
                length += 1
                tmp += char
            else:
                if length > 0:
                    val = int(tmp)
                    number_locations[(y,x-length)] = (val, length)
                    length = 0
                    tmp = ""
                if not char.isdigit() and char != '.' and char != '\n':
                    symbol_locations.append((y, x))
            x+=1
        y+=1

def build_graphs_v2(lines):
    y = 0
    for line in lines:
        x = 0
        tmp = ""
        length = 0
        for char in line:
            if char.isdigit():
                length += 1
                tmp += char
            else:
                if length > 0:
                    val = int(tmp)
                    for i in range (-length, 0):
                        number_locations[(y,x+i)] = (val, length)
                    length = 0
                    tmp = ""
                if char == '*':
                    symbol_locations.append((y, x))
            x+=1
        y+=1

input = open("day3.txt", 'r')
lines = input.readlines()
symbol_locations = []
number_locations = {}
output = 0
# part 1
#build_graphs_v1(lines)
#for number in number_locations:
#    if check_number_surroundings(number[0], number[1], number_locations[number][1]):
#        output += number_locations[number][0]

#part 2
build_graphs_v2(lines)
for gear in symbol_locations:
    output += check_gears_and_get_ratio(gear[0], gear[1])

print(output)
        
        
