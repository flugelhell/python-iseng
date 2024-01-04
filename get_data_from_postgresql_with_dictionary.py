host = "192.168.1.1"
database = "database_name"
user = "database_user"
passwd = "database_password"
port = "database_port"

def get_data():
    # Connection String
    conn = psycopg2.connect(
        database=database,
        user=user,
        password=passwd,
        host=host,
        port=port,
    )
    
    query = f"""
    select * from tbl_users;
    """
    # print(query)
    cursor = conn.cursor()
    cursor.execute(query)
    # Fetch all results as dictionaries
    columns = [column[0] for column in cursor.description]
    results = [dict(zip(columns, row)) for row in cursor.fetchall()]

    cursor.close()
    conn.close()
    return results

users = get_data()
for user in users:
    print(user.get('name'))