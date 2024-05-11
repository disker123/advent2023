File = open("day4input.txt", "r")
data = File.readlines()
result = 0

for game in data:
    winning_numbers = set()
    your_numbers = set()
    stats = game.split()[2:]    #remove the game number
    flag = True #checks if we are reading winning numbers or your numbers
    for num in stats:
        if (num.isnumeric()):
            if(flag):
                winning_numbers.add(num)
            else:
                your_numbers.add(num)
        if(num == "|"):
            flag = False
    wins = len(winning_numbers.intersection(your_numbers))  #get the intersection of the sets
    #print(wins)
    if(wins == 0):  
        continue
    elif (wins == 1):
        result+=1
    else:
        result+= (2 ** (wins-1))

print(result)
File.close()