import pandas as pd
import sqlite3
import argparse

def main(csv_file, first_name, last_name):
    # Read CSV file
    data = pd.read_csv(csv_file)

    # Initiate SQL database
    connect = sqlite3.connect(":memory:")
    data.to_sql("data", connect, index = False)

    # Create the query
    query = "SELECT User_Name \
            FROM data \
            WHERE First_Name = \"{}\" AND Last_Name = \"{}\"".format(first_name, last_name)

    # Execute the SQL query search
    result = pd.read_sql_query(query, connect)

    # Print the search result
    if result.empty:
        print("No matching records found.")
    else:
        print(result)

if __name__ == "__main__":
    # Create parser and add arguments
    parser = argparse.ArgumentParser(description = "Retrieve userid of student")
    parser.add_argument("csv_file", type = str, help = 'Path to CSV file')
    parser.add_argument("first_name", type = str, help = "First name of student")
    parser.add_argument("last_name", type = str, help = "Last name of student")

    # Retrieve arguments
    args = parser.parse_args()
    csv_file = args.csv_file
    first_name = args.first_name
    last_name = args.last_name

    # Execute query
    main(csv_file, first_name, last_name)