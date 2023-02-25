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

def main():
    title()
    game_rules()
    get_username()

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

input("Press Enter to begin...\n")

def get_username():
    """
    get username input from the user 
    """
    while True:
            try:
                username = input("Now...what is your name?\n")
                if validate_username_data(username):
                    print(f"Hello {username}! Let the game begin!")
                    break 
                else:
                    print("Psst...is your name made up of only letters\n")
            except ValueError:
                print("Huh?")

def validate_username_data(username):
    return username.isalpha()

def get_random_card():
    """
    generate a random card selection from a deck
    """
    card_points =['A','K','Q','J','2','3','4','5','6','7','8','9','10']
    card_suits =['Heart','CLUB','DIAMOND','SPADE']
    random_point = random.choice(card_points) 
    random_suit = random.choice(card_suits)
    random_card = random_suit,random_point
    return random_card

def display_5_random_cards():
    print([(get_random_card()) for i in range(5)])

display_5_random_cards()