from flask import Flask, render_template, request, redirect
import difflib

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/compare", methods=['GET', 'POST'])
def compare():
    if request.method == 'POST':
        try:
            text1 = request.form['text1']
            text2 = request.form['text2']

            diff = difflib.ndiff(text1.splitlines(), text2.splitlines())

            return render_template("compare.html", diff=diff)
        except Exception as e:
            return str(e)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
