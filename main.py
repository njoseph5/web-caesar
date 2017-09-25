from flask import Flask,request
from caesar import rotate_string
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
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
            p.error{
                color : red
            }   
        </style>
    </head>
    <body>
        <form action =/encrypt method ="post">
            <label>Rotate by
                <input type = "text" name = "rot" value = "0"/>
            </label>
            <p class ="error"></p>
            <textarea type = "text" name = "text"></textarea>
            <br>
            <input type = "submit" value = "Submit Query"/>
        </form>
    </body>
</html>
"""

@app.route('/')
def index():
    return form

@app.route('/encrypt',methods=['POST'])
def encrypt():
    rot_by = int(request.form['rot'])
    text_to_encrypt= str(request.form['text'])
    encrypted = rotate_string(text_to_encrypt,rot_by)
       
    return encrypted

app.run()

