
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
        if(emoji):
            final += f"{s} {emoji} "
        else:
            final += f"{s} "
         
    return final

print(emojiAdder(my_dict))