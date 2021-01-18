from flask import Flask
import os
from config import Config
application=Flask(__name__,static_folder='static')
# application.config['SECRET_KEY']='secret'

APP_ROOT=os.path.dirname(os.path.abspath(__file__))

# application = Flask(__name__)
application.config.from_object(Config)

from app import routes
