from demostore_automation.src.utilities.genericUtilities import generate_random_string, generate_random_email_and_password

from demostore_automation.src.utilities.wooAPIUtility import WooAPIUtility



class GenericProductReviewsHelper:

    def __init__(self):
        self.woo_api_utility = WooAPIUtility()

    def create_product_review(self, product_id, review, reviewer, reviewer_email, rating, expected_status_code=201, **kwargs):
        """
        Add additional parameters as keyword parameters. All parameters will be included in payload.
        """

        payload = {
                    "product_id": product_id,
                    "review": review,
                    "reviewer": reviewer,
                    "reviewer_email": reviewer_email,
                    "rating": rating
                }

        payload.update(kwargs)

        return self.woo_api_utility.post('products/reviews', params=payload, expected_status_code=expected_status_code)


    def get_product_review(self, review_id, expected_status_code=200):

        return self.woo_api_utility.get(f'products/reviews/{review_id}', expected_status_code=expected_status_code)


    def create_random_review_for_product(self, product_id):

        random_name = f"{generate_random_string(length=5)} {generate_random_string(length=6)}"
        random_email = generate_random_email_and_password()['email']
        random_review = "Automation review: " + generate_random_string(length=25)

        return self.create_product_review(product_id, review=random_review, reviewer=random_name, reviewer_email=random_email, rating=5)