from datetime import datetime
journal_entry = input("How was your day today?")
day_rating = int(input("How would you rate your day out of 5?"))

with open("my_journal.txt", "a") as file:
    file.write(f"JOURNAL ENTRY: {datetime.now()}")
    file.write(journal_entry + "\n")
    file.write(f"Today's self rating : {day_rating} \n")
    file.write("\n")

