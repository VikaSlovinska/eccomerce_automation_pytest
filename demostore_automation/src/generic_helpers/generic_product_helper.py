import logging as logger
import random

from demostore_automation.src.api_helpers.ProductsAPIHelper import ProductsAPIHelper
from demostore_automation.src.utilities.genericUtilities import generate_random_string



class GenericProductHelper:

    def __init__(self):
        self.customers_api_helper = ProductsAPIHelper()

    def get_random_products(self, qty=1, **kwargs):
        """
        Gets random products using the 'products' api.
        It calls the products api with the given parameters in **kwargs, randomly selects the given number of products
        from the response and returns it.
        List of available properties: https://woocommerce.github.io/woocommerce-rest-api-docs/#product-properties
        Example function calls:
            get_random_products(qty=1, status=private, type=variable)
            get_random_products(qty=1, downloadable=True)

        :param qty: number of products to return.
        :param kwargs:
        :return:
        """

        payload = {"per_page": 100}
        products = self.customers_api_helper.call_list_products(payload=payload)

        return random.sample(products, int(qty))

    def get_product_detail_via_api(self, product_id):
        return self.customers_api_helper.call_get_product_by_id(product_id)

    def create_a_product(self, product_type="simple", **kwargs):
        # generate some data
        payload = dict()
        payload['type'] = product_type

        if 'name' not in kwargs.keys():
            payload['name'] = generate_random_string(20)

        if 'regular_price' not in kwargs.keys():
            payload['regular_price'] = str(round(random.uniform(10, 100), 2))

        payload.update(kwargs)

        # make the call
        product_rs = ProductsAPIHelper().call_create_product(payload)

        logger.info(f"Created product. product_id - {product_rs['id']}")

        return product_rs


    def delete_a_product(self, product_id, force=True):
        return ProductsAPIHelper().call_delete_product(product_id, force=force)