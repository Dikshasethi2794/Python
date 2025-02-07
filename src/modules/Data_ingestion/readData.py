"""from src.models.data_model import load_csv
from src.db.connection import create_connection

def ingest_data(file_path):
    # Load data from CSV
    df = load_csv(file_path)
    
    # Process data (example: fill missing values)
    df.fillna(0, inplace=True)
    
    # Insert data into MySQL
    connection = create_connection()
    cursor = connection.cursor()
    
    for _, row in df.iterrows():
        cursor.execute(
            "INSERT INTO your_table_name (column1, column2, column3) VALUES (%s, %s, %s)",
            (row['column1'], row['column2'], row['column3'])
        )
    
    connection.commit()
    cursor.close()
    connection.close()"""