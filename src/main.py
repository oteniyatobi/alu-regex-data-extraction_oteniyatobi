import re
import json 
import os

# OPENS AND READS THE RAW DATA FILE 
with open("input/raw-text.txt", "r") as file:
    text = file.read()

#CHECKS FOR EMAILS
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails = re.findall(email_pattern, text)

#Check For ALU Related emails
alu_official = [e for e in emails if e.endswith('@alueducation.com')]
alu_alumni = [e for e in emails if e.endswith('@alumni.alueducation.com')]
alu_si = [e for e in emails if e.endswith('@si.alueducation.com')]

#Check for credit card details
credit_card_pattern = r'\b\d{4}[\s-]\d{4}[\s-]\d{4}[\s-]\d{4}\b|\b\d{4}[\s-]\d{6}[\s-]\d{5}\b'
credit_cards = re.findall(credit_card_pattern, text)


#check for all phone numbers
phone_pattern = r'\+?[\d\s\-\(\)]{7,20}'
phones = re.findall(phone_pattern, text)

#Checks forall Hash tags in the txt file 

hashtag_pattern = r'#[a-zA-Z0-9_]+'
hashtags = re.findall(hashtag_pattern, text)


unsafe_patterns = [
    r'DROP\s+TABLE',
    r'SELECT\s+\*',
    r'javascript:',
    r'<script',
    r'--',
    r"';"
]


#Calls and use all the functions that were defined above

def is_safe(value):
    for pattern in unsafe_patterns:
        if re.search(pattern, value, re.IGNORECASE):
            return False
    return True


output = {
    "emails": {
        "all": emails,
        "alu_official": alu_official,
        "alu_alumni": alu_alumni,
        "alu_si": alu_si
    },
    "credit_cards": credit_cards,
    "phones": phones,
    "hashtags": hashtags
}

#Dumps all the clean data into a json file 
 
with open("output/sample-output.json", "w") as f:
    json.dump(output, f, indent=4)

print("done! results saved to output/sample-output.json")