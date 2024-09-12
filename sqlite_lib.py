import sqlite3

conn: any = None
cursor: any = None


def connect(file_name: str) -> any:
    global conn, cursor
    conn = sqlite3.connect('hw16.db')
    conn.row_factory = sqlite3.Row  # allow to use column names
    cursor = conn.cursor()  # Create cursor


def run_query_select(query: str) -> list[tuple]:
    cursor.execute(query)
    columns = cursor.fetchall()
    result = [tuple(row) for row in columns]
    return result


def run_query_update(query: str) -> None:
    cursor.execute(query)
    cursor.connection.commit()


def close():
    cursor.close()

