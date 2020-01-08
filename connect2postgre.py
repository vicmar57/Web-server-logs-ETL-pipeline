import psycopg2

DB_NAME = "serv_logs"
conn = psycopg2.connect("dbname=" + DB_NAME + " user=postgres password=admin")

# Create a cursor object
cur = conn.cursor()
query = """
    CREATE TABLE IF NOT EXISTS logs (
      raw_log TEXT NOT NULL UNIQUE,
      remote_addr TEXT,
      time_local TEXT,
      request_type TEXT,
      request_path TEXT,
      status INTEGER,
      body_bytes_sent INTEGER,
      http_referer TEXT,
      http_user_agent TEXT,
      created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
      )
    """
try:
    cur.execute(query)
    # close communication with the PostgreSQL database server
    cur.close()
    # commit the changes
    conn.commit()
    # NB : you won't get an IntegrityError when reading
except (Exception, psycopg2.DatabaseError) as e:
    print(e)
