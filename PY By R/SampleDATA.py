import pandas as pd
import numpy as np

# Number of rows for your sample data
num_rows = 10000

# Define sample data with random or fixed values
data = {
    'id': np.arange(1, num_rows + 1),
    'name': [f"Name_{i}" for i in range(1, num_rows + 1)],
    'department': np.random.choice(['HR', 'Sales', 'Finance', 'Engineering'], num_rows),
    'salary': np.round(np.random.uniform(30000, 120000, num_rows), 2),
    'hire_date': pd.to_datetime(np.random.choice(pd.date_range("2000-01-01", "2023-01-01"), num_rows)),
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to an Excel file
df.to_excel("sample_data.xlsx", index=False)

print("sample_data.xlsx file created successfully!")
