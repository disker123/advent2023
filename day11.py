import os
os.remove("day11output.txt") 
input_file = open("day11input.txt", "r")
data = input_file.readlines()
output_file = open("day11output.txt", "a")


empty_vertical = {}
empty_horizontal = {}
Galaxies = 0
#populate the vertical dict with a defualt of empty 
for i in range(len(data[0].replace("\n", ""))): #don't look at the new line characters only the space data
    empty_vertical[i] = True
#populate the horizontal dict with a default of empty
for line_counter, line in enumerate(data):
    empty_horizontal[line_counter] = True

for line_counter, line in enumerate(data):  #checks every location and if they have a galaxy sets the dicts that those verticals and horizontals aren't empty
    for space_counter, space in enumerate(line):
        if(space == "#"):
            empty_horizontal[line_counter] = False
            empty_vertical[space_counter] = False
            Galaxies += 1
print(empty_horizontal)
print(empty_vertical)
empty_vertical_count = 0    #used to know how many empty spaces to add to each expanded horizontal line
for val in empty_vertical.values():
    if val == True:
        empty_vertical_count += 1

#expand the universe
for line_counter, line in enumerate(data):
    new_text = str(line)
    H_flag = 0  #used so we don't create multiple new horizontal lines
    V_flag = 0  #used to compensate for the change in index of the line as we expand for other new vertical lines
    for space_counter, space in enumerate(line.replace("\n", "")):
        if(empty_horizontal[line_counter] == True and H_flag == 0): #expand a new horizontal line 
            temp = new_text
            for i in range(0,empty_vertical_count): #makes the expanded line the same size as the other lines
                temp = "." + temp[0:]
            output_file.write(temp)
            H_flag = 1
        if(empty_vertical[space_counter] == True):  #expands a vertical line which is created as we move through the image
            new_text = new_text[:space_counter+V_flag] + "." + new_text[space_counter+V_flag:] #add a new sapce where there is an empty vertical line 
            V_flag += 1
    output_file.write(new_text)

#close and reopen the new file in read mode
output_file.close()
xyxy = open("day11output.txt", "r")
data = xyxy.readlines()
length = 0
#loop through the universe finding the length between each paiur of galaxies starting with all pairs including 1,2,3...n
for i in range(0,Galaxies):
    galaxies_skipped = 0
    current_galaxy = (None, None)   #coordinates of the galaxy we are finding all pairs for 
    for line_counter, line in enumerate(data):
        for space_counter, space in enumerate(line):
            if(space == "#" and current_galaxy == (None, None) and i <= galaxies_skipped):    #for the first galaxy we come to 
                current_galaxy = (line_counter, space_counter)
                continue
            elif(space == "#" and i> galaxies_skipped): #checks if this galaxy is one we have already found all the pairs for and skips it if true
                galaxies_skipped += 1

            if(space == "#" and current_galaxy != (None, None)):    #for all other galaxies who come to so we can measure the length 
                x = (abs(space_counter-current_galaxy[1]) + abs(line_counter-current_galaxy[0]))
                length += x
                #print(x)

print("the total length is: ", length)


#    if(is_empty == True):
#        expand = str(line).replace("\n", "") + "." + "\n"
#        output_file.write(expand)
#    else:
#        output_file.write(str(line))
input_file.close()
output_file.close()