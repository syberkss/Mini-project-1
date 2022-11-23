import menufunctions as f
import os
f.load_order_list()
f.load_courierlist()
f.load_productlist()

def main_menu():
    print("[1] Print product menu")
    print("[2] Orders menu")
    print("[3] Couriers menu")
    print("[0] Exit app")

def product_menu():
    print("[1] Print product list")
    print("[2] Create a new product")
    print("[3] Update existing product")
    print("[4] Delete product")
    print("[0] Return to main menu")


def orders_menu():
    print("[1] View orders")
    print("[2] Add new order")
    print("[3] Update order status")
    print("[4] Amend order")
    print("[5] Delete order")
    print("[0] Return to main menu")

def couriers_menu():
    print("[1] View courier")
    print("[2] Add new courier")
    print("[3] Change courier")
    print("[4] Delete courier")
    print("[0] Return to main menu")
   

# load our data into product_list, order_list, courier_list
# product_list = load_data(product_filepath, product_list)
# order_list = load_data(order_filepath, order_list)
# courier_list = load_data(courier_filepath, courier_list)
    
main_menu()
mmenu_option = input("Enter your option: ")
while mmenu_option != 0:
    if mmenu_option == '1':
        print()
        product_menu()
        product_option = input("Enter your option: ")
        while product_option != '0':
            if product_option == '1':
                f.productlist()
            elif product_option == '2':
                f.create_product()
            elif product_option == '3':
                f.update_product()
            elif product_option == '4':
                f.delete_product()
            else:
                print("invalid option. Enter 1-4")
                break

            print()
            product_menu()
            product_option = input("Enter your option: ")
        main_menu()
        mmenu_option = input("Enter your option: ")
    elif mmenu_option == '2':
        print()
        orders_menu()
        order_option = input("Enter your option: ")
        while order_option != '0':
            if order_option == '1':
                f.orderlist()
            elif order_option == '2':
                f.create_order()
            elif order_option == '3': 
                f.update_status()
            elif order_option == '4':
                f.amend_order()
            elif order_option == '5':
                f.delete_order()
            else:
                print("invalid option. Enter 1-4")
                break

            print()
            orders_menu()
            order_option = input("Enter your option: ")      
        main_menu()
        mmenu_option = input("Enter your option: ")
    elif mmenu_option == '3':
        print()
        couriers_menu()
        courier_option = input("Enter your option: ")
        while courier_option != '0':
            if courier_option == '1':
                f.courierlist()
            elif courier_option == '2':
                f.create_courier()
            elif courier_option == '3':
                f.update_courier()
            elif courier_option == 4:
                f.delete_courier()
            else:
                print("Invalid option, please enter 0 - 4")
                break

            print()
            couriers_menu()
            courier_option = input("Enter your option: ")
        main_menu()
        mmenu_option = input("Enter your option: ")
    else:
        print("Invalid option, enter 0 - 3")
        break
    
    print()
    main_menu()
    mmenu_option = input("Enter your option: ")
confirm = input("would you like to exit, type 'yes': ")
if confirm == "yes":
    f.savexit_products()
    f.savexit_couriers()
    f.savexit_orders()
    exit()
else:
    print()
    main_menu()
    mmenu_option = input("Enter your option: ")
    


            