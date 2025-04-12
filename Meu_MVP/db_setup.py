def create_database():
    import mysql.connector
    from config import HOST, USER, PASSWORD

    try:
        connection = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD
        )
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS avaliacao")
        print("Banco de dados 'avaliacao' criado com sucesso (ou já existe).")
        connection.close()
    except mysql.connector.Error as err:
        print(f"Erro ao criar o banco de dados: {err}")

def connect_to_database():
    import mysql.connector
    from config import HOST, USER, PASSWORD, DATABASE

    try:
        connection = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )
        if connection.is_connected():
            print("Successfully connected to the database")
            return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_tables(connection):
    cursor = connection.cursor()
    
    # Table creation with specified columns
    create_table_query = """
    CREATE TABLE IF NOT EXISTS avaliacao (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        criterio VARCHAR(255) NOT NULL,
        tipo VARCHAR(255) NOT NULL,
        nota INT NOT NULL,
        justificativa TEXT,
        data DATE NOT NULL
    )
    """
    
    cursor.execute(create_table_query)
    connection.commit()
    print("Tabela 'avaliacao' criada com sucesso")

def initialize_database():
    create_database()  # Cria o banco de dados, se necessário
    connection = connect_to_database()
    if connection:
        create_tables(connection)
        connection.close()

if __name__ == "__main__":
    initialize_database()