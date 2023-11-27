from flask import Flask, render_template

app = Flask(__name__)
#Index page part
@app.route('/')
def index():
    return render_template('index.htm')

@app.route('/service')
def service():
    return render_template('services.htm')

@app.route('/contact')
def contact():
    return render_template('contact.htm')

@app.route('/signin')
def signin():
    return render_template('sign_in.htm')

#User Signup and Verification
@app.route('/signup')
def signup():
    return render_template('signup.htm')

@app.route('/signup/confirmation')
def confirmation():
    return render_template('confirmation.htm')

@app.route('/signup/user_verified')
def user_verified():
    return render_template('user_verified.htm')

#Dashboard 
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.htm')

@app.route('/add_device')
def add_device():
    return render_template('add_device.htm')

@app.route('/members')
def members():
    return render_template('members.htm')

@app.route('/members/add_members')
def add_members():
    return render_template('add_members.htm')

@app.route('/monitor')
def monitor():
    return render_template('monitor.htm')

@app.route('/notification')
def notification():
    return render_template('notification.htm')

@app.route('/account')
def account():
    return render_template('account.htm')







if __name__ == '__main__':
    app.run(debug=True)
