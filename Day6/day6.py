file = open('Day6\input.txt', 'r')
buffer = file.readline()

#Part1

num = 0
for i in range(4,len(buffer)):
    marker = buffer[i-4:i]
    has_repeated_chars = len(set(marker)) != len(marker)
    if not(has_repeated_chars):
        num = i
        break
    
print('Part 1: The number of characters that have to be processed is %i' % num)


#Part2

num = 0
for i in range(14,len(buffer)):
    marker = buffer[i-14:i]
    has_repeated_chars = len(set(marker)) != len(marker)
    if not(has_repeated_chars):
        num = i
        break
    
print('Part 2: The number of characters that have to be processed is %i' % num)
