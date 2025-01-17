# Copyright (c) 2025, MKO Tevc Concepts and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ShopPayment(Document):
	
	def before_save(self):
		if self.invoice_amount == self.paid_amount:
			payment_done = "Full payment"
		elif self.paid_amount < self.invoice_amount:
			payment_done = f"Partial payment done - "+str(self.invoice_amount - self.paid_amount)+" Outstanding"
		else:
			frappe.throw("Over Payment Done - please reaffirm")
		self.description = f"PD -"+payment_done+" for "+self.contract_no
