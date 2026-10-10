import json


def load_books():
    try:
        with open ("books.json","r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    


def save_books(books):
    with open ("books.json", "w") as f:
        json.dump(books,f)



def add_book (title,author,rating,tags):
    book_discription = load_books()
    book_discription.append({"title":title, "author":author, "rating":rating, "tags":tags })
    save_books(book_discription)


def view_books ():
    book_discription = load_books()
    for row in book_discription:
        print (row["title"],row["author"],row["rating"],row["tags"])


def averager_rating():
    total = 0
    count = 0
    book_discription = load_books()
    for row in book_discription:
                total = total + row["rating"]
                count = count + 1
    if count == 0:
        return 0
    average = total / count
    return average
    
        
def main():
    while True:
        print("1 add a book ")
        print("2 view all books ")
        print("3 average rating ")
        print("4 quit")
        user_input = input("type 1-4 ")
        if user_input == "1":
            title = input("input title ")
            author = input("input author ")
            rating = float(input("input rating "))
            tags = []
            while True:
                item = input("input tag or type done to stop ")
                if item == "done":
                    break
                tags.append(item)
            add_book(title, author, rating, tags)
        elif user_input == "2":
            view_books()
        elif user_input == "3":
            print (averager_rating())
        elif user_input == "4":
            break 
        else:
            print ("inavlid input ")

main()

               
        
                    
