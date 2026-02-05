import os
from flask import Flask, render_template, redirect, request
from cs50 import SQL
from werkzeug.utils import secure_filename
from processor import process_bank_data

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQL("sqlite:///finance.db")

@app.route("/")
def index():
    return render_template("/index.html")

@app.route("/history")
def history():
    transactions = db.execute("SELECT * FROM transactions")
    return render_template("history.html", transactions=transactions)

@app.route("/upload", methods=["GET", "POST"])   
def upload():
    if request.method == "POST":
        file = request.files.get("file")

        if not file:
            return {"error": "No file"}, 400

        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)

        file.save(file_path)

        process_bank_data(file_path)

        return redirect("history")

    return render_template("/upload.html")

if __name__ == '__main__':
    app.run(debug=True)
