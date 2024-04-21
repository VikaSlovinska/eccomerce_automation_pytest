
from demostore_automation.src.utilities.wooAPIUtility import WooAPIUtility


class OrdersAPIHelper:

    def __init__(self):
        self.woo_api_utility = WooAPIUtility()

    def call_create_order(self, payload, expected_status_code=201):
        """
        Calls the 'create order' endpoint.
        Args:
            payload:
            expected_status_code: default is 201
        :return:
        """
        return self.woo_api_utility.post("orders", params=payload,  expected_status_code=expected_status_code)