def add_expence (number):
    with open ("expence.txt", "a") as f:
        f.write(number + "\n")

def view_expence ():
    try:
        with open ("expence.txt", "r") as f:
            for line in f:
                print (line.strip())
    except FileNotFoundError:
        print ("no expences yet")

def total_expences ():
    total = 0
    try: 
        with open ("expence.txt", "r") as f:
            for line in f:
                total = total + float(line)
    except FileNotFoundError:
        pass 
    return total 

def average_expences():
    total = 0
    count = 0
    try:
        with open ("expence.txt", "r") as f:
            for line in f:
                total = total + float(line)
                count = count + 1
    except FileNotFoundError:
        pass 
    if count == 0:
        return 0
    average = total / count
    return average

def main ():
    while True:
        print ("1 add an expence") 
        print ("2 view all epence ")      
        print ("3 total spend ")     
        print ("4 average expence")
        print ("5 quit ")
        user_input = input("choose number 1-5 ")
        if user_input == "1":
            expence = input ("add expence")
            add_expence (expence)
        elif user_input == "2":
            view_expence()
        elif user_input == "3":
            print (total_expences())
        elif user_input == "4":
            print(average_expences())
        elif user_input == "5":
            break 
        else: 
            print ("wrong input ")
main()



