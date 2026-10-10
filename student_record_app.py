import csv
import os

def add_student(name, subject, score):
    file_exists = os.path.exists("students.csv")
    with open("students.csv", "a", newline="") as f:
        fieldnames = ["name", "subject", "score"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow({"name": name, "subject": subject, "score": score})



def view_student ():
    try:
        with open ("students.csv", "r") as f:
            reader =csv.DictReader(f)
            for row in reader:
                print (row["name"],row["subject"],row["score"])
    except FileNotFoundError:
        print ("no students yet")

def average_score():
    total = 0
    count = 0
    try:
        with open("students.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                total = total + float(row["score"]) 
                count = count + 1
    except FileNotFoundError:
        pass
    if count == 0:
        return 0
    average = total / count
    return average


def main ():
    while True:
        print ("1 add a grade")
        print ("2 view all grades")
        print ("3 class average")
        print ("4 quit")
        user_input = input ("choose 1 to 4 ")
        if user_input == "1":
            name = input("input name ")
            subject = input("input subject")
            score = input("input score ")
            add_student (name,subject,score)
        elif user_input == "2":
            view_student()
        elif user_input == "3":
            print (average_score())
        elif user_input == "4":
            break 
        else:
            print ("invalid choice ")
main()

        


