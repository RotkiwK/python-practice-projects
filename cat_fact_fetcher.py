import requests


def get_fact():
    response = requests.get("https://catfact.ninja/fact")

    print("status code:", response.status_code)

    if response.status_code == 200:
        data = response.json()
        print(data)
        print("cat fact:", data["fact"])
    else:
        print ("couldn't fetch")


def main():
    while True:
        print ("1 get cat ")
        print ("2 quit ")
        user_input = input("choose 1 or 2 ")
        if user_input == "1":
            get_fact()
        if user_input == "2":
            break
main()