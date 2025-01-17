// Copyright (c) 2025, MKO Tevc Concepts and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Crew Flight Register", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on('Crew Flight Register', {
    crew_member: function(frm) {
        if (frm.doc.crew_member) {
            frappe.db.get_value('Crew Member', frm.doc.crew_member, 'airline', function(value) {
                frappe.call({
                    method: 'airplane_mode.airplane_mode.fetch_details.get_available_flights',
                    args: {
                        crew_member: frm.doc.crew_member
                    },
                    callback: function(r) {
                        if (r.message) {
                            frm.set_query('flight', function() {
                                return {
                                    filters: {
                                        'name': ['in', r.message]
                                    }
                                };
                            });
                        }
                    }
                });
                
            });
        }
    }
});

// frappe.ui.form.on('Crew Flight Register', {
//     crew_member: function(frm) {
//         if (frm.doc.crew_member) {
//             frappe.db.get_value('Crew Member', frm.doc.crew_member, 'airline', function(value) {
//                 frappe.call({
//                     method: 'your_app_name.your_module_name.your_file_name.get_airplanes_by_airline',
//                     args: {
//                         airline: value.airline
//                     },
//                     callback: function(r) {
//                         if (r.message) {
//                             frm.set_query('flight', function() {
//                                 return {
//                                     filters: {
//                                         'airplane': ['in', r.message]
//                                     }
//                                 };
//                             });
//                         }
//                     }
//                 });
//             });
//         }
//     }
// });
