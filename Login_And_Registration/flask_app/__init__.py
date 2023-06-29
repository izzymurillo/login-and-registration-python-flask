import sys
sys.dont_write_bytecode = True

from flask import Flask

from flask_bcrypt import Bcrypt


app = Flask(__name__)

bcrypt = Bcrypt(app)

app.secret_key = "secret"



