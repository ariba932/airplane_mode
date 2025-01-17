# Copyright (c) 2025, MKO Tevc Concepts and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime, timedelta

class CrewMember(Document):
	def validate(self): 
		self.validate_date_of_birth()
		self.validate_future_dates()

	def before_save(self): 
		if self.last_name and self.other_name: 
			self.full_name = f'{self.other_name} {self.last_name}' 
		elif self.last_name: 
			self.full_name = self.last_name 
		else: 
			self.full_name = ''
	

	def validate_date_of_birth(self): 
		if self.date_of_birth: 
			if type(self.date_of_birth)== datetime:
				dob=self.date_of_birth
			else:
				dob = datetime.strptime(self.date_of_birth, '%Y-%m-%d') 
			age = (datetime.now() - dob).days / 365.25 
			if age < 18: 
				frappe.throw("Crew member must be at least 18 years old.")
	
	def validate_future_dates(self): 
		today = datetime.now().date() 
		if self.license_expiration and datetime.strptime(self.license_expiration, '%Y-%m-%d').date() <= today: 
			frappe.throw("License expiration date must be in the future.") 
		if self.next_medical_check and datetime.strptime(self.next_medical_check, '%Y-%m-%d').date() <= today: 
			frappe.throw("Next medical check date must be in the future.")