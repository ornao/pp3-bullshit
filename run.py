import gspread
from google.oauth2.service_account import Credentials
import random
import os
import colorama
from colorama import Fore, Back, Style
import sys
from time import sleep

# initialize colorama
colorama.init(autoreset=True)

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

# Character 9829 is '♥'
HEART = chr(9829)
discarded_cards = []
communal_pile = len(discarded_cards)
current_player = 0

def main():
    title()
    menu_select()
    global hands
    hands = deal_cards()

    card_hands()
    
    while not any(len(hand) == 0 for hand in hands):
        ask_question()
        user_choice()
        computer_call_bullshit()
        card_hands()
        if any(len(hand) == 0 for hand in hands):
            break
        computer2_card_select()
        user_call_bullshit_player2()
        card_hands()
        if any(len(hand) == 0 for hand in hands):
            break
        computer3_card_select()
        user_call_bullshit_player3()
        card_hands()
    
    data = SHEET.col_values(1)
    for row in data:
        username = row[-1]
    if len(hands[current_player]) == 0:
        print(f"Congratulations {username}! You won!")
        # num_rows = SHEET.row_count
        # print(num_rows)
        values = SHEET.get_all_values()
        for i in range(len(values)-1, -1, -1):
            if any(values[i]):
                last_row = i + 1
                break
        new_data = 'won'
        next_col_index = 2
        SHEET.update_cell(last_row, next_col_index, new_data)

    else:
        print(f"Hard luck {username}, you lost this game")
    while True:
        play_again = input("Would you like to play again? (y/n)\n")
        if play_again == 'y':
            print("blahhh")
            main()
        elif play_again == 'n':
            print("bye bye see ya later")
            break
        else:
            print("Surely you know where y and n are on your keyboard.")

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
    print(Fore.BLUE +   "                                                   A bluffing card game")
    print("                                                Developed by Orna Reynolds")

def menu_select():
    """
    User selects whether to start the game or look at the rules first, validation for 1 and 2 selection
    """
    typewriter_animation("Which are you feeling?\n")
    start_options = "1) Play the game\n2) Have a deeper look at the rules first\n" 
    # typewriter animation that works for input
    for char in start_options:
        sleep(.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    typewriter_animation("(psst...click me if this is your first time playing)\n")
    # Validatation for user input
    start_option_selected = input()
    while start_option_selected not in ["1","2"]:
        print("Surely you know where 1 and 2 are on your keyboard.")
        start_option_selected = input()
    # calls function to continue game when correct input called
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
    print("* The game begins with each player receiving 4 cards")
    print("* The aim of the game is to be the first to get rid of all your cards")
    print("* The game begins by asking player 1 (yes that's you) to play the first card")
    print("* The player can play the card they have called or lie and play another card instead")
    print("* The game then continues with the next player discarding one of their cards")
    print("* And so on")
    print("* The bluff happens when the player decides to lie about what cards they have put down")
    print("* Call bullshit if you sense your opponents bluff, but fear getting all the cards in communal pile!\n")
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
                    print(Fore.CYAN + f"{username_validated}? " + Style.RESET_ALL + f"Hello there, let's get started! {os.linesep}")
                    break 
                else:
                    print("Psst...is your name made up of only letters")
                    print('And yes that means no spaces too')
            except ValueError:
                print("Huh?")          
    return username_validated

def validate_username_data(username):
    """ 
    validate username so that can only accept alphabetical letters 
    """
    return username.isalpha()

def get_deck():
    """get shuffled deck everytime"""
    deck = []
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

def card_hands():
    """display cards number of cards in each players hand in ascii text display """
    print("Communal pile:", len(discarded_cards))
    global player_cards
    player_cards = hands[current_player]
    print(Fore.CYAN + "You " + Style.RESET_ALL + "have", len(hands[current_player]), "cards:")
    cards = get_picture_cards(player_cards, len(player_cards))
    for i in range(5):
        for card in cards:
            print(card[i], end='')
        print()
    print(Fore.MAGENTA + "Player 2 " + Style.RESET_ALL + "has", len(hands[current_player + 1]), "cards:")
    cards = get_hidden_cards(len(hands[current_player + 1]))
    for i in range(5):
        for card in cards:
            print(card[i], end='')
        print()
    print(Fore.YELLOW + "Player 3 " + Style.RESET_ALL + "has", len(hands[current_player + 2]), "cards:")
    cards = get_hidden_cards(len(hands[current_player + 2]))
    for i in range(5):
        for card in cards:
            print(card[i], end='')
        print()


def ask_question():
    """ask user what card they would like to tell other players they are discarding"""
    global question
    # add .upper() to allow for users adding correct value in lowercase
    question = input("Type in a random card from A-K to discard:\n").upper()
    # validatation for user input
    while question not in ['A','2','3','4','5','6','7','8','9','10','J','Q','K']:
        print("When I say A-K, I mean [A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K]")
        question = input("Type in a random card from A-K to discard:\n").upper()
    print(Style.BRIGHT + "Remember you don't actually need to have that card in your hand, your opponents just have to " + Fore.BLACK + Back.WHITE + "believe" + Style.RESET_ALL + Style.BRIGHT + " you have it")       
    return question + HEART 


def user_choice():
    "allows user to discard number 1-4 card in their hands"
    for count, option in enumerate(hands[current_player]):
        print(f"{count+1}. {option + HEART}")

    while True:
                try:
                    card_option = int(input(f"Select a card from 1-{len(hands[current_player])} to discard:"))
                    os.linesep
                    if card_option in [1,2,3,4]:
                        global card_chosen
                        card_chosen = hands[current_player][card_option - 1] 
                        print(f"You have chosen card {card_chosen + HEART} to discard!")
                        print(f"Communal pile: {len(discarded_cards)}")
                        hands[current_player].remove(card_chosen)
                        discarded_cards.append(card_chosen)
                        break
                    else: 
                        print(f"You don't have that card!")
                except ValueError:
                    print("Huh? I know you can count my dear")  


def computer_call_bullshit():
    """computer randomly decided if true or false - so calls bullshit. 
    cards in discarded pile are then added to person who called bullshit incorrectly"""
    print(Fore.MAGENTA + "Player 2" + Style.RESET_ALL + " and " + Fore.YELLOW + "player 3 " + Style.RESET_ALL + "are deciding if you are lying or not...")
    z = random.choice([True, False])
    if z is True:
        random_choice_players = [2,3]
        x = random.choice(random_choice_players)
        if x == 2:
            print(Fore.MAGENTA + f"Player {x} " + Style.RESET_ALL + "called bullshit, they think you are lying!")
        else: 
            print(Fore.YELLOW + f"Player {x} " + Style.RESET_ALL + "called bullshit, they think you are lying!")
        if card_chosen == question:
            print("Computer was wrong, you were telling the truth!")
            # add all cards in discarded to add to losers hand (person who called bullshit)
            if x == 2:
                hands[current_player + 1].extend(discarded_cards)
                discarded_cards.clear()
               
            else:
                hands[current_player + 2].extend(discarded_cards)
                discarded_cards.clear()
                
        else:
            if x == 2:
                print(Fore.MAGENTA + f"Player {x} " + Style.RESET_ALL + "guessed you were lying!")
            else: 
                print(Fore.YELLOW + f"Player {x} " + Style.RESET_ALL + "guessed you were lying!") 
            hands[current_player].extend(discarded_cards)
            discarded_cards.clear()
            
    else:
        print(Fore.MAGENTA + "Player 2" + Style.RESET_ALL + " and " + Fore.YELLOW + " player 3 " + Style.RESET_ALL + "think you are telling the truth, no one called bullshit")
        

def computer2_card_select():
    """computer randomly decides 1-4 so what card to choose to dicard"""
    x = len(hands[current_player +1])
    global computer2_card_chosen
    computer2_card_chosen = hands[current_player + 1][x - 1]
    print("Next player's turn")
    hands[current_player + 1].remove(computer2_card_chosen)
    discarded_cards.append(computer2_card_chosen)
    print(f"Communal pile: {len(discarded_cards)}")
    numbers = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    global y
    y = random.choice(numbers)
    print(Fore.MAGENTA + "Player 2 " + Style.RESET_ALL + f"has discarded card {y + HEART}")
    print('Do you think they are lying?')

def computer3_card_select():
    """computer randomly decides 1-4 so what card to choose to dicard"""
    x = len(hands[current_player + 2])
    global computer3_card_chosen
    computer3_card_chosen = hands[current_player + 2][x - 1]
    print("Next player's turn")
    hands[current_player + 2].remove(computer3_card_chosen)
    discarded_cards.append(computer3_card_chosen)
    print(f"Communal pile: {len(discarded_cards)}")
    numbers = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    global y
    y = random.choice(numbers)
    print(Fore.YELLOW + "Player 3 " + Style.RESET_ALL + f"has discarded card {y + HEART}")
    print('Do you think they are lying?')

def user_call_bullshit_player2():
    """player 2 function to randomly call true or false so bullshit"""
    # os.linsep is a workaround to the heroku input \n problem, 
    # using\n was changing my == value
    bullshit_question = input("Do you want to call bullshit? (y/n)\n")
    if bullshit_question == 'y':
        os.linesep
        if y + HEART == computer2_card_chosen:
            print("x")
            print(Fore.MAGENTA + "Player 2 " + Style.RESET_ALL + "was telling the truth!")
            print("y")
            hands[current_player + 1].extend(discarded_cards)
            discarded_cards.clear()
            # print(discarded_cards)
        else:
            print(Fore.MAGENTA + "Player 2 " + Style.RESET_ALL + "was lying!")
            # print(discarded_cards)
            hands[current_player + 1].extend(discarded_cards)
            discarded_cards.clear()
    # validatation for user input
    while bullshit_question not in ["y","n"]:
        print("Surely you know where y and n are on your keyboard.")
        bullshit_question = input("Do you want to call bullshit? (y/n)\n")

def user_call_bullshit_player3():
    """player 3 function to randomly call true or false so bullshit"""
    # os.linsep is a workaround to the heroku input \n problem, 
    # using\n was changing my == value
    bullshit_question = input("Do you want to call bullshit? (y/n)\n")
    if bullshit_question == 'y':
        os.linesep
        if y + HEART == computer3_card_chosen:
            print(Fore.YELLOW + "Player 3 " + Style.RESET_ALL + "was telling the truth!")
            hands[current_player + 2].extend(discarded_cards)
            discarded_cards.clear()
            # print(discarded_cards)
        else:
            print(Fore.YELLOW + "Player 3 " + Style.RESET_ALL + "was lying!")
            # print(discarded_cards)
            hands[current_player + 2].extend(discarded_cards)
            discarded_cards.clear()
    # validatation for user input
    while bullshit_question not in ["y","n"]:
        print("Surely you know where y and n are on your keyboard.")
        bullshit_question = input("Do you want to call bullshit? (y/n)\n")


def get_picture_cards(player_cards, num_cards):
    cards = []
    for i in range(num_cards):
        x = player_cards[i]
        rows = ['', '', '', '', ''] 
        suit = HEART
        # Code from Blackjack, by Al Sweigart al@inventwithpython.com
        rows[0] += ' ___ ' 
        rows[1] += '|{}  |'.format(x)
        rows[2] += '| {} |'.format(suit)
        rows[3] += '|__{}|'.format(x)
        cards.append(rows)
    return cards


def get_hidden_cards(num_cards):
    cards = []
    for i in range(num_cards):
        rows = ['','','','',''] 
        # Code from Blackjack, by Al Sweigart al@inventwithpython.com
        rows[0] += ' ___ ' 
        rows[1] += '|## |'
        rows[2] += '|###|'
        rows[3] += '|_##|'
        cards.append(rows)
    return cards


def typewriter_animation(words):
    for char in words:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

main()


# fix issue with heart longer in value so they wont be equal
# fix issue with 10 and 7 being weird for card display
# add typewriter font 
# add different colors for text 
# add message if game keeps looping to quit 
# remember who wins
# update cell to count wins of user
#  computer3_card_chosen = hands[current_player + 2][x - 1]
# IndexError: list index out of range - fix this error
