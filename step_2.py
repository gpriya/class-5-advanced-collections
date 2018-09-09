from data import products_string
from pprint import pprint
from step_1 import transform_products_to_list


def group_products_by_customer(products_string):
    customers = {}
    
    products_list = transform_products_to_list(products_string)
    
    for products in products_list:
        customer_id = products[-2]
        
        customers.setdefault(customer_id, [])
        customers[customer_id].append(products)
        
    return customers

#pprint(group_products_by_customer(products_string))
