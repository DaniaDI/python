# 🎨 Flask Playground Boxes

## 📌 Overview

This is a simple Flask project that demonstrates how to:

* Pass data from routes to templates in one templete.
* Use loops in Jinja2 using {%  %}
* Dynamically change content (number of boxes & colors)

 

## 🚀 Features

* Display 3 blue boxes by default
* Display any number of boxes using a URL parameter
* Change box color dynamically via URL
* Uses a single template for all routes

 

## 🛠️ Technologies Used

* Python
* Flask
* HTML
* Jinja2 (template engine)
* CSS (internal styling)

---

## 📂 Project Structure

 
play/
│── play.py
│── templates/
│    └── index.html
 


 
3. Open your browser:

http://localhost:5000

## 🌐 Routes

### 1. Default Route

/play : 3box with color blue.

➡️ Displays 3 blue boxes

### 2. Dynamic Number of Boxes

/play/<x>

➡️ Displays x blue boxes

Example:

/play/7
 
 

### 3. Dynamic Color & Number

/play/<x>/<color>

➡️ Displays x boxes with chosen color

/play/5/red


## 🧠 Key Concepts

### Passing Data to Template
{{ color }}:var in html so we can used in flask file.

render_template("index.html", times=3, color="blue")

### Jinja Loop

 
{% for x in range(times) %}
 
   
### Dynamic Styling
 
style="background-color: {{ color }}"
 

## 👩‍💻 Author

Dania Isead
