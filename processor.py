import pandas as pd 
from cs50 import SQL

db = SQL("sqlite:///finance.db")

def process_bank_data(filename):
    df = pd.read_csv(filename)
    
    for index, row in df.iterrows():
        db.execute("INSERT INTO transactions (date, description, amount, category, source) VALUES (?, ?, ?, ?, ?)",
        row["Date"],
        row["Description"],
        row["Amount"],
        row["Category"],
        row["Source"])

    return len(df)

if __name__ == "__main__":
    file_to_open = input("Enter the name of your CSV file: ")
    process_bank_data(file_to_open)