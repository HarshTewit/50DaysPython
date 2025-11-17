import os
import shutil

EXTENSION_MAP = { 
    "PDFs": [".pdf"],
    "IMAGEs": [".jpeg", ".png", ".jpg"],
    "TEXTs": [".txt"]
}
# extendible


def get_destination_folder(filename):
    extension = os.path.splitext(filename)[1].lower()
    for folder, extensions in EXTENSION_MAP.items():   # FIX 1
        if extension in extensions:
            return folder
    return "Others"


def sort_files(folder_path):
    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)

        if os.path.isfile(full_path):
            dest_folder = get_destination_folder(file)
            dest_path = os.path.join(folder_path, dest_folder)

            os.makedirs(dest_path, exist_ok=True)      # FIX 2

            # move the file 
            shutil.move(full_path, os.path.join(dest_path, file))
            print(f"Moved: {file} -> {dest_folder}/")


if __name__ == "__main__":
    user_path = input("Enter the folder path or leave blank: ").strip()
    folder = user_path or os.getcwd()                  # FIX 3

    if not os.path.isdir(folder):
        print("Invalid Directory")
    else:
        sort_files(folder)
        print("Sorting done.")
