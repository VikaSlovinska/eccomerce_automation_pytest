import pytest
import logging as logger
from demostore_automation.src.api_helpers.CustomerAPIHelper import CustomersAPIHelper
from demostore_automation.src.dao.products_dao import ProductsDAO
from demostore_automation.src.generic_helpers.generic_order_helpers import GenericOrderHelper

@pytest.mark.orders
@pytest.mark.tcid48
def create_paid_order_as_quest_user():

    logger.info("Testing 'Create order' as quest user...")

    # need product for the order
    product_dao = ProductsDAO()
    rand_product = product_dao.get_random_product_from_db(1)
    product_id = rand_product[0]['ID']

    # make call to create the order
    generic_order_helper = GenericOrderHelper()
    args = {"line_items": [
        {
            "product_id": product_id,
            "quantity": 1
        }
    ]}

    api_order_info = generic_order_helper.create_order(additional_args=args)
    order_id = api_order_info['id']

    # verify the order is created by calling API
    expect_cus_id = 0 # bec we are using guest user
    expected_product = [{'product_id': product_id}]
    generic_order_helper.verify_order_is_created(api_order_info, expect_cus_id)





