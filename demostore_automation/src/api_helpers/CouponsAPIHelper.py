
from demostore_automation.src.utilities.wooAPIUtility import WooAPIUtility

class CouponsAPIHelper:

    def __init__(self):
        self.woo_api_utility = WooAPIUtility()

    def call_create_coupon(self, payload):
        return self.woo_api_utility.post(wc_endpoint="coupons", params=payload, expected_status_code=201)
