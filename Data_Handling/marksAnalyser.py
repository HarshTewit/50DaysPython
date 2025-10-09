import os 
import csv 
import sys

FILE_NAME = "marks_record.csv"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, 'w', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Marks"])

def collect_student_data():
    students = {}

    while True:
        name = input("Enter the student name: ").strip()
        if name.lower().strip() == "done":
            break
        if name in students:
            print("Student already exists.")
            continue

        try:
            marks = float(input(f"Enter marks for {name}"))
            students[name] = marks
        except ValueError:
            print("Please enter a valid number for marks.")

    return students

def display_report(students):
    #we know students is a dictionary  
    if not students:
        print("No student data.")
        return 
    
    marks = list(students.values())
    max_score = max(marks)
    min_score = min(marks)
    average = sum(marks)/len(marks)

    topper = [name for name, score in students.items() if score == max_score] #comprehension
    least_scorer = [name for name, score in students.items() if score == min_score]

    print("**REPORT**")
    print(f"Total number of students {len(students)}")
    print(f"Average marks of students {average}")
    print(f"Highest marks of students {max_score} by {topper}")
    print(f"Lowest marks of students {min_score} by {least_scorer}")
    print(f"---Detailed Marks---")
    for name, score in students.items():
        print(f"Name: {name} - Score: {score}")
    
students = collect_student_data()
display_report(students)

    



def input_marks():
    name = input("Enter Name of the Student")
    marks = int(input("How many Marks did they score?").strip())
    with open(FILE_NAME, 'a', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name, marks])

def show_report():
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        total = 0
        qty = 0
        lowest = sys.maxsize 
        name_lowest = ""
        name_highest = ""
        highest = -sys.maxsize - 1
        for entry in reader:
            qty = qty + 1
            marks = int(entry["Marks"])
            name_curr = entry["Name"]
            total = total + marks
            if marks < lowest:
                lowest = marks 
                name_lowest = name_curr 
            if marks > highest:
                highest = marks 
                name_highest = name_curr 
        #Can probably split report generation and printing into two different functions 
        print("REPORT")
        print(f"Average Marks {round(total/qty, 2)}")
        print(f"Highest marks are {highest} score by {name_highest}")
        print(f"Lowest marks are {lowest} score by {name_lowest}")
        print(f"Total number of students are {qty}")

def main():
    while True:
        choice = int(input("What would you like to do? \n 1. Input Marks \n 2.View Report \n 3. Exit.").strip())
        match choice:
            case 1: 
                input_marks()
            case 2: 
                show_report()
            case 3:
                break
            case _:
                print("Please Enter a valid option.")




        
