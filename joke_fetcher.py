import requests 

def get_joke ():
    response = requests.get("https://official-joke-api.appspot.com/jokes/ten")
    print ("status code:", response.status_code)


    if response.status_code == 200:
        data = response.json()
        for joke in data:
            print (joke["setup"])
            print (joke["punchline"])
            print ()
    else:
        print ("couldn't fetch")


def main():
    while True:
        print ("1 to get 10 jokes or 2 to quit ")
        user_input = input("choose 1 or 2 ")
        if user_input == "1":
            get_joke()
        elif user_input == "2":
            break 
        else:
            print ("invalid input ")

main()