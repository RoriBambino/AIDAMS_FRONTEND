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


# User Settings
@app.route('/settings')
def settings():
    return render_template('settings.htm')

@app.route('/settings/auto_lock')
def auto_lock():
    return render_template('auto_lock.htm')

@app.route('/settings/auto_lock/adjust time')
def auto_lock_edit():
    return render_template('auto_lock_edit.htm')

@app.route('/settings/curfew mode')
def curfew_lock():
    return render_template('curfew_lock.htm')

@app.route('/settings/curfew mode/adjust time')
def curfew_lock_edit():
    return render_template('curfew_lock_edit.htm')

@app.route('/information/alert/door')
def door_alarm():
    return render_template('door_alarm.htm')

#Admin Page
@app.route('/dashboard_admin')
def dashboard_admin():
    return render_template('admin_dashboard.htm')

@app.route('/dashboard_admin/users')
def admin_users():
    return render_template('admin_users.htm')

@app.route('/dashboard_admin/users/edit')
def edit_users():
    return render_template('edit_admin_users.htm')

@app.route('/dashboard_admin/device')
def admin_device():
    return render_template('admin_device.htm')

@app.route('/dashboard_admin/device/edit')
def edit_devices():
    return render_template('edit_admin_devices.htm')

@app.route('/dashboard_admin/settings')
def admin_settings():
    return render_template('admin_settings.htm')

@app.route('/404')
def error_404():
    return render_template('404.htm')


if __name__ == '__main__':
    app.run(debug=True)
