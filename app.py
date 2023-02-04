from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/compare", methods=["GET", "POST"])
def compare():
    if request.method == "POST":
        file1 = None
        file2 = None
        encoding_types = ['utf-8', 'utf-16', 'utf-32']
        for encoding in encoding_types:
            try:
                file1 = request.files["file1"].read().decode(encoding).splitlines()
                file2 = request.files["file2"].read().decode(encoding).splitlines()
                break
            except UnicodeDecodeError:
                continue
        if file1 is None or file2 is None:
            return "Error: The uploaded file is not in a supported encoding format. Please upload a file encoded in utf-8, utf-16, or utf-32."
        
        # Compare the contents of the two files
        # ...

        return "The comparison results."
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
