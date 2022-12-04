import string

file = open('Day3\input.txt', 'r')
rucksacks = file.readlines()

priorities_total = 0

priorities_dict = dict()
for index, letter in enumerate(string.ascii_lowercase):
    priorities_dict[letter] = index +1
    
for index, letter in enumerate(string.ascii_uppercase):
    priorities_dict[letter] = index + 27
    
#Part 1
for rucksack in rucksacks:
    half = int(len(rucksack)/2)
    comp1 = rucksack[:half]
    comp2 = rucksack[half:]
    char = list(set(comp1) & set(comp2))[0]
    priorities_total += priorities_dict[char]

print('Part 1: The total sum of priorities is %i' % priorities_total)

#Part 2
groups = []
priorities_total2 =  0
for i in range(0,len(rucksacks),3):
    groups.append([rucksacks[i].strip('\n'),rucksacks[i+1].strip('\n'),rucksacks[i+2].strip('\n')])

for j in groups:
    char = list(set(j[0]) & set(j[1]) & set(j[2]))[0]
    priorities_total2 += priorities_dict[char]

print('Part 2: The total sum of priorities is %i' % priorities_total2)