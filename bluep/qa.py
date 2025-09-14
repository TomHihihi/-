from flask import Blueprint, request, render_template, g, redirect, url_for, session
from exts import db
from models import UserModel, UserModelpa, changwei_liu_morModel
import pymysql
import config
from .forms import changwei_liu_Form

bp = Blueprint("qa", __name__, url_prefix="/")


# /
@bp.route("/qweguahao")
def index():
    return render_template("index.html")


@bp.route("/guahao")
def guahao():
    clms = changwei_liu_morModel.query.all()
    return render_template("guahao.html", clms=clms)


@bp.route("/searchdc")
def searchdc():
    x = request.args.get("x")
    users = UserModel.query.filter(UserModel.username.contains(x)).all()
    return render_template("guahao.html", users=users)
 

@bp.route("/search_doctor")
def search_doctor():
    e = request.args.get("e")
    users = UserModel.query.filter(UserModel.username.contains(e)).all()
    return render_template("admin_dsgl.html", users=users)


@bp.route("/doctor_main")
def doctor_main():
    return render_template("doctor_main.html", patient_users=UserModelpa.query.all())


# 挂号，先准备表的查询功能，挂号数目达到之后进行挂号选项的隐藏(none)
