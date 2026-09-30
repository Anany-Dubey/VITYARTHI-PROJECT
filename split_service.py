"""Coordinates a complete split: validation, QR output and history."""
import json
import re
import segno
from amounts import money, split_amount
from payments import make_link
from qr_files import check_folder
from history import save_transaction

def generate_split(upi, amount, people, FOLDER, HISTORY_FILE):
    if people < 2 or people > 100 or amount < people:
        raise ValueError("Use 2-100 people and at least one paisa per person.")
    if not re.fullmatch(r"[A-Za-z0-9._-]+@[A-Za-z0-9.-]+", upi):
        raise ValueError("Invalid UPI ID format.")
    # Read history before changing QR files. Never reset damaged history.
    with open(HISTORY_FILE, encoding="utf-8") as file:
        records = json.load(file)
    if not isinstance(records, list):
        raise ValueError("History must be a JSON list.")
    check_folder(FOLDER)
    shares = split_amount(amount, people)
    qr_files = []
    lines = [
        "UPI PAYMENT SPLIT", "Total bill: INR " + money(amount),
        "People (including receiver): " + str(people), "Receiver UPI ID: " + upi,
        "Receiver's own share (no QR): INR " + money(shares[0]),
        "Verify the actual recipient name and amount in your UPI app before paying.",
        "These are payment requests, not proof of payment.", "",
    ]
    for i in range(1, people):
        number = i + 1
        link = make_link(upi, shares[i], number)
        qr = segno.make_qr(link, error="m")
        qr_name = "person_" + str(number) + ".png"
        qr.save(str(FOLDER / qr_name), scale=8, border=4)
        qr_files.append("Split/" + qr_name)
        lines.append("Person " + str(number) + ": INR " + money(shares[i]))
        lines.append(link)
    # Remove obsolete QR files from an earlier, larger split only.
    for file in FOLDER.iterdir():
        match = re.fullmatch(r"person_([0-9]+)\.png", file.name)
        if match and (int(match.group(1)) < 2 or int(match.group(1)) > people):
            file.unlink()
    (FOLDER / "summary.txt").write_text("\n".join(lines), encoding="utf-8")
    save_transaction(upi, amount, people, shares, qr_files, HISTORY_FILE)
    print("\nReceiver's share: INR", money(shares[0]))
    for i in range(1, people):
        print("Person", i + 1, "pays INR", money(shares[i]))
    print("Created", people - 1, "QR images in", FOLDER)
    print("Previous generated QR images have been replaced. Do not use previously shared copies.")
    print("Verify the recipient and amount in the payment app. Payment status is not tracked.")


