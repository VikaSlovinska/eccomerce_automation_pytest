
from demostore_automation.src.utilities.dbUtility import DBUtility
import logging as logger


class OrdersDAO:

    def __init__(self):
        self.db_helper = DBUtility()

    def get_order_lines_by_order_id(self, order_id):
        """
        Given an order id it will get all order lines for the order.
        :param order_id
        :return:
        """

        logger.info(f"Getting order lines by order id. Order id = {order_id}")
        sql = f"""SELECT * FROM {self.db_helper.database}.{self.db_helper.table_prefix}woocommerce_order_items
        WHERE order_id = {order_id};"""

        return self.db_helper.execute_select(sql)


