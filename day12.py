def solve(input: str, broken: list, chain_length: int, chain_count: int):
    answer: int = 0
    for counter, x in enumerate(input):
        match x:
            case " ":
                if(chain_length != 0):
                    if(chain_length == broken[chain_count]):
                        if(chain_count+1 == len(broken)):
                            return 1
                elif(chain_count == len(broken)):

                    return 1
                return 0
            case "#":
                chain_length += 1
                try:
                    if(chain_length > broken[chain_count]):#the chain is too long

                        return 0
                except:#if we have more chains then there are suppsoed to be, prevents out of bounds
                    #print("too many broken chains")

                    return 0
            case ".":#checks if its the end of a chain and makes sure its the proper length or does nothing if we weren't on a chain of broken springs
                if(chain_length != 0):
                    try:
                        if(chain_length == broken[chain_count]):
                            chain_length = 0
                            chain_count += 1
                        else:

                            return 0
                    except:#if we have more chains then there are suppsoed to be, prevents out of bounds
                        #print("too many broken chains")

                        return 0
            case "?":
                #recursive call for each 
                #check to see if we are at the end of a chain and only call for '.' and if not at the end oif the chain only call for '#'
                answer += solve("#"+input[counter+1:], broken, chain_length, chain_count)
                answer += solve("."+input[counter+1:], broken, chain_length, chain_count)
                return answer
    print("we should never get here")
    return 0

File = open("day12input.txt", 'r')
data = File.readlines()
answer = 0
for line in data:
    line = line.replace("\n", "")
    num = line.find(" ")
    input = line[:num+1]
    list_of_numbers = line[num+1:].split(",")
    broken = [int(num) for num in list_of_numbers]
    answer += solve(input, broken, 0, 0)
print("answer is ", answer)

