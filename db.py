import sqlite3

# Connect to (or create) the database
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM company")
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)
# Save and close
conn.commit()
conn.close()
