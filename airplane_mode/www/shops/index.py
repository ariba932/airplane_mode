import frappe

def get_context(context):
	context.shops = frappe.get_all(
		"Shop",
		fields=[
			"port",
			"photo",
			"type",
			"location",
			"route",
			"creation",
			"status",

		],
		filters={"is_published": True},
		order_by="creation desc"
	)