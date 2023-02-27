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
    # print("Your cards:")
    # for _ in range(5):
    #     display_picture_cards()
    # print("Opponent1 cards:")
    # for _ in range(5):
    #     display_hidden_cards()
    # print("Opponent2 cards:")
    # for _ in range(5):
    #     display_hidden_cards()
    deal_cards()

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

def get_deck():
    """get shuffled deck everytime"""
    deck = []
    for suit in [HEART,CLUB,DIAMOND,SPADE]:
        for point in ['A','K','Q','J','2','3','4','5','6','7','8','9','10']:
            deck.append(suit+point)

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

    print(player1)
    print(player2)
    print(player3)

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


