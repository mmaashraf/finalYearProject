from flask_login import UserMixin
from .__init__ import db
# from flask_sqlalchemy import SQLAlchemy
# db=SQLAlchemy()

# db = flask.ext.sqlalchemy.SQLAlchemy(app)
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


    if __name__ == '__main__':
        db.create_all()
        db.session.commit()
# db.create_all()
# db.session.commit()