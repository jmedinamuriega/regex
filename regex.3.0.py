# 3.
import re

text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"


occupation_pattern = r"Occupation: (\w+)"
occupation=re.findall(occupation_pattern, text)
print(f"The occupation is: {occupation}")


urls = ["https://example.com", "www.example.com", "http://test.com"]

urls_pattern = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
valid_urls=[]

for url in urls:
    if re.match(urls_pattern, url):
        valid_urls.append(url)
        
print(valid_urls)
