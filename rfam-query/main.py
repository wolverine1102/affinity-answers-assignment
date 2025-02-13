import mysql.connector
from mysql.connector import errorcode
from db.connect import get_connection
from queries.queries import QUERIES
from results.save_results import save_to_file


def main():
    try:
        conn = get_connection()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

    cursor = conn.cursor()

    for query in QUERIES.values():
        cursor.execute(query)
        print(cursor.fetchall())

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()