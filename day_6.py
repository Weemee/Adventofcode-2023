import math

part1 = 0
part2 = 0

data = open('day_6.txt').read().split('\n')
sets = zip(list(filter(None, data[0].split(':')[1].split(' '))), list(filter(None, data[1].split(':')[1].split(' '))))

# PQ-formeln https://www.matteboken.se/lektioner/matte-2/andragradsekvationer/pq-formeln#!/
def quadratic(p, q):
    x1 = math.floor((p / 2) + math.sqrt((p / 2) ** 2 - q))
    x2 = math.ceil((p / 2) - math.sqrt((p / 2) ** 2 - q))

    return x1 - x2 + 1
    
for set in sets:
    time = int(set[0])
    distance = int(set[1]) + 1

    result = quadratic(time, distance)

    if part1 == 0:
        part1 = result
    else:
        part1 *= result

t = int(''.join(list(filter(None, data[0].split(':')[1].split(' ')))))
d = int(''.join(list(filter(None, data[1].split(':')[1].split(' ')))))

part2 = quadratic(t, d)

print('Part 1: ', part1)
print('Part 2: ', part2)