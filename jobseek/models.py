from jobseek import db, login_manager
from datetime import datetime
from flask_login import UserMixin

# using flask login manager to find user in db
@login_manager.user_loader
def user_loader(user_id):
    return employer.query.get(user_id)

# create employer user db model 
class employer(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    companyName = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(50), nullable=False, default='default.jpg')
    job_posts = db.relationship('job_post', backref='author', lazy=True)
    # string to return in shell when employer model called
    def __repr__(self):
        return f"User: {self.companyName}"

# create job_post db model
class job_post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(60), nullable=False)
    jobType = db.Column(db.String(40), nullable=False)
    location = db.Column(db.String(60), nullable=False)
    role_sum = db.Column(db.Text, nullable=False)
    resp = db.Column(db.Text, nullable=False)
    requirements = db.Column(db.Text, nullable=False)
    how_to_apply = db.Column(db.Text, nullable=False)
    emp_id = db.Column(db.Integer, db.ForeignKey('employer.id'), nullable=False )
    sector_id = db.Column(db.Integer, db.ForeignKey('sector.id'), nullable=False )
    # string to return in shell when job_post model called
    def __repr__(self):
        return f"Job Post: {self.date_posted}, {self.title}"

class sector(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sector = db.Column(db.String(60), nullable=False)
    def __repr__(self):
        return f"Sector: {self.id}, {self.sector}"

