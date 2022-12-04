file = open('Day2\input.txt', 'r')
plays = file.readlines()

# A Rock B Paper C Scissors
# X Rock(1) Y Paper(2) Z Scissors(3)
# Win 6, Draw 3

points = 0

for play in plays:
    if play[2] == 'X':
        points += 1
        if play[0] == 'A':
            points += 3
        elif play[0] == 'C':
            points += 6
    elif play[2] == 'Y':
        points += 2
        if play[0] == 'A':
            points += 6
        elif play[0] == 'B':
            points += 3
    elif play[2] == 'Z':
        points += 3
        if play[0] == 'B':
            points += 6
        elif play[0] == 'C':
            points += 3
print('Total amount of points following the first instructions is  %i' % points)
        
        

# A Rock B Paper C Scissors
# X lose Y draw Z win
points = 0
for play in plays:
    if play[2] == 'X':
        if play[0] == 'A':
            points += 3 #scissors
        elif play[0] == 'B':
            points += 1 #rock
        elif play[0] == 'C':
            points += 2 #paper
    elif play[2] == 'Y':
        points += 3
        if play[0] == 'A':
            points += 1
        elif play[0] == 'B':
            points += 2
        elif play[0] == 'C':
            points += 3
    elif play[2] == 'Z':
        points += 6
        if play[0] == 'A':
            points += 2
        elif play[0] == 'B':
            points += 3
        elif play[0] == 'C':
            points += 1
print('Total amount of points following the second instructions is  %i' % points)
