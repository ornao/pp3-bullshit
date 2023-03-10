import random

current_player = 0

def get_deck():
    """get shuffled deck everytime"""
    deck = []
    # for suit in [HEART,CLUB,DIAMOND,SPADE]:
    for number in ['A','K','Q','J','2','3','4','5','6','7','8','9','10']:
        deck.append(number)

    random.shuffle(deck)
    return deck

def deal_cards():
    """return 3 seperate unique hands to players"""
    player1 = []
    player2 = []
    player3 = []
    card = get_deck()
    for i in range(4):
        player1.append(card.pop())
        player2.append(card.pop())
        player3.append(card.pop())
    return player1, player2, player3

hands = deal_cards()


print("You have", len(hands[current_player + 1]), "cards:", hands[current_player + 1])
# print(ask_question())




computer_card_option = [1,2,3,4]
x = random.choice(computer_card_option)
print(x)
computer2_card_chosen = hands[current_player + 1][x - 1]
print(computer2_card_chosen)