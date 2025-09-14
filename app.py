from flask import Flask, render_template, session, g, redirect, url_for, request
import config
from exts import db
from models import UserModel, UserModelpa
from bluep.qa import bp as qa_bp
from bluep.auth import bp as auth_bp
from flask_migrate import Migrate
import pymysql


app = Flask(__name__)
# 绑定配置文件
app.config.from_object(config)

db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(qa_bp)
app.register_blueprint(auth_bp)


# @app.route("/")
# def hello():
#     return render_template("doctor_main.html")


@app.route("/")
def hello():
    return render_template("shili.html")


@app.before_request
def my_before_request():
    user_id = session.get("user_id")
    if user_id:
        user = UserModel.query.get(user_id)
        setattr(g, "user", user)
    else:
        setattr(g, "user", None)


@app.context_processor
def my_context_processor():
    return {"user": g.user}


@app.before_request
def my_before_request_patient():
    user_id = session.get("user_id")
    if user_id:
        patient_user = UserModelpa.query.get(user_id)
        setattr(g, "patient_user", patient_user)
    else:
        setattr(g, "patient_user", None)


@app.context_processor
def my_context_processor_patient():
    return {"patient_user": g.patient_user}


# conn = pymysql.connect(**config)


# @app.route("/guahaomod")
# def guahaomod():
#     cursor = conn.cursor()
#     query = "SELECT COUNT(*) FROM user"
#     cursor.execute(query)

#     result = cursor.fetchone()

#     return f"Row count: {result[0]}"


if __name__ == "__main__":
    app.run(debug=True, host=("0.0.0.0"))
