from flask import Flask, request
import config
from exts import db
from flask_migrate import Migrate


app = Flask(__name__)


db.init_app(app)


if __name__ == "__main__":
    app.run()
