import requests


def guess_age (name):
    response = requests.get("https://api.agify.io/?name=" + name)

    print("status code:", response.status_code)


    if response.status_code == 200:
        data = response.json()
        print(data)
        print("name:", data["name"],"age", data["age"])
    else:
        print ("couldn't fetch")

def main():
    while True:
        print ("1 guess the age ")
        print ("2 quit ")
        user_input = input("choos 1 or 2 ")
        if user_input == "1":
            name = input("input the name ")
            guess_age(name)
        elif user_input == "2":
            break 
        else:
            print ("invalid input ")
main()



