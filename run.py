import gspread
from google.oauth2.service_account import Credentials
import random

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
    # display_5_random_cards()
    display_picture_cards()

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
    print("* The games begins with each player having 5 cards")
    print("* The aim of the game is to be the first to get rid of all your cards")
    print("* Players can put down a single card or multiple matching cards")
    print("* For example, a single Queen or three Queens")
    print("* The bluff happens when the player decides to lie about what cards they have put down")
    print("* Play bullshit and test your bluffing skills!\n")
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
                    print(f"{username_validated}, lets get started!")
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

def get_random_suit():
    """
    generate a random suit selection from a deck
    """
    card_suits = [HEART,CLUB,DIAMOND,SPADE]
    random_suit = random.choice(card_suits)
    return random_suit

def get_random_point():
    """
    generate a random level of card selection from a deck
    """
    card_points =['A','K','Q','J','2','3','4','5','6','7','8','9','10']
    random_point = random.choice(card_points) 
    return random_point
   
# def get_random_card():
#     """
#     generate a random card selection from a deck
#     """
#     random_card = get_random_suit(),get_random_point()
#     return random_card
#     print(random_card)

# random_card = get_random_card()

def display_5_random_cards():
    """
    displays 5 random cards in a list
    """
    print("These are your cards:\n")
    # print(display_picture_cards() for i in range(5))
    print(display_picture_cards())

def display_picture_cards():
    rows = ['', '', '', '', ''] 
    x = get_random_point()
    rows[0] += ' ___ ' 
    rows[1] += '|{}  |'.format(x)
    rows[2] += '| {} |'.format(get_random_suit())
    rows[3] += '|__{}|'.format(x)

    for row in rows: 
         print([row for rows in range(5)])

    
      
def display_hidden_cards():
    print(' ___  ') 
    print('|## | ')
    print('|###| ')
    print('|_##| ')

    
main()

