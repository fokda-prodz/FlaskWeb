# python3
# importer la clase Flask
from flask import Flask, render_template

app = Flask(__name__)

# Config de la page par défaut
@app.route("/")
def main():
    #return "Welcome to my Flask page"
    return render_template('index.html')

# Config de la page about
@app.route("/about")
def about():
    #return "Welcome to my Flask page"
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)