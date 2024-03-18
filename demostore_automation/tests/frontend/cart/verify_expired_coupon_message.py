"""
Author: Vika Slovinska
TestCardExpireCoupon:

This test class contains test cases to verify the behavior of expired coupons in the cart.

Attributes:
    None

Methods:
    test_expired_coupon_message:
        Tests the behavior when an expired coupon is applied in the cart. It verifies that
        the expected error message is displayed when an expired coupon is applied.
"""
import pytest
import logging as logger
from demostore_automation.src.pages.HomePage import HomePage
from demostore_automation.src.pages.CartPage import CartPage
from demostore_automation.src.generic_helpers.generic_coupon_helper import GenericCouponHelper
from demostore_automation.src.pages.Header import Header

@pytest.mark.usefixure("init_driver")
class TestCardExpireCoupon:

    @pytest.mark.tcid66
    def test_expired_coupon_message(self):
        """
        test_expired_coupon_message:

        Tests the behavior when an expired coupon is applied in the cart. It verifies that
        the expected error message is displayed when an expired coupon is applied.
        """

        logger.info("testing expired coupon message")

        # go to home
        home_page = HomePage(self.driver)
        home_page.go_to_home_page()

        # add item to cart
        home_page.click_first_add_to_cart_button()
        header = Header()
        header.wait_until_cart_item_count(1)

        # go to cart
        cart_page = CartPage(self.driver)
        cart_page.go_to_cart_page()

        # enter expired coupon
        code = GenericCouponHelper().create_coupon(expired=True)
        cart_page.apply_coupon(code)

        # verify the error message shows up
        displayed_err = cart_page.get_displayed_error()
        expected_err = "This coupon has expired."
        assert displayed_err == expected_err, f"After appied expired coupon, expected to see:" \
                                              f"Error message: '{expected_err}'," \
                                              f"but actual error message: '{displayed_err}'."









