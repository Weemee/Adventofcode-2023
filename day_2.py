import re

part1 = 0
part2 = 0

redPattern = r'\b(?!([1-9]|1[0-2])\s*red\b)\d+\s*red\b'
greenPattern = r'\b(?!([1-9]|1[0-3])\s*green\b)\d+\s*green\b'
bluePattern = r'\b(?!([1-9]|1[0-4])\s*blue\b)\d+\s*blue\b'

reds =  r'(\d+)\s*red'
greens = r'(\d+)\s*green'
blues = r'(\d+)\s*blue'

finalPattern = rf'({redPattern}|{greenPattern}|{bluePattern})'

with open('day_2.txt', 'r') as t:
   for i, c in enumerate(t):
      matches = re.findall(finalPattern, c.rstrip('\n'))

      if not matches:
         part1 += (i + 1)
      
      r = max(list(map(int, re.findall(reds, c))))
      g = max(list(map(int, re.findall(greens, c))))
      b = max(list(map(int, re.findall(blues, c))))

      part2 += (r * g * b)
      
print('Part 1: ', part1)
print('Part 2: ', part2)