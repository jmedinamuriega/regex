# 4. Python Regex Challenge: Enhancing E-Commerce Operations
# Objective:
import re
# This assignment aims to refine your skills in using Python Regular Expressions to address common challenges in e-commerce operations. You will focus on tasks such as product categorization, customer review analysis, and data formatting, crucial for efficient e-commerce management.

# Task 1: Product Description Keyword Tagging

# Problem Statement:
# You have a list of product descriptions. Your task is to tag each product based on keywords in the description. 
# For instance, tag products as 'Electronics', 'Apparel', or 'Home & Kitchen' based on
# relevant keywords found in their descriptions.

# Code Example:

descriptions = [
    "Smartphone with 6-inch screen and 128GB memory",
    "Cotton t-shirt in medium size",
    "Stainless steel kitchen knife set"
]
electronics = []
apparel = []
home_kitchen = []
electronics_pattern = r"Smartphone"
apparel_pattern = r"t-shirt"
home_kitchen_pattern = r"knife"

for description in descriptions:
    if electronics_pattern in description:
        electronics.append(description)
    elif apparel_pattern in description:
        apparel.append(description)
    elif home_kitchen_pattern in description:
        home_kitchen.append(description)

print("Electronics: ", electronics)
print("Apparel: ", apparel)
print("Home & Kitchen: ", home_kitchen)
# Tag each product based on keywords in the description
# Your code here
# Expected Outcome:

# Efficiently tag each product with the appropriate category ('Electronics', 'Apparel', 'Home & Kitchen') using regex to identify relevant keywords.
# Use regex to match specific product-related keywords in each description.
# Task 2: Pricing Format Standardization

# Problem Statement:
# You have a string containing various price formats from an international e-commerce site. 
# Standardize all prices to the format 'USD XX.XX', converting from formats like '$XX.XX', 'XX.XX USD', and 'XX.XX$'.

# Code Example:


price_data = "Items cost $15.99, 20.00 USD, and 7.50$."
price_pattern = r"\d+\.\d+"
prices = re.findall(price_pattern, price_data)
for price in prices:
    print(f"USD{price}")


price_data = "Items cost $15.99, 20.00 USD, and 7.50$."
def USD(USD):
    return 'USD' + USD.group()
    
    
standardized_data = re.sub(r"(\d+\.\d+)",USD, price_data)

print(standardized_data)


# Convert all price formats in the string to a standardized 'USD XX.XX' format.
# Use re.sub() to perform the necessary replacements and format transformations.