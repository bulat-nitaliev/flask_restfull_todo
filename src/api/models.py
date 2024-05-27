from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()


# class Todo(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     task = db.Column(db.String(255))
#     is_done = db.Column(db.Boolean())

#     def __init__(self, task, is_done):
#         self.task = task
#         self.is_done = is_done

#     def __repr__(self):
#         return '<TODO %r>' % self.task

class Todo(db.Model):
    __tablename__ = "todos"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime())
    updated_at = db.Column(db.DateTime())

    # def __init__(self, title, description, created_at):
    #     self.title = title
    #     self.description = description

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
