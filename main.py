from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('newuser.html')       

@app.route("/", methods=['POST'])
def verify():
    
    username = request.form['username'] 
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verification_error = ''
    email_error = ''
    error = 0

    if username == "":
        username_error = "Your username cannot be blank"
        error = 1
    elif (" " in username) == True:
        username_error = "Your username cannot contain a space"
        error = 1
    elif len(username) < 3:
        username_error = "Your username cannot contain fewer than three characters"
        error = 1
    elif len(username) > 20:
        username_error = "Your username cannot contain more than 20 characters"
        error = 1

    if password == "":
        password_error = "Your password cannot be blank"
        error = 1        
    elif (" " in password) == True:
        password_error = "Your password cannot contain a space"
        error = 1
    elif len(password) < 3:
        password_error = "Your password cannot contain fewer than three characters"
        error = 1
    elif len(password) > 20:
        password_error = "Your password cannot contain more than 20 characters"
        error = 1

    if verify == "":
        verify_error = "Your password verification cannot be blank"
        error = 1
    elif password != verify:
        verification_error = "Your passwords did not match"
        error = 1

    if email != "":
        if (" " in email) == True:
            email_error = "Your email cannot contain a space"
            error = 1    
        elif len(email) < 3:
            email_error = "Your email cannot contain fewer than three characters"
            error = 1
        elif len(email) > 20:
            email_error = "Your email cannot contain more than 20 characters"
            error = 1
        elif email.count("@") != 1:
            email_error = "Your email is not valid"
            error = 1
        elif email.count(".") != 1:
            email_error = "Your email is not valid"
            error = 1
  
    if error == 0:
        return render_template('success.html',
        username=username,
        email=email)    
    else:
        return render_template('newuser.html',
        username=username,
        email=email,
        username_error=username_error,
        password_error=password_error,
        verification_error=verification_error,
        email_error=email_error)          

app.run()
