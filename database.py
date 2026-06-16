import os
import mysql.connector
from dotenv import load_dotenv
load_dotenv()

def connect():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    
def init_db():
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS energy_consumption (
            id INT AUTO_INCREMENT PRIMARY KEY,
            appliance VARCHAR(50),
            power FLOAT,
            hours FLOAT,
            quantity INT,
            daily_kwh FLOAT,
            monthly_kwh FLOAT,
            tariff FLOAT,
            total_bill FLOAT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    conn.commit()
    cursor.close()
    conn.close()   
    
def insert_record(month, appliance, power, hours, quantity, daily_kwh, monthly_kwh, tariff, total_bill):
    conn = connect()
    cursor = conn.cursor()
    
    query = """
        INSERT INTO energy_consumption (month, appliance, power, hours, quantity, daily_kwh, monthly_kwh, tariff, total_bill)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (month, appliance, power, hours, quantity, daily_kwh, monthly_kwh, tariff, total_bill)
    
    cursor.execute(query, values)
    conn.commit()
    
    cursor.close()
    conn.close()
    
def fetch_all():
    conn = connect()
    cursor = conn.cursor()
    
    query = "SELECT * FROM energy_consumption"
    cursor.execute(query)
    records = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return records    