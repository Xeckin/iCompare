# app.py

from flask import Flask, request, render_template
import difflib

app = Flask(__iComapre__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/compare", methods=["POST"])
def compare():
    file1 = request.files["file1"].read().decode("utf-8").splitlines()
    file2 = request.files["file2"].read().decode("utf-8").splitlines()

    diff = list(difflib.unified_diff(file1, file2))

    return render_template("compare.html", diff=diff)

if __name__ == "__main__":
    app.run()
