import pandas as pd
import mysql.connector

# Load the Excel file
data = pd.read_excel('sample_data.xlsx')

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Rohan15@',
    database='rohanpy'
)
cursor = conn.cursor()

# Insert data into MySQL table
for index, row in data.iterrows():
    cursor.execute(
        "INSERT INTO employees (id, name, department, salary) VALUES (%s, %s, %s, %s)",
        (row['id'], row['name'], row['department'], row['salary'])
    )

conn.commit()
cursor.close()
conn.close()




