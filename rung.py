import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('bullshit').worksheet('username')

# Get the total number of rows in the worksheet
num_rows = SHEET.row_count
print(num_rows)

# Get all the values in the worksheet
values = SHEET.get_all_values()

# Iterate over the rows from the end to find the last non-empty row
for i in range(len(values)-1, -1, -1):
    if any(values[i]):
        last_row = i + 1
        break

# Insert a new value in the next column of the last row with data
new_data = 1
next_col_index = 2
SHEET.update_cell(last_row, next_col_index, new_data)