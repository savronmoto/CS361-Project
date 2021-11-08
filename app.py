from flask import Flask, render_template, flash, redirect, url_for
import os
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

# Configuration

app = Flask(__name__)
app.config.from_pyfile('config.py')  


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

# Form Class

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

# Routes 

@app.route('/', methods=['GET', 'POST'])
def root():
    form = LoginForm()
    if form.validate_on_submit():
    
        # Placeholder code until I figure out actual request to login service
        # Will be something like:
        # credentials = form.username.data + ":" + form.password.data
        # request_file = open("request.txt", 'w+')
        # request_file.write(credentials)
        # response_file = open("response.txt", 'r+')
        # response_file.truncate(0)
        # valid = response_file.read()
        # if valid:
        #   credentials were correct, go to menu
        # else:
        #   credentials were incorrenct, flash error and reload main page
        for dic in users:

            if dic["username"] == form.username.data:
                if dic["password"] == form.password.data:
                    return redirect(url_for('menu'))
                else:
                    flash('Invalid password')
                    return redirect(url_for('root'))

            else:
                flash('Invalid username')
                return redirect(url_for('root'))        

    return render_template('main.j2', title='Sign In', form=form)


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
