// Copyright (c) 2024, MKO Tevc Concepts and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", 
    { 	
        refresh(frm) {

            frm.add_custom_button("Assign Seat", ()=> { 
                    let d= new frappe.ui.Dialog({
                        title:'Select Seat',
                        fields:[
                            {
                                label:'Seat Number',
                                fieldname:'seat',
                                fieldtype:'Data'
                            }
                        ],
                        size: 'small',
                        primary_action_lable:'Assign',
                        primary_action (values){
                            frm.set_value("seat", values.seat)
                            frm.save();
                            console.log(values);
                            d.hide();
                        }
                    });
                    d.show();
                    }, "Action");
	    },

        flight_price(frm){
            frm.trigger("update_total_amount");
        },

        update_total_amount(frm){
            let sum = 0;
            for(let add_on in frm.doc.add_ons){
                sum+=add_on.amount;
            }
            sum = frm.doc.flight_price+sum
            frm.set_value("total_amount", sum);
        },
    }
);

frappe.ui.form.on('Airplane Ticket Add-on Item', {
    refresh(frm) {
    },
    //track changes on add_on item amount
    amount(frm) {
        frm.trigger("update_total_amount");
    },
    //track changes when add_on item is remove
    items_remove(frm){
        frm.trigger("update_total_amount");
    },
   });
