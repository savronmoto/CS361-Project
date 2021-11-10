from flask import Flask, session, render_template, redirect, request

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    '''
    This will write to a file called credentials.txt.
    Username and password should be able to be parsed using .split(',')
    '''
    if request.method == "POST":
        credentials_username = request.form['username'] # uses the register.html input name="username"
        credentials_password = request.form['password'] # uses the register.html input name="password"
        credentials_filename = "credentials.txt"
        credentials_file = open(credentials_filename, "a")
        # saved as "[username], [password], " in credentials.txt
        credentials_file.write(str(credentials_username) + ', ' + str(credentials_password) + ', ')
        credentials_file.close()

    return render_template("register.html")

app.run(debug=True)
