"""
Read the desired product from the user and compare its prices among 5 of UK's top supermarket franchises
1. Reduce datasets to 50000 samples each (to improve efficiency of the program).
2. Read data and parse it using pandas library.
3. Get the desired user product name and find matching stock from supermarkets.
4. Compare the price (per unit if applicable).
5. Print all the product prices and the cheapest one.
"""

import pandas as pd
from rapidfuzz import fuzz,process

def get_best_match(file_path, column_name, item):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    name_list = df[column_name].tolist()
    best_match, score, index = process.extractOne(item, name_list, scorer=fuzz.ratio)
    print(best_match, score)
    return get_row(file_path, column_name, best_match)

def get_row(file_path, column_name, item):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Filter the DataFrame to get the row(s) containing the specific item
    result = df[df[column_name] == item]
    print(result)

    # Check if any rows were found
    if result.empty:
        print("No rows found containing ", item, " in column ", column_name)
        return None
    else:
        #print("Row containing ", item, " in column ", column_name, ":\n", first_row)
        return result.iloc[0]

# Assigning parameter values
file_path = "Sains.csv"
column_name = 'names'
item = 'chicken thighs 500g'

# Calling the function
row = get_best_match(file_path, column_name, item)

print(row['names'], " : ", row['prices_(£)'])
