import sqlite3

class ItemscraperPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("Scrapy.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute(""" DROP TABLE IF EXISTS quot_tb""")
        self.curr.execute("""create table quot_tb(
                        product_name text,
                        product_price text,
                        product_reviews text,
                        product_available text,
                        product_image text
                        )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute(""" insert into quot_tb values (?,?,?,?,?)""", (
            item['product_name'],
            item['product_price'],
            item['product_reviews'],
            item['product_available'][0],
            item['product_image']
            ))
        self.conn.commit()