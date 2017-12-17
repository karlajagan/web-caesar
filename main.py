from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

page_header = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>

"""

#inicial form to capture the text the user gives to be encrypted
form = """
    <body>
    <form>
        <action="/encrypt" method="POST">
            <label>Rotate by:
                <input name="rot" type="text"  value="0"/>
             </label>
             <br>
             <lable>
                <textarea name="text"></textarea>
             </lable>
             <br>
             <label>
                    <input type="submit" value="Submit Query" />
             </label>
        </method>
     </form>
    </body>
</html>
"""

#displays the form with the encrypted text
encrypt = """
    <body>
    <form>
        <method="POST">
             <lable>Your encryption code is:
                <textarea name="text" value=" " ></textarea>
             </lable>
             <br>
        </method>
     </form>
    </body>
</html>
"""
#handler for the encrypted text
@app.route("/", methods=['POST'])
def encrypt():
    text_to_encrypt = request.form['text']
    rotation = request.form['rot']
    encrypted_text = rotate_string(text_to_encrypt,rotation)
    content = page_header + "<h1>" + encrypted_text + "</h1>"
    return content


@app.route("/")
def index():
    content = page_header+form
    return content

app.run()