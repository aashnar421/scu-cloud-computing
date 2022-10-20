from flask import Flask
import random
import psycopg2
import os
from psycopg2.extras import RealDictCursor
app = Flask(__name__)

conn = psycopg2.connect(
    host=os.getenv('POSTGRES_HOST'),
    database=os.getenv('POSTGRES_DB'),
    user=os.getenv('POSTGRES_USER'),
    password=os.getenv('POSTGRES_PASSWORD'),
    port =os.getenv('POSTGRES_PORT'),
    cursor_factory=RealDictCursor)


@app.route('/get_meal')
def get_meal():    
    cur = conn.cursor()
    cur.execute('SELECT MealName, MealPrice from meals ORDER BY RANDOM() LIMIT 1')
    data = cur.fetchone()
    cur.close()
    return {"name": data['mealname'], "price":data['mealprice']}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
