part1 = 0
part2 = 0

dict = {}

with open('day_4.txt', 'r') as t:
    for i, c in enumerate(t):
        data = c.rstrip('\n').split(':')
        winningNumbers = data[1].split('|')[0].split(' ')
        myNumbers = data[1].split('|')[1].split(' ')

        total = 0
        last = i + 1

        part2 += 1

        while('' in winningNumbers):
            winningNumbers.remove('')

        while('' in myNumbers):
            myNumbers.remove('')

        for j, d in enumerate(winningNumbers):
            if d in myNumbers:
                last += 1
                if total == 0:
                    total = 1
                else:
                    total *= 2

                add = 1

                if i + 1 in dict.keys():
                    add += dict[i + 1]

                if last in dict.keys():
                    add += dict[last]
                
                dict[last] = add
        part1 += total

        if i + 1 in dict.keys():
            part2 += dict[i + 1]

print('Part 1: ', part1)
print('Part 2: ', part2)