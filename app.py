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
        # flash('Login requested for user {}, remember_me={}'.format(
        #     form.username.data, form.remember_me.data))
        # return redirect(url_for('menu'))

        # Placeholder code until I figure out actual request to login service
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

# @app.route('/login')
# def login():
#     return render_template("login.j2", users = users)

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
