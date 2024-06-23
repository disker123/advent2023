from collections import Counter
import re

def score_hands(hands: list, check: int) -> list:   #takes all hands of a type and sorts them by strength, check is what card we are comparing 
    if(len(hands) == 1):    #base case 
        return hands
    if(len(hands) == 0):    #base case
        return
    final = []
    for x in (card_to_value):   #check every card rank
        deep_list = []
        hands_copy = hands.copy()   #need to itterate over a copy becuase we are editing the hands list to save time
        for hand in hands_copy:
            if(hand.cards[check] == x): #each hand that ties on the high card will be put into a new list
                deep_list.append(hand)
                hands.remove(hand)

        i = []
        if(len(deep_list) != 0):    #we will recursively call the new lists until they are empty 
            i = score_hands(deep_list, check+1)
        if(i != None):
            final =  final + i
    return final    #returns the final sorted list of hands by strength after each 


class camel_hand:
    cards = ""
    ante = 0
    def __init__(self, my_cards, my_ante ):
        self.cards = my_cards
        self.ante = int(my_ante)

    def get_type(self):   #finds what kind of hand it is
        x = Counter(self.cards)
        x = x.most_common()
        #print(x[0][1])
        if(x[0][1] == 5):
#            print("5 of a kind")
            return 6
        if(x[0][1] == 4):
#            print("4 of a kind")
            return 5
        if(x[0][1] == 3):
            if(x[1][1] == 2):
#                print("Full house")
                return 4
            else:
#                print("3 of a kind")
                return 3
        if(x[0][1] == 2):
            if(x[1][1] == 2):
#                print("2 pair")
                return 2
            else:
#                print("1 pair")
                return 1
        if(x[0][1] == 1):
#            print("high card")
            return 0


File = open("day7input.txt", "r")
data = File.readlines()
five_of_a_kind = []
four_of_a_kind = []
full_house = []
three_of_a_kind = []
two_pair = []
pair = []
high_card = []
total = []
answer = 0
card_to_value = {   #used for checking high cards when scoring hands of the same type
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}

for lines in data:  #sort all the hands into type
    hand_data = lines.split()
    my_hand = camel_hand(hand_data[0], hand_data[1])
    type = my_hand.get_type()
    match type:
        case 0:
            high_card.append(my_hand)
        case 1:
            pair.append(my_hand)
        case 2:
            two_pair.append(my_hand)
        case 3:
            three_of_a_kind.append(my_hand)
        case 4:
            full_house.append(my_hand)
        case 5:
            four_of_a_kind.append(my_hand)
        case 6:
            five_of_a_kind.append(my_hand)

total = score_hands(high_card, 0) + score_hands(pair, 0) + score_hands(two_pair, 0) + score_hands(three_of_a_kind, 0) + score_hands(full_house, 0) + score_hands(four_of_a_kind, 0) + score_hands(five_of_a_kind, 0)
hand_rank = 1
for i in total:
    answer += i.ante * hand_rank
    hand_rank += 1
print(answer)
File.close()