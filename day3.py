def check_for_symbols(line_index, char_index, endex):
    for x in range(char_index-1, endex+2):  #loop the run of chars in the line that are adjacent to the part number
        try:    #avoid out of bounds
            line = data[line_index]
        except:
            pass
        else:    
            if(line[x] in symbols):
                return True
    return False

def get_part_number(line, char_index, endex):
    part = ""
    for x in range(char_index, endex+1):
        part+= line[x]
    return part



File = open("day3input.txt", "r")
data = File.readlines()
result = 0
symbols =  "/@*$=&#-+%"
for line_index, line in enumerate(data):
    for char_index, char in enumerate(line):   #loop through each char
        if(line[char_index-1].isnumeric()):
            continue
        if(char.isnumeric()):   #when we find a number start doing stuff
            endex = char_index   #I thought it was a clever name
            while line[endex+1].isnumeric():    #find the end of the part number
                endex+=1           
            #print("part number:", get_part_number(line, char_index, endex))
            if(check_for_symbols(line_index-1, char_index, endex) or check_for_symbols(line_index, char_index, endex) or check_for_symbols(line_index+1, char_index, endex)):   #if therre is an adjacent symbol add the part number to our result
                part = get_part_number(line, char_index, endex)
                #print("part number:", part)
                result+= int(part)

            


print("result is: ", result)
File.close()

