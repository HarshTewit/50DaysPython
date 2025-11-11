
sentence = input("Enter your sentence.")
my_dict = sentence.split(' ')

emoji_map = {
    "love": "❤️",
    "happy": "😊",
    "code": "💻",
    "tea": "🍵",
    "music": "🎵",
    "food": "🍕",
}

def emojiAdder(my_dict):
    final = ""
    for s in my_dict:
        cleaned = s.lower().strip(".,/!?")
        emoji = emoji_map.get(cleaned, "") 
        """
        We can also do emoji_map[cleaned] but if cleaned does not exist in the dictionary 
        it will throw an error. 
        So we use dictionary_name.get()
        """
        if(emoji):
            final += f"{s} {emoji} "
        else:
            final += f"{s} "
         
    return final

print(emojiAdder(my_dict))