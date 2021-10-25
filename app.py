from flask import Flask, render_template
import os

# Configuration

app = Flask(__name__)

# Data

campaigns = ["Ghosts of Saltmarsh", "Waterdeep", "Homebrew Campaign", "Curse of Strahd"]

# Routes 

@app.route('/')
def root():
    return render_template("main.j2")

@app.route('/login')
def login():
    return render_template("login.j2")

@app.route('/menu')
def menu():
    return render_template("menu.j2", campaigns=campaigns)


# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9112)) 
    #                                 ^^^^
    #              You can replace this number with any valid port
    
    app.run(port=port, debug=True)
