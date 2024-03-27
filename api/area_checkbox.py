from init import db
from models.models import Area_Checkbox


def delete_area_checkbox(data):
    area_checkbox = Area_Checkbox.query.filter_by(area_id=data["area_id"]).filter_by(checkbox_id=data["checkbox_id"]).first()
    db.session.delete(area_checkbox)
    db.session.commit()
    return "ok"


def add_area_checkbox(data):
    #Не работает
    last_area = 0
    if Area_Checkbox.query.first():
        last_area = int(Area_Checkbox.query.order_by(Area_Checkbox.id.desc()).first().id) + 1
    area_checkbox = Area_Checkbox(id=last_area, area_id=data["area_id"], checkbox_id=data["checkbox_id"])
    db.session.add(area_checkbox)
    db.session.commit()
    return "ok"

