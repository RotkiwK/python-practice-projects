import csv


def add_grade(name,score):
    with open ("grades.csv" ,"a", newline="") as f:
        writer =csv.writer(f)
        writer.writerow([name,score])

def view_all():
    try:
        with open("grades.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print ("no greades yet")

def class_average ():
    total = 0
    count = 0
    try:
        with open("grades.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                total = total + float(row[1]) 
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
            score = input("input score ")
            add_grade (name,score)
        elif user_input == "2":
            view_all()
        elif user_input == "3":
            print (class_average())
        elif user_input == "4":
            break 
        else:
            print ("invalid choice ")
main()
