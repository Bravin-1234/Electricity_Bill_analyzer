from database import connect

def fetch_all():
    conn = connect()
    
    if conn is None:
        print("Database connection Failed")
        return []
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM energy_consumption")
    records= cursor.fetchall()
    
    cursor.close()
    conn.close()
    return records

# Test fetching data
data = fetch_all()
for record in data:
    print(record)