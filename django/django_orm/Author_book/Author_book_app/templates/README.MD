# Books and Authors Manager (Django)

A lightweight web application built with Python and Django that manages a **Many-to-Many** relationship between Books and Authors. Users can add books, add authors, view specific detail pages for each, and associate authors to books  dynamically via dropdown interfaces.

---

## 🚀 Features

* **Book Management:** Add books with a title and description, and view a complete list of all recorded books.
* **Author Management:** Add authors with their first name, last name, and custom notes.
* **Many-to-Many Association:** * Assign multiple authors to a single book from the book's detail page.
    * Assign multiple books to a single author from the author's detail page.
    * Dropdown menus intelligently exclude authors/books that are already linked.
    * Styled Interface:** Uses Bootstrap 5 for clean and responsive forms and tables.

---

## 🛠️ Tech Stack

* **Backend:** Python , Django 
* **Database:** SQLite3 (Default Django DB)
* **Frontend:** HTML5, Jinja/Django Template Language, Bootstrap 5

---

## 📂 Project Structure & Routes

### URL Routing (`urls.py`)
| URL Path | View Function | Description |
| :--- | :--- | :--- |
| `/` | `views.add_book` | Homepage: View all books & add a new book |
| `/add_book/` | `views.add_book` | Process adding a new book (POST) |
| `/books/<int:id>/` | `views.view_book` | Detailed view of a specific book + append authors |
| `/add_author/` | `views.add_author` | View all authors & add a new author |
| `/authors/<int:id>/` | `views.view_author` | Detailed view of a specific author + append books |

### Templates Context Mapping (`views.py`)
* **`book.html`**  Receives `all_books` to display the library catalog.
* **`book_show.html`**  Receives `book`, `book_authors`, and `other_authors` to show details and build the linkage dropdown.
* **`author.html`** Receives `all_authors` to list out creators.
* **`author_show.html`**  Receives `author`, `book_authors`, and `other_books` to display profiles and link pending books.

---

## 💾 Database Schema (Models)

The database structure relies on two main tables connected via a Many-to-Many field:
 two class (Book,Author)


## Developer:
--Dania Danial Isead -Full Stack Web Developer

