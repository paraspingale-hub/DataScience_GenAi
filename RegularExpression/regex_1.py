
import re

email = "user@example.com"
pattern = r'^[\w.-]+@[\w.-]+\.\w{2,}$'

if re.match(pattern, email):
    print("Valid email")