import os
import dotenv
import psycopg2

dotenv.load_dotenv()
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

def connect_to_db():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

def fetch_places():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT place_id, name, description FROM place")
    places = cursor.fetchall()
    cursor.close()
    conn.close()
    return [{"place_id": str(row[0]), "name": row[1], "description": row[2]} for row in places]
