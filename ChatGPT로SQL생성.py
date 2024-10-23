import sqlite3
import random

class ElectronicsDatabase:
    def __init__(self, db_name="electronics.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS electronics (
                product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_name TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        self.conn.commit()

    def insert_product(self, product_name, price):
        self.cursor.execute('''
            INSERT INTO electronics (product_name, price)
            VALUES (?, ?)
        ''', (product_name, price))
        self.conn.commit()

    def update_product(self, product_id, product_name=None, price=None):
        if product_name is not None and price is not None:
            self.cursor.execute('''
                UPDATE electronics
                SET product_name = ?, price = ?
                WHERE product_id = ?
            ''', (product_name, price, product_id))
        elif product_name is not None:
            self.cursor.execute('''
                UPDATE electronics
                SET product_name = ?
                WHERE product_id = ?
            ''', (product_name, product_id))
        elif price is not None:
            self.cursor.execute('''
                UPDATE electronics
                SET price = ?
                WHERE product_id = ?
            ''', (price, product_id))
        self.conn.commit()

    def delete_product(self, product_id):
        self.cursor.execute('''
            DELETE FROM electronics
            WHERE product_id = ?
        ''', (product_id,))
        self.conn.commit()

    def select_all_products(self):
        self.cursor.execute('SELECT * FROM electronics')
        return self.cursor.fetchall()

    def select_product_by_id(self, product_id):
        self.cursor.execute('SELECT * FROM electronics WHERE product_id = ?', (product_id,))
        return self.cursor.fetchone()

    def __del__(self):
        self.conn.close()

# 샘플 데이터 100개 생성
def generate_sample_data(db):
    product_names = ["TV", "Smartphone", "Laptop", "Tablet", "Camera", "Headphones", "Smartwatch", "Speaker", "Monitor", "Printer"]
    for i in range(1, 101):
        product_name = random.choice(product_names) + f" {i}"
        price = round(random.uniform(100, 1000), 2)
        db.insert_product(product_name, price)

# 사용 예시
db = ElectronicsDatabase()
generate_sample_data(db)

# 데이터 출력
products = db.select_all_products()
for product in products:
    print(product)

# 특정 제품 수정
db.update_product(1, price=999.99)

# 특정 제품 삭제
db.delete_product(2)

# 특정 제품 선택
product = db.select_product_by_id(1)
print(product)
