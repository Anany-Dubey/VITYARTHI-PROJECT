# Project Statement - UPI Payment Splitter

## Problem Statement

### The Problem We're Solving

When friends go out together, one person usually pays the entire bill - whether it's a restaurant, movie tickets, or a cab ride. Then comes the annoying part: figuring out how much each person owes and actually collecting that money.

**Current problems people face:**

1. **Math is tedious** - Someone has to pull out their phone calculator and divide the bill. If it's ₹1,237, what's each person's share? People make mistakes.

2. **Entering payment details is repetitive** - Each person opens their payment app, types in the UPI ID, enters the amount, adds a note. If there are 5 people, that's 5 times someone has to carefully type everything without errors.

3. **People forget or delay** - "I'll pay you tomorrow" becomes next week. The person who paid is stuck chasing people for money.

4. **Confusion about amounts** - "Wait, was it ₹246 or ₹264?" People remember different numbers and arguments start.

5. **Uneven splits cause confusion** - ₹100 divided by 3 doesn't work out evenly. Who pays ₹33.33 and who pays ₹33.34? Most people just guess and the total doesn't match.

**Why existing solutions don't work:**

- **Manual calculation apps** - You still have to copy-paste the UPI ID and amount into your payment app
- **Payment apps with split features** - Everyone needs the same app, and many people use different apps (PhonePe, Google Pay, Paytm)
- **Sending payment links manually** - Tedious to create individual links for each person
- **Just asking people to pay** - Relies on memory and goodwill, easy to forget

### What this means in real life

Imagine you're a college student. You and 7 friends order food worth ₹1,842.50. One person pays using their card. Now what?

- Someone calculates: "That's ₹230.31 each... wait, let me recalculate..."
- Seven people need to open their payment apps
- Each person asks "What's your UPI ID again?"
- Someone sends ₹230, someone sends ₹231, totals don't match
- Two weeks later, you're still waiting for one friend who "forgot"

**This project eliminates all of that.** The person who paid runs this tool once, generates QR codes, sends one to each friend, and everyone just scans and pays. No typing, no confusion, no delays.

---

## Scope of the Project

### What This Project Does

This is a **command-line Python tool** that helps one person collect money from a group after paying a shared bill.

####  Features Included (In Scope)

**Core Functionality:**
- Calculate equal splits for any amount in Indian Rupees
- Works with 2 to 100 people (including the person who paid)
- Handle both whole numbers (₹500) and decimals (₹1,234.56)
- Distribute extra paise fairly when amounts don't divide evenly

**QR Code Generation:**
- Create individual QR codes for each person who needs to pay
- QR codes work with ALL UPI apps (Google Pay, PhonePe, Paytm, BHIM, Amazon Pay, etc.)
- Payment amount is pre-filled automatically
- Includes a note explaining which person it's for

**Payment Links:**
- Generate `upi://pay` links that open payment apps directly
- Links can be shared via WhatsApp, SMS, email, etc.
- No manual typing of UPI ID or amount required

**Organization & History:**
- Save a text summary with all payment details
- Keep a history of all previous splits
- Track when each split was created
- Record who was supposed to pay what (not actual payment confirmation)

**Safety Features:**
- Validate UPI ID format before generating anything
- Warn before overwriting old QR codes
- Ensure each person gets at least ₹0.01 (one paisa)
- Clean up outdated QR codes automatically

####  What This Does NOT Do (Out of Scope)

**Payment Processing:**
- Does NOT actually transfer money or process payments
- Does NOT track who has paid and who hasn't
- Does NOT send payment confirmations
- Does NOT integrate with bank accounts

**Advanced Splitting:**
- Does NOT support unequal splits (e.g., "Person A pays more because they ordered extra")
- Does NOT split by items (e.g., "This person pays for pizza, that person pays for drinks")
- Does NOT calculate tips or taxes separately
- Does NOT support percentage-based splits

**User Interface:**
- Does NOT have a mobile app
- Does NOT have a website or web interface
- Does NOT have a graphical desktop application
- Only works through terminal/command prompt

**Other Limitations:**
- Only supports Indian Rupees (INR), no other currencies
- Only works for UPI payments (India-specific)
- QR codes must be shared manually (no automatic WhatsApp sending)
- No cloud storage or syncing between devices
- No user accounts or online database

### Why These Limits?

This is designed as a **simple, focused tool** that does one thing well: make it easy to collect equal shares from a group. Adding features like unequal splits, payment tracking, or a web interface would make it much more complex to use and maintain.

For most common situations (splitting a bill equally among friends), this tool gives you everything you need in under 30 seconds.

---

## Target Users

### Who Should Use This Tool?

This project is designed for **anyone who frequently splits bills with groups** and wants a faster way to collect money. You don't need to be a programmer or tech expert - just someone comfortable opening a terminal and following simple instructions.

#### Primary User Groups

**1. College Students**

Students constantly share expenses:
- Food delivery from Swiggy/Zomato with roommates
- Cab/auto rides to campus or events
- Movie tickets, concert passes
- Group study supplies or photocopies
- Hostel/PG room shared expenses

**Why this helps:** Students use different payment apps (some use PhonePe, others use Google Pay) and often have limited budgets, so every rupee matters. QR codes make it easy to collect exact amounts quickly.

**Example:** Four students order food worth ₹840. Person A pays. They run this tool, send three QR codes to their friends, and everyone pays their ₹210 share in under a minute.

---

**2. Friend Groups**

Friends who hang out regularly:
- Restaurant dinners and lunches
- Weekend trips and outings
- Birthday party expenses
- Shared gifts for someone
- Activity costs (bowling, gaming zones, etc.)

**Why this helps:** Keeps friendships drama-free. No awkwardness about money, no "I'll pay you later" that turns into never. Everyone pays immediately and accurately.

**Example:** Six friends go bowling. Total: ₹1,200. One friend pays at the counter, generates QR codes right there, everyone scans and pays their ₹200 before leaving.

---

**3. Office Colleagues**

Coworkers who share expenses:
- Team lunch orders
- Coffee runs
- Farewell or birthday gift contributions
- Shared cab to office events
- Office supplies purchased by one person

**Why this helps:** Professional and quick. No need to discuss money extensively at work. One person buys, generates QR codes, sends in the office group chat, done.

**Example:** Five colleagues order lunch worth ₹1,750. Senior team member pays. They create QR codes, drop them in Slack, everyone pays their ₹350 during lunch break.

---

**4. Small Event Organizers**

People organizing small gatherings:
- Potluck dinner supply costs
- Group travel bookings
- Sports equipment for friendly matches
- Picnic or camping supplies
- Workshop materials

**Why this helps:** Makes collecting contributions transparent and easy. Everyone sees exactly how much they're contributing and pays the same amount.

**Example:** Organizing a cricket match for 15 people. Equipment costs ₹3,000. Organizer pays, generates 14 QR codes, shares in the WhatsApp group. Everyone contributes their ₹200 share.

---

**5. Families & Relatives**

Extended family expense sharing:
- Joint celebration costs
- Shared grocery shopping
- Family vacation expenses
- Elder care or medical costs split among siblings
- Utility bills in joint families

**Why this helps:** Keeps family relationships smooth. Money matters handled cleanly without repeated discussions.

**Example:** Three siblings split their parents' medical bill of ₹15,000. One pays at the hospital, generates QR codes, other two pay their ₹5,000 shares immediately.

---

#### User Requirements (What You Need to Know)

**Technical Skills Required:** 
-  Basic - Know how to open a terminal/command prompt
-  Basic - Can navigate to a folder using `cd` command
-  Basic - Can run a Python script
-  No coding knowledge needed
-  No understanding of how the code works required

**What You Need:**
- A computer with Python installed (Windows, Mac, or Linux)
- Any UPI-enabled payment app on your phone to receive payments
- Ability to share images (QR codes) via WhatsApp, email, or any messaging app

**Who This Is NOT For:**
- Businesses needing payment processing systems
- People who need to track payment confirmations
- Users who need unequal or complex splits
- Anyone who can't run a simple Python script

---

## High-Level Features

### What Can You Do With This Tool?

Here are the main things this project lets you accomplish:

---

### 1. **Automatic Bill Splitting**

**What it does:**
- You enter the total bill amount
- You enter how many people are splitting it
- The tool calculates each person's exact share

**Why it's useful:**
- No manual math or calculator needed
- Handles decimals accurately (no rounding errors)
- If the amount doesn't divide evenly, extra paise are distributed fairly
- Works for any amount from ₹0.01 to ₹99,999.99

**Example:**
- Bill: ₹1,237
- People: 4
- Result: Person 1 (you) = ₹309.25, Persons 2-4 = ₹309.25 each
- Total: Exactly ₹1,237 (not ₹1,237.01 or ₹1,236.99)

---

### 2. **QR Code Generation**

**What it does:**
- Creates a separate QR code image for each person who needs to pay
- QR codes are standard UPI payment QR codes
- Saved as PNG image files you can share anywhere

**Why it's useful:**
- People just scan with their phone camera
- Their payment app opens automatically
- Amount and receiver details are already filled in
- Works with ANY UPI app (PhonePe, Google Pay, Paytm, etc.)
- No typing errors possible

**Example:**
- Split among 5 people
- Tool creates 4 QR code files: `person_2.png`, `person_3.png`, `person_4.png`, `person_5.png`
- Send person_2.png to Friend #2, person_3.png to Friend #3, and so on
- Each friend scans their QR, sees their exact amount, confirms, done

---

### 3. **Payment Link Creation**

**What it does:**
- Generates standard UPI payment links (`upi://pay?...`)
- Links can be copied and shared via text, WhatsApp, email
- Clicking the link opens the user's default payment app

**Why it's useful:**
- Alternative to QR codes if someone can't scan
- Easy to share in group chats
- Works on all devices (phones, tablets)
- Can be saved for future reference

**Example:**
- Generated link: `upi://pay?pa=john@paytm&pn=Bill+receiver&am=250.00&cu=INR&tn=Bill+split+-+person+2`
- Send in WhatsApp group
- Person clicks link → Google Pay opens → Amount ₹250 already filled → Pay

---

### 4. **Payment Summary Export**

**What it does:**
- Creates a text file (`summary.txt`) with all details
- Includes total amount, everyone's shares, all payment links
- Human-readable format

**Why it's useful:**
- You have a written record of the split
- Can reference it later if someone asks "How much was I supposed to pay?"
- Can copy-paste payment links from the file
- Proof of what amount was requested (not proof of payment)

**Example Summary File:**
```
UPI PAYMENT SPLIT
Total bill: INR 1000.00
People (including receiver): 4
Receiver UPI ID: john@paytm
Receiver's own share (no QR): INR 250.00

Person 2: INR 250.00
upi://pay?pa=john@paytm&am=250.00...

Person 3: INR 250.00
upi://pay?pa=john@paytm&am=250.00...

Person 4: INR 250.00
upi://pay?pa=john@paytm&am=250.00...
```

---

### 5. **Transaction History**

**What it does:**
- Keeps a record of every split you create
- Stores date, time, amount, number of people, and file locations
- Accessible anytime through the menu

**Why it's useful:**
- Look back at previous splits ("When did we split that restaurant bill?")
- Track how much you've collected over time
- Remember who you created payment requests for
- Helps settle disputes ("Yes, I did create that split on March 15th")

**Example History View:**
```
Split 1 | 2024-03-15T14:30:00 | INR 500.00 | 4 people | payment_request_created
Split 2 | 2024-03-16T19:15:00 | INR 1234.50 | 3 people | payment_request_created
Split 3 | 2024-03-18T12:00:00 | INR 840.00 | 8 people | payment_request_created
```

---

### 6. **Input Validation & Safety**

**What it does:**
- Checks that your UPI ID is in the correct format
- Ensures the number of people is reasonable (2-100)
- Validates that amounts are positive and properly formatted
- Warns you before overwriting previous splits
- Protects your history file from accidental corruption

**Why it's useful:**
- Prevents creating invalid QR codes that won't work
- Catches typos before generating files
- Avoids accidentally losing previous splits
- Gives clear error messages if something is wrong

**Example Validations:**
-  `john.paytm` → Error: "Try a format like name@bank"
-  `0` amount → Error: "The amount must be greater than zero"
-  `1` person → Error: "Need at least 2 people"
-  `john@paytm` → Accepted

---

### 7. **Smart File Management**

**What it does:**
- Creates a `Split/` folder for all generated files
- Automatically deletes outdated QR codes from previous splits
- Keeps your workspace clean and organized
- Prevents confusion about which files are current

**Why it's useful:**
- You always know which QR codes are the latest ones
- No risk of sharing an old, invalid QR code by mistake
- Folder is ready to share or upload as-is
- Clean slate for each new split

**Example:**
- First split: 5 people → Creates person_2 through person_6 QR codes
- Second split: 3 people → Deletes person_4, 5, 6; keeps person_2 and 3 updated
- You always have exactly the right number of QR codes, no extras

---

### 8. **Universal UPI Compatibility**

**What it does:**
- Uses standard UPI deep linking format
- Works with every major Indian payment app
- No app-specific dependencies

**Why it's useful:**
- Your friends can use whichever UPI app they prefer
- You don't need to know what app they use
- Same QR code works for everyone regardless of their app
- Future-proof as new UPI apps emerge

**Compatible with:**
- Google Pay (GPay)
- PhonePe
- Paytm
- BHIM
- Amazon Pay
- WhatsApp Pay
- Bank UPI apps (like BHIM SBI, BHIM Axis, etc.)
- Any other UPI-enabled app

---

### Feature Summary Table

| Feature | Benefit | Time Saved |
|---------|---------|------------|
| Automatic calculation | No math errors | 2-3 minutes |
| QR generation | No manual typing | 5-10 minutes for 5 people |
| Payment links | Alternative to QR | Instant sharing |
| Summary export | Written record | Always available |
| History tracking | Reference past splits | Find old splits in seconds |
| Validation | Catch errors early | Prevents redo work |
| File cleanup | Stay organized | No confusion |
| Universal compatibility | Works for everyone | No "which app?" discussions |

**Total time to split a bill with 5 people:**
- **Old way:** 10-15 minutes (calculate, type UPI IDs, send amounts, repeat 5 times)
- **With this tool:** 30 seconds (run tool, share QR codes)

---

## Why These Features Matter

All these features work together to solve one core problem: **making it effortless to collect money from a group**.

- **Speed:** What used to take 10 minutes now takes 30 seconds
- **Accuracy:** No calculation or typing errors
- **Convenience:** QR codes eliminate all manual data entry
- **Clarity:** Everyone knows exactly what they owe
- **Records:** You have proof of what was requested
- **Simplicity:** Even non-technical people can use it

This isn't just about splitting bills - it's about removing friction from shared expenses so you can focus on enjoying time with friends and family instead of worrying about money collection.
