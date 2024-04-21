
import json
import os

from demostore_automation.src.api_helpers.OrdersAPIHelper import OrdersAPIHelper
from demostore_automation.src.dao.orders_dao import OrdersDAO


class GenericOrderHelper:

    def __init__(self):
        self.order_api_helper = OrdersAPIHelper()
        self.cur_file_dir = os.path.dirname(os.path.realpath(__file__))

    def create_order(self, additional_args=None):

        # payload_template = self.cur_file_dir + '/../data/create_order_payload.json'
        payload_template = os.path.join(self.cur_file_dir, '..', 'data',  'create_order_payload.json')
        with open(payload_template, 'r') as f:
            order_payload = json.load(f)
        if additional_args:
            assert isinstance(additional_args, dict), f"The parameter 'additional_args' must be type dictionary"
            order_payload.update(additional_args)

        # if additional args(passed in argument) does not have line items then add line items to the payload
        if additional_args and 'line_items' not in additional_args.keys():
            rand_product = self.product_dao.get_random_product_from_db(qty=1)
            rand_product_id = rand_product[0]['ID']
            order_payload['line_items'] = [{"product_id": rand_product_id, "quantity": 1}]



        response_create_order = self.order_api_helper.call_create_order(payload=order_payload)

        return response_create_order
    def verify_order_is_created(self, order_json, exp_cust_id, exp_products):

        # get the order id from json
        order_id = order_json['id']

        # verify the json respond is not empty
        assert order_json, f"Create order response is empty"

        # verify expected customer id
        assert order_json['customer_id'] == exp_cust_id, f"Create order with given customer id returned bad " \
                                                         f"customer id" \
                                                         f"Expected customer id={exp_cust_id}," \
                                                         f" but got 'order_json[customer_id]'"

        # verify the number of products in api response is as expected
        assert order_json['line_items'] == len(exp_products), f"Expected only {len(exp_products)} in the order" \
                                                              f"found '{len(order_json['line_items'])}'" \
                                                              f"order_id: {order_json['id']}."

        # verify the products id's in Api response are as expected
        # get list od products ids in the response
        api_products_id = [i['product_id'] for i in order_json['line_items']]

        for product in exp_products:
            exp_id = product['product_id']
            assert exp_id in api_products_id

        # verify db
        order_dao = OrdersDAO()
        line_info = order_dao.get_order_lines_by_order_id(order_id)

        # verify db info is not empty
        assert line_info, f"Create order line item is not found in db. Order id: {order_id}"

        # get th eline items only exclude shipping
        line_items = []
        for i in line_info:
            if i['order_item_type'] == 'line_item':
                line_items.append(i)
        assert len(line_items) == len(exp_products), f"Expected {len(exp_products)} but found len{line_items}"













