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
        file1_decoded = False
        file2_decoded = False
        decodings = ["utf-8", "utf-16", "utf-32"]
        for encoding in decodings:
            try:
                file1_lines = file1.decode(encoding).splitlines()
                file1_decoded = True
                break
            except:
                continue
        if not file1_decoded:
            return "Error: Unable to decode file1 as UTF-8, UTF-16, or UTF-32."
        for encoding in decodings:
            try:
                file2_lines = file2.decode(encoding).splitlines()
                file2_decoded = True
                break
            except:
                continue
        if not file2_decoded:
            return "Error: Unable to decode file2 as UTF-8, UTF-16, or UTF-32."

        diff = difflib.unified_diff(file1_lines, file2_lines, fromfile='file1', tofile='file2')

        diff = list(diff)
        return render_template("compare.html", diff=diff)

if __name__ == "__main__":
    app.run(debug=True)
