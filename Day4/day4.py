file = open('Day4\input.txt', 'r')
assignnments = file.readlines()


#Part1
count = 0
for pair in assignnments:
    limits = pair.strip('\n').replace('-',' ').replace(',',' ').split()
    
    for i in range(len(limits)):
        limits[i] = int(limits[i])
    
    if (limits[0]>=limits[2] and limits[1]<=limits[3]) or (limits[2]>=limits[0] and limits[3]<=limits[1]):
        count += 1
        
print('Part 1: The total number of pairs with repeated assignments is %i' % count)


#Part2
count = 0
for pair in assignnments:
    limits = pair.strip('\n').replace('-',' ').replace(',',' ').split()
    
    for i in range(len(limits)):
        limits[i] = int(limits[i])
    
    if (limits[0]<=limits[2] and limits[1]>=limits[2]) or (limits[2]<=limits[0] and limits[3]>=limits[0]):
        count += 1
  
print('Part 2: The total number of pairs with repeated assignments is %i' % count)