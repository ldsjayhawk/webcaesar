from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True


def form_input():
    
form = """     
<!doctype html>
<html>
    <head>
        <style>
            form {
                background-color:#eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px;
                border-radius: 10px;
            }
            textarea{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="/form" method="post" >
        <label>Rotate by:
            <input name="rot" type="text" value="0"/>
        </label>
        <textarea name="text"></textarea>
        <input type="submit">
        </form>
    </body>
</html>
"""

@app.route("/encrypt", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    letter2 = ""
    for letter in text:
        new_letter = rotate_string(letter, rot)
        letter2 = letter2 + new_letter
    return letter2

@app.route("/form")
def index():
    return form

app.run()