from flask import Flask
from scheduler import submit_form

app = Flask(__name__)

@app.route("/")
def index():
    try:
        submit_form()
        return "Form submitted successfully!"
    except Exception as e:
        return f"❌ Error: {e}"