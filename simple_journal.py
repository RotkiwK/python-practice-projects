def add_note(text):
    with open("journal.txt", "a") as f:
        f.write(text + "\n")




def show_notes():
    try:
        with open("journal.txt", "r") as f:
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print("no notes yet")


def main():
    while True:
        print ("1 add note ")
        print ("2 view note ")
        print ("3 quit ")
        user_input = input("choose 1-3 ")
        if user_input == "1":
            text = input ("write your node")
            add_note(text)
        elif user_input == "2":
            show_notes()
        elif user_input == "3":
            break 
        else:
            print ("invalid choice ")
            
main()