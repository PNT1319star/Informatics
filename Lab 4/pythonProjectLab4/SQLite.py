import sqlite3
from sqlite3 import Error

# Создаем соединение с базой данных
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Successfully connected to SQLite Database")
    except Error as error:
        print(f"The error '{error}' occurred")
    return connection

# Kết nối đến cơ sở dữ liệu
connection = create_connection(r"D:\Năm 1\Informatics\Lab 4\Book.sqlite")

#=============================================================================================
# Создать таблицы
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as error:
        print(f"The error '{error}' occurred")

# Создать таблицу книг
create_books_table = """
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    yearOfPublication INTEGER,
    genre TEXT,
    authorID INTEGER NOT NULL,
    publisherID INTEGER NOT NULL,
    FOREIGN KEY (authorID) REFERENCES authors (id),
    FOREIGN KEY (publisherID) REFERENCES publishers (id)
);
"""
execute_query(connection, create_books_table)

# Создать таблицу авторов
create_authors_table = """
CREATE TABLE IF NOT EXISTS authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
"""
execute_query(connection, create_authors_table)

# Создать таблицу издателей
create_publishers_table = """
CREATE TABLE IF NOT EXISTS publishers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT,
    city TEXT
);
"""
execute_query(connection, create_publishers_table)

# Создать таблицу пользователей
create_users_table = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT
);
"""
execute_query(connection, create_users_table)

# Создать таблицу отзывов
create_reviews_table = """
CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    comment TEXT,
    rating INTEGER CHECK (rating BETWEEN 1 AND 5),
    bookID INTEGER NOT NULL,
    userID INTEGER NOT NULL,
    FOREIGN KEY (bookID) REFERENCES books(id),
    FOREIGN KEY (userID) REFERENCES users (id)
);
"""
execute_query(connection, create_reviews_table)

#=======================================================================================================================
# Вставлять данные

create_books = """
INSERT INTO 
    books (title, yearOfPublication, genre, authorID, publisherID)
VALUES
    ('To Kill a Mockingbird', 1960, 'Fiction', 1, 1),
    ('1984', 1949, 'Dystopian', 2, 2),
    ('Pride and Prejudice', 1813, 'Romance', 3, 1),
    ('The Great Gatsby', 1925, 'Classic', 1, 3),
    ('Harry Potter and the Sorcerer''s Stone', 1997, 'Fantasy', 4, 4);
"""
execute_query(connection, create_books)


create_authors = """
INSERT INTO 
    authors (name)
VALUES
    ('Harper Lee'),
    ('George Orwell'),
    ('Jane Austen'),
    ('F. Scott Fitzgerald'),
    ('J.K. Rowling');
"""
execute_query(connection, create_authors)


create_publishers = """
INSERT INTO
    publishers(name, address, city)
VALUES
    ('Penguin Books', '123 Main St', 'New York'),
    ('Random House', '456 Oak St', 'London'),
    ('HarperCollins', '789 Maple St', 'Toronto'),
    ('Vintage Books', '101 Pine St', 'San Francisco'),
    ('Scholastic', '202 Elm St', 'Paris');
"""
execute_query(connection, create_publishers)


create_users = """
INSERT INTO
    users(name, email)
VALUES 
    ('John Doe', 'john@email.com'),
    ('Alice Smith', 'alice@email.com'),
    ('Bob Johnson', 'bob@email.com'),
    ('Eva Brown', 'eva@email.com'),
    ('David White', 'david@email.com');
"""
execute_query(connection, create_users)


create_reviews = """
INSERT INTO
    reviews(comment, rating, bookID, userID)
VALUES
    ('A classic!', 5, 1, 1),
    ('Thought-provoking', 4, 2, 2),
    ('Love it!', 5, 3, 3),
    ('Captivating', 4, 4, 4),
    ('Magical world', 5, 5, 5);
"""
execute_query(connection, create_reviews)
#======================================================================================================================
#выбрать все записи из таблиц
def execute_read_query(connection, query):
    cursor = connection.cursor()
    results = None
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except Error as error:
        print(f"The error '{error}' occurred")

select_books = "SELECT * FROM books"
books = execute_read_query(connection, select_books)
for book in books:
    print(book)
print("\n")

select_authors = "SELECT * FROM authors"
authors = execute_read_query(connection, select_authors)
for author in authors:
    print(author)
print("\n")

select_publishers = "SELECT * FROM publishers"
publishers = execute_read_query(connection, select_publishers)
for publisher in publishers:
    print(publisher)
print("\n")

select_users = "SELECT * FROM users"
users = execute_read_query(connection, select_users)
for user in users:
    print(user)
print("\n")

select_reviews = "SELECT * FROM reviews"
reviews = execute_read_query(connection, select_reviews)
for review in reviews:
    print(review)
print("\n")
#=======================================================================================================================
#составить запрос по извлечению данных с использованием JOIN
select_books_reviews = """
SELECT
    books.title,
    reviews.comment
FROM
    books
INNER JOIN reviews ON books.id = reviews.bookID;  
"""
books_reviews = execute_read_query(connection, select_books_reviews)
for books_review in books_reviews:
    print(books_review)
print("\n")
#=======================================================================================================================
# составить запрос по извлечению данных с использованием WHERE и GROUP BY
select_avg_rating = """
SELECT 
    books.title,
    AVG(reviews.rating) AS average_rating
FROM reviews
JOIN books ON reviews.bookID = books.id
WHERE reviews.rating >= 4
GROUP BY books.title;
"""

avg_ratings = execute_read_query(connection, select_avg_rating)
for avg_rating in avg_ratings:
    print(avg_rating)
print("\n")
#=======================================================================================================================
#Составить два запроса, в которых будет вложенный SELECT-запрос (вложение с помощью WHERE.)
select_reviews_for_books_after_1900 = """
SELECT *
FROM reviews
WHERE bookID IN (SELECT id FROM books WHERE yearOfPublication > 1900);
"""
reviews_after_1900 = execute_read_query(connection, select_reviews_for_books_after_1900)
print("Reviews for Books Published After 1900:")
for review in reviews_after_1900:
    print(review)
print("\n")


select_reviews_for_author = """
SELECT *
FROM reviews
WHERE bookID IN (SELECT id FROM books WHERE authorID = (SELECT id FROM authors WHERE name = 'George Orwell'));
"""
reviews_for_author = execute_read_query(connection, select_reviews_for_author)
print("Reviews for Books by George Orwell:")
for review in reviews_for_author:
    print(review)
print("\n")
#======================================================================================================================
# UNION Query 1
select_union_query_1 = """
SELECT title
FROM books
JOIN reviews ON books.id = reviews.bookID
WHERE reviews.rating >= 3
UNION
SELECT title
FROM books
JOIN reviews ON books.id = reviews.bookID
WHERE reviews.rating <= 2;
"""

# Execute UNION Queries
union_result = execute_read_query(connection, select_union_query_1)
for record in union_result:
    print(record)
print("\n")

#=======================================================================================================================
# DISTINCT Query
select_distinct_query = """
SELECT DISTINCT genre
FROM books;
"""

# Execute DISTINCT Query
distinct_result = execute_read_query(connection, select_distinct_query)
print("Distinct Genres:")
for genre in distinct_result:
    print(genre)
print("\n")

#=======================================================================================================================
update_book_publication_year = """
UPDATE books
SET yearOfPublication = 2000
WHERE title = 'To Kill a Mockingbird';
"""
execute_query(connection, update_book_publication_year)

update_publisher_address = """
UPDATE publishers
SET address = 'New Address'
WHERE name = 'Random House';
"""
execute_query(connection, update_publisher_address)
#=======================================================================================================================
delete_book_query = """
DELETE FROM books
WHERE id = 1; 
"""
execute_query(connection, delete_book_query)

delete_author_query = """
DELETE FROM authors
WHERE id = 1; 
"""
execute_query(connection, delete_author_query)

delete_publisher_query = """
DELETE FROM publishers
WHERE id = 1; 
"""
execute_query(connection, delete_publisher_query)

delete_user_query = """
DELETE FROM users
WHERE id = 1; 
"""
execute_query(connection, delete_user_query)

delete_review_query = """
DELETE FROM reviews
WHERE id = 1; 
"""
execute_query(connection, delete_review_query)
#=======================================================================================================================
delete_all_books_query = """
DELETE FROM books;
"""
execute_query(connection, delete_all_books_query)