from flask import Flask
from flask_bootstrap import Bootstrap
from .config import DevConfig


#initialize application 
app = Flask (__name__, instance_relative_config=True)

#setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

#initializze bootstrap extension
bootstrap = Bootstrap(app)

from app import views
from app import error