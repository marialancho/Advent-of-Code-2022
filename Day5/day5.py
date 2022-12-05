import copy

f = open('Day5\input.txt', 'r')
rows = []
for i in range(8):
    rows.append(f.readline())
    
arrangement_initial = [[],[],[],[],[],[],[],[],[]]
for line in reversed(rows):   
    for j in range(9):
        if not(line[4*j+1] == ' '):
            arrangement_initial[j].append(line[4*j+1])        


f.readline()
f.readline()
lines = f.readlines()


#Part1
arrangement = copy.deepcopy(arrangement_initial)
for line in lines:
    count = int(line.split(" ")[1])
    stack1 = int(line.split(" ")[3])
    stack2 = int(line.split(" ")[5].strip())
    for i in range(count):
        crate = arrangement[stack1-1].pop()
        arrangement[stack2-1].append(crate)
sol = ''
for i in arrangement:
    sol += i[-1]

print('Part 1: The crates that are on top of each stack are: %s' % sol)



#Part2
arrangement = copy.deepcopy(arrangement_initial)
for line in lines:
    count = int(line.split(" ")[1])
    stack1 = int(line.split(" ")[3])
    stack2 = int(line.split(" ")[5].strip())
    
    move = arrangement[stack1-1][-count:]
    for crate in move:
        arrangement[stack1-1].pop()
        arrangement[stack2-1].append(crate)

sol = ''
for i in arrangement:
    sol += i[-1]

print('Part 2: The crates that are on top of each stack are: %s' % sol)