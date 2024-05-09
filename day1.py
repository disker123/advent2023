File = open("day1input.txt", "r")
data = File.readlines()
#print(data)
result = 0
for i in data:
    first = None
    second = None

    for j in i:
        if(j.isnumeric()):
            first = j
            break
    for j in reversed(i):
        if(j.isnumeric()):
            second = j
            break
    value = first + second
    result += int(value)
print(result)
File.close()