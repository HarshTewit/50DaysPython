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

save = input("Do you want to save this bio to a text file? {y/n)}").lower()

if save == "y":
    filename = f"{name.lower().replace(' ', '_')}_bio.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(bio)
    print("File Saved.")

