"""Main terminal script for the UPI Payment Splitter."""
from pathlib import Path
import re
from amounts import get_amount, money, split_amount
from payments import make_link
from history import show_history
from split_service import generate_split

PROJECT_FOLDER= Path(__file__).resolve().parent
FOLDER =PROJECT_FOLDER / "Split"
HISTORY_FILE= PROJECT_FOLDER / "data" / "transactions.json"


def generate(upi,amount,people):
    generate_split(upi,amount,people,FOLDER,HISTORY_FILE)


def main():
    print("UPI PAYMENT SPLITTER")
    print("The total number of people includes the person who paid.")
    print("Creating new splits replaces older files.")
    while True:
        print("\n1. New payment split\n2. Exit\n3. View history")
        choice = input("Choice: ").strip()
        if choice== "2":
            break
        if choice =="3":
            try:
                show_history(HISTORY_FILE)
            except (OSError, ValueError, KeyError, TypeError) as error:
                print("Unable to load history:", error)
            continue
        if choice!= "1":
            print("Choose 1,2or3.")
            continue
        amount = get_amount()
        while True:
            text =input("Total people including reciever (2-100): ").strip()
            if text.isascii() and text.isdigit() and 2<= int(text)<= 100:
                people = int(text)
                if amount >= people:
                    break
                print("Each individual must receive a minimum share of one paisa.")
            else:
             print("Enter a wholeno.from 2 to 100.")
        while True:
            upi = input("Receiver's UPI ID: ").strip()
            if re.fullmatch(r"[A-Za-z0-9._-]+@[A-Za-z0-9.-]+", upi):
                break
            print("Spaces aren't allowed here.Try a format like name@bank.")
        print("Checks format,not account existence.")
        if input("Generating a new split will overwrite your preveous one.Continue? (y for YES/n for NO): ").strip().lower() != "y":
            print("Action cancelled.No changes are made .")
            continue
        try:
            generate(upi,amount,people)
        except (OSError,ValueError) as error:
            print("Error:",error)
            print("Error:Process did not finish.Fix the issue and rerun before distributing output.")


if __name__ == "__main__":
    main()
