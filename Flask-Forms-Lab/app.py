from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "farid"
password = "123"
facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina"]


@app.route('/', methods= ["GET","POST"])  # '/' for the default page
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        name = request.form['username']
        Password = request.form['password']
       
        if name == "farid" and Password == "123":
            return render_template('home.html' , facebook_friends = facebook_friends)
        else:
            return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')



@app.route('/friends_exits/<string:name>' , methods= ["GET","POST"])
def existing_friends( name ):
    isfriend=False
    for x in facebook_friends:
        if name ==x:
            isfriend=True
    return render_template('friend_exists.html', isfriend = isfriend)

    if request.method == 'GET':
        return render_template('friends_exits.html')
    







   



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)