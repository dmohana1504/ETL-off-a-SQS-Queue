import psycopg2

def connect_to_database():
    """Establish a connection to the PostgreSQL database and return the connection object."""
    connection = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='postgres',
        host='localhost',
        port='5432'
    )
    return connection

def create_table():
    """Create the 'user_logins' table in the database."""
    connection = None
    cursor = None
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        
        create_table_query = """
        CREATE TABLE IF NOT EXISTS user_logins(
            user_id varchar(128),
            device_type varchar(32),
            masked_ip varchar(256),
            masked_device_id varchar(256),
            locale varchar(32),
            app_version varchar(32),
            create_date date
        );
        """


        cursor.execute(create_table_query)
        connection.commit()
        
    except Exception as error:
        print("Error while creating the table:", error)
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def store_data_in_postgres(data: dict):
    """Store the processed data in a Postgres database."""
    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        insert_query = """INSERT INTO user_logins (user_id, device_type, masked_ip, 
                          masked_device_id, locale, app_version, create_date) 
                          VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        record_to_insert = (
            data.get('user_id'), 
            data.get('device_type'), 
            data.get('masked_ip'),  # Use the masked IP
            data.get('masked_device_id'),  # Use the masked device ID
            data.get('locale'), 
            data.get('app_version'), 
            data.get('create_date', None)  # provide None if the field doesn't exist
        )
        cursor.execute(insert_query, record_to_insert)
        
        connection.commit()
        cursor.close()
        connection.close()
    except Exception as error:
        print("Error while storing data in Postgres:", error)
