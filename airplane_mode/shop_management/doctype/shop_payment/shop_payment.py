# Copyright (c) 2025, MKO Tevc Concepts and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import add_months

class ShopPayment(Document):
	
	def before_save(self):
		#Check the payment amout is valid with invoice amount (rent amount) based on that update status and message
		if self.invoice_amount == self.paid_amount:
			payment_done = "Full payment"
			self.status ="Paid"
		elif self.paid_amount < self.invoice_amount:
			payment_done = f"Partial payment done - "+str(self.invoice_amount - self.paid_amount)+" Outstanding"
			self.status = "Partial"
		else:
			frappe.throw("Over Payment Done - please reaffirm")
		self.description = f"PD -"+payment_done+" for "+self.contract_no
	


	def before_submit(self):
		#This to compute the next payment due date if there is submit action.
		if self.status == "Paid":
			contract = frappe.get_doc("Shop Contract", self.contract_no)
			if contract.payment_term =='Monthly':
				next_due_date = add_months(contract.payment_due_date, 1)
			elif contract.payment_term == 'Quarterly':
				next_due_date = add_months(contract.payment_due_date, 3)
			elif contract.payment_term == 'Bi-annual':
				next_due_date = add_months(contract.payment_due_date, 6)
			elif contract.payment_term == 'Yearly':
				next_due_date = add_months(contract.payment_due_date, 12)
			contract.payment_due_date = next_due_date
			contract.save()



