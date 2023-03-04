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
SHEET = GSPREAD_CLIENT.open('bullshit')
# Code from Blackjack, by Al Sweigart al@inventwithpython.com
HEART = chr(9829) # Character 9829 is '♥'.
DIAMOND = chr(9830) # Character 9830 is '♦'.
SPADE = chr(9824) # Character 9824 is '♠'.
CLUB = chr(9827) # Character 9827 is '♣'.

def main():
    title()
    game_rules()
    get_username()

    hands = deal_cards()
    communal_pile = 0
    current_player = 0
    global discarded_cards
    discarded_cards = []

    print("Communal pile:", communal_pile)
    print("You have", len(hands[current_player + 1]), "cards:", hands[current_player])
    print("Player", current_player + 2, "has", len(hands[current_player]), "cards")
    print("Player", current_player + 3, "has", len(hands[current_player]), "cards\n")
    for count, option in enumerate([hands[current_player][0], hands[current_player][1], hands[current_player][2], hands[current_player][3], hands[current_player][4]]):
                print(f"{count+1}. {option}")
    while True:
                try:
                    card_option = int(input("Select a card to discard: "))
                    if card_option in [1,2,3,4,5]:
                        global card_chosen
                        card_chosen = hands[current_player][card_option - 1 ]
                        print(f"You have chosen card {card_chosen} to discard!")
                        print(f"Communal pile: {communal_pile + 1}")
                        discarded_cards.append(card_chosen)
                        break
                    else: 
                        print(f"You don't have that card!")
                except ValueError:
                    print("Huh?")        
    call_bullshit()

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
    for suit in [HEART,CLUB,DIAMOND,SPADE]:
        for number in ['A','K','Q','J','2','3','4','5','6','7','8','9','10']:
            deck.append(number+suit)

    random.shuffle(deck)
    return deck

def deal_cards():
    player1 = []
    player2 = []
    player3 = []
    for i in range(5):
        player1.append(get_deck().pop())
        player2.append(get_deck().pop())
        player3.append(get_deck().pop())
    return player1, player2, player3

def call_bullshit():
    if input("Do you want to call bullshit? (y/n) ") == 'y':
        if card_chosen == discarded_cards[0]:
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


