from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from jobseek.models import employer

# wtforms registration class
class registerForm(FlaskForm):
    companyName = StringField('Company Name', validators=[DataRequired(), Length(min=3, max=20)])
    companyEmail = StringField('Company Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Register')

    # custom validation checking if a user has already signed up with company name and email
    def validate_companyName(self, companyName):
        emp = employer.query.filter_by(companyName=companyName.data).first()
        if emp:
            raise ValidationError('Company already exists on Jobseek. Please login')

    def validate_Email(self, email):
        emp = employer.query.filter_by(email=companyEmail.data).first()
        if emp:
            raise ValidationError('Email already exists on Jobseek. Please use an alternate email')

# wtforms login class
class loginForm(FlaskForm):
    companyName = StringField('Company Name', validators=[DataRequired(), Length(min=3, max=20)])
    companyEmail = StringField('Company Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Login')

# wtforms create a job class
class jobForm(FlaskForm):
    title = StringField('Job Title', validators=[DataRequired(), Length(min=5, max=30)])
    sector = StringField('Sector', validators=[DataRequired(), Length(min=5, max=30)])
    jobType = SelectField('Type', choices=[('Full-time','Full-time' ), ('Part-time', 'Part-time'), ('Contract', 'Contract')])
    location = StringField('Location eg London, UK', validators=[DataRequired(), Length(min=5, max=60)])
    salary = IntegerField('Salary', validators=[DataRequired()])
    summary = TextAreaField('Role Summary', validators=[DataRequired(), Length(min=100, max=300)])
    responsibilities = TextAreaField('Skills/Responsibilities', validators=[DataRequired(), Length(min=100, max=400)])
    requirements = TextAreaField('Requirements', validators=[DataRequired(), Length(min=100, max=400)])
    how_to_apply = TextAreaField('How to Apply', validators=[DataRequired(), Length(min=20, max=200)])
    submit = SubmitField('Create Job!')