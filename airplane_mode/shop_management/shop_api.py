import frappe

@frappe.whitelist(allow_guest=False)
def get_all_shops():
    try: 
        if not frappe.has_permission('Shop', 'read'): 
            frappe.throw(("Not permitted"), frappe.PermissionError) 

        shops = frappe.get_all('Shop', fields=['*']) 
        return shops 
    except Exception as e: 
        frappe.throw(("Error fetching shops: {0}").format(str(e)))

@frappe.whitelist(allow_guest=False)
def create_shop(shop_no,shop_name,port,location,area,shop_type):
    try:
        if not frappe.has_permission('Shop', 'create'): 
            frappe.throw(("Not permitted"), frappe.PermissionError)
        new_shop = frappe.get_doc({
            'doctype': 'Shop',
            'shop_no': shop_no,
            'shop_name': shop_name,
            'port': port,
            'location': location,
            'type': shop_type,
            'area': area
        })
        new_shop.insert()
        frappe.db.commit()
        return new_shop
    except Exception as e:
        frappe.throw(("Error creating shop: {0}").format(str(e)))

@frappe.whitelist(allow_guest=False)
def get_all_ports():
    try: 
        if not frappe.has_permission('Airport', 'read'): 
            frappe.throw(("Not permitted"), frappe.PermissionError) 

        ports = frappe.get_all('Airport', fields=['name']) 
        return ports 
    except Exception as e: 
        frappe.throw(("Error fetching Airports details: {0}").format(str(e)))


@frappe.whitelist(allow_guest=True)
def create_lead(**args):
    full_name = args.get("first_name") +" "+ args.get("last_name")
    lead = frappe.get_doc({
        "doctype": "Shop Online Lead",
        "prospect_name": full_name,
        "email": args.get("email"),
        "phone": args.get("company"),
        "message": args.get("message"),
        "shop_no": args.get("shop_no")
    })
    lead.insert(ignore_permissions=True)
    return lead.name

