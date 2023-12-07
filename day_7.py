from functools import cmp_to_key

part1 = 0

data = open('day_7.txt').read().split('\n')
cardStrength = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}

def sortHand(hand):
    return  dict(sorted(hand.items(), key=lambda item: (item[1], cardStrength.get(item[0], 0)), reverse=True))

def extractHand(hand):
    count = {}

    for card in hand:
        if card[0] in count.keys():
            count[card[0]] += 1
        else:
            count[card[0]] = 1

    return count

def compare(a, b):
    a = a.split(' ')[0]
    b = b.split(' ')[0]
    
    cardsA = list(sortHand(extractHand(a)).items())
    cardsB = list(sortHand(extractHand(b)).items())

    # Compare counts first
    index = 0
    for card in cardsA:
        countA = cardsA[index][1]
        countB = cardsB[index][1]

        if countA > countB:
            # print('A is stronger')
            return 1
        elif countA < countB:
            # print('B is stronger')
            return -1
        index += 1
        
    # If counts are equal, compare by card strength
    for i, card in enumerate(a):
        strengthA = cardStrength.get(card, 0)
        strengthB = cardStrength.get(b[i], 0)
        
        if strengthA > strengthB:
            # print('A is stronger')
            return 1
        elif strengthA < strengthB:
            # print('B is stronger')
            return -1
        index += 1

    return 0  # a and b are equal

data.sort(key=cmp_to_key(compare))

for index, hand in enumerate(data):
    value = int(hand.split(' ')[1])
    multiplier = index + 1
    score = value * multiplier

    part1 += score

print('Part 1: ', part1)