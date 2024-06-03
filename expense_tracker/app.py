from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

DATA_FILE = "expenses.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file)

@app.route("/")
def index():
    expenses = load_data()
    return render_template("index.html", expenses=expenses)

@app.route("/add", methods=["POST"])
def add_expense():
    expense = {
        "date": request.form["date"],
        "description": request.form["description"],
        "amount": float(request.form["amount"])
    }
    expenses = load_data()
    expenses.append(expense)
    save_data(expenses)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
