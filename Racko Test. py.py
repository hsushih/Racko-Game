import random
import string

def shuffle():
    ''' Suffles the deck or the discard pile, it choose which one to shuffle'''
    global deck
    global discard
#shuffle the deck if the deck is not empty otherwise shuffle the discard pile
    if len(deck)== 0:
        random.shuffle(discard)
    else:
        random.shuffle(deck)

def check_racko(rack):
    '''Given a rack, check if the cards are in ascending order, return boolean'''
    ideal = rack[:]
    ideal.sort()
#The deck is drown in the order of slot 10 to slot 1
    ideal.reverse()
    if ideal == rack:
        return True
    else:
        return False

def deal_card():
    '''return the top card from the deck'''
    global deck
    return deck.pop(0)

def deal_initial_hands():
    '''start the game, draw 10 cards for both the gamer and pc, return both'''
    global deck
    player = []
    pc = []
    for i in range(0,10):
        pc.append(deal_card())
        player.append(deal_card())
    return (pc,player)

def does_user_begin():
    '''return true if the player gets a head, hence start the game first'''
    chance = random.randint(0,9)
    if chance <= 4:
        return True
    else:
        return False

def print_top_to_bottom(rack):
    '''Print the list from top to bottom'''
    for x in rack:
        print x

def find_and_replace(newCard, cardToBeReplaced, hand):
    '''place the old card by the new card of a given hand, return the old car that is being replaced'''
    count = hand.count(cardToBeReplaced)
#check if the number user entered existed in the hand, if not ask the user to reenter
    while count == 0:
        print ('Sorry, the card you just entered is not in your current hand')
        cardToBeReplaced=input('please re-enter a card that you want to replace\n')
        count = hand.count(cardToBeReplaced)
#replace the selected existing card with the new card
    i = hand.index(cardToBeReplaced)
    hand[i] = newCard
    return cardToBeReplaced

def add_card_to_discard(card):
    '''add the card to the top of the discard pile'''
    global discard
    discard.insert(0,card)


def computer_play_index(loweLimit,upperLimit,nextLowerLimit,lastUpperLimit,index,pickCard,isFull,hand):
    '''Make the slection of whether to replace the new card for a specific index of the hand'''
    '''or draw a new crad from the deck '''
    if isFull == False:
        if pickCard >= loweLimit and pickCard <= upperLimit:
            temp = find_and_replace(pickCard,hand[index],hand)
            add_card_to_discard(temp)
            upperLimit = pickCard
            nextLowerLimit = pickCard+1
            lastUpperLimit = pickCard-1
            isFull = True
    if isFull == True:
        if pickCard >= loweLimit and pickCard <= upperLimit :
            add_card_to_discard(deal_card())




def computer_play_1(lowerLimit,upperLimit,carddraw,isFull,hand):
    if isFull == False:
        if carddraw > lowerLimit and carddraw <= upperLimit :
            trashcard = find_and_replace(carddraw, hand[9], hand)
            add_card_to_discard(trashcard)
            upperLimit = carddraw
            isFull = True
            return upperLimit
    elif isFull == True:
        if carddraw > lowerLimit and carddraw <= upperLimit :
            add_card_to_discard(deal_card())
            
            

def computer_play_2(lowerLimit,upperLimit,carddraw,isFull,hand):
    if isFull == False:
        if carddraw > lowerLimit and carddraw <= upperLimit :
            trashcard = find_and_replace(carddraw, hand[8], hand)
            add_card_to_discard(trashcard)
            upperLimit = carddraw
            isFull = True
            return upperLimit
    elif isFull == True:
        if carddraw > lowerLimit and carddraw <= upperLimit :
            add_card_to_discard(deal_card())
            
            

def computer_play_3(lowerLimit,upperLimit,carddraw,isFull,hand):
    if isFull == False:
        if carddraw > lowerLimit and carddraw <= upperLimit :
            trashcard = find_and_replace(carddraw, hand[7], hand)
            add_card_to_discard(trashcard)
            upperLimit = carddraw
            isFull = True
            return upperLimit
    elif isFull == True:
        if carddraw > lowerLimit and carddraw <= upperLimit :
            add_card_to_discard(deal_card())
            

            
def computer_play_4(lowerLimit,upperLimit,carddraw,isFull,hand):
    if isFull == False:
        if carddraw > lowerLimit and carddraw <= upperLimit :
            trashcard = find_and_replace(carddraw, hand[6], hand)
            add_card_to_discard(trashcard)
            upperLimit = carddraw
            isFull = True
            return upperLimit
    elif isFull == True:
        if carddraw > lowerLimit and carddraw <= upperLimit :
            add_card_to_discard(deal_card())
            
            



def computer_play_5(lowerLimit,upperLimit,carddraw,isFull,hand):
    if isFull == False:
        if carddraw > lowerLimit and carddraw <= upperLimit :
            trashcard = find_and_replace(carddraw, hand[5], hand)
            add_card_to_discard(trashcard)
            upperLimit = carddraw
            isFull = True
            return upperLimit
    elif isFull == True:
        if carddraw > lowerLimit and carddraw <= upperLimit :
            add_card_to_discard(deal_card())
            


def computer_play_6(lowerLimit,upperLimit,carddraw,isFull,hand):
    if isFull == False:
        if carddraw > lowerLimit and carddraw <= upperLimit :
            trashcard = find_and_replace(carddraw, hand[4], hand)
            add_card_to_discard(trashcard)
            upperLimit = carddraw
            isFull = True
            return upperLimit
    elif isFull == True:
        if carddraw > lowerLimit and carddraw <= upperLimit :
            add_card_to_discard(deal_card())
            
            



def computer_play_7(lowerLimit,upperLimit,carddraw,isFull,hand):
    if isFull == False:
        if carddraw > lowerLimit and carddraw <= upperLimit :
            trashcard = find_and_replace(carddraw, hand[3], hand)
            add_card_to_discard(trashcard)
            upperLimit = carddraw
            isFull = True
            return upperLimit
    elif isFull == True:
        if carddraw > lowerLimit and carddraw <= upperLimit :
            add_card_to_discard(deal_card())
            




def computer_play_8(lowerLimit,upperLimit,carddraw,isFull,hand):
    if isFull == False:
        if carddraw > lowerLimit and carddraw <= upperLimit :
            trashcard = find_and_replace(carddraw, hand[2], hand)
            add_card_to_discard(trashcard)
            upperLimit = carddraw
            isFull = True
            return upperLimit
    elif isFull == True:
        if carddraw > lowerLimit and carddraw <= upperLimit :
            add_card_to_discard(deal_card())
            
            


def computer_play_9(lowerLimit,upperLimit,carddraw,isFull,hand):
    if isFull == False:
        if carddraw > lowerLimit and carddraw <= upperLimit :
            trashcard = find_and_replace(carddraw, hand[1], hand)
            add_card_to_discard(trashcard)
            upperLimit = carddraw
            isFull = True
            return upperLimit
    elif isFull == True:
        if carddraw > lowerLimit and carddraw <= upperLimit :
            add_card_to_discard(deal_card())
            
            



def computer_play_10(lowerLimit,upperLimit,carddraw,isFull,hand):
    if isFull == False:
        if carddraw > lowerLimit and carddraw <= upperLimit :
            trashcard = find_and_replace(carddraw, hand[0], hand)
            add_card_to_discard(trashcard)
            upperLimit = carddraw
            isFull = True
            return upperLimit
    elif isFull == True:
        if carddraw > lowerLimit and carddraw <= upperLimit :
            add_card_to_discard(deal_card())
            
            



def computer_play(hand):
    a=0
    b=6
    c=b+6
    d=c+6
    e=d+6
    f=e+6
    g=f+6
    h=g+6
    i=h+6
    j=i+6
    k=j+6
    
 
    
    isFull1 = isFull2 = isFull3 = isFull4 = isFull5 = isFull6 = False
    isFull7 = isFull8 = isFull9 = isFull10 = False

    count = 1


    for count in range(1,2):
        computer_play_1(a,b,discard[0],isFull1,hand)
        computer_play_2(b,c,discard[0],isFull2,hand)
        computer_play_3(c,d,discard[0],isFull3,hand)
        computer_play_4(d,e,discard[0],isFull4,hand)
        computer_play_5(e,f,discard[0],isFull5,hand)
        computer_play_6(f,g,discard[0],isFull6,hand)
        computer_play_7(g,h,discard[0],isFull7,hand)
        computer_play_8(h,i,discard[0],isFull8,hand)
        computer_play_9(i,j,discard[0],isFull9,hand)
        computer_play_10(j,k,discard[0],isFull10,hand)
        count = count +1
        print a,b,c,d,e,f,g,h,i,j,k  
    return hand 


def main():
    '''the main function that runs the Racko game'''
    
#define global variable deck and discard, give the full deck of 1 to 60, empty discard hand
#shuffle the deck
    global deck
    global discard
    deck = range(1,61)
    discard = []
    shuffle()
    
#deal 10 cards each to the player and pc, saved in lists called computer_hand, human_hand
    computer_hand, human_hand = deal_initial_hands()
    
#determine whether the user start or not
    userStarts = does_user_begin()
    if userStarts == True:
        print 'Here is your 10 cards, the top card is in slot 10'
        print 'You need to arrange the order such that is is assending from bottom to top'
        print_top_to_bottom(human_hand)
        print ' computer hand initial', computer_hand
    
#Draw the first card from the deck and put into discard to begin the game
        add_card_to_discard(deal_card())
        print ''
        print "The first card drawn from the deck is "+ str(discard[0])
        print ''
    else:
        #While neither player has Racko
        while check_racko(human_hand)==False and check_racko(computer_hand)==False:
            computer_hand = computer_play(computer_hand)

        if check_racko(computer_hand)==True:
            print('You Lost!!!!!!!')
            break
        
        print 'the top card in the discard pile is '+ str(discard[0])
        print 'computer hand', computer_hand
        print 'Here is your current hand'
        print_top_to_bottom(human_hand)
        print ''
        choice = raw_input ('Do you want to keep it? enter y or n\n')
        print ''
        
#If the player choose to use the discarded card by the computer
#Ask the user to input a card to be replaced and print the new hand
        if choice == 'y':
            print ''
            oldCard = input ('Please enter the card you want to replace\n')
            oldCard = find_and_replace(discard[0],oldCard,human_hand)
            add_card_to_discard(oldCard)
            
#If the player choose not to use the discarded card by the computer, draw a card from the deck
#Ask the user to input a card to be replaced and print the new hand
        elif choice == 'n':
            card = deck.pop()
            print "The card you drwan from the deck is "+ str(card) 
            secondChoice = raw_input ('Do you want to keep it? enter y or n\n')
            if secondChoice == 'y':
                print ''
                oldCard = input ('Please enter the card you want to replace\n')
                oldCard = find_and_replace(card,oldCard,human_hand)
                add_card_to_discard(oldCard)
            else:
                add_card_to_discard(card)
                   
#Check if the deck is empty, if it is, reshuffle the discard and restart
        if len(deck)== 0:
            topCard = discard.pop(0)
            shuffle()
            deck = discard[:]
            discard = [].insert(0,topCard)

#When while ends, out put whether the player won or not
    if check_racko(human_hand) == True:
        print ('You Won!!!!!!!')
    else:
        print('You Lost!!!!!!!')
    print ''
    print('Here is your hand')
    print_top_to_bottom(human_hand)
    print("Here is your Component's hand")
    print_top_to_bottom(computer_hand)
        
        
if __name__ == "__main__":
    main()
