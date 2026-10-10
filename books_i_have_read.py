def add_book(text):
    with open("books.txt", "a") as f:
        f.write(text + "\n")

def view_book():
    try:
        with open ("books.txt", "r")as f:
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print("no books yet")

def count_totla():
    count = 0
    try:
        with open("books.txt" , "r") as f :
            for line in f:
                count += 1
    except FileNotFoundError:
        pass
    return count

def main():
    while True:
        print ("1 add book")
        print ("2 view book")
        print ("3 count total books")
        print ("4 quit ")
        user_input = input ("choose 1 to 4 ")
        if user_input == "1":
            title = input ("add new title ")
            add_book(title)
        elif user_input == "2":
            view_book()
        elif user_input == "3":
            print (count_totla())
        elif user_input == "4":
            break 
        else:
            print ("invalid input ")
main()
