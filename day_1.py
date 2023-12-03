import re

part1 = 0
part2 = 0
sn = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

with open('day_1.txt', 'r') as t:
    for c in t:
        n = re.findall(r'\d', c.rstrip('\n'))
        part1 += int(n[0]+n[-1])
        
        n = re.findall(rf'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', c)
        first = n[0]
        last = n[-1]
        
        if not first.isnumeric():
            first = str(sn.index(first) + 1)
        
        if not last.isnumeric():
            last = str(sn.index(last) + 1)
            
        part2 += int(first+last)

print('Part 1: ', part1)
print('Part 2: ', part2)