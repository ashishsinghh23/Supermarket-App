# product_dao = DAO = data access object. 
from sql_connection import get_sql_connection

def get_all_products(connection):
    

    cursor = connection.cursor()
    query = "SELECT products.product_id , products.name , products.uom_id , products.price_per_unit ,uom_table.uom_name  FROM grocery_store.products inner join uom_table on products.uom_id = uom_table.uom_id;"

    cursor.execute(query)

    response =[]

    for (product_id , product_name , uom_id, price_per_unit , uom_name) in cursor:
        response.append(
            {'product_id':product_id , 
            'product_name':product_name, 
            'uom_id':uom_id, 
            'price_per_unit':price_per_unit , 'uom_name':uom_name} 
        )
   

    return response

def insert_new_product(connection , product) :
    cursor = connection.cursor()
    query = ("INSERT INTO products" "(name , uom_id , price_per_unit)"  "VALUES (%s , %s , %s)")
    data = (product['product_name'] , product['uom_id'] , product['price_per_unit'])
    cursor.execute(query , data)
    connection.commit()

    return cursor.lastrowid

def delete_product (connection, product_id):
    cursor = connection.cursor()
    query = 'DELETE FROM products WHERE product_id = %s'
    cursor.execute(query , (product_id,))
    connection.commit()

if __name__ == '__main__':
    connection = get_sql_connection()
    # print(get_all_products(connection))
    # print(insert_new_product(connection , {'name':'cabbage','uom_id':'2','price_per_unit':'10'}))
    product_id = 9  
    delete_product(connection, product_id)
