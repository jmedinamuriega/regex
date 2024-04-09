# 1. Python Regular Expressions Mastery
# Task 1: Code Correction

import re
text ="Contact emails are: john.doe@example.com and jane.doe@example.com."
emails = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
email=re.findall(emails,text)
print(email)

# Task 2: Log File Analysis
# Code Example:

log_data = "12-25-2022: @john Logged in. 01-01-2023: @jane Accessed the dashboard."
data=r"@\w+"
replace="ANONYMIZED USER"
log_username=re.sub(data, replace,log_data)
print(log_username)

