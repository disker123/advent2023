def forecast(history: list):
    if(all(element == 0 for element in history)):   #base case
        return 0
    new_history = []
    for i in range(0,len(history)-1):
        new_history.append(int(history[i+1])-int(history[i]))
    next_val = forecast(new_history)    #get the last value of the next itteration 
    return(int(history[len(history)-1])+next_val)   #return the last value of this itteration


File = open("day9input.txt", "r")
data = File.readlines()

solution = 0

for line in data:
    line = line.split()
    solution += forecast(line)
print(solution)
        