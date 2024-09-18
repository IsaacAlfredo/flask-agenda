from flask import Flask, request
import json
from uuid import uuid4

app = Flask(__name__)


def get_contacts_data():
    with open("data/contacts.json", "r") as file:
        contacts_data = json.load(file)
    return contacts_data


@app.route("/contacts")
def contacts():
    return get_contacts_data()


@app.route("/contact", methods=["POST"])
def create_contact():
    new_contact_data = request.json
    contacts_data = get_contacts_data()
    for cont in contacts_data:
        if cont["number"] == request.json["number"]:
            return "number already registered"
    new_contact_data["id"] = str(uuid4())
    print(new_contact_data)

    contacts_data.append(new_contact_data)
    with open("data/contacts.json", "w") as file:
        file.write(json.dumps(contacts_data, sort_keys=True, indent=2))
    return contacts_data


@app.route("/contact/<id>", methods=["GET", "DELETE"])
def contact(id):
    contacts_data = get_contacts_data()
    for cont in range(len(contacts_data)):
        if contacts_data[cont]["id"] == id:
            if request.method == "DELETE":
                contacts_data.pop(cont)
                with open("data/contacts.json", "w") as file:
                    file.write(json.dumps(contacts_data, sort_keys=True, indent=2))
                return f"{id} deleted"
            return cont
    return "id not found"
