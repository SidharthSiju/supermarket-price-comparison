def get_row(file_path, column_name, item):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Filter the DataFrame to get the row(s) containing the specific item
    result = df[df[column_name] == item]

    # Check if any rows were found
    if result.empty:
        print("No rows found containing ", item, " in column ", column_name)
        return None
    else:
        first_row = result.iloc[0]
        #print("Row containing ", item, " in column ", column_name, ":\n", first_row)
        return first_row

# Assigning parameter values
file_path = "Aldi.csv"
column_name = 'names'
item = 'Annabel Karmel Chicken & Potato Pie Toddler Meal 200g 12 Month+'

# Calling the function
row = get_row(file_path, column_name, item)

print(row)