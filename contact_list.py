import json



def load_contact():
    try:
        with open ("contacts.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    
def save_contacts(contacts):
    with open("contacts.json", "w") as f:
        json.dump(contacts,f)


def add_contact(name, phone):
    contacts = load_contact()
    contacts.append({"name": name, "phone": phone})
    save_contacts(contacts)


def view_contact ():
    contact = load_contact()
    for row in contact:
        print (row["name"],row["phone"])


def main():
    while True:
        print ("1 add contact ")
        print ("2 view all contacts ")
        print ("3 quit ")
        user_input = input("choose 1 to 3 ")
        if user_input == "1":
            name = input("type the name ")
            phone = input("type the phone ")
            add_contact(name,phone)
        elif user_input == "2":
            view_contact()
        elif user_input == "3":
            break
        else:
            print("wrong input ")
main()