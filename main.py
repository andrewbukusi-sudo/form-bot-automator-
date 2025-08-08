from flask import Flask
from scheduler import submit_form

app = Flask(__name__)

@app.route("/", methods=["GET", "HEAD"])
def index():
    try:
        submit_form()
        return "✅ Form submitted successfully!"
    except Exception as e:
        return f"❌ Error: {str(e)}"
        if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

