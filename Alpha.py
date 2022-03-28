from flask import Flask,render_template,request,redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'KAKAROt'

@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/Signup')
def Signup():
	Form = Signupform()
	return render_template('Signup.html', title = 'Sign Up', form = form) 


@app.route('/Login')
def Login():
	Form = LoginForm()
	return render_template('Login.html', title = 'Log In', form = form)

#if __name__ == '__main__':
#	app.run(debug=True)