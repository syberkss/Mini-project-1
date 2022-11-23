# Monty Cafe app

The client required a CLI management app to log and track orders for a café that delivers food and drinks to nearby customers. 


## Description

The app allows for the following:
*Item Availability;The branch Manager can declare which items are currently available and edit product availability as required.
*Manage and Accept Orders;
 Whenever a customer orders something, the order request can be put into a system and assign a courier.
*Courier Register;
The manager can also create and delete courier profile 
*Update  Delivery Status;
The previous order entry can be updated and will be waiting for the courier to pick up and deliver. 

* The client required a system that stores  products, couriers and orders, and modify/view them using basic CRUD operations.
* The client wants this data to be persisted such that all changes made in prior sessions are maintained.
* The order wants all of the persisted data to be loaded upon start-up.
* The client requires a robust, well-tested app.
* The client wants the app to have frequent updates.

The client’s requirements were fulfilled by focusing on specific requirements on a weekly basis and gradually improve my program to reflect every aspect of of the client specification. Being an absolute beginner in python, this meant I had time to improve on my knowledge and create a robust program.

## What i enjoyed:
One aspect I particularly enjoyed was troubleshooting the app and working together to find a solution to these problems made the work an enjoyable experience. It was fun to learn how to write a programme that meets the given specifications and to see how it runs when you have no prior knowledge of the field.


## I would have liked to:
Improve on my unit test knowledge to create more tests.

### Demo create product function
```
def create_product():
    addproduct = input("Add product name: ")
    addprice = input("Add product price: ")
    products["Product"] = addproduct
    products["Price £"] = addprice
    product_list.append(products)
    print(product_list)







