// Copyright (c) 2025, MKO Tevc Concepts and contributors
// For license information, please see license.txt

// Custom Script for Shop Contract Doctype

frappe.ui.form.on('Shop Contract', {
    before_submit: function(frm) {
        if (frm.doc.shop_no) {
            frappe.prompt([
                {
                    'fieldname': 'shop_name',
                    'fieldtype': 'Data',
                    'label': 'Shop Name',
                    'reqd': 1
                }
            ],
             (values)=> {
                frappe.db.set_value('Shop', frm.doc.shop_no, {'status':'Occupied','shop_name':values.shop_name}) 
                    .then(() => { 
                        frappe.msgprint(__('Shop status and name updated')); 
                    });
            },
            __('Enter Shop Name'),
            __('Submit')
           );
        }
    }
});

