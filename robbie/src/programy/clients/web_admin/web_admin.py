from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def web_admin():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)