from flask import Flask, request, jsonify
from crm_utils import get_customer_by_name, create_ticket_for_customer, update_ticket_status

app = Flask(__name__)

@app.route("/crm/get_customer", methods=["POST"])
def get_customer():
    name = request.json.get("name")
    customer = get_customer_by_name(name)
    return jsonify(customer if customer else {"error": "Customer not found"}), 200

@app.route("/crm/create_ticket", methods=["POST"])
def create_ticket():
    name = request.json.get("name")
    issue = request.json.get("issue")
    ticket = create_ticket_for_customer(name, issue)
    return jsonify(ticket if ticket else {"error": "Ticket creation failed"}), 200

@app.route("/crm/update_ticket", methods=["POST"])
def update_ticket():
    name = request.json.get("name")
    ticket_id = request.json.get("ticket_id")
    status = request.json.get("status")
    ticket = update_ticket_status(name, ticket_id, status)
    return jsonify(ticket if ticket else {"error": "Ticket update failed"}), 200

if __name__ == "__main__":
    app.run(debug=True, port=5002)
