from flask import Flask, render_template
from cs50 import SQL
from processor import process_bank_data

app = Flask(__name__)

db = SQL("sqlite:///finance.db")

@app.route("/")
def index():
    return "<h1>Finance Tracker is alive!</h1>"

if __name__ == '__main__':
    app.run(debug=True)

@app.route("/history")
def history():
    transactions = db.execute("SELECT * FROM transactions")
    return render_template("history.html", transactions=transactions)