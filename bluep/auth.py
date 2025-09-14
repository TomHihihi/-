from flask import (
    Blueprint,
    render_template,
    request,
    jsonify,
    redirect,
    url_for,
    session,
    jsonify,
    g,
)
from exts import db
import string
from .forms import (
    RegisterForm,
    LoginForm,
    RegisterFormpa,
    LoginFormpa,
    LiiForm,
    MedForm,
    Adm_registerForm,
    Adm_loginForm,
    changwei_liu_Form,
    LfForm,
    MedForm_chaxun,
    LiiModel_chaxun,
)
from models import (
    UserModel,
    UserModelpa,
    LiiModel,
    MedModel,
    AdminModel,
    changwei_liu_morModel,
    changwei_liu_aftModel,
    changwei_liu_eveModel,
    LfModel,
)
from werkzeug.security import generate_password_hash, check_password_hash


bp = Blueprint("auth", __name__, url_prefix="/auth")


# /auth
@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("shili.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            username = form.username.data
            password = form.password.data
            user = UserModel.query.filter_by(username=username).first()
            if not user:
                print("用户不存在")
                return redirect(url_for("auth.shili"))
            if check_password_hash(user.password, password):
                session["user_id"] = user.id
                return redirect(url_for("auth.doctor_success"))
            else:
                print("密码错误！")
                return redirect(url_for("auth.shili"))
        else:
            print(form.errors)
            return redirect(url_for("auth.shili"))


# GET从服务器上获取数据
# POST：将客户端的数据提交给服务器
@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        form = RegisterForm(request.form)
        if form.validate():
            username = form.username.data
            password = form.password.data
            sex = form.sex.data
            id_number = form.id_number.data
            address = form.address.data
            tel = form.tel.data
            workid = form.workid.data
            wordad = form.wordad.data
            sp = form.sp.data
            simp = form.simp.data
            user = UserModel(
                username=username,
                password=generate_password_hash(password),
                sex=sex,
                id_number=id_number,
                address=address,
                tel=tel,
                workid=workid,
                wordad=wordad,
                sp=sp,
                simp=simp,
            )
            # with app.app_context():
            db.create_all()
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("auth.doctor_success"))
        # "/auth/login"
        else:
            print(form.errors)
            return redirect(url_for("auth.register"))


@bp.route("/patient_register", methods=["GET", "POST"])
def patient_register():
    if request.method == "GET":
        return render_template("patient_register.html")
    else:
        form = RegisterFormpa(request.form)
        if form.validate():
            username = form.username.data
            password = form.password.data
            sex = form.sex.data
            id_number = form.id_number.data
            address = form.address.data
            tel = form.tel.data
            re_tel = form.re_tel.data
            nation = form.nation.data
            patient_user = UserModelpa(
                username=username,
                password=generate_password_hash(password),
                sex=sex,
                id_number=id_number,
                address=address,
                tel=tel,
                re_tel=re_tel,
                nation=nation,
            )
            # with app.app_context():
            db.create_all()
            db.session.add(patient_user)
            db.session.commit()
            return redirect(url_for("auth.shili"))
        else:
            print(form.errors)
            return redirect(url_for("auth.patient_register"))


@bp.route("/patient_login", methods=["GET", "POST"])
def patient_login():
    if request.method == "GET":
        return render_template("patient_login.html")
    else:
        form = LoginFormpa(request.form)
        if form.validate():
            username = form.username.data
            password = form.password.data
            patient_user = UserModelpa.query.filter_by(username=username).first()
            if not patient_user:
                print("用户不存在")
                return redirect(url_for("auth.shili"))
            if check_password_hash(patient_user.password, password):
                session["user_id"] = patient_user.id
                return redirect(url_for("qa.guahao"))
            else:
                print("密码错误！")
                return redirect(url_for("auth.shili"))
        else:
            print(form.errors)
            return redirect(url_for("auth.shili"))


@bp.route("/doctor_nav_hzgl")
def doctor_nav_hzgl():
    return render_template(
        "doctor_nav_hzgl.html", patient_users=UserModelpa.query.all()
    )


@bp.route("/doctor_nav_bzfx", methods=["GET", "POST"])
def doctor_nav_bzfx():
    if request.method == "GET":
        return render_template("doctor_nav_bzfx.html")
    else:
        form = LiiForm(request.form)
        if form.validate():
            patient = form.patient.data
            genetic_lii = form.genetic_lii.data
            past_lii = form.past_lii.data
            allergy_lii = form.allergy_lii.data
            e5_eye = form.e5_eye.data
            e5_nose = form.e5_nose.data
            e5_ear = form.e5_ear.data
            e5_lip = form.e5_lip.data
            e5_tongue = form.e5_tongue.data
            hair = form.hair.data
            face = form.face.data
            limb = form.limb.data
            skin = form.skin.data
            lii_site = form.lii_site.data
            mentality = form.mentality.data
            etiology = form.etiology.data
            doctor = form.doctor.data
            lii = LiiModel(
                patient=patient,
                genetic_lii=genetic_lii,
                past_lii=past_lii,
                allergy_lii=allergy_lii,
                e5_eye=e5_eye,
                e5_nose=e5_nose,
                e5_ear=e5_ear,
                e5_lip=e5_lip,
                e5_tongue=e5_tongue,
                hair=hair,
                face=face,
                limb=limb,
                skin=skin,
                lii_site=lii_site,
                mentality=mentality,
                etiology=etiology,
                doctor=doctor,
            )
            # with app.app_context():
            db.create_all()
            db.session.add(lii)
            db.session.commit()
            return redirect(url_for("auth.doctor_nav_dzkf"))
        else:
            print(form.errors)
            return redirect(url_for("auth.doctor_nav_bzfx"))


@bp.route("/doctor_nav_dzkf", methods=['GET', 'POST'])
def doctor_nav_dzkf():
    if request.method == "GET":
        return render_template("doctor_nav_dzkf.html")
    else:
        form = MedForm(request.form)
        if form.validate():
            patient = form.patient.data
            treatment = form.treatment.data
            treatment_time = form.treatment_time.data
            fllow_treatment = form.fllow_treatment.data
            cost = form.cost.data
            doctor = form.doctor.data
            med = MedModel(
                patient=patient,
                treatment=treatment,
                treatment_time=treatment_time,
                fllow_treatment=fllow_treatment,
                cost=cost,
                doctor=doctor,
            )
            # with app.app_context():
            db.create_all()
            db.session.add(med)
            db.session.commit()
            return redirect(url_for("auth.doctor_nav_hzgl"))
        else:
            print(form.errors)
            return redirect(url_for("auth.doctor_nav_dzkf"))


@bp.route("/search")
def search():
    q = request.args.get("q")
    patient_users = UserModelpa.query.filter(UserModelpa.username.contains(q)).all()
    return render_template("doctor_nav_hzgl.html", patient_users=patient_users)


@bp.route("/search_ad")
def search_ad():
    w = request.args.get("w")
    patient_users = UserModelpa.query.filter(UserModelpa.username.contains(w)).all()
    return render_template("admin_hzgl.html", patient_users=patient_users)


@bp.route("/admin_register", methods=["GET", "POST"])
def admin_register():
    if request.method == "GET":
        return render_template("admin_register.html")
    else:
        form = Adm_registerForm(request.form)
        if form.validate():
            username = form.username.data
            password = form.password.data
            adm = AdminModel(
                username=username,
                password=generate_password_hash(password),
            )
            # with app.app_context():
            db.create_all()
            db.session.add(adm)
            db.session.commit()
            return redirect(url_for("auth.shili"))
        # "/auth/login"
        else:
            print(form.errors)
            return redirect(url_for("auth.shili"))


@bp.route("/doctor_success")
def doctor_success():
    return render_template("doctor_success.html")


@bp.route("/shili")
def shili():
    return render_template("shili.html")


# @bp.route("/yuyue", methods=["GET", "POST"])
# def yuyue():
#     return render_template("预约.html")


@bp.route("/admin_login", methods=["GET", "POST"])
def admin_login():
    if request.method == "GET":
        return render_template("shili.html")
    else:
        form = Adm_loginForm(request.form)
        if form.validate():
            username = form.username.data
            password = form.password.data
            adm = AdminModel.query.filter_by(username=username).first()
            if not adm:
                print("用户不存在")
                return redirect(url_for("auth.shili"))
            if check_password_hash(adm.password, password):
                session["user_id"] = adm.id
                return redirect(url_for("auth.admin_success"))
            else:
                print("密码错误！")
                return redirect(url_for("auth.shili"))
        else:
            print(form.errors)
            return redirect(url_for("auth.shili"))


@bp.route("/admin_success", methods=["GET", "POST"])
def admin_success():
    return render_template("admin_success.html")


@bp.route("/admin_hzgl")
def admin_hzgl():
    patients = UserModelpa.query.all()
    return render_template("admin_hzgl.html", patients=patients)


@bp.route("/admin_dsgl")
def admin_dsgl():
    doctors = UserModel.query.all()
    asds = UserModelpa.query.all()
    return render_template("admin_dsgl.html", doctors=doctors, asds=asds)


@bp.route("/admin_yaofanggl")
def admin_yaofanggl():
    yaofangs = MedModel.query.all()
    return render_template("admin_yaofanggl.html", yaofangs=yaofangs)


@bp.route("/admin_login1", methods=["GET", "POST"])
def admin_login1():
    if request.method == "GET":
        return render_template("shili.html")
    else:
        form = Adm_loginForm(request.form)
        if form.validate():
            username = form.username.data
            password = form.password.data
            adm = AdminModel.query.filter_by(username=username).first()
            if not adm:
                print("用户不存在")
                return redirect(url_for("auth.shili"))
            if check_password_hash(adm.password, password):
                session["user_id"] = adm.id
                return redirect(url_for("auth.admin_success"))
            else:
                print("密码错误！")
                return redirect(url_for("auth.shili"))
        else:
            print(form.errors)
            return redirect(url_for("auth.shili"))


@bp.route("/admin_guahao")
def admin_guahao():
    clms = changwei_liu_morModel.query.all()
    return render_template("admin_guahao.html", clms=clms)


@bp.route("/del", methods=["GET", "POST"])
def delete():
    form = changwei_liu_Form(request.form)
    if form.validate():
        patient = form.patient.data
        clm = changwei_liu_morModel.query.filter_by(patient=patient).first()
        db.session.delete(clm)
        db.session.commit()
        return redirect(url_for("auth.admin_success"))
    else:
        print(form.errors)
    return redirect(url_for("auth.admin_success"))


@bp.route("/seacher_patient_dzkfdao")
def seacher_patient_dzkfdao():
    m = request.args.get("m")
    meds = MedModel.query.filter(MedModel.patient.contains(m)).all()
    return render_template("patient_dzkfdao.html", meds=meds)


@bp.route("/patient_dzkfdao", methods=["GET", "POST"])
def patient_dzkfdao():
    form = MedForm_chaxun(request.form)
    if form.validate():
        patient = form.patient.data
        meds = MedModel.query.filter_by(patient=patient).first()
        return render_template("patient_dzkfdao.html", meds=meds)


@bp.route("/seacher_patient_bzfx")
def seacher_patient_bzfx():
    l = request.args.get("l")
    liis = LiiModel.query.filter(LiiModel.patient.contains(l)).all()
    return render_template("patient_bzfx.html", liis=liis)


@bp.route("/patient_bzfx", methods=["GET", "POST"])
def patient_bzfx():
    liis = LiiModel.query.all()
    return render_template("patient_bzfx.html", liis=liis)


@bp.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@bp.route("/admin_yclfgl", methods=["GET", "POST"])
def admin_yclfgl():
    lfs = LfModel.query.all()
    return render_template("admin_yclfgl.html", lfs=lfs)


@bp.route("/admin_yclfgl_add", methods=["GET", "POST"])
def admin_yclfgl_add():
    if request.method == "GET":
        return render_template("admin_yclfgl_add.html")
    else:
        form = LfForm(request.form)
        if form.validate():
            lfname = form.lfname.data
            lfjj = form.lfjj.data
            lf = LfModel(
                lfname=lfname,
                lfjj=lfjj,
            )
            # with app.app_context():
            db.create_all()
            db.session.add(lf)
            db.session.commit()
            return redirect(url_for("auth.admin_success"))
        else:
            print(form.errors)
            return redirect(url_for("auth.admin_success"))


#  meds = MedModel.query.filter_by(patient="{{ patient_user.username }}").first()


# 注释注释注释注释注释注释注释注释注释注释注释注释注释注释
# 注释注释注释注释注释注释注释注释注释注释注释注释注释注释
# 注释注释注释注释注释注释注释注释注释注释注释注释注释注释
@bp.route("/doctor_nav_bzf_main", methods=["GET", "POST"])
def doctor_nav_bzf_main():
    if request.method == "GET":
        return render_template("doctor_main.html")
    else:
        form = LiiForm(request.form)
        if form.validate():
            patient = form.patient.data
            genetic_lii = form.genetic_lii.data
            past_lii = form.past_lii.data
            allergy_lii = form.allergy_lii.data
            e5_eye = form.e5_eye.data
            e5_nose = form.e5_nose.data
            e5_ear = form.e5_ear.data
            e5_lip = form.e5_lip.data
            e5_tongue = form.e5_tongue.data
            hair = form.hair.data
            face = form.face.data
            limb = form.limb.data
            skin = form.skin.data
            lii_site = form.lii_site.data
            mentality = form.mentality.data
            etiology = form.etiology.data
            doctor = form.doctor.data
            lii = LiiModel(
                patient=patient,
                genetic_lii=genetic_lii,
                past_lii=past_lii,
                allergy_lii=allergy_lii,
                e5_eye=e5_eye,
                e5_nose=e5_nose,
                e5_ear=e5_ear,
                e5_lip=e5_lip,
                e5_tongue=e5_tongue,
                hair=hair,
                face=face,
                limb=limb,
                skin=skin,
                lii_site=lii_site,
                mentality=mentality,
                etiology=etiology,
                doctor=doctor,
            )
            # with app.app_context():
            db.create_all()
            db.session.add(lii)
            db.session.commit()
            return redirect(url_for("qa.doctor_main"))
        else:
            print(form.errors)
            return redirect(url_for("qa.doctor_main"))


@bp.route("/doctor_nav_dzkf_main", methods=["GET", "POST"])
def doctor_nav_dzkf_main():
    if request.method == "GET":
        return render_template("doctor_main.html")
    else:
        form = MedForm(request.form)
        if form.validate():
            patient = form.patient.data
            treatment = form.treatment.data
            treatment_time = form.treatment_time.data
            fllow_treatment = form.fllow_treatment.data
            cost = form.cost.data
            doctor = form.doctor.data
            med = MedModel(
                patient=patient,
                treatment=treatment,
                treatment_time=treatment_time,
                fllow_treatment=fllow_treatment,
                cost=cost,
                doctor=doctor,
            )
            # with app.app_context():
            db.create_all()
            db.session.add(med)
            db.session.commit()
            return redirect(url_for("qa.doctor_main"))
        else:
            print(form.errors)
            return redirect(url_for("qa.doctor_main"))


@bp.route("/seacher_doctor_ckgh")
def seacher_doctor_ckgh():
    l = request.args.get("l")
    clms = changwei_liu_morModel.query.filter(
        changwei_liu_morModel.doctor.contains(l)
    ).all()
    return render_template("doctor_ckgh.html", clms=clms)


# 注释注释注释注释注释注释注释注释注释注释注释注释注释注释
# 注释注释注释注释注释注释注释注释注释注释注释注释注释注释
# 注释注释注释注释注释注释注释注释注释注释注释注释注释注释


@bp.route("/changwei_liu_mor", methods=["GET", "POST"])
def changwei_liu_mor():
    if request.method == "GET":
        return render_template("guahao.html")
    else:
        form = changwei_liu_Form(request.form)
        if form.validate():
            patient = form.patient.data
            clm = changwei_liu_morModel(
                patient=patient,
            )
            # with app.app_context():
            db.create_all()
            db.session.add(clm)
            db.session.commit()
            return redirect(url_for("auth.patient_bzfx"))
        # "/auth/login"
        else:
            print(form.errors)
            return redirect(url_for("auth.guahao"))


@bp.route("/changwei_liu_aft", methods=["GET", "POST"])
def changwei_liu_aft():
    if request.method == "GET":
        return render_template("guahao.html")
    else:
        form = changwei_liu_Form(request.form)
        if form.validate():
            patient = form.patient.data
            workad = form.workad.data
            doctor = form.doctor.data
            jl = form.jl.data
            time = form.time.data
            cost = form.tecostl.data
            cla = changwei_liu_aftModel(
                patient=patient,
                workad=workad,
                doctor=doctor,
                jl=jl,
                time=time,
                cost=cost,
            )
            # with app.app_context():
            db.create_all()
            db.session.add(cla)
            db.session.commit()
            return redirect(url_for("auth.patient_bzfx"))
        # "/auth/login"
        else:
            print(form.errors)
            return redirect(url_for("auth.guahao"))


@bp.route("/changwei_liu_eve", methods=["GET", "POST"])
def changwei_liu_eve():
    if request.method == "GET":
        return render_template("guahao.html")
    else:
        form = changwei_liu_Form(request.form)
        if form.validate():
            patient = form.patient.data
            workad = form.workad.data
            doctor = form.doctor.data
            jl = form.jl.data
            time = form.time.data
            cost = form.tecostl.data
            cla = changwei_liu_eveModel(
                patient=patient,
                workad=workad,
                doctor=doctor,
                jl=jl,
                time=time,
                cost=cost,
            )
            # with app.app_context():
            db.create_all()
            db.session.add(cla)
            db.session.commit()
            return redirect(url_for("auth.patient_bzfx"))
        # "/auth/login"
        else:
            print(form.errors)
            return redirect(url_for("auth.guahao"))
