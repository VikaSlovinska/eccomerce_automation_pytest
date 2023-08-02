


import pytest
import logging as logger
from demostore_automation.src.pages.HomePage import HomePage
from demostore_automation.src.pages.CartPage import CartPage
from demostore_automation.src.pages.Header import Header
from demostore_automation.src.generic_helpers.generic_coupon_helper import GenericCouponHelper

@pytest.mark.usefixtures("init_driver")
class TestCartExpiredCoupon:


    @pytest.mark.tcid66
    @pytest.mark.test66
    def test_expired_coupon_message(self):
        """
        A test to verify applying an expired coupon will show and error
        saying 'This coupon has expired.'.
        :return:
        """

        logger.info("Testing expired coupon message")

        # goto home
        home_page = HomePage(self.driver)
        home_page.go_to_home_page()

        # add item to cart
        home_page.click_first_add_to_cart_button()
        header = Header(self.driver)
        header.wait_until_cart_item_count(1)

        # go to cart
        cart_page = CartPage(self.driver)
        cart_page.go_to_cart_page()

        # input expired coupon
        coupon_code = GenericCouponHelper().create_coupon(expired=True)
        cart_page.apply_coupon(coupon_code)

        # verify an error message shows up
        displayed_err = cart_page.get_displayed_error()
        expected_err = 'This coupon has expired.'
        assert displayed_err == expected_err, f"After applying expired coupon, expted to see " \
                                              f"Error message '{expected_err}', but " \
                                              f"actual displayed is '{displayed_err}'."
