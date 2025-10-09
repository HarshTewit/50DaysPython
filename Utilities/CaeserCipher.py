
while True:
    try:
        status = input("Do you want to encrypt of decrypt (e/d)")
        if not (status == "e" or status == "d"):
            continue
        break
    except ValueError:
        print("Please enter a valid Value.")

def encrypt_msg(msg, key):
    fin = ""
    for c in msg:
        index = ord(c)
        new_index = ord('a') + (((ord(c) - ord('a') + key)) % 26)
        fin += chr(new_index)
    return fin

def decrypt_msg(msg, key):
    fin = ""
    for c in msg:
        index = ord(c)
        new_index = ord('a') + (((ord(c) - ord('a') - key + 26)) % 26)
        fin += chr(new_index)
    return fin

if status == 'e':
    msg = input("Enter the message.")
    key = int(input("Kindly enter the number secret key."))
    print(f"The encryption is {encrypt_msg(msg, key)}")
else:
    msg = input("Enter the message.")
    key = int(input("Kindly enter the number secret key."))
    print(f"The decryption is {decrypt_msg(msg, key)}")

 
