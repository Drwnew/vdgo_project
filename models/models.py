from sqlalchemy import ForeignKey, Integer, Column
from init import db


class Area_Checkbox(db.Model):
    id = Column(Integer(), primary_key=True)
    area_id = Column(Integer(), ForeignKey('areas.id'))
    checkbox_id = Column(Integer(), ForeignKey('checkboxes.id'))

# area_checkbox = Table('area_checkbox', db.metadata,
#     Column('area_id', Integer(), ForeignKey('area.id')),
#     Column('checkbox_id', Integer(), ForeignKey('checkbox.id)'))
#
# )

class Area(db.Model):
    __tablename__ = 'areas'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(200),  nullable=False)
    # shifts = db.relationship('Shift', backref='Area')
    checkboxes = db.relationship('Area_Checkbox', backref='area')
    next = db.Column(db.Integer())

    @property
    def get_obj(self):
        return {"id": self.id, "name": self.name}


# class Shift(db.Model):
#     id = db.Column(db.Date(), primary_key=True)
#     worker_id = db.relationship('Worker', backref='Shift')
#     area_id = db.Column(db.Integer(), db.ForeignKey('area.id'), nullable=False)
#     accepted = db.Column(db.Boolean(), nullable=False)
#
#
# class Worker(db.Model):
#     id = db.Column(db.Integer(), primary_key=True, nullable=False)


class Checkbox(db.Model):
    __tablename__ = 'checkboxes'
    id = db.Column(db.Integer(), primary_key=True, nullable=False)
    text = db.Column(db.String(200), nullable=False)
    count = db.Column(db.Boolean(), nullable=False)
    select = db.Column(db.Boolean(), nullable=False)
    areas = db.relationship('Area_Checkbox', backref='checkbox')

    @property
    def get_obj(self):
        return {"id": self.id, "text": self.text, "count": self.count, "select": self.select}
