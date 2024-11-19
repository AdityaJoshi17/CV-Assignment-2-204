from flask import Flask, request, render_template
import os
from transformations import apply_transformations

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        file = request.files["image"]
        path = os.path.join("uploads", file.filename)
        file.save(path)

        transformations = apply_transformations(path)
        return render_template("results.html", transformations=transformations)

    return render_template("index.html")

if __name__ == "__main__":
    os.makedirs("uploads", exist_ok=True)
    os.makedirs("static", exist_ok=True)
    app.run(debug=True)
