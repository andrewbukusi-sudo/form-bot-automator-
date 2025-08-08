from flask import Flask
import threading
from scheduler import submit_form

app = Flask(__name__)

@app.route("/")
def index():
    # Run the bot in background so Render doesn't kill it
    thread = threading.Thread(target=submit_form)
    thread.daemon = True
    thread.start()
    return "Form bot started in the background ✅"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
