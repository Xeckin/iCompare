from flask import Flask, render_template, request
import difflib

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/compare", methods=["GET", "POST"])
def compare():
    if request.method == "POST":
        file1 = request.files["file1"].read()
        file2 = request.files["file2"].read()
        try:
            file1_lines = file1.decode("utf-8").splitlines()
        except:
            try:
                file1_lines = file1.decode("utf-16").splitlines()
            except:
                try:
                    file1_lines = file1.decode("utf-32").splitlines()
                except:
                    return "Error: Unable to decode file1 as UTF-8, UTF-16, or UTF-32."
        try:
            file2_lines = file2.decode("utf-8").splitlines()
        except:
            try:
                file2_lines = file2.decode("utf-16").splitlines()
            except:
                try:
                    file2_lines = file2.decode("utf-32").splitlines()
                except:
                    return "Error: Unable to decode file2 as UTF-8, UTF-16, or UTF-32."

        diff = difflib.unified_diff(file1_lines, file2_lines, fromfile='file1', tofile='file2')

if isinstance(diff, dict) and len(diff) == 2:
    return render_template("compare.html", diff=diff)
else:
    return "Error: Invalid comparison data"


if __name__ == "__main__":
    app.run(debug=True)
