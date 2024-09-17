from flask import Flask, request
import json

app = Flask(__name__)


def get_contacts_data():
    with open("data/contacts.json", "r") as file:
        contacts_data = json.load(file)
    return contacts_data

@app.route("/contacts")
def contacts():
    return get_contacts_data()


@app.route("/contact", methods=["POST"])
def contact():
    new_contact_data = request.json
    contacts_data = get_contacts_data()
    for cont in contacts_data:
        if cont["email"] == request.json["email"]:
            return "email already registered"
    contacts_data.append(new_contact_data)
    with open("data/contacts.json", "w") as file:
        file.write(json.dumps(contacts_data, sort_keys=True, indent=2))
    return contacts_data
