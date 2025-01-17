// Copyright (c) 2025, MKO Tevc Concepts and contributors
// For license information, please see license.txt

frappe.ui.form.on('Crew Member', {
    onload: function(frm) {
        // Set the max date for the date picker to 18 years before today
        let today = new Date();
        let maxDate = new Date(today.setFullYear(today.getFullYear() - 18));
        frm.fields_dict['date_of_birth'].df.options = {
            max: maxDate.toISOString().split('T')[0]
        };
        //control the license expiration and next medical check fields
        frm.fields_dict['license_expiration'].df.options = { min: today }; 
        frm.fields_dict['next_medical_check'].df.options = { min: today }; 
        frm.refresh_field('date_of_birth');
        frm.refresh_field('license_expiration'); 
        frm.refresh_field('next_medical_check');
    },

    validate: function(frm) {
        // Validate that the date of birth is at least 18 years in the past
        let dob = new Date(frm.doc.date_of_birth);
        let age = (new Date() - dob) / (1000 * 60 * 60 * 24 * 365.25);
        if (age < 18) {
            frappe.msgprint(__('Crew member must be at least 18 years old.'));
            frappe.validated = false;
        }

        // Validate that the license expiration and medical check dates 
        // are in the future 
        let today = new Date(); 
        let license_expiration = new Date(frm.doc.license_expiration); 
        let next_medical_check = new Date(frm.doc.next_medical_check); 
        if (license_expiration <= today) { 
            frappe.msgprint(__('License expiration date must be in the future.')); 
            frappe.validated = false; 
        } 
        if (next_medical_check <= today) { 
            frappe.msgprint(__('Next medical check date must be in the future.')); 
            frappe.validated = false; 
        }
    }
});

