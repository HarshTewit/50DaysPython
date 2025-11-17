import os 
import shutil

CURR_DIRECTORY = "/Users/harshit/Desktop/50Python/50proj/Automation Projects/to_be_organized"

def organise_photos(dir):
    new_names = {}
    user_pref = input("What is the base name").strip().upper()
    user_extension = input("Prefferred extnsion?").strip().lower()

    files = [
        f for f in os.listdir(dir)
        if os.path.isfile(os.path.join(dir, f)) 
        and f.lower().endswith("." + user_extension)
    ] #this filtering is crucial or else it will rename even txt files to jpg

    if not files:
        print(f"No files found with .{user_extension} extension.")
        return

    files.sort()

    for index, file in enumerate(files):
        new_names[file] = f"{user_pref}_{index}.{user_extension}"
    
    #print the preview 
    print("-" * 30)
    print("\n")
    print("Here are the changed names")
    for key, value in new_names.items():
        print(f"{key} -> {value}")
    choice = input("Do you want to continue? Y/N").strip().lower()
    if choice == "y":
        rename(dir, new_names)
    else:
        return 

    
def rename(dir, new_names):
    for file in os.listdir(dir):
        os.rename(os.path.join(dir, file), os.path.join(dir, new_names[file]))




if __name__ == "__main__":
    

    organise_photos(CURR_DIRECTORY)