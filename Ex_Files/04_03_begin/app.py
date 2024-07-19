import csv
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)


@app.route("/")
def index():
    # template found in templates/index.html
    return render_template("index.html")


@app.route("/laureates/")
def laureate_list():
    # template found in templates/laureate.html
    results = []
    if not request.args.get("surname"):
        return jsonify(results)

    # Your code here!
    # return "your code here!"
    search_string = request.args.get("surname").lower().strip()
    return jsonify([x for x in laureates if search_string in x["surname"].lower()])
    #for laureate in laureates:
    #    if search_string in laureate["surname"].lower():
    #        results.append(laureate)
    #return jsonify(results)

app.run(debug=True)
