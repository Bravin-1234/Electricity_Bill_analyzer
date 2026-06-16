from database import connect

def fetch_all():
    conn = connect()
    cursor = conn.curcor()
    
    query = "SELECT * FROM energy_consumption"
    cursor.execute(query)
    records = cursor.fetchall()
    cursor.close()
    conn.close()
    return records

# Display the fetched data
records = fetch_all()

if records:
    for record in records:
        print(record)
else:
    print("No records found.")