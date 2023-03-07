import gspread
from google.oauth2.service_account import Credentials
import random
import os
from itertools import cycle

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
SHEET = GSPREAD_CLIENT.open('bullshit')

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
    game_rules()
    get_username()
    global hands
    hands = deal_cards()
 
    print("Communal pile:", communal_pile)
    print("You have", len(hands[current_player]), "cards:", hands[current_player])
    print("Player 2 has", len(hands[current_player]), "cards", hands[current_player + 1])
    print("Player 3 has", len(hands[current_player]), "cards", hands[current_player + 2])
    print(f"Discard {ask_question():}")

    user_choice()
       
    computer_call_bullshit()

    computer_card_select()

    user_call_bullshit()

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
    print("                                                Developed by Orna Reynolds")

def game_rules():
    """
    displays rules of game 
    """
    print("* This is a game of bluff. ")
    print("* The game begins with 52 deck cards being split evenly between players")
    print("* The aim of the game is to be the first to get rid of all your cards")
    print("* The player begins the game by playing an ace")
    print("* The game then continues with the next player discarding any 2s they have")
    print("* Then the next player discards any 3s they have and so on")
    print("* Player can put down all multiples of the card they have")
    print("* The bluff happens when the player decides to lie about what cards they have put down")
    print("* Call bullshit if you sense your opponents bluff, but fear getting all the cards in commual pile!\n")
    input("Press enter to begin...\n")

def get_username():
    """
    get username input from the user 
    """
    while True:
            try:
                username = input("Now...what is your name?\n")
                username_validated = username.capitalize()
                if validate_username_data(username):
                    print(f"{username_validated}? Hello there, lets get started!{os.linesep}")
                    break 
                else:
                    print("Psst...is your name made up of only letters\n")
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
    player1 = []
    player2 = []
    player3 = []
    card = get_deck()
    for i in range(4):
        player1.append(card.pop())
        player2.append(card.pop())
        player3.append(card.pop())
    return player1, player2, player3

# trying to get to loop through to next quextion
def ask_question():
    numbers = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    x = iter(numbers)
    print(x)
    # question_number.append(number)
        
 
ask_question()

def user_choice():
    for count, option in enumerate([hands[current_player][0], hands[current_player][1], hands[current_player][2], hands[current_player][3]]):
                    print(f"{count+1}. {option}")
    while True:
                try:
                    card_option = int(input("Select a card to discard: "))
                    if card_option in [1,2,3,4]:
                        global card_chosen
                        card_chosen = hands[current_player][card_option - 1]
                        print(f"You have chosen card {card_chosen} to discard!")
                        global communal_pile
                        communal_pile += 1
                        print(f"Communal pile: {communal_pile}")
                        discarded_cards.append(card_chosen)
                        break
                    else: 
                        print(f"You don't have that card!")
                except ValueError:
                    print("Huh?")  

def computer_call_bullshit():
    print("Player 2 and 3 are deciding if you are lying or not...")
    random.choice([True, False])
    if True:
        print("Player called bullshit, they think you are lying!")
        if card_chosen == ask_question():
            print("Computer was wrong, you were telling the truth!")
            discarded_cards.remove(card_chosen)
            hands[current_player + 1].append(card_chosen)
        else:
            print("Computer guessed you were lying!") 
            discarded_cards.remove(card_chosen)
            hands[current_player].append(card_chosen)
    else:
        print("Players think you are telling the truth, no one called bullshit")

def computer_card_select():
    computer_card_option = [1,2,3,4]
    x = random.choice(computer_card_option)
    computer_card_chosen = hands[current_player + 1][x - 1]
    print("Next player's turn")
    global communal_pile
    communal_pile += 1
    print(f"Communal pile: {communal_pile}")
    discarded_cards.append(computer_card_chosen)
    print(f"Player has discarded card {ask_question()}")


def user_call_bullshit():
    if input("Do you want to call bullshit? (y/n) ") == 'y':
        if card_chosen == ask_question():
            print("Player was telling the truth!")
        else:
            print("Player was lying!")
       

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


