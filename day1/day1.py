#part 1
def part_one(lines):
    output = 0
    for line in lines:
        output += sum_line(line)
    return output

def sum_line(line):
    first = '-1'
    newest = '-1'
    for char in line:
        if char.isdigit():
            if first == '-1':
                first = char
            newest = char
    line_value = first+newest
    return int(line_value)

def clean_line(line):
    words = {"one" : 'one1one', "two": 'two2two', "three": 'three3three', "four": 'four4four', "five": 'five5five', "six": 'six6six', "seven": 'seven7seven', "eight": 'eight8eight', "nine": 'nine9nine'}
    for word in words:
        line = line.replace(word, words[word])
    return line

#part 2
# O(m*n) so not that good but clean
def part_two(lines):
    output = 0
    for line in lines:
        line = clean_line(line)
        line_sum = sum_line(line)
        output += line_sum
    return output

input = open("day1.txt", 'r')
lines = input.readlines()      
print(part_two(lines))