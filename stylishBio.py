import textwrap
name = input("Enter your name!").strip()
profession = input("Enter your profession").strip()
passion = input("Enter you passion.").strip()
handle = input("Enter your handle.").strip() 

print("Choose your style.")
print("1: Simple Lines. \n 2.Vertical Flair. \n 3.Emoji Sandwich")

style = input("Choose: 1,2,3")

def generateBio(style):
    if(style == "1"):
        return f"{name} | {profession} \n passionate about {passion} \n {handle}"
    elif style == "2":
        return f"{name} \n {profession} \n passionate about \n {passion} \{handle}"
    else:
        return f"{name} {profession} {passion} {handle}"
    
bio = generateBio(style)
print("*" * 50)
print(textwrap.dedent(bio))
print("*"*50)
