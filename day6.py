import math

def winning_options_odd(time: int, mark: int):  #for an odd amount of time
    for i in range(0,time+1):
        if(i*(time-i) > mark): #when we hit the first wining option
            return (((time+1)/2)-(i))*2 #the number of winning options for a game win an even number of miliseconds - ((total_options / 2) - current_index) * 2

def winning_options_even(time: int, mark: int):  #for an even amount of time
    for i in range(0,time+1):
        if(i*(time-i) > mark): #when we hit the first wining option
            return ((math.ceil((time+1)/2))-(i))*2-1 #the number of winning options for a game win an even number of miliseconds - ((total_options / 2) - current index) * 2 - 1 [note half the total options needs to be rounded up in the case of an even time/odd option count]

result = winning_options_even(60,475) * winning_options_even(94, 2138) * winning_options_even(78,1015) * winning_options_even(82, 1650)

print(result)



