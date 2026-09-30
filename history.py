"""Local payment-request history; the data folder is supplied with the project."""
import json
from datetime import datetime
from amounts import money

def save_transaction(upi, amount, people, shares, qr_files, HISTORY_FILE):
    with open(HISTORY_FILE, "r", encoding="utf-8") as file:
        transactions = json.load(file)

    if not isinstance(transactions, list):
        raise ValueError("Transaction history must be a JSON list. Existing history was not changed.")

    transaction = {
        "transaction_number": len(transactions) + 1,
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "status": "payment_request_created",
        "total_amount": money(amount),
        "total_amount_paise": amount,
        "people_including_receiver": people,
        "receiver_upi_id": upi,
        "receiver_share": money(shares[0]),
        "payer_shares": [],
        "qr_files": qr_files,
    }

    for i in range(1, people):
        transaction["payer_shares"].append({
            "person_number": i + 1,
            "amount": money(shares[i]),
            "amount_paise": shares[i],
            "qr_file": qr_files[i - 1],
        })

    transactions.append(transaction)
    # Write a temporary file first to protect the previous history.
    temp_file = HISTORY_FILE.with_suffix(".tmp")
    with open(temp_file, "w", encoding="utf-8") as file:
        json.dump(transactions, file, indent=4)
    temp_file.replace(HISTORY_FILE)



def show_history(path):
    with open(path, encoding="utf-8") as file:
        records = json.load(file)
    if not isinstance(records, list):
        raise ValueError("History must be a JSON list.")
    if not records:
        print("No payment requests saved yet.")
    for record in records:
        print("Split", record["transaction_number"], "|", record["created_at"], "| INR", record["total_amount"], "|", record["people_including_receiver"], "people |", record["status"])
