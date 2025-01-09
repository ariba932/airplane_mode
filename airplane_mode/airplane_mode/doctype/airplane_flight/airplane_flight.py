# Copyright (c) 2024, MKO Tevc Concepts and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class AirplaneFlight(WebsiteGenerator):
	def validate(self):
		pass

	def before_submit(self):
		self.status="Completed"



