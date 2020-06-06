import csv


def read_books():
    all_books = []
    with open('books.csv', 'r', newline='\n') as fp:
        reader = csv.reader(fp, delimiter=",")
        next(reader)    # skip header
        for line in reader:
            library = {
                'isbn': line[0],
                'title': line[1],
                'author': line[2],
                'year_published': line[3]
            }
            all_books.append(library)
    # print(all_books)
    return all_books


def find_book_by_title(title):
    matches = []
    with open('books.csv', 'r', newline='\n') as fp:
        reader = csv.reader(fp, delimiter=",")
        next(reader)    # skip header
        for line in reader:
            if line[1] == title:
                matches.append({
                    'isbn': line[0],
                    'title': line[1],
                    'author': line[2],
                    'year_published': line[3]
                })
    return matches


def find_book_generic(arg):
    with open('books.csv', 'r', newline='\n') as fp:
        reader = csv.reader(fp, delimiter=",")
        next(reader)    # skip header
        for line in reader:
            if line[0] == arg or line[1] == arg or line[2] == arg or line[3] == arg:
                record = {
                    'isbn': line[0],
                    'title': line[1],
                    'author': line[2],
                    'year_published': line[3]
                }
                break
    return record

def add_book(title,isbn,author,year):
    with open('books.csv','a',newline='\n') as fp:
        writer = csv.writer(fp, delimiter=",")
        writer.writerow([isbn, title, author, year]) # note this is appending to the data
    

def write_to_file(book_list):
    with open('books.csv','w',newline='\n') as fp:
        writer = csv.writer(fp, delimiter=",")
        #write the header first
        writer.writerow(['isbn', 'title', 'author', 'year_published']) #note: must have string because this is writing header in string

        for book in book_list:
            writer.writerow([book['isbn'], book['title'], book['author'], book['year_published']])
