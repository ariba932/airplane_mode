# Copyright (c) 2024, MKO Tevc Concepts and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class AirplaneTicket(Document):
	def validate(self):
		#To check for duplicate 
		self.remove_duplicate_add_ons()

		#To calculate the total amount
		sum=0
		for add_on in self.add_ons:
			sum+=add_on.amount
		self.total_amount = self.flight_price+sum
  

	def remove_duplicate_add_ons(self):
		seen_items = set()
		unique_add_ons = []
		for add_on in self.add_ons:
			if add_on.item not in seen_items:
				seen_items.add(add_on.item)
				unique_add_ons.append(add_on)
				self.add_ons = unique_add_ons
	
	def before_submit(self):
		if self.status !="Boarded":
			frappe.throw("You can only submit when status is boarded")


