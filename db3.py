import sqlite3
import random

class FoodBeverageDB:
    def __init__(self, db_name='food_beverage.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL
        )
        ''')
        self.conn.commit()

    def insert_product(self, name, price):
        self.cursor.execute('INSERT INTO products (name, price) VALUES (?, ?)', (name, price))
        self.conn.commit()

    def update_product(self, id, name, price):
        self.cursor.execute('UPDATE products SET name = ?, price = ? WHERE id = ?', (name, price, id))
        self.conn.commit()

    def delete_product(self, id):
        self.cursor.execute('DELETE FROM products WHERE id = ?', (id,))
        self.conn.commit()

    def select_all_products(self):
        self.cursor.execute('SELECT * FROM products')
        return self.cursor.fetchall()

    def select_product_by_id(self, id):
        self.cursor.execute('SELECT * FROM products WHERE id = ?', (id,))
        return self.cursor.fetchone()

    def close_connection(self):
        self.conn.close()

# 샘플 데이터 생성 함수
def generate_sample_data():
    foods = ['피자', '햄버거', '파스타', '샐러드', '스테이크', '초밥', '라면', '김치찌개', '비빔밥', '치킨']
    beverages = ['콜라', '사이다', '주스', '커피', '차', '맥주', '와인', '소주', '물', '에이드']
    
    samples = []
    for i in range(100):
        if i % 2 == 0:
            name = random.choice(foods) + str(i//2 + 1)
        else:
            name = random.choice(beverages) + str(i//2 + 1)
        price = round(random.uniform(1000, 50000), -2)  # 100원 단위로 반올림
        samples.append((name, price))
    
    return samples

# 메인 실행 코드
if __name__ == "__main__":
    db = FoodBeverageDB()

    # 샘플 데이터 삽입
    samples = generate_sample_data()
    for sample in samples:
        db.insert_product(sample[0], sample[1])

    print("100개의 샘플 데이터가 삽입되었습니다.")

    # 전체 제품 조회
    all_products = db.select_all_products()
    print("\n전체 제품 목록:")
    for product in all_products:
        print(product)

    # 특정 제품 조회
    product_id = 50
    product = db.select_product_by_id(product_id)
    print(f"\n제품 ID {product_id}의 정보:")
    print(product)

    # 제품 업데이트
    db.update_product(product_id, "업데이트된 제품", 99999)
    updated_product = db.select_product_by_id(product_id)
    print(f"\n업데이트된 제품 ID {product_id}의 정보:")
    print(updated_product)

    # 제품 삭제
    db.delete_product(product_id)
    deleted_product = db.select_product_by_id(product_id)
    print(f"\n삭제된 제품 ID {product_id}의 정보:")
    print(deleted_product)

    db.close_connection()