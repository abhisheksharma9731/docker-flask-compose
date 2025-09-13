from flask import Flask
import os
import psycopg2

app = Flask(__name__)

# Get DB config from environment variables
DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("POSTGRES_DB", "mydb")
DB_USER = os.getenv("POSTGRES_USER", "user")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "password")

@app.route("/")
def home():
    return "🚀 Flask + Docker + PostgreSQL demo is running!"

@app.route("/db")
def test_db():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()
        cur.close()
        conn.close()
        return f"✅ Connected to PostgreSQL! Version: {version}"
    except Exception as e:
        return f"❌ Database connection failed: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
