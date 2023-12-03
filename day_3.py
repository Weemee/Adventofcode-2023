import re

part1 = 0
part2 = 0

lines = []
pattern = r'[0-9]'

with open('day_3.txt', 'r') as t:
    lines = t.readlines()

def grabNumbersForwards(x, line, number = ''):
    if re.match(pattern, line[x]):
        number += line[x]
        if x != len(line) - 1:
            return grabNumbersForwards(x+1, line, number)
        else:
            return number
    else:
        return number

def grabStartingIndex(x, line):
    if x < 0:
        return 0
    elif not re.match(pattern, line[x]):
        return x+1
    else:
        return grabStartingIndex(x-1, line)
    
for i, c in enumerate(lines):
    above = i != 0
    below = i != len(lines) - 1
    line = c.rstrip('\n')
    
    for j, d in enumerate(line):
        if not re.match(pattern, d) and not '.' in d:
            left = j != 0
            right = j != len(line) - 1

            adjacent = []
            gear = bool('*' in d)
            
            if above:
                if left:
                    if re.match(pattern, lines[i-1][j-1]):
                        index = grabStartingIndex(j-1, lines[i-1])
                        n = grabNumbersForwards(index, lines[i-1])

                        if n:
                            adjacent.append(int(n))
                            part1 += int(n)
                if re.match(pattern, lines[i-1][j]) and not re.match(pattern, lines[i-1][j-1]):
                    index = grabStartingIndex(j, lines[i-1])
                    n = grabNumbersForwards(index, lines[i-1])

                    if n:
                        adjacent.append(int(n))
                        part1 += int(n)
                if right:
                    if re.match(pattern, lines[i-1][j+1]) and not re.match(pattern, lines[i-1][j]):
                        index = grabStartingIndex(j+1, lines[i-1])
                        n = grabNumbersForwards(index, lines[i-1])

                        if n:
                            adjacent.append(int(n))
                            part1 += int(n)
            if left:
                if re.match(pattern, lines[i][j-1]):
                    index = grabStartingIndex(j-1, lines[i])
                    n = grabNumbersForwards(index, lines[i])

                    if n:
                        adjacent.append(int(n))
                        part1 += int(n)
            if right:
                if re.match(pattern, lines[i][j+1]):
                    index = grabStartingIndex(j+1, lines[i])
                    n = grabNumbersForwards(index, lines[i])
                    
                    if n:
                        adjacent.append(int(n))
                        part1 += int(n)
            if below:
                if left:
                    if re.match(pattern, lines[i+1][j-1]):
                        index = grabStartingIndex(j-1, lines[i+1])
                        n = grabNumbersForwards(index, lines[i+1])

                        if n:
                            adjacent.append(int(n))
                            part1 += int(n)
                if re.match(pattern, lines[i+1][j]) and not re.match(pattern, lines[i+1][j-1]):
                    index = grabStartingIndex(j, lines[i+1])
                    n = grabNumbersForwards(index, lines[i+1])

                    if n:
                        adjacent.append(int(n))
                        part1 += int(n)
                if right:
                    if re.match(pattern, lines[i+1][j+1]) and not re.match(pattern, lines[i+1][j]):
                        index = grabStartingIndex(j+1, lines[i+1])
                        n = grabNumbersForwards(index, lines[i+1])

                        if n:
                            adjacent.append(int(n))
                            part1 += int(n)

            if gear and len(adjacent) == 2:
                part2 += (adjacent[0] * adjacent[1])

print('Part 1: ', part1)
print('Part 2: ', part2)