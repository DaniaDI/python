## Dojo Survey :
A Flask-based web application that allows users to submit a survey form. The application captures user input, processes it on the server side, and redirects the user to a "results" page to display their information safely.  

## 🚀 Features:
Form Submission: A form using bootstrap5 to collect names, locations, language and comments.

Data Persistence via Redirect: Implements a redirect after a POST request to prevent form resubmission errors.  

Variable Extraction: Demonstrates the difference between request.form (for POST data) and request.args (for GET/URL data).

## 🌐 Routes

Home Page (/)
Method: GET

Purpose: Renders the form.html file containing the survey.

Processing (/result)
Method: POST

Purpose: Collects data from request.form. It then uses redirect(url_for('show', ...)) to pass that data to the next page as URL arguments.  

Display (/show)
Method: GET

Purpose: Retrieves the passed data using request.args.get() and renders it in show.html.

## 👩‍💻 Author

Dania Isead