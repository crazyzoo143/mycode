from flask import Flask, render_template

app = Flask(__name__)

email_addresses = [
    "user1@fakemeial.com",
    "user2@fakeemail.com",
    "user3@fakeemail.com"
    "user4@fakeemail.com"
    "user5@fakeemail.com"
]

@app.route('/')
def index():
    return render_template('index.html', email_addresses=email_addresses)

if __name__ == '__main__':
    app.run(debug=True)

