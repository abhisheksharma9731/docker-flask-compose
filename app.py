from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Flask with Docker & Postgres!"

@app.route("/db")
def db_check():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB", "mydb"),
            user=os.getenv("POSTGRES_USER", "user"),
            password=os.getenv("POSTGRES_PASSWORD", "password"),
            host="db",  # service name in docker-compose
            port=5432
        )
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()
        cur.close()
        conn.close()
        return f"Connected to Postgres! Version: {version}"
    except Exception as e:
        return f"DB connection failed: {e}"

if __name__ == "__main__":
    # must bind to 0.0.0.0 so container exposes it
    app.run(host="0.0.0.0", port=5000)
