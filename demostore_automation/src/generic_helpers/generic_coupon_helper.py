
from datetime import datetime
from demostore_automation.src.utilities.genericUtilities import generate_random_string
from demostore_automation.src.api_helpers.CouponsAPIHelper import CouponsAPIHelper


class GenericCouponHelper:

    def __init__(self):
        self.coupon_api_helper = CouponsAPIHelper()

    def create_coupon(self, coupon_code=None, length=7, expired=False, **kwargs):

        # if expired parameter is set to True generate expiration date which is now.
        if expired:
            expiration_date = datetime.now().isoformat()
        else:
            expiration_date = None

        # if coupon code is not provided generate code
        if not coupon_code:
            coupon_code = generate_random_string(length=length)

        payload = {
            "code": coupon_code.upper(),
            "discount_type": "percent",
            "amount": "100",
            "date_expires": expiration_date
        }

        # update the payload with any additional key/value that are passed into the function
        payload.update(kwargs)

        rs_api = self.coupon_api_helper.call_create_coupon(payload)
        coupon_code = rs_api['code']

        return coupon_code

