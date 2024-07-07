File = open("day8input.txt", "r")
data = File.readlines()

directions = data[0]
directions = directions.rstrip()    #remove new line chars from the end of the string
#clean up the file so we just have map 
del data[0] 
del data[0]

wasteland = {}
for line in data:   #create a dictionary that maps each location to a tupple with its left and right location
    key = line[0:3]
    paths = (line[7:10], line[12:15])
    wasteland[key] = paths

key = "AAA" #start key
counter = 0
while(key != "ZZZ"):
    for x in directions:
        if(x == "L"):
            key = wasteland[key][0]
        if(x == "R"):
            key = wasteland[key][1]
        counter += 1
        #print(x)

        if(key == "ZZZ"):
            break
print(counter)