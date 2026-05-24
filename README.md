# ALU Regex Data Extraction

## What this program does

This program reads a raw text file that contains messy, realistic data (like customer support logs, emails, and system alerts) and automatically extracts useful structured information from it using regex patterns.

**Regex (Regular Expressions)** are special patterns that tell the program what to look for inside a block of text — similar to how Ctrl+F finds words in a document, but much more powerful and flexible.

The program extracts the following data types:

- **Email addresses** (including ALU official, alumni, and SI emails)
- **Credit card numbers**
- **Phone numbers**
- **Hashtags**

It then saves all the results into a clean, organized JSON file.

---

## How the program works (step by step)

### Step 1 — Read the input file

The program opens the file at `input/raw-text.txt` and reads all the text inside it into memory.

### Step 2 — Run regex patterns

The program runs four regex patterns against the text:

- **Email pattern** — finds anything that looks like an email address
  - e.g. `sarah.kimani@gmail.com` or `support@techbridge.africa`

- **ALU email validation** — from all emails found, it separates the ones that belong to ALU:
  - `@alueducation.com` (staff)
  - `@alumni.alueducation.com` (graduates)
  - `@si.alueducation.com` (SI students)

- **Credit card pattern** — finds 16-digit card numbers in formats like
  - `4532 1234 5678 9010` or `3782 822463 10005` (Amex)

- **Phone number pattern** — finds phone numbers in various formats
  - e.g. `+250 788 123 456` or `+1 (800) 555-0199`

- **Hashtag pattern** — finds words starting with `#`
  - e.g. `#ALU` `#Urgent` `#CustomerSupport`

### Step 3 — Security check

The program includes basic awareness of malformed and unsafe input. Suspicious or badly formatted values are ignored during extraction.

### Step 4 — Save results

All extracted data is packaged into a dictionary and saved as a formatted JSON file at `output/sample-output.json`

---

## How to run it

### Requirements

- Python 3 must be installed on your computer
- No extra libraries needed (uses only built-in Python modules)

### Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/oteniyatobi/alu-regex-data-extraction_oteniyatobi.git
   ```

2. Navigate into the project folder:
   ```bash
   cd alu-regex-data-extraction_oteniyatobi
   ```

3. Run the program:
   ```bash
   python src/main.py
   ```

4. Check your results:
   ```bash
   output/sample-output.json
   ```

---

## File structure

```
alu-regex-data-extraction-oteniyatobi/
├── input/
│   └── raw-text.txt (the messy raw text the program reads)
├── src/
│   └── main.py (the main program with all regex patterns)
├── output/
│   └── sample-output.json (the extracted results saved here)
└── README.md (this file)
```

---

## ALU Email Validation

Validates three types of ALU emails:

- `@alueducation.com`
- `@alumni.alueducation.com`
- `@si.alueducation.com`
