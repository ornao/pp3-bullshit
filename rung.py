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
SHEET = GSPREAD_CLIENT.open('bullshit').worksheet('username')

data = SHEET.get_all_values()
for row in data:
    username = row[-1]
if len(hands[current_player]) == 0:
    print(data)
    print(f"Congratulations {username}! You won!")
    num_rows = SHEET.row_count
    print(num_rows)
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