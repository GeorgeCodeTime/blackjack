import random
import time

suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
index_labels = {1: "First",2: "Second",3: "Third",4: "Fourth",5: "Fifth",6: "Sixth",7: "Seventh",8: "Eighth",9: "Ninth"}

def newDeck():
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def handCards(hand, title="Text", show_output=True):
    total = 0
    if show_output:
        print("*******************************")
    for index, (rank, suit) in enumerate(hand):
        index_label = index_labels.get(index+1)
        if show_output:
            print(f"{title} {index_label} card : {rank} of {suit}, Value: {values[rank]}")
        total += values[rank]
    if show_output:
        print("Total: " + str(total))
        print("*******************************")
    return total

def get_bet(balance):
    while True:
        try:
            your_bet = int(input("Place your bet: "))
            if your_bet <= 0:
                print("Your bet must be greater than 0!")
            elif your_bet > balance:
                print("Your bet must be less than your balance!")
            else:
                return your_bet
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
def play():
    
    balance = 1000
    deck = newDeck()
    
    while True:
        if len(deck) < 10:
            deck = newDeck()
      
        print("*******************************")
        print("Your balance is: " + str(balance) + "$")
        print("*******************************")
        time.sleep(1)
        if balance == 0:
            print("*******************************")
            print("You lost all of your money!")
            print("*******************************")
            break
        
        bet = get_bet(balance)
        
        balance -= bet
        print("*******************************")
        print(f"New balance: {balance}$")
        print("*******************************")
        time.sleep(1)
        
        myHand = [deck.pop(), deck.pop()]
        dealerHand = [deck.pop(), deck.pop()]
        
        player_total = handCards(myHand, "Your", show_output=True)
        time.sleep(1.5)
        
        if player_total == 21:
            balance += bet * 2.5
            print("*******************************")
            print("Blackjack!")
            print("You won!")
            print("Now your balance is: " + str(balance))
            print("*******************************")
            time.sleep(1)
            continue
        elif player_total > 21:
            print("*******************************")
            print("You lost")
            print("Now your balance is: " + str(balance))
            print("*******************************")
        print("*******************************")
        
        
        print("Dealer's first card: " + dealerHand[0][0] + " of " + dealerHand[0][1] + ", Value: " + str(values[dealerHand[0][0]]))
        print("Dealer's second card: hidden")
        print("*******************************")
        
        choice = None
        while choice != "h" and choice != "s":
            choice = input("Hit or Stand?(h/s): ").lower()
            
        time.sleep(1)
        
        while choice == "h":
            myHand.append(deck.pop())
            player_total = handCards(myHand, "Your", show_output=True)
            if player_total == 21:
                print("*******************************")
                print("You have 21!")
                print("*******************************")
                time.sleep(1)
                break
            elif player_total > 21:
                print("*******************************")
                print("You lost!")
                print("*******************************")
                time.sleep(1)
                break
            
            choice = input("Hit or Stand?(h/s): ").lower()
        
        if player_total > 21:
            continue
        
        if choice == "s" or player_total <= 21:
            print("*******************************")
            print("You stand!")
            print("*******************************")
            time.sleep(1)
            print("*******************************")
            print("Dealer's first card: " + dealerHand[0][0] + " of " + dealerHand[0][1] + ", Value: " + str(values[dealerHand[0][0]]))
            print("Dealer's second card: " + dealerHand[1][0] + " of " + dealerHand[1][1] + ", Value: " + str(values[dealerHand[1][0]]))
            dealer_total = values[dealerHand[0][0]] + values[dealerHand[1][0]]
            print(f"Total: {dealer_total}")
            print("*******************************")
            time.sleep(1)
            
        if dealer_total == 21:
            print("*******************************")
            print("Dealer has Blackjack!")
            print("You lost!")
            print("*******************************")
            continue
            
        while dealer_total < 17:
            print("*******************************")
            print("Dealer hits!")
            print("*******************************")
            time.sleep(2)
            dealerHand.append(deck.pop())
            dealer_total = handCards(dealerHand, "Dealer's", show_output=True)
            time.sleep(1)
            if dealer_total == 17:
                print("*******************************")
                print("Dealer stand!")
                print("*******************************")
                break
            if dealer_total > 21:
                print("*******************************")
                print("Dealer's total: " + str(dealer_total))
                print("*******************************")
                print("You won!")
                print("*******************************")
                balance += bet*2
                break
        
        if dealer_total > 21:
            continue
        
        time.sleep(2)    
        if player_total > dealer_total:
            print("*******************************")
            print(f"Your total is: {player_total}")
            print("*******************************")
            time.sleep(1)
            print("*******************************")
            print(f"Dealer's total is: {dealer_total}")
            print("*******************************")
            time.sleep(1)
            print("*******************************")
            print("You won!")
            print("*******************************")
            balance += bet*2
        elif player_total < dealer_total:
            print("*******************************")
            print(f"Your total is: {player_total}")
            print("*******************************")
            time.sleep(1)
            print("*******************************")
            print(f"Dealer's total is: {dealer_total}")
            print("*******************************")
            time.sleep(1)
            print("*******************************")
            print("You lost!")
            print("*******************************")
        elif player_total == dealer_total:
            print("*******************************")
            print(f"Your total is: {player_total}")
            print("*******************************")
            time.sleep(1)
            print("*******************************")
            print(f"Dealer's total is: {dealer_total}")
            print("*******************************")
            time.sleep(1)
            print("*******************************")
            print("Draw!")
            print("*******************************")
            balance += bet

play()