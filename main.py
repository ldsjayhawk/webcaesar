from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/form" method="post"/>
            <label>Rotate by:
                <input name="rot" type="text" value="0"/>
            </label>
            <textarea name="text">{0}</textarea>
            <input type="submit">
            </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format(...)

@app.route("/hello", methods=['POST'])
def hello():
    first_name = request.form['first_name']
    return '<h1>Hello, ' + first_name + '</h1>'

@app.route("/form", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    #integer = int(request.form['variable_from_form'])
    text = request.form['text']
    letter2 = ""
    for letter in text:
        new_letter = rotate_string(letter, rot)
        letter2 = letter2 + new_letter
    #return '<h1> ' + letter2 + '</h1>'
    return form.format(letter2)
app.run()