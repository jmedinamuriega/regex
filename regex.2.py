# 2. 
# Task 1: 
import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)

excluded_emails_pattern = r"\b[A-Za-z0-9._%+-]+@exclude\.com\b"
filtered_emails = []

for email in emails:
    if not re.match(excluded_emails_pattern, email):
        filtered_emails.append(email)

print(filtered_emails)

