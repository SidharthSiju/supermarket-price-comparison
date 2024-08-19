import pandas as pd


def read_and_write_first_50000_rows(input_csv_file, output_csv_file):
    # Read the first 100 rows of the CSV file into a DataFrame
    df = pd.read_csv(input_csv_file, nrows=50000)

    # Save the first 100 rows to a new CSV file
    df.to_csv(output_csv_file, index=False)

    print(f"First 50000 rows read from '{input_csv_file}' and written to '{output_csv_file}'")


# Example usage
input_csv_file_path = 'All_Data_Morrisons.csv'  # Replace with the path to your input CSV file
output_csv_file_path = 'Morrisons.csv'  # Replace with the desired output file path

# Call the function to read and write the first 100 rows
read_and_write_first_50000_rows(input_csv_file_path, output_csv_file_path)