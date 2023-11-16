from flask import Flask, redirect, url_for, request

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def home_page():
    return ''


if __name__ == '__main__':
    app.run(debug=True)
