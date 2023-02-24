from configparser import ConfigParser
from pathlib import Path
import psycopg2

config = ConfigParser()
config.read('config.ini')

conn = psycopg2.connect(
    host=config['db']['host'],
    port=config['db']['port'],
    dbname=config['db']['dbname'],
    user=config['db']['user'],
    password=config['db']['password']
)

def getEntries():
    sql_file = Path('sql/get_entries.sql')
    with sql_file.open(mode='r') as file:
        query = file.read()

    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    data = []
    for row in rows:
        data.append({
            'id':row[0],
            'text':row[1]
            })

    return data
def sayHi():
    print("hi!")
