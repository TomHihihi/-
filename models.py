from exts import db
from datetime import datetime


class UserModel(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    sex = db.Column(db.String(100), nullable=False)
    id_number = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    tel = db.Column(db.String(100), nullable=False)
    workid = db.Column(db.String(100), nullable=False)
    wordad = db.Column(db.String(200), nullable=False)
    sp = db.Column(db.String(200), nullable=False)
    simp = db.Column(db.String(200), nullable=False)
    join_time = db.Column(db.DateTime, default=datetime.now)


class UserModelpa(db.Model):
    __tablename__ = "patient_user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    sex = db.Column(db.String(100), nullable=False)
    id_number = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    tel = db.Column(db.String(100), nullable=False)
    re_tel = db.Column(db.String(100), nullable=False)
    nation = db.Column(db.String(200), nullable=False)
    join_time = db.Column(db.DateTime, default=datetime.now)


class LiiModel(db.Model):
    __tablename__ = "lii"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    patient = db.Column(db.String(200), nullable=False)
    genetic_lii = db.Column(db.String(200), nullable=False)
    past_lii = db.Column(db.String(200), nullable=False)
    allergy_lii = db.Column(db.String(200), nullable=False)
    e5_eye = db.Column(db.String(200), nullable=False)
    e5_nose = db.Column(db.String(200), nullable=False)
    e5_ear = db.Column(db.String(200), nullable=False)
    e5_lip = db.Column(db.String(200), nullable=False)
    e5_tongue = db.Column(db.String(200), nullable=False)
    hair = db.Column(db.String(200), nullable=False)
    face = db.Column(db.String(200), nullable=False)
    limb = db.Column(db.String(200), nullable=False)
    skin = db.Column(db.String(200), nullable=False)
    lii_site = db.Column(db.String(200), nullable=False)
    mentality = db.Column(db.String(200), nullable=False)
    etiology = db.Column(db.String(200), nullable=False)
    doctor = db.Column(db.String(200), nullable=False)
    join_time = db.Column(db.DateTime, default=datetime.now)


class MedModel(db.Model):
    __tablename__ = "med"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    patient = db.Column(db.String(200), nullable=False)
    treatment = db.Column(db.String(200), nullable=False)
    treatment_time = db.Column(db.String(200), nullable=False)
    fllow_treatment = db.Column(db.String(200), nullable=False)
    cost = db.Column(db.String(200), nullable=False)
    doctor = db.Column(db.String(200), nullable=False)
    join_time = db.Column(db.DateTime, default=datetime.now)


class AdminModel(db.Model):
    __tablename__ = "adm"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    join_time = db.Column(db.DateTime, default=datetime.now)


class LfModel(db.Model):
    __tablename__ = "lf"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    lfname = db.Column(db.String(100), nullable=False)
    lfjj = db.Column(db.String(1000), nullable=False)


# class GuahaoModel(db.Model):
#     __tablename__ = "adm"
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     doctor = db.Column(db.String(100), nullable=False)
#     username = db.Column(db.String(100), nullable=False)
#     password = db.Column(db.String(200), nullable=False)
#     join_time = db.Column(db.DateTime, default=datetime.now)


class changwei_liu_morModel(db.Model):
    __tablename__ = "clm"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    patient = db.Column(db.String(200), nullable=False)
    workad = db.Column(db.String(200), default="肠胃科")
    doctor = db.Column(db.String(200), default="刘医生")
    jl = db.Column(db.String(200), default="特级医师")
    time = db.Column(db.String(200), default="9:00——11:00")
    cost = db.Column(db.String(200), default="50")
    join_time = db.Column(db.DateTime, default=datetime.now)


class changwei_liu_aftModel(db.Model):
    __tablename__ = "cla"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    patient = db.Column(db.String(200), nullable=False)
    workad = db.Column(db.String(200), default="肠胃科")
    doctor = db.Column(db.String(200), default="刘医生")
    jl = db.Column(db.String(200), default="特级医师")
    time = db.Column(db.String(200), default="14:00——16:00")
    cost = db.Column(db.String(200), default="50")
    join_time = db.Column(db.DateTime, default=datetime.now)


class changwei_liu_eveModel(db.Model):
    __tablename__ = "cle"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    patient = db.Column(db.String(200), nullable=False)
    workad = db.Column(db.String(200), default="肠胃科")
    doctor = db.Column(db.String(200), default="刘医生")
    jl = db.Column(db.String(200), default="特级医师")
    time = db.Column(db.String(200), default="20:00——22:00")
    cost = db.Column(db.String(200), default="50")
    join_time = db.Column(db.DateTime, default=datetime.now)
