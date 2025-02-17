import random
import string
import pandas as pd

# Function to generate random name
def generate_random_name(length=8):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

# Read the original CSV (adjust the path to your CSV)
input_csv = 'C:/ProgramData/MySQL/MySQL Server 9.0/Uploads/dreamers.csv'
df = pd.read_csv(input_csv)

# Create the SQL script
sql_file_path = 'update_dreamers_names.sql'

with open(sql_file_path, 'w') as file:
    # Adding an initial line to ignore errors (useful for testing)
    file.write("SET SQL_SAFE_UPDATES = 0;\n")
    
    for index, row in df.iterrows():
        new_name = generate_random_name(8)  # 8 characters for the name
        update_sql = f"UPDATE IGNORE dreamers SET name = '{new_name}' WHERE id = {row['id']};\n"
        file.write(update_sql)

    # Optionally, you could reset safe updates after the script is done
    file.write("SET SQL_SAFE_UPDATES = 1;\n")

print(f"SQL script generated and saved to {sql_file_path}")
