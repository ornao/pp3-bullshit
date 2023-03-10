import gspread
from google.oauth2.service_account import Credentials
import random
import os

# Below code taken from Code Institute's Love Sandwiches Walkthrough Project:
# Getting Set Up (Creating the Google Sheets API)
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('bullshit').worksheet('username')

# Code from Blackjack, by Al Sweigart al@inventwithpython.com
HEART = chr(9829) # Character 9829 is '♥'.
# DIAMOND = chr(9830) # Character 9830 is '♦'.
# SPADE = chr(9824) # Character 9824 is '♠'.
# CLUB = chr(9827) # Character 9827 is '♣'.
question_number = []
communal_pile = 0
current_player = 0
discarded_cards = []

def main():
    title()
    menu_select()
    global hands
    hands = deal_cards()

    card_hands()

    ask_question()
    
    user_choice()
       
    computer_call_bullshit()

    card_hands()

    computer2_card_select()

    user_call_bullshit_player2()

    card_hands()

    # computer3_card_select()

    # user_call_bullshit()

def title():
    """
    displays title of game and name of developer
    """
    print("██████╗░██╗░░░██╗██╗░░░░░██╗░░░░░░██████╗██╗░░██╗██╗████████╗░░░░░░░░░███ ")
    print("██╔══██╗██║░░░██║██║░░░░░██║░░░░░██╔════╝██║░░██║██║╚══██╔══╝░░░░░░░░░███ ")
    print("██████╦╝██║░░░██║██║░░░░░██║░░░░░╚█████╗░███████║██║░░░██║░░░░░░░░░░░░███  ")
    print("██╔══██╗██║░░░██║██║░░░░░██║░░░░░░╚═══██╗██╔══██║██║░░░██║░░░░░▄█████▄█▀▀ ")
    print("██████╦╝╚██████╔╝███████╗███████╗██████╔╝██║░░██║██║░░░██║░░░░░▀█████  ")
    print("╚═════╝░░╚═════╝░╚══════╝╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░░╚═╝░░░░░░▄████▄ \n")
    print("                                                  A bluffing card game")
    print("                                                Developed by Orna Reynolds")

def menu_select():
    """
    User selects whether to start the game or look at the rules first
    """
    print("Which are you feeling?")
    start_options = "1) Play the game\n2) Have a deeper look at the rules first\n (psst...click me if this is your first time playing)\n"
    start_option_selected = input(start_options)

    # Validatation for user input
    choice = start_option_selected
    while choice not in ["1","2"]:
        print("Surely you know where 1 and 2 are on your keyboard.")
        choice = input(start_options)

    if start_option_selected == "1":
        get_username()

    elif start_option_selected == "2":
        game_rules()
        get_username()
            
    return start_option_selected

def game_rules():
    """
    displays rules of game 
    """
    print("* This is a game of bluff. ")
    print("* The game begins with each player receiving 5 cards")
    print("* The aim of the game is to be the first to get rid of all your cards")
    print("* The game begins by asking player 1 to play the first card: Ace")
    print("* The player can play the ace card or lie and play another card instead")
    print("* The game then continues with the next player discarding any 2s they have")
    print("* Then the next player discards any 3s they have and so on")
    print("* Player can put down all multiples of the card they have")
    print("* The bluff happens when the player decides to lie about what cards they have put down")
    print("* Call bullshit if you sense your opponents bluff, but fear getting all the cards in commual pile!\n")
    input("Press enter to begin...\n")

def get_username():
    """
    get username input from the user and add to google sheets
    """
    while True:
            try:
                username = input("Now...what is your name?\n")
                username_validated = username.capitalize()
                new_row = [username_validated]
                SHEET.append_row(new_row)
                if validate_username_data(username):
                    print(f"{username_validated}? Hello there, let's get started!{os.linesep}")
                    break 
                else:
                    print("Psst...is your name made up of only letters\n")
                    print('And yes that means no spaces too')
            except ValueError:
                print("Huh?")          
    return(username_validated)

def validate_username_data(username):
    """ 
    validate username so that can only accept alphabetical letters 
    """
    return username.isalpha()

def get_deck():
    """get shuffled deck everytime"""
    deck = []
    # for suit in [HEART,CLUB,DIAMOND,SPADE]:
    for number in ['A','K','Q','J','2','3','4','5','6','7','8','9','10']:
        deck.append(number+HEART)

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

def card_hands():
    """display cards number of cards in each players hand """
    print("Communal pile:", communal_pile)
    print("You have", len(hands[current_player]), "cards:", hands[current_player])
    print("Player 2 has", len(hands[current_player + 1]), "cards", hands[current_player + 1])
    print("Player 3 has", len(hands[current_player + 2]), "cards", hands[current_player + 2])
    # print(ask_question())

# trying to get to loop through to next quextion
def ask_question():
    global question
    question = input("Type in a random card from A-K to discard:")
    print("Remember you don't actually need to have that card in your hand, your opponents just have to believe you have it")
    
    # numbers = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    # print(num)
    # thiselem = numbers[num]
    # running = True
    # idx = 0
    # while running:
    #         thiselem = numbers[idx]
    #         # idx = (idx) % len(numbers)
    #         idx +=1
    #         # nextelem = numbers[idx +1] 
    #         if thiselem == numbers[0]:
    #             break
            
    return question + HEART 

# numbers = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
# for i in numbers:
#     current_question = i + HEART
    # print(current_question)


# for i in range(len(numbers)):
# current_question = ask_question()

def user_choice():
    "allows user to discard number 1-4 card in their hands"
    for count, option in enumerate([hands[current_player][0], hands[current_player][1], hands[current_player][2], hands[current_player][3]]):
                    print(f"{count+1}. {option}")
    while True:
                try:
                    card_option = int(input("Select a card from 1-4 to discard: "))
                    if card_option in [1,2,3,4]:
                        global card_chosen
                        card_chosen = hands[current_player][card_option - 1]
                        print(f"You have chosen card {card_chosen} to discard!")
                        global communal_pile
                        communal_pile += 1
                        print(f"Communal pile: {communal_pile}")
                        hands[current_player].remove(card_chosen)
                        discarded_cards.append(card_chosen)
                        print(discarded_cards)
                        break
                    else: 
                        print(f"You don't have that card!")
                except ValueError:
                    print("Huh?")  

def computer_call_bullshit():
    """computer randomly decided if true or false - so calls bullshit"""
    print("Player 2 and 3 are deciding if you are lying or not...")
    z = random.choice([True, False])
    if z is True:
        random_choice_players = [2,3]
        x = random.choice(random_choice_players)
        print(f"Player {x} called bullshit, they think you are lying!")
        if card_chosen == question + HEART:
            print("Computer was wrong, you were telling the truth!")
            # trying to get all cards in discarded to add to losers hand
            if x == 2:
                hands[current_player + 1].extend(discarded_cards)
                discarded_cards.clear()
                print(discarded_cards)
            else:
                hands[current_player + 2].extend(discarded_cards)
                discarded_cards.clear()
                print(discarded_cards)

        else:
            print(f"Player {x} guessed you were lying!") 
            hands[current_player].extend(discarded_cards)
            discarded_cards.clear()
            print(discarded_cards)
    else:
        print("Player 2 and 3 think you are telling the truth, no one called bullshit")

def computer2_card_select():
    """computer randomly decides 1-4 so what card to choose to dicard"""
    computer_card_option = [1,2,3,4]
    x = random.choice(computer_card_option)
    computer_card_chosen = hands[current_player + 1][x - 1]
    print("Next player's turn")
    global communal_pile
    communal_pile += 1
    print(f"Communal pile: {communal_pile}")
    discarded_cards.append(computer_card_chosen)
    numbers = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    global y
    y = random.choice(numbers)
    print(f"Player 2 has discarded card {y + HEART}")
    print('Do you think they are lying?')

def computer3_card_select():
    """computer randomly decides 1-4 so what card to choose to dicard"""
    computer_card_option = [1,2,3,4]
    x = random.choice(computer_card_option)
    computer_card_chosen = hands[current_player + 2][x - 1]
    print("Next player's turn")
    global communal_pile
    communal_pile += 1
    print(f"Communal pile: {communal_pile}")
    discarded_cards.append(computer_card_chosen)
    numbers = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    global y
    y = random.choice(numbers)
    print(f"Player 3 has discarded card {y + HEART}")
    print('Do you think they are lying?')

def user_call_bullshit_player2():
    if input("Do you want to call bullshit? (y/n) ") == 'y':
        if y == question + HEART:
            print("Player 2 was telling the truth!")
        else:
            print("Player 2 was lying!")
            print(discarded_cards)
            hands[current_player + 1].extend(discarded_cards)
            discarded_cards.clear()

def user_call_bullshit_player3():
    if input("Do you want to call bullshit? (y/n) ") == 'y':
        if y == question + HEART:
            print("Player 3 was telling the truth!")
        else:
            print("Player 3 was lying!")
            print(discarded_cards)
            hands[current_player + 2].extend(discarded_cards)
            discarded_cards.clear()
       

# def display_picture_cards():
#     rows = ['', '', '', '', ''] 
#     x = get_random_point()
#     rows[0] += ' ___ ' 
#     rows[1] += '|{}  |'.format(x)
#     rows[2] += '| {} |'.format(get_random_suit())
#     rows[3] += '|__{}|'.format(x)
#     for row in rows: 
#         print(row)

# def display_hidden_cards():
#     rows = ['', '', '', '', '']
#     rows[0] += ' ___ ' 
#     rows[1] += '|## | '
#     rows[2] += '|###| '
#     rows[3] += '|_##| '
#     for row in rows: 
#          print(row)

main()


