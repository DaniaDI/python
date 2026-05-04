🍓 Fruit Store Web App (Flask)

📌 Overview:

This is a simple web application built using Flask that simulates a fruit store checkout system.
Users can select fruits, enter their personal information, and receive a summary of their order.

🚀 Features:
Select fruits and quantities
Submit customer information (first name, last name, student ID)
Calculate total items
Display checkout summary page
Show current date and time
Redirect flow from form → processing → result page

🛠️ Technologies Used:
Python 3
Flask Framework
HTML / CSS (Bootstrap optional)
Jinja2 Templates
datetime module


🔄 Application Flow:
User opens home page /
Select fruits in form
Submit form → /checkout (POST)
Backend calculates total + adds date
Redirect to /show
Display checkout summary

📊 Example Input:
Strawberry: 2
Apple: 1
Raspberry: 3


📤 Output:
Total items: 6
Customer info
Date of order
