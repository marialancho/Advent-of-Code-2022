#import os
#print(os.getcwd())

file = open('Day1\input.txt', 'r')
calories = file.readlines()

elves = []
elf_calories = 0

for line in calories:
    cal = line.strip('\n')
    if cal =='':
        elves.append(elf_calories)
        elf_calories = 0
    else:
        elf_calories += int(cal)
        

elves.append(elf_calories)
top1 = max(elves)
print('Maximum calories carried by top 1 elf is %i' % top1)

sorted_cal = sorted(elves)
top3 = sorted_cal[-3:]
total = sum(top3)
print('Maximum calories carried by top 3 elves is %i' % total)