# Copyright (c) 2025, MKO Tevc Concepts and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.website.utils import cleanup_page_name


class Shop(WebsiteGenerator):
	def validate(self):
		if not self.route:
			self.route = f"shops/{cleanup_page_name(self.name)}"
