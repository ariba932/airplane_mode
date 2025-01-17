# Copyright (c) 2025, MKO Tevc Concepts and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class CrewFlightRegister(Document):
	def validate(self):
		pass

	def before_submit(self):
		self.allocation_status="Completed"