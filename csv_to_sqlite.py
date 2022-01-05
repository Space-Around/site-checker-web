import ast
import random
import sqlite3
import pandas as pd


def insert_into_table(cursor, conn, row):
    links = ast.literal_eval(row["sites"])
    
    for link in links:
        file_name = "-".join([str(random.randint(1000, 9999)) for i in range(4)])
        cursor.execute("INSERT INTO t VALUES (?, ?, ?, ?, ?);", (row["kw"], link, file_name, 0, 0))
        conn.commit()

def main():
    conn = sqlite3.connect("alfa_bee.db")
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS t (kw text, sites text, screenshot text, checked text, in_proccess text);")
    conn.commit()
    df = pd.read_csv("kw_links.csv")
    df.agg(lambda row: insert_into_table(cursor, conn, row), axis=1)


if __name__ == "__main__":
    main()