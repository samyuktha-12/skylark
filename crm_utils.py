import json

CRM_FILE = "crm_data.json"

def load_crm_data():
    with open(CRM_FILE, "r") as f:
        return json.load(f)

def save_crm_data(data):
    with open(CRM_FILE, "w") as f:
        json.dump(data, f, indent=2)

def get_customer_by_name(name):
    crm = load_crm_data()
    for customer in crm:
        if customer["name"].lower() == name.lower():
            return customer
    return None

def create_ticket_for_customer(name, issue):
    crm = load_crm_data()
    for customer in crm:
        if customer["name"].lower() == name.lower():
            ticket_id = f"T{len(customer['tickets']) + 1:03}"
            ticket = {
                "ticket_id": ticket_id,
                "issue": issue,
                "status": "open"
            }
            customer["tickets"].append(ticket)
            save_crm_data(crm)
            return ticket
    return None

def update_ticket_status(name, ticket_id, status):
    crm = load_crm_data()
    for customer in crm:
        if customer["name"].lower() == name.lower():
            for ticket in customer["tickets"]:
                if ticket["ticket_id"] == ticket_id:
                    ticket["status"] = status
                    save_crm_data(crm)
                    return ticket
    return None
