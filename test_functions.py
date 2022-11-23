from unittest import mock
import pytest


#product functions
def create_product(product_name, product_list):
    product_list.append(product_name)
    return product_list

def test_create_product():
    mock_product = "Fanta"
    mock_product_list = []

    updated_product_list = create_product(mock_product, mock_product_list)

    assert updated_product_list == ["Fanta"]
        
def update_product(product_index, product, product_price, product_list):
    product_list[product_index][product][product_price]
    return product_list

def test_update_product():
    mock_new_product = "Coke"
    mock_new_price = "5.00"
    mock_product_index = 0

    mock_product_list = [{"Product": "Pepsi", "Price": "4.00"}]

    updated_product_list = update_product(mock_product_index, mock_new_product, mock_new_price, mock_product_list)

    assert updated_product_list == [{"Product": "Coke", "Price": "5.00"}]

#     mock_product = "Fanta"
#     mock_product_list = []

#     updated_product_list = create_product(mock_product, mock_product_list)

#     assert updated_product_list == ["Fanta"]
        
# def test_update_product():
#     mock_product_index = 0
#     mock_product = "Coca Cola"
#     mock_product_list = ["Pepsi", "Luscombe"]

#     updated_product_list = update_product(product_index, mock_product, mock_product_list)

#     assert updated_product_list == ["Coca Cola", "Luscombe"]
