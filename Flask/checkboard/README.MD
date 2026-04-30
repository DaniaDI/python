# 🎯 Flask Checkerboard Project

## 📌 Overview

This project is a simple web application built using Flask that generates a dynamic checkerboard based on URL parameters. It demonstrates routing, template rendering, loops in Jinja2, and static file usage.



## 🚀 Features

* Default 8×8 checkerboard
* Dynamic rows and columns via URL
* Custom colors for checkerboard
* Uses Jinja2 templating
* External CSS styling


## 🛠️ Technologies Used

* Python
* Flask
* HTML
* CSS
* Jinja2


## 🌐 Routes

### 🔹 Default Checkerboard (8×8)

  defualt: row = 8 and col = 8 => 8x8

### 🔹 Custom Rows

/<x> :rows
 

### 🔹 Custom Rows and Columns

/<x>/<y>
 

### 🔹 Custom Colors (Bonus)


/<x>/<y>/<color1>/<color2>:/8/8/white/black

## 🧠 Key Concepts Learned

### 🔁 Nested Loops (Jinja2)

{% for x in range(row) %}
    {% for y in range(col) %}


### 🎨 Conditional Coloring

(row + col) % 2


### 🌐 Passing Data from Flask

render_template("index.html", row=x, col=y)
 
## ⚠️ Notes

* URL parameters must be integers where required
* Colors are passed as strings (e.g. "white", "black")
* Make sure Flask server is running before accessing routes


## 👩‍💻 Author

Dania Isead
