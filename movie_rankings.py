import os 
import csv


def add_movie (title, genre,rating):
    file_exist = os.path.exists("movie.csv")
    with open ("movie.csv","a",newline="") as f:
        fieldname = ("title","genre","rating")
        write = csv.DictWriter(f, fieldnames=fieldname)
        if not file_exist:
            write.writeheader()
        write.writerow({"title":title ,"genre":genre, "rating": rating})


def view_movies ():
    try:
        with open ("movie.csv","r",newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(row["title"],row["genre"],row["rating"])
    except FileNotFoundError:
        print ("file not found")

def highest_rated_movie():
    best = None
    try:
        with open("movie.csv", "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if best is None or float(row["rating"]) > float(best["rating"]):
                    best = row
    except FileNotFoundError:
        print("no movies yet")
    if best is None:
        return "no movies yet"
    return best["title"]


def main ():
    while True:
        print ("1 add movie")
        print ("2 view movie")
        print ("3 highest ranked movie")
        print ("4 quit")
        user_input = input("choose 1 to 4 ")
        if user_input == "1":
            title = input("type title ")
            genre = input("type genre ")
            rating = input("type rating ")
            add_movie(title,genre,rating)
        elif user_input == "2":
            view_movies()
        elif user_input == "3":
            print(highest_rated_movie())
        elif user_input == "4":
            break
        else:
            print ("no movies yet")

main()