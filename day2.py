File = open("day2input.txt", "r")
data = File.readlines()
result = 0

for game in data:   #loop through each game
    #print("game start")
    cubes = {   #creates a zeroed dict to hold each rounds values
        "red": 0,
        "blue": 0,
        "green": 0
    }
    stats = game.split()[2:]    #gets into the rounds
    index = 0
    for word in stats:  #loops through each word starting after the Game x:
        #print(word)
        if(word.isnumeric()):   #when we hit a number
            #temp = int(word)
            color = stats[index+1]  #we get the next word which is the color of cubes that go with the current number
            if(not(color[len(color)-1].isalpha())): #remove the ,/; in the word so I can key it to my dict
                cubes[color[:-1]] = int(word)
                #print(cubes)
            else:
                cubes[color] = int(word)    #the last cube of the last round will match my keys so need need to remove that last char
            if(not(color[len(color)-1] == ",")): #round over
                if(cubes["red"]> 12 or cubes["blue"]>14 or cubes["green"]>13):  #if the round is invalid break out of the game and move on, or reset the dict and continue on to the next round
                    #print("this game is impossible")
                    break
                #print(cubes)
                cubes["red"] = 0
                cubes["blue"] = 0
                cubes["green"] = 0
                #print("this round was all good")
        index+=1
        if(index==len(stats)-1):    #You Win!
            result+=int(game.split()[1][:-1])




print(result)
File.close()