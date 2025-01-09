# Copyright (c) 2025, MKO Tevc Concepts and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters: dict | None = None):
	"""Return columns and data for the report.

	This is the main entry point for the report. It accepts the filters as a
	dictionary and should return columns and data. It is called by the framework
	every time the report is refreshed or a filter is updated.
	"""
	#columns, data, chart = [], [], {}
	columns = get_columns()
	data = get_data()
	summary_message = get_summary(data)
	chart = {
		"data": {
			"labels": [x["airline"] for x in data],
			"datasets":[{"values":[x["total_revenue"] for x in data]}],
		},
		"type":"donut",
		"legend": [x["airline"] for x in data],
	}

	return columns, data, None, chart, summary_message, 


def get_columns() -> list[dict]:
	"""Return columns for the report.

	One field definition per column, just like a DocType field definition.
	"""
	return [
		{
			"label": _("Airline"),
			"fieldname": "airline",
			"fieldtype": "Link",
			"options": "Airline",
			"width": 150
		},
		{
			"label": _("Revenue"),
			"fieldname": "total_revenue",
			"fieldtype": "Currency",
			"options": "NGN",
			"width": 150
		},
	]

def get_data() -> list[list]:
	"""Return data for the report.

	The report data is a list of rows, with each row being a list of cell values.
	"""
	# Get all airlines 
	airlines = frappe.get_all("Airline", fields=["name"])
	#get all the tickets
	tickets = frappe.get_all("Airplane Ticket",fields=["name","flight","total_amount"])

	revenue_airline = {airline.name: 0 for airline in airlines}
	
	#run through each ticket and reference flight to get the airplane and airline
	for ticket in tickets:
		flight=frappe.get_value("Airplane Flight",ticket.flight,"airplane")
		airline=frappe.get_value("Airplane", flight,"airline")

		if airline not in revenue_airline:
			revenue_airline[airline] =0
		#sum it um
		revenue_airline[airline] += ticket.total_amount
		#print("data issue",flight,airline,ticket.total_amount)
	
	data = []
	for airline, total_revenue in revenue_airline.items():
		data.append({
			"airline":airline,
			"total_revenue":total_revenue
		})
	print("data dump:", data)
	return data

def get_summary(data): 
	total_revenue = sum(x["total_revenue"] for x in data) 
	return [ { "label": "Total Revenue in the Industry", 
		   		"value": total_revenue, 
				"indicator": "Green", 
				"datatype": "Currency", 
				"center": True } ]