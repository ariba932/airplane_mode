// Copyright (c) 2024, MKO Tevc Concepts and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airline", {
refresh(frm) {
    
  if (frm.doc.website && frm.doc.website.trim() !== ''){
        //const website = frm.doc.website;
        frm.add_web_link(frm.doc.website, "Airline Website");
        } 
    },
// validate: function(frm) { 
//     // Regular expression for URL validation 
//      var urlPattern = /^(https?:\/\/)?([\da-z.-]+)\.([a-z.]{2,6})([/\w .-]*)*\/?$/; 
//      var website = frm.doc.website; 
//      if (website && website.trim() !== '' && !urlPattern.test(website)) { 
//         frappe.msgprint(__('Please enter a valid URL in the Website field.')); 
//         frappe.validated = false; }
//     }

});
