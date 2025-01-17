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
def create_shop(shop_no, location,area,shop_type):
    try:
        if not frappe.has_permission('Shop', 'create'): 
            frappe.throw(("Not permitted"), frappe.PermissionError)
        new_shop = frappe.get_doc({
            'doctype': 'Shop',
            'shop_no': shop_no,
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
def get_all_locations():
    try: 
        if not frappe.has_permission('Shop', 'read'): 
            frappe.throw(("Not permitted"), frappe.PermissionError) 

        shops = frappe.get_all('Airport', fields=['name']) 
        return shops 
    except Exception as e: 
        frappe.throw(("Error fetching shops: {0}").format(str(e)))