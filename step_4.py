from data import products_string
from pprint import pprint
from step_1 import transform_products_to_list
from step_3 import group_products_by_customer_and_invoice


def calculate_total_per_invoices(products_string):
    
    products_dicts = group_products_by_customer_and_invoice(products_string)
    
    invoices_total = {}
    
    for customer_id, invoices in products_dicts.items():
        
        invoices_total.setdefault(customer_id, {})
        
        for invoice, invoice_list in invoices.items():
            
            total = 0
            quantity = 0
            price_per_unit = 0
            invoices_total[customer_id].setdefault(invoice)
            
            for each_invoice in invoice_list:
                
                quantity = int(each_invoice[3])
                price_per_unit = float(each_invoice[5])
            
                total += quantity * price_per_unit
        
            invoices_total[customer_id][invoice] = round(total, 2)
        
    return invoices_total

#pprint(calculate_total_per_invoices(products_string))
    
