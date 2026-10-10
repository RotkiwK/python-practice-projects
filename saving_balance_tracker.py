def load_blance():
    number = 0
    try:
        with open("balance.txt" , "r") as f :
            content = f.read()
            number = float(content)
    except FileNotFoundError:
        pass
    return number

def save_balance(amount):
    with open("balance.txt" , "w") as f:
        f.write(str(amount))

def main():
    while True:
        print ("1 deposite money")
        print ("2 view balance ")
        print ("3 quit")
        user_input = input("choose 1-3 ")
        if user_input == "1":
            amount = float(input("add ballance "))
            new_balance = load_blance() + amount
            save_balance(new_balance)
        elif user_input == "2":
            print (load_blance())
        elif user_input == "3":
            break
        else: 
            print ("invalid input ")
    
main()







