import logging as logger
import pytest
from demostore_automation.src.generic_helpers.generic_product_helper import GenericProductHelper
from demostore_automation.src.generic_helpers.generic_product_review_helper import GenericProductReviewsHelper
from demostore_automation.src.utilities.genericUtilities import (
    generate_random_string,
    generate_random_email_and_password
)


@pytest.mark.smoke
class TestProductsReviewsSmoke:
    """
    A test class for testing product reviews functionality.
    This class includes smoke tests for verifying the creation and management of product reviews.
    """

    def setup_method(self):
        """
        Sets up the necessary objects and state before each test method.
        Initializes product and product review helpers, creates a product,
        and captures the initial rating count and product ID.
        """
        self.product_helper = GenericProductHelper()
        self.product_review_helper = GenericProductReviewsHelper()
        self.product = self.product_helper.create_a_product()
        self.rating_count_before = self.product['rating_count']
        self.product_id = self.product['id']

    @pytest.mark.ecombe40
    @pytest.mark.tcid199
    def test_create_product_review(self):
        """
        Test to verify that the create product review endpoint successfully creates a review for a product.
        Creates multiple reviews for the product and verifies the rating count.
        """
        logger.info("Creating product review test")
        assert self.rating_count_before == 0, "New product should have 0 reviews"

        for _ in range(5):
            self.product_review_helper.create_random_review_for_product(self.product_id)

        product = self.product_helper.get_product_detail_via_api(self.product_id)
        rating_count_after = product['rating_count']

        assert rating_count_after == 4, f"Expected 4 reviews, got {rating_count_after}"

    @pytest.mark.tcid200
    @pytest.mark.ecombe41
    def test_duplicate_review_fails(self):
        """
        Test to verify that creating a review with all fields duplicated fails
        and returns the expected status code and error message.
        """
        review_rs = self.product_review_helper.create_random_review_for_product(self.product_id)
        rs_duplicate = self.product_review_helper.create_product_review(
            product_id=self.product_id,
            review=review_rs['review'],
            reviewer=review_rs['reviewer'],
            reviewer_email=review_rs['reviewer_email'],
            rating=review_rs['rating'],
            expected_status_code=409
        )
        assert rs_duplicate['code'] == 'woocommerce_rest_comment_duplicate'
        assert 'Duplicate comment detected' in rs_duplicate['message']
        assert rs_duplicate['data']['status'] == 409

    @pytest.mark.ecombe42
    @pytest.mark.tcid201
    def test_different_reviewer_succeeds(self):
        """
        Test to verify that creating a review with all fields the same except the 'reviewer' field
        succeeds and returns the expected status code.
        """
        review_rs = self.product_review_helper.create_random_review_for_product(self.product_id)
        rs_duplicate = self.product_review_helper.create_product_review(
            product_id=self.product_id,
            review=review_rs['review'],
            reviewer=f"{generate_random_string(5)} {generate_random_string(6)}",
            reviewer_email=review_rs['reviewer_email'],
            rating=review_rs['rating'],
            expected_status_code=201
        )
        assert rs_duplicate['status'] == 'approved'

    @pytest.mark.ecombe43
    @pytest.mark.tcid202
    def test_different_review_succeeds(self):
        """
        Test to verify that creating a review with all fields the same except the 'review' field
        succeeds and returns the expected status code.
        """
        review_rs = self.product_review_helper.create_random_review_for_product(self.product_id)
        rs_duplicate = self.product_review_helper.create_product_review(
            product_id=self.product_id,
            review="Automation review: " + generate_random_string(25),
            reviewer=review_rs['reviewer'],
            reviewer_email=review_rs['reviewer_email'],
            rating=review_rs['rating'],
            expected_status_code=201
        )
        assert rs_duplicate['status'] == 'approved'

    @pytest.mark.ecombe44
    @pytest.mark.tcid203
    def test_different_email_succeeds(self):
        """
        Test to verify that creating a review with all fields the same except the 'reviewer_email' field
        succeeds and returns the expected status code.
        """
        review_rs = self.product_review_helper.create_random_review_for_product(self.product_id)
        rs_duplicate = self.product_review_helper.create_product_review(
            product_id=self.product_id,
            review=review_rs['review'],
            reviewer=review_rs['reviewer'],
            reviewer_email=generate_random_email_and_password()['email'],
            rating=review_rs['rating'],
            expected_status_code=201
        )
        assert rs_duplicate['status'] == 'approved'

    @pytest.mark.ecombe45
    @pytest.mark.tcid204
    def test_default_status_approved(self):
        """
        Test to verify that the default status for a created review is set to "approved" as expected.
        """
        review_rs = self.product_review_helper.create_random_review_for_product(self.product_id)
        assert review_rs['status'] == 'approved'
