# Copyright (c) 2024, MKO Tevc Concepts and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class AirplaneFlight(WebsiteGenerator):
	def validate(self):
		pass

	#Ensure the status is set to Completed on submission
	def before_submit(self):
		self.status="Completed"

	#Checking of the seat number changes
	def on_update(self):
		if self.has_value_changed('gate_number'):
			# Enqueue background job to update tickets
			frappe.enqueue(
				'airplane_mode.tasks.update_ticket_gate_numbers',
				flight=self.name,
				new_gate=self.gate_number
			)


