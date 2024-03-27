import json

from init import db
from models.models import Area


def create_area(name):
    """In data should be param name"""
    last_area = 0
    if Area.query.first():
        last_area = int(Area.query.order_by(Area.id.desc()).first().id) + 1
    area = Area(id=last_area, name=name)
    db.session.add(area)
    db.session.commit()
    return "ok"

def delete_area(data):
    area = Area.query.filter_by(id=data["id"]).first()
    if area:
        db.session.delete(area)
        db.session.commit()
        return "ok"
    return "error"

def update_area(data):
    area = Area.query.filter_by(id=data["id"]).first()
    if area:
        area.name = data['name']
        db.session.commit()
        return "ok"
    return "error"


def get_area_checkboxes(id):
    area = Area.query.filter_by(id=id).first()
    checkboxes = []
    for checkbox in area.checkboxes:
        checkboxes.append(checkbox.checkbox.get_obj)
    js = json.dumps({"checkboxes": checkboxes})
    return js

def get_area_links(id):
    areas = Area.query.all()
    area = Area.query.filter_by(id=id).first()
    links = []
    while True:
        links.append(area)
        next_area_id = area.next

        if next_area_id:
            area = get_area_by_id_from_list(areas, next_area_id)

        if area in links:
            break

    return links

def get_area_by_id_from_list(list, id):
    for area in list:
        if area.id == id:
            return area
    return None
