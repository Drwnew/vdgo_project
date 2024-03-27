from init import db
from models.models import Checkbox


def add_checkbox(data):
    last_checkbox_id = 0
    if Checkbox.query.first():
        last_checkbox_id = Checkbox.query.order_by(Checkbox.id.desc()).first().id
        checkbox_id = last_checkbox_id + 1
    checkbox = Checkbox(id=checkbox_id, text=data["text"], count=data["count"], select=False)
    db.session.add(checkbox)
    db.session.commit()
    return checkbox_id


def delete_checkbox(data):
    checkbox = Checkbox.query.filter_by(id=id).first()
    if checkbox:
        db.session.delete(checkbox)
        db.session.commit()
        return "ok"
    return "error"

def update_checkbox(data):
    checkbox = Checkbox.query.filter_by(id=data["id"]).first()
    if checkbox:
        checkbox.text = data['text']
        checkbox.count = data['count']
        checkbox.select = data['select']
        db.session.commit()
        return "ok"
    return "error"