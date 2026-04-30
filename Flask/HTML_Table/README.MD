# 👥 Flask Users Table

## 📌 Overview

This project is a simple Flask web application that displays a list of users in an HTML table. It demonstrates how to pass data from the backend (Flask) to the frontend (Jinja2 template) and render it dynamically.



## 🚀 Features

* Display users in a structured table
* Use of Jinja2 templating
* Loop through a list of dictionaries
* Generate dynamic content (Full Name)
* Optional Bootstrap styling for better UI


## 🛠️ Technologies Used

* Python
* Flask
* HTML
* Jinja2
* Bootstrap

## 🌐 Route

### 🔹 Home Route

Displays the users table.

## 🧠 Data Structure

The application uses a list of dictionaries:

users = [
   {'first_name': 'Michael', 'last_name': 'Choi'},
   {'first_name': 'John', 'last_name': 'Supsupin'},
   {'first_name': 'Mark', 'last_name': 'Guillen'},
   {'first_name': 'KB', 'last_name': 'Tonel'}
]
 

## 🔁 Jinja Loop Example

 
{% for user in users %}
 

## 📊 Output Table

| First Name | Last Name | Full Name     |
| ---------- | --------- | ------------- |
| Michael    | Choi      | Michael Choi  |
| John       | Supsupin  | John Supsupin |
| Mark       | Guillen   | Mark Guillen  |
| KB         | Tonel     | KB Tonel      |

 

## 🎨 Optional Styling (Bootstrap)

adding Bootstrap:
 
class="table table-striped table-bordered"
 

## 👩‍💻 Author

Dania Isead
