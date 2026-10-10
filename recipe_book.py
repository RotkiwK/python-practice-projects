import json

def add_recipie(name,ingridiends):
    recipie = load_recipie()
    recipie.append({"name":name, "ingridiends": ingridiends })
    save_recipie(recipie)





def load_recipie():
    try:
        with open ("recipie.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    
def save_recipie(contacts):
    with open("recipie.json", "w") as f:
        json.dump(contacts,f)

def view_contacts():
    recipie = load_recipie()
    for row in recipie:
        print (row["name"],row["ingridiends"])


def main():
    while True:
        print ("1 add recipie ")
        print ("2 view all recipies ")
        print ("3 quit ")
        user_input = input("choose 1-3 ")
        if user_input == "1":
            ingridiends =[]
            name = input("input the name ")
            while True:
                item = input ("input the ingridiends or 2 to stop")
                if item == "2":
                    break
                ingridiends.append(item)
            add_recipie(name,ingridiends)
        elif user_input == "2":
            view_contacts()
        elif user_input == "3":
            break
        else:
            print ("invalid input")
                
main()