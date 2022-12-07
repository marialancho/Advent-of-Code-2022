file = open('Day7\input.txt', 'r')
lines = file.readlines()

dirs_to_see_sizes = []
final_sizes = []


for line in lines:
    match line.strip().split():
        case "$", "cd", "..":
            closed_dir_size = dirs_to_see_sizes.pop(-1)
            final_sizes.append(closed_dir_size)
            if dirs_to_see_sizes:
                dirs_to_see_sizes[-1] += final_sizes[-1]
        case "$", "cd", _:
            dirs_to_see_sizes.append(0)
        case "dir", _:
            pass 
        case "$", ls:
            pass
        case num, _:
            dirs_to_see_sizes[-1] += int(num)

while dirs_to_see_sizes:
    dir_size = dirs_to_see_sizes.pop(-1)
    final_sizes.append(dir_size)
    if dirs_to_see_sizes:
        dirs_to_see_sizes[-1] += final_sizes[-1]


result = 0
for size in final_sizes:
    if size <= 100000:
        result += size

print('Part 1: The sum of the sizes of directories of maximum 100000 is: %i' % result)



used = max(final_sizes)
free = 70000000-used
possible =[]
for s in final_sizes:
    if (s + free) >= 30000000:
        possible.append(s)
result = min(possible)
print('Part 2: The size of the smallest directory to delete is: %i' % result)
