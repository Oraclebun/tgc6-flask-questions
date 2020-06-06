from flask import Flask, render_template, request, redirect, url_for
import os
import csv
import re
from data import read_books, find_book_by_title, find_book_generic, add_book, write_to_file

app = Flask(__name__)

@app.route('/')
def read_book():
    all_books = read_books()
    return render_template('index.template.html',books=all_books)

@app.route('/search')
def find_book():
    return render_template('books/search_books.template.html')

def repl_func(m):
   # process regular expression match groups for word upper-casing problem
    return m.group(1) + m.group(2).upper()

@app.route('/search',methods=['POST'])
def show_book():
    title = request.form.get('book_title')
    title1 = re.sub(r"(^|\s)(\S)", repl_func, title)   #need 'r' to tell python its a raw string or string literal
    searched_book = find_book_by_title(title1)
    return render_template('books/view_books.template.html',book_result=searched_book)

@app.route('/book/add')
def add_record_book():
    return render_template('books/add_book.template.html')

@app.route('/book/add',methods=['POST'])
def process_add_book():
    book_title = request.form.get('book_title')
    isbn = request.form.get('isbn')
    author = request.form.get('author')
    year_published = request.form.get('year-published')
    add_book(book_title,isbn,author,year_published)
    return redirect(url_for('read_book'))

@app.route('/book/edit')
def select_book_to_edit():
    # Get all books into a list
    all_books = read_books()
    return render_template('books/select_book.template.html', books = all_books)

@app.route('/book/edit', methods=['POST'])
def any1():
    isbn = request.form.get('isbn')
    return redirect(url_for('edit_selected_book', isbn=isbn))
    
@app.route('/book/editting/<isbn>')
def edit_selected_book(isbn):
    book_to_be_editted = find_book_generic(isbn)
    print(book_to_be_editted)
    return render_template('books/edit_book.template.html',book=book_to_be_editted)

@app.route('/book/editting/<isbn>', methods=['POST'])
def process_edit(isbn):
    # step 1. retrieve all books in the .csv file in a list
    all_books = read_books()

    # step 2. find the book that we have changed
    changed_book = find_book_generic(isbn)

    print(changed_book)

    # step 3. update the changed book to match the form
    changed_book['title'] = request.form.get('book_title')
    changed_book['author'] = request.form.get('author')
    changed_book['year_published'] = request.form.get('year-published')

    # step 4. overwrite the book information in the list
    for index in range(0, len(all_books)):
        if all_books[index]['isbn'] == changed_book['isbn']:
            all_books[index] = changed_book

    # step 5. write the entire list back to the csv file
    with open('books.csv', 'w', newline="\n") as fp:
        writer = csv.writer(fp, delimiter=",")

        # write in the header
        writer.writerow(['isbn', 'title', 'author', 'year_published'])

        for b in all_books:
            writer.writerow([b['isbn'], b['title'], b['author'], b['year_published']])

    return redirect(url_for('read_book'))


@app.route('/choose_delete')
def select_to_delete():
    all_books = read_books()
    return render_template('/books/show_delete.template.html', books=all_books)

@app.route('/choose_delete',methods=['POST'])
def go_to_confirm():
    book_prop = request.form.get('book_prop')
    props = book_prop.split("-")
    title = props[0]
    isbn = props[1]
    return redirect(url_for('confirm_delete', isbn = isbn, title=title))

@app.route('/delete_book/<isbn>/<title>')
def confirm_delete(isbn,title):
    return render_template('/books/confirm_delete.template.html', isbn=isbn, title=title)

@app.route('/delete_book/<isbn>/<title>', methods=['POST'])
def process_delete(isbn,title):
    #step 1. put all books from csv into a list
    all_books = read_books()
    #step 2. find the book to be deleted
    book_to_delete = find_book_generic(isbn)
    #step 3. find the item to be deleted in the all_books list & delete it
    for index in range(len(all_books)):
        if book_to_delete['isbn'] == all_books[index]['isbn']:
            del all_books[index]
            break
    #4. write back the list to the file
    write_to_file(all_books)
    return redirect(url_for('read_book'))

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('127.0.0.1'),
            port=int(os.environ.get('PORT','8000')),
            debug=True)