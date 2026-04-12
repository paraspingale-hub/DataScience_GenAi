import re
text = "Call us at 987-654-3210 or 123-456-7890"
pattern = r'\d{3}-\d{3}-\d{4}'

numbers = re.findall(pattern, text)
print(numbers)  # ['987-654-3210', '123-456-7890']