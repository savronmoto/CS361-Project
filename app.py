from flask import Flask, render_template, request
import os
from flask.helpers import url_for


# Configuration

app = Flask(__name__)

# Data

campaigns = ["Ghosts of Saltmarsh", "Waterdeep", "Homebrew Campaign", "Curse of Strahd"]

users = [
    {
        "username": "bilbobaggins",
        "password": "mithril"
    },
    {
        "username": "RogueOne",
        "password": "sneaky"
    }
]

# Routes 

@app.route('/')
def root():
    return render_template("main.j2")

@app.route('/login')
def login():
    return render_template("login.j2", users = users)

@app.route('/menu/<campaign>', methods=['GET', 'POST'])
def campaignView(campaign):
    return render_template("defaultView.j2", campaign=campaign)

@app.route('/menu')
def menu():
    return render_template("menu.j2", campaigns=campaigns)

    # if request.method == 'GET':
    #     return render_template("menu.j2", campaigns=campaigns)
    # elif request.method == 'POST':
    #     data = request.form.get("campaigns")
    #     return redirect(url_for('campaign', campaign=data))




# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9112)) 
    #                                 ^^^^
    #              You can replace this number with any valid port
    
    app.run(port=port, debug=True)
