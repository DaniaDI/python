Flask Basic Routes & Error Handling:
This repository contains a simple Flask application demonstrating basic routing, dynamic URL parameters, and custom error handling. It's a great "Hello World" starting point for understanding how Flask maps URLs to Python functions.

Routing:
@app.route('/')
@app.route('/Champion')
@app.route('/say/<name>')
@app.route('/repeat/<int:num>/<word>')


🧩 Key :
Dynamic Routing: The /say/<name> :route captures part of the URL as a variable and passes it to the function.

Variable Rules: The /repeat/<int:num>/<word>: route uses int: to ensure the first variable is treated as an integer, preventing string-multiplication errors.

Custom 404 Page: Instead of the default browser error, the @app.errorhandler(404) decorator catches "Page Not Found" errors and returns a custom message:

"Sorry! No response. Try again."

Debug Mode: Enabled via app.run(debug=True), allowing for auto-reloading and helpful error tracking during development.

📂 File :
app.py: The main application file containing all routes and logic.
 
