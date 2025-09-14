import wtforms
from wtforms.validators import Length, EqualTo, DataRequired
from exts import db


# 用于验证前端提交的数据是否符合要求
class RegisterForm(wtforms.Form):
    username = wtforms.StringField(validators=[DataRequired(message="用户名格式错误")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="密码格式错误")])
    password_confirm = wtforms.StringField(
        validators=[EqualTo("password", message="两次密码不一致")]
    )
    sex = wtforms.StringField(validators=[Length(min=1, max=6, message="性别格式错误")])
    id_number = wtforms.StringField(
        validators=[Length(min=18, max=18, message="身份证号格式错误")]
    )
    address = wtforms.StringField(validators=[DataRequired(message="住址格式错误")])
    tel = wtforms.StringField(validators=[Length(min=11, max=11, message="联系电话格式错误")])
    workid = wtforms.StringField(validators=[Length(min=1, max=20, message="工号格式错误")])
    wordad = wtforms.StringField(validators=[Length(min=1, max=50, message="科室格式错误")])
    sp = wtforms.StringField(validators=[Length(min=1, max=200, message="擅长方面格式错误")])
    simp = wtforms.StringField(validators=[Length(min=1, max=200, message="简历格式错误")])


class RegisterFormpa(wtforms.Form):
    username = wtforms.StringField(validators=[DataRequired(message="用户名格式错误")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="密码格式错误")])
    password_confirm = wtforms.StringField(
        validators=[EqualTo("password", message="两次密码不一致")]
    )
    sex = wtforms.StringField(validators=[DataRequired(message="性别格式错误")])
    id_number = wtforms.StringField(
        validators=[Length(min=18, max=20, message="身份证号格式错误")]
    )
    address = wtforms.StringField(validators=[DataRequired(message="住址格式错误")])
    tel = wtforms.StringField(validators=[Length(min=11, max=11, message="个人联系电话格式错误")])
    re_tel = wtforms.StringField(
        validators=[Length(min=11, max=11, message="亲属联系电话格式错误")]
    )
    nation = wtforms.StringField(validators=[DataRequired(message="民族格式错误")])

    # 自定义验证

    # db.session.commit()


class LoginForm(wtforms.Form):
    username = wtforms.StringField(validators=[DataRequired(message="用户名格式错误")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="密码格式错误")])


class LoginFormpa(wtforms.Form):
    username = wtforms.StringField(validators=[DataRequired(message="用户名格式错误")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="密码格式错误")])


class LiiForm(wtforms.Form):
    patient = wtforms.StringField(validators=[DataRequired(message="患者姓名格式错误")])
    genetic_lii = wtforms.StringField(validators=[DataRequired(message="遗传病史格式错误")])
    past_lii = wtforms.StringField(validators=[DataRequired(message="过往病史格式错误")])
    allergy_lii = wtforms.StringField(validators=[DataRequired(message="过敏史格式错误")])
    e5_eye = wtforms.StringField(validators=[DataRequired(message="目格式错误")])
    e5_nose = wtforms.StringField(validators=[DataRequired(message="鼻格式错误")])
    e5_ear = wtforms.StringField(validators=[DataRequired(message="耳格式错误")])
    e5_lip = wtforms.StringField(validators=[DataRequired(message="唇格式错误")])
    e5_tongue = wtforms.StringField(validators=[DataRequired(message="舌格式错误")])
    hair = wtforms.StringField(validators=[DataRequired(message="毛发格式错误")])
    face = wtforms.StringField(validators=[DataRequired(message="脸色名格式错误")])
    limb = wtforms.StringField(validators=[DataRequired(message="四肢名格式错误")])
    skin = wtforms.StringField(validators=[DataRequired(message="皮肤状态名格式错误")])
    lii_site = wtforms.StringField(validators=[DataRequired(message="发病部位名格式错误")])
    mentality = wtforms.StringField(validators=[DataRequired(message="精神状态名格式错误")])
    etiology = wtforms.StringField(validators=[DataRequired(message="确定病因名格式错误")])
    doctor = wtforms.StringField(validators=[DataRequired(message="主治医师名格式错误")])


class MedForm(wtforms.Form):
    patient = wtforms.StringField(validators=[DataRequired(message="患者姓名格式错误")])
    treatment = wtforms.StringField(validators=[DataRequired(message="治疗方案格式错误")])
    treatment_time = wtforms.StringField(validators=[DataRequired(message="开处方时间格式错误")])
    fllow_treatment = wtforms.StringField(validators=[DataRequired(message="复诊时间格式错误")])
    cost = wtforms.StringField(validators=[DataRequired(message="合计费用格式错误")])
    doctor = wtforms.StringField(validators=[DataRequired(message="主任医生格式错误")])


class Adm_loginForm(wtforms.Form):
    username = wtforms.StringField(validators=[DataRequired(message="用户名格式错误")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="密码格式错误")])


class Adm_registerForm(wtforms.Form):
    username = wtforms.StringField(validators=[DataRequired(message="用户名格式错误")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="密码格式错误")])
    password_confirm = wtforms.StringField(
        validators=[EqualTo("password", message="两次密码不一致")]
    )


class LfForm(wtforms.Form):
    lfname = wtforms.StringField(validators=[DataRequired(message="疗法格式错误")])
    lfjj = wtforms.StringField(validators=[DataRequired(message="疗法简介格式错误")])


# 注释注释注释注释注释注释注释注释注释注释注释注释注释注释
# 注释注释注释注释注释注释注释注释注释注释注释注释注释注释
# 注释注释注释注释注释注释注释注释注释注释注释注释注释注释
# 注释注释注释注释注释注释注释注释注释注释注释注释注释注释
# 注释注释注释注释注释注释注释注释注释注释注释注释注释注释
# 注释注释注释注释注释注释注释注释注释注释注释注释注释注释


class changwei_liu_Form(wtforms.Form):
    patient = wtforms.StringField(validators=[DataRequired(message="用户名格式错误")])


class changwei_liu_aftModel(wtforms.Form):
    patient = wtforms.StringField(validators=[DataRequired(message="用户名格式错误")])


class changwei_liu_eveModel(wtforms.Form):
    patient = wtforms.StringField(validators=[DataRequired(message="用户名格式错误")])


class MedForm_chaxun(wtforms.Form):
    patient = wtforms.StringField(validators=[DataRequired(message="用户名格式错误")])


class LiiModel_chaxun(wtforms.Form):
    patient = wtforms.StringField(validators=[DataRequired(message="用户名格式错误")])
