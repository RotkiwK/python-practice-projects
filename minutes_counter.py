def add_minutes(number):
    with open ("workdone.txt", "a") as f:
        f.write(number + "\n")

def view_work():
    try:
        with open ("workdone.txt", "r")as f:
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print("no work yet")

def count_total():
    total = 0
    try:
        with open ("workdone.txt", "r")as f:
            for line in f:
                total = total + float(line)
    except FileNotFoundError:
        print("no work yet")
    return total

def main ():
    while True:
        print ("1 log a sesion ")
        print ("2 view all sesions ")
        print ("3 total minutes ")
        print ("4 quit ")
        user_input = input ("choose 1 to 4 ")
        if user_input == "1":
            minutes = input ("add more minutes")
            add_minutes(minutes)
        elif user_input == "2":
            view_work()
        elif user_input == "3":
            print (count_total())
        elif user_input == "4":
            break
        else:
            print("invalid choice")
main()

