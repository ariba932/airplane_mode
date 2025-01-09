import random
import frappe
from frappe.model.docstatus import DocStatus

def execute():
	airplane_tickets = frappe.db.sql("select name from `tabAirplane Ticket` where seat is null", pluck="name")
	#airplane_tickets = frappe.db.get_list("Airplane Ticket", pluck='name', filters={"seat":DocStatus.draft()})
	for t in airplane_tickets:
		ticket = frappe.get_doc("Airplane Ticket",t)
		ticket.set_seat()
		ticket.save()
        
	frappe.db.commit()






