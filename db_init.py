import sqlite3 as sl


def get_connection():
    return sl.connect('docdoc.db')


def create_table_doctors():
    connection = get_connection()
    with connection:
        connection.execute("""
                    CREATE TABLE IF NOT EXISTS doctors (
                       id INTEGER PRIMARY KEY,
                       name TEXT,
                       clinic_id INTEGER,
                       spec_id INTEGER,
                       rating REAL,

            );
                """)


def create_table_clinics():
    connection = get_connection()
    with connection:
        connection.execute("""
                        CREATE TABLE IF NOT EXISTS clinics (
                           id INTEGER PRIMARY KEY,
                           name TEXT,
                           rating REAL,

                );
                    """)


def create_table_specs():
    connection = get_connection()
    with connection:
        connection.execute("""
                            CREATE TABLE IF NOT EXISTS specs (
                               id INTEGER PRIMARY KEY,
                               name TEXT,
                               clinic_id INTEGER,

                    );
                        """)
