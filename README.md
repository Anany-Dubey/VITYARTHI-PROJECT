# UPI Payment Splitter

## Overview of the Project

Ever been in a situation where one person pays the entire restaurant bill, and then everyone scrambles to figure out how much they owe? Calculating splits, sending multiple payment requests, and ensuring everyone pays the exact amount becomes messy and time-consuming.

**UPI Payment Splitter** is a simple Python tool that solves this problem. It automatically calculates how much each person owes, generates individual QR codes for each person's share, and keeps a history of all your splits. No more manual calculations, no more "I'll pay you later" excuses - everyone gets their own scannable QR code with the exact amount pre-filled in their UPI app.

---

## Problem Statement

When groups of people share expenses, the payment collection process is inefficient and error-prone:
- **Manual calculation errors** - People miscalculate their share, especially when splitting uneven amounts
- **Payment friction** - Each person has to manually enter the amount and receiver details in their UPI app
- **Tracking difficulty** - The person who paid loses track of who still owes money
- **Time waste** - Coordinating multiple small payments takes unnecessary effort

This project automates the entire bill-splitting process and makes payment collection as simple as scanning a QR code.

---

## Scope of the Project

This project provides a **command-line tool** for generating UPI payment requests with the following scope:

**In Scope:**
- Split any bill amount (in INR) among 2-100 people equally
- Generate individual QR codes for each person's share
- Create UPI payment links compatible with all major Indian payment apps (Google Pay, PhonePe, Paytm, BHIM, etc.)
- Maintain local history of all payment splits
- Export summary with payment links and amounts
- Handle decimal amounts accurately (down to paisa level)

**Out of Scope:**
- Actual payment processing or money transfers
- Unequal splits (e.g., one person pays more)
- Payment tracking or confirmation
- Web interface or mobile app
- Multi-currency support
- Integration with banking systems

---

## Target Users

This tool is designed for:

1. **Students** - Splitting food delivery, cab fares, event tickets, or hostel expenses
2. **Friends & Family** - Sharing costs for group dinners, trips, movie tickets, or gifts
3. **Office colleagues** - Splitting lunch bills, team outings, or shared supplies
4. **Small groups** - Anyone who frequently shares expenses and needs a quick way to collect money
5. **Event organizers** - Collecting equal contributions from participants

**User Profile:** Anyone comfortable running a simple Python script. No coding knowledge required - just basic ability to open a terminal and follow instructions.

---

## Features

### Core Features

 **Equal Bill Splitting** - Enter total amount and number of people, get exact shares calculated automatically

 **QR Code Generation** - Creates scannable QR codes for each person with their payment amount pre-filled

 **UPI Link Creation** - Generates standard UPI payment links that work with any UPI app

 **Fair Distribution** - When amounts don't divide evenly, extra paise are distributed fairly across the first few people

 **Payment History** - Tracks all splits with timestamp, amounts, people count, and generated QR files

 **Summary Export** - Creates a text file with all payment details and links for easy sharing

 **Validation** - Checks UPI ID format, ensures minimum payment amounts, and validates input

 **File Management** - Automatically cleans up old QR codes when generating new splits

### User Experience Features

- Interactive command-line menu
- Clear error messages and guidance
- Confirmation before overwriting previous splits
- Detailed summary after each split
- View history of all previous splits
- No manual calculation needed
- Copy-paste ready payment links

---

## Technologies/Tools Used

### Programming Language
- **Python 3.x** - Core language for the entire application

### Libraries
- **segno** - QR code generation (PNG format with error correction)
- **json** - Store and retrieve transaction history
- **datetime** - Timestamp each transaction
- **pathlib** - Cross-platform file path handling
- **urllib.parse** - Create properly formatted UPI payment URLs
- **re** - Validate UPI ID format with regex

### Standards
- **UPI Deep Linking Specification** - Standard `upi://pay` URL scheme recognized by all Indian payment apps
- **JSON** - Data storage format for transaction history

### Development Tools
- Standard Python built-in modules (no complex dependencies)
- File I/O operations for QR and history management
- Modular code architecture (separate files for different concerns)

---

## Steps to Install & Run the Project

### Prerequisites
- **Python 3.11 or higher** installed on your computer
- Internet connection (only for initial setup)
- Terminal/Command Prompt access

### Installation Steps

**Step 1: Download or clone this project**
```bash
# If you have git installed
git clone <repository-url>

# Or download the ZIP file and extract it
```

**Step 2: Navigate to the project folder**
```bash
cd "UPI SPLITER- VITYARTHI PROJECT"
```

**Step 3: Install required library**
```bash
pip install segno
```

That's it! Installation is complete.

### Running the Project

**Step 1: Open terminal in the project folder**

On Windows:
- Right-click in the project folder → "Open in Terminal" or "Open PowerShell window here"

On Mac/Linux:
- Open Terminal and navigate to the project folder using `cd`

**Step 2: Run the main script**
```bash
python upi_spliter.py
```

**Step 3: Follow the on-screen menu**
```
UPI PAYMENT SPLITTER
The total number of people includes the person who paid.
Creating new splits replaces older files.

1. New payment split
2. Exit
3. View history
Choice: 
```

### Creating Your First Split

1. Type `1` and press Enter
2. Enter total bill amount: `500` (or `500.50` for decimals)
3. Enter number of people: `4` (including the person who paid)
4. Enter receiver's UPI ID: `yourname@paytm`
5. Confirm by typing `y`

**Output:** The `Split/` folder now contains:
- `person_2.png` - QR code for person 2
- `person_3.png` - QR code for person 3
- `person_4.png` - QR code for person 4
- `summary.txt` - Text file with all details

Share the appropriate QR code with each person. They scan it, their UPI app opens with amount pre-filled, and they just confirm the payment.

---

## Instructions for Testing

### Test 1: Basic Split (Even Division)

**Input:**
- Total amount: `100`
- People: `4`
- UPI ID: `test@paytm`

**Expected Output:**
- Person 1 (receiver): ₹25.00
- Person 2: ₹25.00 (QR code generated)
- Person 3: ₹25.00 (QR code generated)
- Person 4: ₹25.00 (QR code generated)
- 3 PNG files created in `Split/` folder
- Entry added to `data/transactions.json`

**Verification:**
1. Check that 3 QR images exist: `person_2.png`, `person_3.png`, `person_4.png`
2. Open `Split/summary.txt` and verify amounts
3. Scan a QR code with your UPI app - it should open with ₹25.00 pre-filled

---

### Test 2: Uneven Division (With Remainders)

**Input:**
- Total amount: `100`
- People: `3`
- UPI ID: `test@paytm`

**Expected Output:**
- Person 1 (receiver): ₹33.34 (gets extra paisa)
- Person 2: ₹33.33 (QR code generated)
- Person 3: ₹33.33 (QR code generated)
- Total: ₹100.00 (verify sum is exact)

**Verification:**
1. Open `summary.txt` and add all three amounts
2. Total should be exactly ₹100.00 with no rounding errors

---

### Test 3: Decimal Amounts

**Input:**
- Total amount: `1234.56`
- People: `5`
- UPI ID: `test@ybl`

**Expected Output:**
- 4 QR codes generated (for persons 2-5)
- All shares are in rupees and paise (e.g., ₹246.92)
- Sum of all 5 shares = ₹1234.56 exactly

**Verification:**
1. Check each amount has exactly 2 decimal places
2. Verify total adds up correctly

---

### Test 4: Invalid Inputs

**Test 4a: Invalid UPI ID**
- Input: `testpaytm` (missing @)
- Expected: Error message "Spaces aren't allowed here. Try a format like name@bank."

**Test 4b: Too Few People**
- Input: `1` person
- Expected: Prompt keeps asking for 2-100 people

**Test 4c: Zero Amount**
- Input: `0` rupees
- Expected: Error "The amount must be greater than zero."

**Test 4d: Amount Too Small for People**
- Amount: `2` paise (₹0.02)
- People: `5`
- Expected: Error about minimum one paisa per person

---

### Test 5: History Feature

**Steps:**
1. Create 2-3 different splits
2. Choose option `3` from main menu
3. Verify all previous splits are listed with:
   - Transaction number
   - Date and time
   - Total amount
   - Number of people
   - Status

**Expected Output:**
```
Split 1 | 2024-03-20T15:30:00 | INR 100.00 | 4 people | payment_request_created
Split 2 | 2024-03-20T15:35:00 | INR 1234.56 | 5 people | payment_request_created
```

---

### Test 6: Overwrite Protection

**Steps:**
1. Create a split for 4 people
2. Immediately create another split for 3 people
3. When asked "Continue? (y/n)", type `n`

**Expected Output:**
- "Action cancelled. No changes are made."
- Previous split files remain unchanged

**Now type `y` to confirm:**
- Old files are replaced
- Only 2 QR codes exist now (person_2.png, person_3.png)
- person_4.png from the previous split is deleted

---

### Test 7: QR Code Scanning (Manual)

**Steps:**
1. Generate any split
2. Open one of the QR code images
3. Scan it with any UPI app (Google Pay, PhonePe, Paytm, etc.)

**Expected Result:**
- Payment screen opens automatically
- Payee name shows "Bill receiver"
- Amount is pre-filled correctly
- Currency is INR
- Transaction note says "Bill split - person X"
- You only need to authenticate and confirm

---

### Test 8: Edge Cases

**Maximum People:**
- Amount: `10000`
- People: `100`
- Expected: 99 QR codes generated, each person gets ₹100.00

**Minimum Split:**
- Amount: `0.02` (2 paise)
- People: `2`
- Expected: Each person gets ₹0.01

**Large Amount:**
- Amount: `99999.99`
- People: `2`
- Expected: Handles correctly without overflow

---

## File Structure

```
UPI SPLITER- VITYARTHI PROJECT/
│
├── upi_spliter.py          # Main entry point - run this file
├── amounts.py              # Input validation and splitting logic
├── payments.py             # UPI payment link generation
├── split_service.py        # Core splitting and QR generation
├── history.py              # Transaction history management
├── qr_files.py            # Output folder validation
├── README.md              # This file
│
├── data/
│   └── transactions.json   # History storage (auto-created)
│
└── Split/                  # Generated output (auto-created)
    ├── person_2.png        # QR code for person 2
    ├── person_3.png        # QR code for person 3
    ├── person_N.png        # ... and so on
    └── summary.txt         # Human-readable summary
```

---

## Important Notes

 **Payment Verification** - Always verify the receiver name and amount in your UPI app before confirming payment. This tool creates payment requests, not actual transfers.

 **One Active Split** - Generating a new split overwrites previous QR codes. Don't share old QR codes after creating new ones.

 **No Payment Tracking** - This tool doesn't track who actually paid. Check your UPI transaction history for confirmations.

 **Local Storage Only** - All data is stored on your computer. No cloud sync or online accounts.

 **Fair Distribution** - When the amount doesn't divide evenly, extra paise go to the receiver and first few payers (e.g., ₹100 ÷ 3 = ₹33.34 + ₹33.33 + ₹33.33).

---

## Troubleshooting

**"segno not found"**  
→ Run `pip install segno`

**"Permission denied" when creating files**  
→ Make sure you have write permissions in the project folder

**QR code doesn't scan**  
→ Ensure the image is clear and well-lit. Try zooming in or adjusting screen brightness.

**UPI app doesn't open**  
→ Make sure you have a UPI-enabled app installed (Google Pay, PhonePe, Paytm, BHIM, etc.)

**"History must be a JSON list" error**  
→ Don't edit `data/transactions.json` manually. If corrupted, delete it and let the program create a fresh one.

---

## Future Enhancements (Out of Current Scope)

- Web interface for easier access
- Unequal split support (e.g., one person pays more)
- Payment status tracking
- WhatsApp/email integration for sharing QR codes
- Receipt upload and OCR for automatic amount detection
- Multi-currency support

---

## License

This is an educational project. Use freely and modify as needed.

---

## Support

For issues or questions about running this project, check:
1. All prerequisites are installed (Python 3.11+, segno library)
2. You're running the correct file (`upi_spliter.py`)
3. The `data/` folder exists with `transactions.json`
4. UPI IDs are in correct format (`name@bank`)

This tool makes bill splitting effortless. No more awkward "who owes what" conversations - just scan, pay, done!
