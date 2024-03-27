import json

from flask import request, render_template

from api.area import add_area, delete_area, update_area, get_area_checkboxes
from api.area_checkbox import delete_area_checkbox, add_area_checkbox
from api.checkbox import add_checkbox, delete_checkbox, update_checkbox
from init import app, db
from models.models import Area_Checkbox, Area, Checkbox


@app.route('/api/create', methods=['POST'])
def create_instance():
    # data = request.form['name']
    data = request.get_json()
    if data["instance"] == "area":
        return add_area(data)
    elif data["instance"] == "checkbox":
        checkbox_id = add_checkbox(data)
        data = json.dumps({"area_id": int(data["area_id"]), "checkbox_id": checkbox_id})
        return add_area_checkbox(data)
    elif data["instance"] == "link":
        return add_area_checkbox(data)
    return "Invalid input"

@app.route('/api/delete', methods=['POST'])
def delete_instance():
    data = request.get_json()
    if data["instance"] == "area":
        return delete_area(data)
    elif data["instance"] == "checkbox":
        return delete_checkbox(data)
    elif data["instance"] == "link":
        return delete_area_checkbox(data)
    return "err"

@app.route('/api/update', methods=['POST'])
def update_instance():
    data = request.get_json()
    if data["instance"] == "area":
        return update_area(data)
    elif data["instance"] == "checkbox":
        return update_checkbox(data)

@app.route('/settings/create_connection', methods=['POST'])
def create_connection():
    print(request.get_json())
    data = request.get_json()
    connection = Area_Checkbox(area_id=data["area_id"], checkbox_id=data["checkbox_id"])
    db.session.add(connection)
    db.session.commit()
    return "ok"

@app.route('/api/get_area_checkboxes', methods=['POST'])
def api_get_area_checkboxes():
    data = request.get_json()
    return get_area_checkboxes(data["id"])

@app.route("/admin")
def setting_page():
    # first = Area.query.first()
    areas = Area.query.all()
    area_links = areas
    checkboxes = Checkbox.query.all()
    # area_checkboxes = []
    # for area in area_links:
    #     checkboxes = area.checkboxes.checkboxes
    #     area_checkboxes.append({area, ch})
    return render_template('admin.html', area_links=area_links, area_links_length=len(area_links),
    areas=areas, areas_length=len(areas), checkboxes=checkboxes)

if __name__ == '__main__':
  with app.app_context():
      db.create_all()
  app.run(host="0.0.0.0", debug=True, port=3000)

