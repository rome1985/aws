import pymysql

host = "bd-rome.cb4448em843u.us-east-2.rds.amazonaws.com"
user = "rome"
passw = "Mozilla1985*"
db_name = "db_users"

def connection_SQL():
    try:
        connection = pymysql.connect(
            host=host,
            user=user,
            password=passw,
            database=db_name
        )
        print("Succesfull connection to database")
        return connection
    except Exception as err:
        print("Error", err)
        return None
       
def insert():
    try:
        instruction = "INSERT INTO users VALUES (531,'calos','Eduardo','1985-12-15');"
        connection = connection_SQL()
        cursor = connection.cursor()
        cursor.execute(instruction)
        connection.commit()
        print("User added")
    except Exception as err:
        print("Error", err)
        return None        