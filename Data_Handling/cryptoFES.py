import json 
import os 
from cryptography.fernet import Fernet
from datetime import datetime 

VAULT_FILE = "notes_vault.json"
KEY_FILE = "vault.key"

def load_or_create_key():
    key = ""
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, 'wb') as f:
            f.write(key)
    else:
        with open(KEY_FILE, 'rb') as f:
            key = f.read()

    return Fernet(key)

fernet = load_or_create_key()

def load_vault():
    if not os.path.exists(VAULT_FILE):
        return []
    with open(VAULT_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_vault(data):
    with open(VAULT_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

def add_note():
    title = input("Enter note title").strip()
    content = input("Enter the note content.").strip()

    encrypted_content = fernet.encrypt(content.encode()).decode()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data = load_vault()
    data.append( { 
        "title": title,
        "content": encrypted_content,
        "timestamp": timestamp
    })

    save_vault(data)
    print("Data saved!")

def list_notes():
    data = load_vault()
    if not data:
        print("No notes to share!")
        return
    
    for i, note in enumerate(data, 1):
        print(f"{i}. {note["title"]} {note["timestamp"]}")

def search_notes():
    keyword = input("Enter the keyword to search for.").strip().lower()
   # lower()
    data = load_vault()
    found = [note for note in data if keyword in note['title'].lower()]
    if not found:
        print("NO MATCHING NOTES")
    else:
        for note in found:
            print(f"{note['title']} {note['timestamp']}")


def view_note():
    list_notes()
    try:
        index = int(input("Enter note number to view: ")) - 1
        data = load_vault()

        if 0 <= index < len(data):
            encrypted = data[index]["content"]
            decrypted = fernet.decrypt(encrypted.encode()).decode()
            print(f"\n {data[index]['title']} - {data[index]['timestamp']} \n \n {decrypted}")
        else:
            print("Invalid selection")
    except:
        print("Invalid Input.")

def main():
    while True:
        print("Notes manager!")
        print("1. Add Note")
        print("2. View Note")
        print("3. Search Note")
        print("4. List Notes")
        print("5. Exit")

        choice = input("Enter an option").strip()

        match choice:
            case '1':add_note()
            case '2':view_note()
            case '3':search_notes()
            case '4':list_notes()
            case '5': return 
            case _: print("Invalid Choice")

main()
