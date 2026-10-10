def add_grade(name,score):
    with open ("grade.txt" , "a") as f:
        f.write (name +","+ score + "\n" )

def view_all():
    try:
        with open("grade.txt", "r") as f:
            for line in f:
                name, score = line.strip().split(",")
                print(name + ": " + score)
    except FileNotFoundError:
        print ("no greades yet")

def class_average ():
    total = 0
    count = 0
    try:
        with open("grade.txt","r") as f:
            for line in f:
                parts = line.strip().split(",")
                total = total + float(parts[1]) 
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
