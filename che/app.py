from flask import Flask, render_template
import random

app = Flask(__name__)

elements = [
    {"symbol": "H", "name": "Hydrogen", "number": 1},
    {"symbol": "O", "name": "Oxygen", "number": 8},
    {"symbol": "Na", "name": "Sodium", "number": 11},
    {"symbol": "Cl", "name": "Chlorine", "number": 17}
]

compounds = {
    "Water": "H2O",
    "Carbon dioxide": "CO2",
    "Salt": "NaCl"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/game1")
def game1():
    return render_template("game1.html", element=random.choice(elements), elements=elements)

@app.route("/game2")
def game2():
    name, formula = random.choice(list(compounds.items()))
    return render_template("game2.html", name=name, formula=formula)

@app.route("/game3")
def game3():
    return render_template("game3.html")

@app.route("/game4")
def game4():
    return render_template("game4.html")

if __name__ == "__main__":
    app.run(debug=True)
