# Copyright (c) 2024, MKO Tevc Concepts and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import random


class AirplaneTicket(Document):
	def validate(self):
		#To check for duplicate 
		self.remove_duplicate_add_ons()

		#To calculate the total amount
		sum=0.00
		for add_on in self.add_ons:
			sum+=add_on.amount
		
		self.total_amount = int(self.flight_price)+int(sum)

		#generate seat if non exist
		#if not self.seat:
		#	self.set_seat()
  

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

	def before_insert(self):
		capacity=frappe.db.get_all('Airplane Flight', ['airplane.capacity as Cap'],filters={'name':['=',self.flight]})
		ticket_count = frappe.db.get_all('Airplane Ticket', fields=['COUNT(flight) as cnt'],filters=[{'docstatus':['<',2]},{'flight':['=',self.flight]}])
		print('cap contents-', capacity)
		print('ticket count-',ticket_count)
		if ticket_count[0]['cnt'] > capacity[0]['Cap']:
			frappe.throw('Flight Capacity  is Full, Unable to book new ticket!')
		

	def set_seat(self):
		alphabet= random.choice(['A','B','C','D','E'])    
		number=random.randrange(10,99)
		self.seat = f'{number}{alphabet}'

