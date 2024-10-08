#trail definition
#1 = came from the top
#2 = came from the right
#3 = came from the bottom
#4 = came from the left

def find_path_size(line_index: int, pipe_index: int, trail: int, counter: int, finish: int):    #maps the pipe path and returns the length
    while True:
        pipe = data[line_index][pipe_index]
        print(pipe)
        counter+=1
        match pipe: #gets the pipe shape and goes through to the other end to the next pipe
            case "S":
                if(finish == 1):    #finish case
                    print("the length is : ", counter-1)
                    return counter-1
                if(finish == 0):    #initial case
                    finish = 1
                    if(data[line_index-1][pipe_index] == "|" or data[line_index-1][pipe_index] == "7" or data[line_index-1][pipe_index] == "F"):
                        print("follow the top path")
                        #counter+=1
                        line_index -= 1
                        trail = 3
                    elif(data[line_index][pipe_index+1] == "-" or data[line_index][pipe_index+1] == "J" or data[line_index][pipe_index+1] == "7"):
                        print("follow the right path")
                        #counter+=1
                        pipe_index += 1
                        trail = 4
                    elif(data[line_index+1][pipe_index] == "|" or data[line_index+1][pipe_index] == "J" or data[line_index+1][pipe_index] == "L"):
                        print("follow the bottom path")
                        #counter+=1
                        line_index += 1
                        trail = 1
                    elif(data[line_index][pipe_index-1] == "-" or data[line_index][pipe_index-1] == "L" or data[line_index][pipe_index-1] == "F"):
                        print("follow the left path")
                        #counter+=1
                        pipe_index -= 1
                        trail = 2
            case "|":
                if(trail == 1):
                    #going down
                    line_index += 1
                    trail = 1
                else:
                    #going up
                    line_index -= 1
                    trail = 3
            case "-":
                if(trail == 2):
                    #going left
                    pipe_index -= 1
                    trail = 2
                else:
                    #going right
                    pipe_index += 1
                    trail = 4
            case "L":
                if(trail == 1):
                    #going right
                    pipe_index += 1
                    trail = 4
                else:
                    #going up
                    line_index -= 1
                    trail = 3
            case "J":
                if(trail == 1):
                    #going left
                    pipe_index -= 1
                    trail = 2
                else:
                    #going up
                    print("8")
                    line_index -= 1
                    trail = 3
            case "7":
                if(trail == 4):
                    #going down
                    line_index += 1
                    trail = 1
                else:
                    #going left
                    pipe_index -= 1
                    trail = 2
            case "F":
                if(trail == 2):
                    #going down
                    line_index += 1
                    trail = 1
                else:
                    #going right
                    pipe_index += 1
                    trail = 4
            case _:
                print("error line index: ", line_index, "pipe index: ", pipe_index)
                return 0



File = open("day10input.txt", "r")
data = File.readlines()
for line_index, line in enumerate(data):
    for pipe_index, pipe in enumerate(line):
        if(pipe == "S"):
            print(find_path_size(line_index, pipe_index, -1, 0, 0)/2)
            break


