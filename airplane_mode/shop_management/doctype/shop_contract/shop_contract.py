# Copyright (c) 2025, MKO Tevc Concepts and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime, timedelta


class ShopContract(Document):
	
	def before_save(self):
		#Compute the Rent_amount.
		rate = frappe.db.get_single_value("Shop Settings","shop_rate")
		shop = frappe.get_doc('Shop',self.shop_no)
		if shop.area:
			self.rent_amount = rate*shop.area
		else:
			frappe.throw("Rent settings is required")
		print("duration data",self.contract_period)
		#compute the expiration date
		if self.start_date and self.contract_period:
			start_date = datetime.strptime(self.start_date, '%Y-%m-%d') 
			self.expiration_date  = start_date + timedelta(days=(self.contract_period// 86400)) 
			
	def before_submit(self):
		self.status ="Active"

		