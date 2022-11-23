import csv
product_list = []
courier_list = []
order_list = []
products = {}
couriers = {}
orders = []
items = []
basket = {}
#product functions
def load_productlist():
    with open("/Users/mini project 1/csvfiles/productlist.csv", "r") as f:
        products = csv.DictReader(f)
        for product in products:
            product_list.append(product)

def productlist():
    for product in product_list:
        print(product)

def create_product():
    addproduct = input("Add product name: ")
    addprice = input("Add product price: ")
    products["Product"] = addproduct
    products["Price £"] = addprice
    product_list.append(products)
    print(product_list)
    
def update_product():
    for i in enumerate(product_list):
        print(i)
    oldproduct = int(input("Type in product position: "))
    newproduct = input("Enter new name: ")
    newprice = input("Type in new price: ")
    product_list[oldproduct]['Product'] = newproduct
    product_list[oldproduct]['Price £'] = newprice
    print(product_list)
    

def delete_product():
    for i in enumerate(product_list):
        print(i)
    deleteproduct = int(input("Type in position of item you would like to remove: "))
    del product_list[deleteproduct]
    print(product_list)

#courier functions
def load_courierlist():
    with open("/Users/mini project 1/csvfiles/courierlist.csv", "r") as f:
        couriers = csv.DictReader(f)
        for courier in couriers:
            courier_list.append(courier)

def courierlist(): 
    for courier in courier_list:
        print(courier)

def create_courier():
    addcourier = input("Add courier name: ")
    addnumber = input("Add courier number: ")
    couriers["Name"] = addcourier
    couriers["Phone number"] = addnumber
    courier_list.append(couriers)
    print(courier_list)   

def update_courier():
    for courier in enumerate(courier_list):
        print(courier)
    courier_position = int(input("Type in courier position: "))
    newcourier = input("Enter new name: ")
    newnumber = input("Enter new number: ")
    courier_list[courier_position]["name"] = newcourier
    product_list[courier_position]["phone number"] = newnumber
    print(courier_list)

def delete_courier():
    for courier in enumerate(courierlist):
        print(courier)
    deletecourier = input("Type in position of courier you would like to remove: ")
    del courier_list[deletecourier]
    print(courier_list)


#order functions
def load_order_list():
    with open("/Users/dami/Desktop/mini project 1/csvfiles/courierlist.csv", "r") as f:
        orders = csv.DictReader(f)
        for order in orders:
            order_list.append(order)

            
def order_items():
    exit = int(input("0,To Exit , 1 To Continue: "))
    while exit != 0:
        for product in enumerate(product_list):
            print(product)
        item_in_basket = int(input("Enter position to addd product: "))
        items.append(item_in_basket)
        exit = int(input("0,To Exit , 1 To Continue: "))
        return items


def orderlist(): 
    for order in order_list:
        print(order)
        
def create_order():
    print("Add new order")
    order_list.append(
            {
             "customer name": input("Please enter customer name: "),
             "address": input("Please enter customer's address: "),
              "phone number": input("Please enter customer's telephone number: "),
             "status": 'Preparing'
             }
             )
    print(order_list)
    print("Order placed. Returning to orders menu.")


def update_status():
    for order in enumerate(order_list):
        print(order)
    change_status = int(input("Number of order you would like to change: "))
    status_update = input('Input new order status: ')
    order_list[change_status]['status'] = status_update
    print(order_list)  

def amend_order():
    for order in enumerate(order_list):
        print(order)
    change_order = int(input("Enter the position of order you would like to change: "))
    print(order_list[change_order])
    new_name = input("Enter customer's name: ")
    new_address = input("Enter customer's address: ")
    new_status = input("Enter order status: ")
    new_number = input("Enter customer's number: ")
    for courier in enumerate(order_list):
        print(courier)
    new_courier = input("put in the position of new courier")
    items = order_items()
    new_dict = {"Customer name:": new_name,
        "Address:": new_address,
        "Phone number:": new_number,
        "Courier": new_courier,
        "Status": new_status,
        "Items": items,
        }
    order_list[change_order] = new_dict
    print(order_list)

   

def delete_order():
    for order in enumerate(order_list):
        print(order)
    delete_an_order = int(input("Pick number of order you would like to delete: "))
    del order_list[delete_an_order]
    print(order_list)

#Data persistence

def savexit_products():
    with open("productlist.csv", "w") as f:
        fields = ["Product","Price £"]
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(product_list)

def savexit_couriers():
    with open("courier.csv", "w") as f:
        fields = ["name", "number"]
        headers = csv.DictWriter(f, fieldnames=fields)
        headers.writeheader()
        headers.writerows(courier_list)

def savexit_orders():
    with open("orderlist.csv", "w") as f:
        fields = [
            "customer_name",
            "customer_address",
            "customer_phone",
            "courier",
            "status",
            "items",
        ]
        headers = csv.DictWriter(f, fieldnames=fields)
        headers.writeheader()
        headers.writerows(order_list)