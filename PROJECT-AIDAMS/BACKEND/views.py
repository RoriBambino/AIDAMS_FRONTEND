from flask import Blueprint, render_template, request, redirect, session, url_for, jsonify, abort, send_file
import psycopg2
from psycopg2 import extras, Binary
from configparser import ConfigParser
from datetime import date
import os
from io import BytesIO
from functools import wraps

views = Blueprint('views', __name__)
# Configuration
config = ConfigParser()

# Read the config.ini file
config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
config.read(config_path)

#database connection
conn = psycopg2.connect(
    host=config.get('conn', 'host'),
    port=config.get('conn', 'port'),
    database=config.get('conn', 'database'),
    user=config.get('conn', 'user'),
    password=config.get('conn', 'password')
)

'''
==============================
     Decorator to check if the user is logged in or is admin
==============================
'''

def login_required(f):
    @wraps(f)
    def wrapped_view(*args, **kwargs):
        # Check if the user is logged in
        if not session.get('acc_id'):
            return redirect('/')
        # Call the original route function
        return f(*args, **kwargs)
    return wrapped_view

def admin_required(f):
    @wraps(f)
    def wrapped_admin(*args, **kwargs):
        # Check if the user is logged in
        if not session.get('acc_id'):
            return redirect('/')

        is_admin = True if session.get('acc_type') == 'ADMIN' else False
        # Check if the user is an admin
        if not is_admin:
            return "<h1><strong>Forbidden Access</strong></h1>"
        # Call the original route function
        return f(*args, **kwargs)
    return wrapped_admin

'''
==============================
     Index page part
==============================
'''
@views.route('/')
def index():
    return render_template('index.htm')

@views.route('/service')
def service():
    return render_template('services.htm')

@views.route('/contact')
def contact():
    return render_template('contact.htm')


'''
==============================
        User Sign up
==============================
'''

@views.route('/signup/confirmation')
def confirmation():
    return render_template('confirmation.htm')

@views.route('/signup/user_verified')
def user_verified():
    return render_template('user_verified.htm')

'''
==============================
        Dashboard 
==============================
'''
@views.route('/dashboard')
def dashboard():
    if request.method == "GET":
        all_device = None
        cur = conn.cursor(cursor_factory=extras.RealDictCursor)
        cur.execute("SELECT * FROM DEVICE WHERE acc_id ='"+str(session['acc_id'])+"';")
        rows = cur.fetchall()
        cur.close()
        if (rows):
            all_device = rows
   
        return render_template('dashboard.htm', devices = all_device)

# Parameters sa URL
@views.route('/dashboard_btn/<int:dv_id>/<dv_status>', methods = ['GET', 'POST'])
def dashboard_btn_lock(dv_status, dv_id):
    if request.method == "POST":
        dv_status = True  if dv_status == 'False' else False
     
        cur = conn.cursor(cursor_factory=extras.RealDictCursor)
        print('asdlkjasdk')
        cur.execute("UPDATE DEVICE SET dv_status = "+str(dv_status)+" WHERE dv_id = "+str(dv_id)+"; ")
        conn.commit()
        cur.close()
        response_data = {"message": "Success"}
        return jsonify(response_data), 200
       
    
@views.route('/add_device')
def add_device():
    return render_template('add_device.htm')

@views.route('/members')
def members():
    return render_template('members.htm')

@views.route('/members/add_members')
def add_members():
    return render_template('add_members.htm')

@views.route('/monitor')
def monitor():
    return render_template('monitor.htm')

@views.route('/notification')
def notification():
    return render_template('notification.htm')

@views.route('/account')
def account():
    return render_template('account.htm')

'''
==============================
        User Settings
==============================
'''
@views.route('/settings')
def settings():
    return render_template('settings.htm')

@views.route('/settings/auto_lock')
def auto_lock():
    return render_template('auto_lock.htm')

@views.route('/settings/auto_lock/adjust_time')
def auto_lock_edit():
    return render_template('auto_lock_edit.htm')

@views.route('/settings/curfew_mode')
def curfew_lock():
    return render_template('curfew_lock.htm')

@views.route('/settings/curfew mode/adjust_time')
def curfew_lock_edit():
    return render_template('curfew_lock_edit.htm')

@views.route('/information/alert/door')
def door_alarm():
    return render_template('door_alarm.htm')

'''
==============================
        Admin Page
==============================
'''

@views.route('/dashboard_admin')
def dashboard_admin():
    return render_template('admin_dashboard.htm')

@views.route('/dashboard_admin/users')
def admin_users():
    return render_template('admin_users.htm')

@views.route('/dashboard_admin/users/edit')
def edit_users():
    return render_template('edit_admin_users.htm')

@views.route('/dashboard_admin/device')
def admin_device():
    return render_template('admin_device.htm')

@views.route('/dashboard_admin/device/edit')
def edit_devices():
    return render_template('edit_admin_devices.htm')

@views.route('/dashboard_admin/settings')
def admin_settings():
    return render_template('admin_settings.htm')

'''
==============================
        Error Page
==============================
'''
@views.route('/page-not-found')
def error_404():
    return render_template('404.htm')

