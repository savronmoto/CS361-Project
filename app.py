from flask import Flask, render_template, flash, redirect, url_for
import os
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
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

npcs = [
    {
        "name": "Reaner Neverember",
        "desc": "Some noble guy."
    },
    {
        "name": "Volothamp Geddarm",
        "desc": "Sent us on the job, paid us with a house."
    },
    {
        "name": "Durnan",
        "desc": "Owner of the Yawning Portal."
    },
    {
        "name": "Yagra Stonefist",
        "desc": "Orc lady, member of the Doom Raiders, a subset of the Zentharum faction."
    }
]

locations = [
    {
        "name": "Old Xoblob's Shop",
        "desc": "A shop where everything inside is purple. Across the street from the Skewered Dragon on Net St & Flay Ln."
    },
    {
        "name": "The Yawning Portal",
        "desc": "Famous tavern in Waterdeep known for drawing adventurers. There is a giant hole that leads to Undermount."
    },
    {
        "name": "Sewer Throne Room",
        "desc": "Where we ended up after searching the sewers. Seems like goblins lived here."
    }
]

notes = [
    "Xoblob told me my cloak had a 'special property involving water?'",
    "Za-ev is charmed for 4 more hours",
    "Lost my shoes when Hugh threw me over the wall.",
    "City Guards = walls, City Watch = everywhere",
    "Rainer's father embezzled $500,000 to Neverwinter?"
]


# Form Class

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class NpcAddForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    desc = TextAreaField('Description', render_kw={"rows": 10, "cols": 40}, validators=[DataRequired()])
    submit = SubmitField('Submit')

class LocationAddForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    desc = TextAreaField('Description', render_kw={"rows": 10, "cols": 40}, validators=[DataRequired()])
    submit = SubmitField('Submit')    

class NotesAddForm(FlaskForm):
    desc = TextAreaField('Description', render_kw={"rows": 10, "cols": 40}, validators=[DataRequired()])
    submit = SubmitField('Submit')

# Routes 

@app.route('/', methods=['GET', 'POST'])
def root():
    form = LoginForm()
    if form.validate_on_submit():
        # Open the pipe file
        credentials_file = open("CS361-David-Service/credentials.txt", 'r+')
        # Parse the text into a string, and then into a list
        cred_string = credentials_file.read()
        cred_list = cred_string.split(", ")
        # Iterate over credentials
        # Allow access for correct credentials, otherwise flash incorrect portion
        for i in range(len(cred_list) - 1):
            if cred_list[i] == form.username.data:
                if cred_list[i+1] == form.password.data:
                    return redirect(url_for('menu'))
                else:
                    flash('Invalid password')
                    return redirect(url_for('root'))
            
        credentials_file.close()

        flash('Invalid username')
        return redirect(url_for('root'))

    return render_template('main.j2', title='Sign In', form=form)


@app.route('/menu/<campaign>', methods=['GET', 'POST'])
def campaignView(campaign):
    return render_template("defaultView.j2", campaign=campaign)

@app.route('/menu')
def menu():
    return render_template("menu.j2", campaigns=campaigns)

@app.route('/menu/<campaign>/NPCs', methods=['GET', 'POST'])
def npcView(campaign):
    form = NpcAddForm()
    if form.validate_on_submit():
        npcs.append({   "name" : form.name.data,
                        "desc" : form.desc.data}) 
        return redirect(url_for('npcView', campaign=campaign))

    return render_template("NPCs.j2", campaign=campaign, npcs=npcs, form=form)

@app.route('/menu/<campaign>/Locations', methods=['GET', 'POST'])
def locationView(campaign):
    form = LocationAddForm()
    if form.validate_on_submit():
        locations.append({   "name" : form.name.data,
                        "desc" : form.desc.data}) 
        return redirect(url_for('locationView', campaign=campaign))
    return render_template("locations.j2", campaign=campaign, locations=locations, form=form)

@app.route('/menu/<campaign>/Notes', methods=['GET', 'POST'])
def notesView(campaign):
    form = NotesAddForm()
    if form.validate_on_submit():
        notes.append(form.desc.data) 
        return redirect(url_for('notesView', campaign=campaign))
    return render_template("notes.j2", campaign=campaign, notes=notes, form=form)

# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9112))     
    app.run(port=port, debug=True)
