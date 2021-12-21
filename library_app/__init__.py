from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config, MIGRATION_DIR
from .views import main
from .rest import api_main


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db, directory=MIGRATION_DIR)

app.register_blueprint(main, url_prefix='')
app.register_blueprint(api_main, url_prefix='/api')

from .models import Genre, Book
