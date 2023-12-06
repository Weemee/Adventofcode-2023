# Fuck yeah it exists! https://docs.python.org/3/library/functools.html#functools.reduce
from functools import reduce

part1 = None
part2 = None

seeds = []
segments = []

# Turns out double new line is a split factor

# Fuck this shit
# with open('day_5.txt', 'r') as t:
#     for i, c in enumerate(t):
#         data = c.rstrip('\n')

#         if i == 0:
#             seeds = map(int, data.split(' ')[1:])
#         else:
#             segments.append(c.split('\n'))

# for i, c in enumerate(seeds):
#     print(c)

# print(segments)

# Split double new lines
data = open('day_5.txt').read().split('\n\n')

# Python lists (arrays) are... fun
# A = [1, 2, 3] => A[1:] == [2, 3]
# A = [1, 2, 3] => A[1] == 2
# Apparently...
# Just grabbing [1] from an array does not cut it because it's just the first element
# However, with [1:], we instead grab from the first element
seeds = map(int, data[0].split()[1:])
segments = data[1:]

# After some Python learning, let's make a function to look up this stupid position
# With the help of reduce we should be able to go through it all

# Originally called `findPosition`, but this is a mess so it's now `inception`
# I made a function in anticipation of part 2 ...
def inception(origin, input):
    # Need to split input (segments) into segment, starting from first index (like above to skipe the text line), and we split on new line
    for segment in input.split('\n')[1:]:
        # print(segment) # Gives us `50 98 2` [destination, source, length]

        # Can we split these three values into three variables right away?
        # Yes we can
        destination, source, length = map(int, segment.split())

        # print('Destination: ', destination) # Gives us `50`
        # print('Source: ', source) # Gives us `98`
        # print('Length: ', length) # Gives us `2`

        # We need to check the difference (delta) between the origin and the source

        difference = origin - source

        if difference in range(length):
            # print('Difference: ', difference) # Gives us `48`

            # If the difference is less than the length, we can add the difference to the destination
            # This is because the destination is the same as the source
            # So we can add the difference to the destination
            # print('Destination + Difference: ', destination + difference) # Gives us `146`

            # We can then return the destination + difference
            return destination + difference
    else:
        # If the difference is not in range, we can just return the origin
        return origin

for seed in seeds:
    value = reduce(inception, segments, int(seed))

    if part1 == None or value < part1:
        part1 = value

print('Part 1: ', part1)

# Part 2 then ...

# Give the seeds: `seeds: 79 14 55 13`
# The values on the initial seeds: line come in pairs.
# Within each pair, the first value is the start of the range and the second value is the length of the range.
# So, in the first line of the example above:

# This line describes two ranges of seed numbers to be planted in the garden.
# The first range starts with seed number 79 and contains 14 values: 79, 80, ..., 91, 92.
# The second range starts with seed number 55 and contains 13 values: 55, 56, ..., 66, 67.

# Now, rather than considering four seed numbers, you need to consider a total of 27 seed numbers.

# Looks like I need to zip the seeds with a list of 1s (to make it a list of tuples) https://docs.python.org/3.3/library/functions.html#zip
# Map has no length, so we need to use list
seeds = list(map(int, data[0].split()[1:]))

# We can fancy slice things apparently with: https://docs.python.org/release/2.3.5/whatsnew/section-slices.html
# Min function should be easier https://sparkbyexamples.com/python/python-list-min-method/
# Generators https://realpython.com/introduction-to-python-generators/

def inceptions(origins, input):
    # Iterate over each (index, origin) pair in origins
    for index, origin in origins:
        # print('Start: ', index)
        # print('Origin: ', origin)

        # While we have an origin to process
        while origin > 0:
            for segment in input.split('\n')[1:]:
                # Split the segment into destination, source, and length
                destination, source, length = map(int, segment.split())

                # print('Destination: ', destination) # Gives us `50`
                # print('Source: ', source) # Gives us `98`
                # print('Length: ', length) # Gives us `2`

                # Calculate the difference between the index and the source
                difference = index - source

                # If the offset falls within the segment, yield the adjusted destination and the overlap
                if difference in range(length):
                    # Calculate the overlap between the origin and the segment
                    length = min(length - difference, origin)

                    # Yield the adjusted destination and the overlap
                    yield (destination + difference, length)

                    # Update the index and reduce the remaining origin
                    index += length
                    origin -= length

                    # Break the inner loop to move to the next origin
                    break
            else:
                # When a generator function encounters a yield statement, it temporarily suspends its execution and returns a value to the caller.
                # The generator function's state is preserved, allowing it to resume from where it left off the next time it's called

                # If no valid segment is found, yield the current index and remaining origin
                yield (index, origin)

                # Break the outer loop to move to the next (index, origin) pair
                break

# pairs = seeds[0::2] # [79, 55]
# print(pairs)

# pairs = seeds[1::2] # [14, 13]
# print(pairs)

# These are the pairs we need to zip together

# zipped = zip(seeds[0::2], seeds[1::2])
# print(list(zipped)) # [(79, 14), (55, 13)]

# Need to make it a list of tuples

zipped = [zip(seeds[0::2], seeds[1::2])]
# print(zipped) # [<zip object at 0x000002B369D6C600>]

# for z in zipped:
#     print(list(z)) # [(79, 14), (55, 13)]

# part2 = min(reduce(inceptions, segments, seed))[0] for seed in zipped # invalid syntax
part2 = [min(reduce(inceptions, segments, seed))[0] for seed in zipped] # Placing this in brackets gives us a generator object

print('Part 2: ', part2[0])