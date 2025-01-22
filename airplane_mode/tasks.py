import frappe

def update_ticket_gate_numbers(flight, new_gate):
    #Update gate numbers for all tickets of a flight
    try:
        # Get all tickets for this flight
        tickets = frappe.get_all(
            "Airplane Ticket",
            filters={"flight": flight},
            fields=["name"]
        )
        
        for ticket in tickets:
            frappe.db.set_value("Airplane Ticket", ticket.name, "departure_gate", new_gate)
        
        frappe.db.commit()
        
        # Log successful update
        frappe.log_error(
            f"Successfully updated gate numbers for flight {flight}. Affected tickets: {len(tickets)}",
            "Gate Number Update"
        )
        #Send email notification to inform customer  (future )
    except Exception as e:
        frappe.log_error(
            f"Failed to update gate numbers for flight {flight}: {str(e)}",
            "Gate Number Update Error"
        )