
import string 
import random 
import getpass 

def checker(password):
    issues = []
    #as we figure out what all is wrong with the password, we will append it to this issues array 
    if len(password) < 8:
        issues.append("Too Short (minimum 8 characters)")
    if not any(c.islower() for c in password): #if any character is in lowercase, then any(c.islower() for c in password) will return true 
        issues.append("Missing LowerCase letter.")
    if not any(c.isupper() for c in password):
        issues.append("Missing Upper Case letter.")
    if not any(c.isdigit() for c in password):
        issues.append("Missing a digit")
    if not any(c in string.punctuation for c in password):
        issues.append("Missing special Character")
    return issues 

def generate_strong_password(length=12):
    chars = string.ascii_letters + string.digits + string.digits
    password = "".join(random.choice(chars) for _ in range(length))
    return password 

password = getpass.getpass("Enter your password")
issues = checker(password)
if issues:
    print("There are several issues in this password")
    for issue in issues:
        print(f" -{issue} \n")
    print(f"Suggested passoword f{generate_strong_password()}")
else:
    print("Valid Password!")



