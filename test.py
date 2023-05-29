import random
import psycopg2

# Connect to PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="your_password"
)

# Create a table to store processed data if it doesn't exist
create_table_query = """
    CREATE TABLE IF NOT EXISTS processed_data (
        id SERIAL PRIMARY KEY,
        data TEXT NOT NULL
    )
"""
with conn.cursor() as cursor:
    cursor.execute(create_table_query)
    conn.commit()

# Check if data has been processed before
def check_data_processed(data):
    with conn.cursor() as cursor:
        cursor.execute("SELECT id FROM processed_data WHERE data = %s", (data,))
        return cursor.fetchone() is not None

# Generate random number list
def generate_random_list(length):
    return [random.randint(1, 100) for _ in range(length)]

# Save processed data to the database
def save_processed_data(data):
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO processed_data (data) VALUES (%s)", (data,))
        conn.commit()

# Example usage
random_list = generate_random_list(10)
random_list_str = ', '.join(str(num) for num in random_list)

if check_data_processed(random_list_str):
    print("Data already processed!")
else:
    save_processed_data(random_list_str)
    print("Data processed and saved!")

# Close the database connection
conn.close()
