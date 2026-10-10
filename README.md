# Python Practice Projects

Small command-line programs I wrote in summer 2026 while teaching myself Python, as the second phase of a self-directed study plan (after Python basics, before machine learning).

Each program practises one or two concepts: reading and writing files, CSV and JSON, calling REST APIs, and object-oriented programming.

## Programs

**Files and text**
- `simple_journal.py`: add notes to a text file and read them back
- `books_i_have_read.py`: keep a reading list in a text file and count the books
- `expense_tracker.py`: log expenses and show the total and the average
- `minutes_counter.py`: log study sessions and total the minutes
- `saving_balance_tracker.py`: keep a running savings balance in a file
- `grade_log.py`: store names and scores and work out the class average

**CSV**
- `grade_log_csv.py`: the grade log rewritten with Python's `csv` module
- `student_record_app.py`: student records with name, subject and score, using `csv.DictReader`/`DictWriter`
- `inventory_tracker.py`: inventory of items, quantities and prices, with total stock value
- `movie_rankings.py`: rate movies and find the highest-rated one

**JSON**
- `contact_list.py`: save and load contacts as JSON
- `book_ranking.py`: books with author, rating and a list of tags; average rating
- `recipe_book.py`: recipes with nested ingredient lists

**APIs** (using `requests`)
- `cat_fact_fetcher.py`: first API call, fetching a random fact
- `joke_fetcher.py`: fetches ten jokes and prints them
- `age_guesser.py`: predicts an age from a first name using the Agify API

**Object-oriented programming**
- `bank_account_oop.py`: a `BankAccount` class with deposits, withdrawals and an insufficient-funds check
- `student_oop.py`: a `Student` class that stores grades and computes an average
- `dog_oop.py`: a first class with attributes and methods

## How to run

Requires Python 3. The API programs also need the `requests` library:

```
pip install requests
python3 expense_tracker.py
```

Most programs show a numbered menu. Data files (`.txt`, `.csv`, `.json`) are created automatically the first time you add something.
