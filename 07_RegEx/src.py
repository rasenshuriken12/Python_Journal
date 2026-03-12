# 🚧 Regular Expressions

import re

# Basic pattern matching
text = "The quick brown fox jumps over 42 lazy dogs."
print(f"Original: {text}")

# Search for a pattern
match = re.search(r"fox", text)
if match:
    print(f"Found 'fox' at position {match.start()}-{match.end()}")

# Match at beginning
if re.match(r"The", text):
    print("Text starts with 'The'")

# Find all occurrences
words = re.findall(r"\b\w+\b", text)
print(f"Words: {words}")

# Find all digits
digits = re.findall(r"\d+", text)
print(f"Digits: {digits}")

# Find all email addresses
email_text = "Contact us at info@example.com or support@company.co.uk"
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", email_text)
print(f"Emails: {emails}")

# Find all URLs
url_text = "Visit https://python.org or http://example.com/page?q=test"
urls = re.findall(r"https?://[^\s]+", url_text)
print(f"URLs: {urls}")

# Substitution (replace)
censored = re.sub(r"fox", "***", text)
print(f"Censored: {censored}")

# Replace with function
def replace_with_upper(match):
    return match.group(0).upper()

uppercased = re.sub(r"\b\w{3}\b", replace_with_upper, text)
print(f"3-letter words uppercased: {uppercased}")

# Splitting
split_text = re.split(r"\s+", text)
print(f"Split by whitespace: {split_text}")

# Compiling patterns for reuse
pattern = re.compile(r"\b\w{5}\b")  # 5-letter words
five_letter_words = pattern.findall(text)
print(f"5-letter words: {five_letter_words}")

# Groups and capturing
date_text = "Today is 2025-03-12 and tomorrow is 2025-03-13"
date_pattern = re.compile(r"(\d{4})-(\d{2})-(\d{2})")

for match in date_pattern.finditer(date_text):
    year, month, day = match.groups()
    print(f"Date: {year}/{month}/{day}")

# Named groups
named_pattern = re.compile(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})")
match = named_pattern.search("2025-12-25")
if match:
    print(f"Year: {match.group('year')}, Month: {match.group('month')}, Day: {match.group('day')}")

# Lookahead and lookbehind
text_with_context = "price: $100, cost: $50, value: $75"

# Positive lookahead (find numbers followed by ',')
prices_with_comma = re.findall(r"\$\d+(?=,)", text_with_context)
print(f"Prices with comma: {prices_with_comma}")

# Positive lookbehind (find numbers preceded by 'price: ')
price_value = re.findall(r"(?<=price: )\$\d+", text_with_context)
print(f"Price value: {price_value}")

# Validation examples
def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

def validate_phone(phone):
    pattern = r"^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$"
    match = re.match(pattern, phone)
    if match:
        return f"({match.group(1)}) {match.group(2)}-{match.group(3)}"
    return None

print(f"\nEmail 'test@example.com' valid: {validate_email('test@example.com')}")
print(f"Phone '(123)456-7890' formatted: {validate_phone('(123)456-7890')}")

# Common patterns
patterns = {
    "IP Address": r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b",
    "MAC Address": r"\b([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})\b",
    "Date (YYYY-MM-DD)": r"\b\d{4}-\d{2}-\d{2}\b",
    "Time (HH:MM:SS)": r"\b([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]\b",
    "HTML Tags": r"<[^>]+>",
}

sample_text = "Server IP: 192.168.1.1, MAC: 00:1A:2B:3C:4D:5E, Date: 2025-03-12"
for name, pattern in patterns.items():
    matches = re.findall(pattern, sample_text)
    if matches:
        print(f"{name}: {matches}")
