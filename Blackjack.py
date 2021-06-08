import random

def createhand(player,cards):
    random.shuffle(cards)
    card1 = cards[0]
    card2 = cards[1]
    player.append(card1)
    player.append(card2)

def hit(player,cards):
    random.shuffle(cards)
    card = cards[0]
    player.append(card)

def dealerhit(player,cards):
    # the dealer needs to randomly choose when to stop hitting
    # or
    # the dealer needs to strategically choose when to stop hitting
    dealerhit = True
    while dealerhit:
        if sumofcards(player) >= 21:
            print("Bust! Score too high.")
            break
        else:
            random.shuffle(cards)
            player.append(cards[0])
            print("Dealer hit")
            x = random.randint(0,1)
            if x == 0:
                continue
            elif x == 1:
                break

def printcards(player):
    print(player)

def sumofcards(player):
    total = 0
    for x in player:
        if x == "King" or x == "Queen" or x == "Jack":
            total += 10
        elif x == "Ace":
            if (total + 11) >= 21:
                total += 1
            else:
                total += 11
 
        else:
            total += int(x)
    print("Sum of cards: " + str(total))
    return total
    
def playgame():
    cards = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
    player = []
    dealer = []
    print("Welcome to Blackjack")
    stillgoing = True
    while stillgoing:
        createhand(player,cards)
        printcards(player)
        sumofcards(player)
        createhand(dealer,cards)
        printcards(dealer)
        sumofcards(dealer)
        hitting = True
        while hitting:
            if sumofcards(player) >= 21:
                print("Bust! Score too high.")
                hitting = False
            else:
                x = input("Hit? (y/n): ")
                if x == "y":
                    hit(player,cards)
                    printcards(player)
                    sumofcards(player)
                if x == "n":
                    hitting = False
        dealerhit(dealer,cards)
        if sumofcards(player) > sumofcards(dealer):
            print("Congrats! You won!")
        else:
            print("Dealer wins!")
            player.clear()
            dealer.clear()
            x = input("Do you want to play again? (y/n) ")
            if x == "y":
                continue
            elif x == "n":
                stillgoing = False

        
playgame()

