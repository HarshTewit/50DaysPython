import os 
import csv 
import base64

VAULT_FILE = "vault.txt"

def encode(text):
    return base64.b64encode(text.encode()).decode()

def decode(text):
    return base64.b64decode(text.encode()).decode()

def password_strength(password):
    length = len(password)
    has_upper = any (c.isupper() for c in password)
    has_lower = any (c.islower() for c in password)
    has_digit = any (c.isdigit() for c in password)
    has_char = any (c in "!&$#@" for c in password)

    score = sum([length >= 8, has_upper, has_digit, has_char]) #the true false to be converted to 0 and 1 
    return ["Weak", "Medium", "Strong", "Very Strong"][min(score, 3)]

def add_credentials():
    website = input("Website.. ").strip()
    username = input("Username.. ").strip()
    password = input("Password.. ").strip()

    strength = password_strength(password)

    line = f"{website}||{username}||{password}"
    encoded_line = encode(line)

    with open(VAULT_FILE, 'a', encoding='utf-8') as f:
        f.write(f"{encoded_line}\n")
    
    print("Credentials saved!")

def view_credentials():
    if not os.path.exists(VAULT_FILE):
        print("File not found.")
    
    with open(VAULT_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            data = line.strip()
            decoded = decode(data)
            website, username, password = decoded.split("||")
            hidden_password = "*" * len(password) 
            print(f"{website} -||- {username} -||- {password}")

def update_credentials():
    website = input("Which website credentials do you wish to update?").strip()

    updated_lines = []

    with open(VAULT_FILE, "r") as f:
        lines = f.readlines()

    with open(VAULT_FILE, 'r', encoding='utf-8') as f:
        for encoded_line in f:
            line = decode(encoded_line.strip())
            website_old, username_old, password_old = line.split("||")
            if(website_old == website):
                new_username = input("Enter the new username")
                new_password = input("Enter the new password")
                new_line = encode(f"{website}||{new_username}||{new_password}")
                updated_lines.append(new_line + "\n")
               # f.write(new_line + "\n")
            else:
                updated_lines.append(encoded_line + "\n")
              #  f.write(encoded_line + "\n")
    
    with open(VAULT_FILE, 'w', encoding="utf-8") as f:
        f.writelines(updated_lines)
        
    print("Credentials saved!")
        
def main():
    while True:
        print("Credentials manager!")
        print("1. Add Credentials")
        print("2. View Credentials")
        print("3. Update password")
        print("4. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                add_credentials() 
            case "2":
                view_credentials()
            case "3":
                update_credentials()
            case "4":
                return 
            case _:
                print("Please enter a valid choice.")

if __name__ == "__main__":
    main()


