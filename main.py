from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
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
    <body>
    <form action= "/" method="POST">
            <label>Rotate by:
                <input name="rot" type="text"  value="0"/>
             </label>
             <br>
             <label>
                <textarea name="text"></textarea>
             </label>
             <br>
             <label>
                    <input type="submit" value="Submit Query" />
             </label>
        </method>
     </form>
    </body>
</html>
"""

#handler for the encrypted text
@app.route("/", methods=['POST'])
def encrypt():
    text_to_encrypt = request.form['text']
    rotation = int(request.form['rot'])
    encrypted_text = "<h1>" + rotate_string(text_to_encrypt,rotation) + "<h1>"
#    content = form.format(encrypted_text)
    return encrypted_text

#initial webpage
@app.route("/")
def index():
    empty = " "
    return form
    
app.run()