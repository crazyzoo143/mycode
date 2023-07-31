from flask import Flask, render_template, request
from churchillquotes import winston_churchill_quotes
import random

app = Flask(__name__)

@app.route("/")
def start():
    return render_template("churchillsite.html")

@app.route("/quotecount", methods = ["POST"])
def login():
    # first, getting a number of quotes to display
    if request.form.get("Quotes"): # did someone type in a number of quotes?
            quote_num = request.form.get("Quotes") # grab the value of nm from the POST
    else: # if a user sent a post without nm then assign value defaultuser
            quote_num = "101"

    # second, convert that string into an integer
    quote_num= int(quote_num)

    # third, grab that number of churchill quotes
    chosenquotes= random.sample(winston_churchill_quotes, quote_num)

    # fourth, send an HTML file that has a line of HTML for each selected quote
    return render_template("churchilldisplay.html", quotelist= chosenquotes)

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)
