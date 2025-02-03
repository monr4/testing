# requirements.txt
flask==2.0.1
python-dotenv==0.19.0

# app.py
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Base template with user input reflection
BASE_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Message Board</title>
</head>
<body>
    <h1>Message Board</h1>
    <form method="GET">
        <input type="text" name="message" placeholder="Enter your message">
        <input type="submit" value="Post">
    </form>
    
    <div id="messages">
        <p>Latest message: {{ message }}</p>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    # Vulnerable: Directly reflecting user input without sanitization
    message = request.args.get('message', '')
    return render_template_string(BASE_TEMPLATE, message=message)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

# README.md
'''
XSS Vulnerable Web Application Demo
---------------------------------

Setup:
1. Create virtual environment:
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

2. Install dependencies:
   pip install -r requirements.txt

3. Run the application:
   python app.py

The application will be accessible at http://localhost:5000

Warning: This application is intentionally vulnerable to XSS attacks.
Do not use in production environments.
'''