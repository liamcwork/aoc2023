#part 1
def process_line(line):
    red_limit = 12
    green_limit = 13
    #blue_limit = 14
    tmp = ""
    for char in line:
        if char.isdigit():
            tmp += char
        else:
            try:
                val = int(tmp)
                if val > 14 or (char == 'g' and val > green_limit) or (char == 'r' and val > red_limit):
                    return False
            except:
                # tmp wasn't a number
                tmp = ""
            tmp = ""
    return True


#part 2
def fewest_cubes(line):
    min_red = 0
    min_blue = 0
    min_green = 0
    tmp=""
    for char in line:
        if char.isdigit():
            tmp += char
        else:
            try:
                val = int(tmp)
                if char =='g' and min_green < val:
                    min_green = val
                elif char =='b' and min_blue < val:
                    min_blue = val
                elif char =='r' and min_red < val:
                    min_red = val
            except:
                tmp = ""
            tmp = ""
    return min_red * min_blue * min_green

input = open("day2.txt", 'r')
lines = input.readlines()
output = 0
for line in lines:
    idend = line.find(':')
    id = line[5:idend]
    line = line[idend+1:].replace(' ','')
    output += fewest_cubes(line)
print(output)
    
