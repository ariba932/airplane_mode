import frappe
from frappe.utils import nowdate, add_days, date_diff, getdate

def send_payment_reminders():

    # First check if reminder is enabled in Shop Settings
    shop_settings = frappe.get_single("Shop Settings")
    if not shop_settings.payment_reminder:
        frappe.log_error("Payment reminders are disabled in Shop Settings")
        return
    
    #Proceed with other items.
    today = getdate(nowdate())

    # Get contracts where due date is between today+5 and today
    contracts = frappe.get_all(
        "Shop Contract",
        filters=[
            ["payment_due_date", ">=", today],
            ["payment_due_date", "<=", add_days(today, 5)],
            ["status","==","Active"],
        ],
        fields=["name", "payment_due_date", "rent_amount", "tenant_name"]
    )

    # If no contracts found, exit early
    if not contracts:
        return
    
    for contract in contracts:
        tenant = frappe.get_doc("Tenant", contract.tenant_name)
        days_to_due = date_diff(contract.payment_due_date, today)
          
        # Customize message based on days remaining
        if days_to_due == 0:
            message = "payment is due today"
        elif days_to_due == 1:
            message = "payment is due tomorrow"
        else:
            message = f"payment is due in {days_to_due} days"
            
        # Send reminder email
        try:
            frappe.sendmail(
                recipients=[tenant.email],
                subject=f"Payment Reminder - {contract.name}",
                message=f"""Dear {tenant.full_name},
                    <br><br>
                    This is a reminder that your {message} for contract {contract.name}.<br>
                    Amount Due: <strong>{contract.rent_amount}</strong><br>
                    Due Date: <strong>{contract.payment_due_date}</strong>
                    <br><br>
                    Please ensure timely payment to avoid any late fees.
                    <br><br>
                    Thank you.
                """
            )
            frappe.db.commit()       
        except Exception as e:
            frappe.log_error(f"Failed to send payment reminder for {contract.name}: {str(e)}")