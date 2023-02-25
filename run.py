import gspread
from google.oauth2.service_account import Credentials

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

print("██████╗░██╗░░░██╗██╗░░░░░██╗░░░░░░██████╗██╗░░██╗██╗████████╗░░░░░░░░░███ ")
print("██╔══██╗██║░░░██║██║░░░░░██║░░░░░██╔════╝██║░░██║██║╚══██╔══╝░░░░░░░░░███ ")
print("██████╦╝██║░░░██║██║░░░░░██║░░░░░╚█████╗░███████║██║░░░██║░░░░░░░░░░░░███  ")
print("██╔══██╗██║░░░██║██║░░░░░██║░░░░░░╚═══██╗██╔══██║██║░░░██║░░░░░▄█████▄█▀▀ ")
print("██████╦╝╚██████╔╝███████╗███████╗██████╔╝██║░░██║██║░░░██║░░░░░▀█████  ")
print("╚═════╝░░╚═════╝░╚══════╝╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░░╚═╝░░░░░░▄████▄ ")
print("                                                Developed by Orna Reynolds")

print("This is a game of bluff. ")
print("The games begins with each player having 5 cards")
print("The aim of the game is to be the first to get rid of all your cards")
print("Players can put down a single card or multiple matching cards")
print("For example, a single Queen or three Queens")
print("The bluff happens when the player decides to lie about what cards they have put down")
print("Play bullshit and test your bluffing skills!\n")

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
                    print("You forgot to enter your username silly!\n")
            except ValueError:
                print("Huh?")

def validate_username_data(username):
    return len(username) > 1

get_username()

