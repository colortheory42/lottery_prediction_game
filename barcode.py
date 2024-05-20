import os
import pandas as pd

# Initialize an empty dataset with the correct structure
columns = [
    'Barcode',
    'WinningNumber1', 'WinningNumberText1',
    'WinningNumber2', 'WinningNumberText2',
    'WinningNumber3', 'WinningNumberText3',
    'WinningNumber4', 'WinningNumberText4',
    'YourNumber1', 'YourNumberText1', 'Prize1', 'PrizeText1',
    'YourNumber2', 'YourNumberText2', 'Prize2', 'PrizeText2',
    'YourNumber3', 'YourNumberText3', 'Prize3', 'PrizeText3',
    'YourNumber4', 'YourNumberText4', 'Prize4', 'PrizeText4',
    'YourNumber5', 'YourNumberText5', 'Prize5', 'PrizeText5',
    'YourNumber6', 'YourNumberText6', 'Prize6', 'PrizeText6',
    'YourNumber7', 'YourNumberText7', 'Prize7', 'PrizeText7',
    'YourNumber8', 'YourNumberText8', 'Prize8', 'PrizeText8',
    'YourNumber9', 'YourNumberText9', 'Prize9', 'PrizeText9',
    'YourNumber10', 'YourNumberText10', 'Prize10', 'PrizeText10',
    'YourNumber11', 'YourNumberText11', 'Prize11', 'PrizeText11',
    'YourNumber12', 'YourNumberText12', 'Prize12', 'PrizeText12',
    'YourNumber13', 'YourNumberText13', 'Prize13', 'PrizeText13',
    'YourNumber14', 'YourNumberText14', 'Prize14', 'PrizeText14',
    'YourNumber15', 'YourNumberText15', 'Prize15', 'PrizeText15'
]
dataset = pd.DataFrame(columns=columns)


def load_and_display_csvs(directory):
    # Load the CSV files for winning numbers
    winning_numbers_sheets = {
        f'Winning{i + 1}': pd.read_csv(os.path.join(directory, f'Winning{i + 1}.csv'), header=None)
        for i in range(4)
    }

    # Load the CSV files for your numbers
    your_numbers_sheets = {
        f'Your{i + 1}': pd.read_csv(os.path.join(directory, f'Your{i + 1}.csv'), header=None)
        for i in range(15)
    }

    # Display the contents of winning numbers
    print("Winning Numbers:")
    for sheet_name, sheet_data in winning_numbers_sheets.items():
        print(f"\nSheet: {sheet_name}")
        print(sheet_data)

    # Display the contents of your numbers and prizes
    print("\nYour Numbers:")
    for sheet_name, sheet_data in your_numbers_sheets.items():
        print(f"\nSheet: {sheet_name}")
        print(sheet_data)

    return winning_numbers_sheets, your_numbers_sheets


def add_new_ticket_data_from_csv(barcode, winning_numbers_sheets, your_numbers_sheets):
    new_data = {'Barcode': barcode}
    print("Processing winning numbers sheets...")  # Debug statement

    # Load and add winning numbers
    for i, (sheet_name, sheet_data) in enumerate(winning_numbers_sheets.items()):
        number = str(sheet_data.iloc[0, 0]).strip()
        text = str(sheet_data.iloc[1, 0]).strip()
        new_data[f'WinningNumber{i + 1}'] = number
        new_data[f'WinningNumberText{i + 1}'] = text
        print(f"Loaded winning number {i + 1}: {number}, {text}")  # Debug statement

    print("Processing your numbers sheets...")  # Debug statement

    # Load and add your numbers
    for i, (sheet_name, sheet_data) in enumerate(your_numbers_sheets.items()):
        number = str(sheet_data.iloc[0, 0]).strip()
        number_text = str(sheet_data.iloc[1, 0]).strip()
        prize = str(sheet_data.iloc[2, 0]).strip()
        prize_text = str(sheet_data.iloc[3, 0]).strip()
        new_data[f'YourNumber{i + 1}'] = number
        new_data[f'YourNumberText{i + 1}'] = number_text
        new_data[f'Prize{i + 1}'] = prize
        new_data[f'PrizeText{i + 1}'] = prize_text
        print(f"Loaded your number {i + 1}: {number}, {number_text}, {prize}, {prize_text}")  # Debug statement

    return new_data


# Main loop
while True:
    action = input("Do you want to add new ticket data from CSV or exit? (add/exit): ").strip().lower()

    if action == 'add':
        barcode = input("Enter the barcode: ")
        directory = '.'  # Use the current directory where the CSV files are located
        winning_numbers_sheets, your_numbers_sheets = load_and_display_csvs(directory)
        new_data = add_new_ticket_data_from_csv(barcode, winning_numbers_sheets, your_numbers_sheets)
        dataset = pd.concat([dataset, pd.DataFrame([new_data])], ignore_index=True)
        print("New ticket data added. Here is the data you entered:")
        print(new_data)
    elif action == 'exit':
        break
    else:
        print("Invalid input. Please enter 'add' or 'exit'.")

print("Final dataset:")
print(dataset)
