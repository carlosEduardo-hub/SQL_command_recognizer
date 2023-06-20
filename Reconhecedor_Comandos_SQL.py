import re

# Função para obter o próximo token da entrada
def get_next_token(comando):
    comando = comando.strip()

    # Expressões regulares para identificar os tokens
    padrao_create_database = r"^CREATE\s+DATABASE\s+(\w+);$"
    padrao_use = r"^USE\s+(\w+);$"
    padrao_create_table = r"^CREATE\s+TABLE\s+(\w+)\s+\(((?:\w+\s+\w+\s*(?:,\s*)?)*)\);$"
    padrao_insert_into = r"^INSERT\s+INTO\s+(\w+)\s+\(((?:\w+\s*(?:,\s*)?)*)\)\s+VALUES\s+\(((?:[\w\s\"]+\s*(?:,\s*)?)*)\);$"
    padrao_select_from = r"^SELECT\s+(\*|(?:\w+\s*(?:,\s*)?)*)\s+FROM\s+(\w+)(?:\s+ORDER\s+BY\s+(\w+))?(?:\s+WHERE\s+(\w+)\s*=\s*([\w\s\"]+))?;$"
    padrao_update_set_where = r"^UPDATE\s+(\w+)\s+SET\s+(\w+)\s+=\s+([\w\s\"]+)\s+WHERE\s+(\w+)\s+=\s+([\w\s\"]+);$"
    padrao_delete_from_where = r"^DELETE\s+FROM\s+(\w+)\s+WHERE\s+(\w+)\s+=\s+([\w\s\"]+);$"
    padrao_truncate_table = r"^TRUNCATE\s+TABLE\s+(\w+);$"

    # Verificar padrões para cada comando
    if re.match(padrao_create_database, comando):
        return "CREATE DATABASE"
    elif re.match(padrao_use, comando):
        return "USE"
    elif re.match(padrao_create_table, comando):
        return "CREATE TABLE"
    elif re.match(padrao_insert_into, comando):
        return "INSERT INTO"
    elif re.match(padrao_select_from, comando):
        return "SELECT"
    elif re.match(padrao_update_set_where, comando):
        return "UPDATE"
    elif re.match(padrao_delete_from_where, comando):
        return "DELETE"
    elif re.match(padrao_truncate_table, comando):
        return "TRUNCATE TABLE"
    else:
        return "INVALID"

# Função para analisar o comando SQL
def parse_command(comando):
    token = get_next_token(comando)

    if token == "CREATE DATABASE":
        match = re.match(r"^CREATE\s+DATABASE\s+(\w+);$", comando)
        if match:
            database_name = match.group(1)
            print(f"Criando o banco de dados '{database_name}'")
        else:
            print("Comando inválido")

    elif token == "USE":
        match = re.match(r"^USE\s+(\w+);$", comando)
        if match:
            database_name = match.group(1)
            print(f"Usando o banco de dados '{database_name}'")
        else:
            print("Comando inválido")

    elif token == "CREATE TABLE":
        match = re.match(r"^CREATE\s+TABLE\s+(\w+)\s+\(((?:\w+\s+\w+\s*(?:,\s*)?)*)\);$", comando)
        if match:
            table_name = match.group(1)
            column_definitions = match.group(2).split(", ")
            print(f"Criando a tabela '{table_name}' com as colunas:")
            for column_definition in column_definitions:
                print(f"- {column_definition}")
        else:
            print("Comando inválido")

    elif token == "INSERT INTO":
        match = re.match(r"^INSERT\s+INTO\s+(\w+)\s+\(((?:\w+\s*(?:,\s*)?)*)\)\s+VALUES\s+\(((?:[\w\s\"]+\s*(?:,\s*)?)*)\);$", comando)
        if match:
            table_name = match.group(1)
            columns = match.group(2).split(", ")
            values = match.group(3).split(", ")
            print(f"Inserindo dados na tabela '{table_name}':")
            for column, value in zip(columns, values):
                print(f"- {column}: {value}")
        else:
            print("Comando inválido")

    elif token == "SELECT":
        match = re.match(r"^SELECT\s+(\*|(?:\w+\s*(?:,\s*)?)*)\s+FROM\s+(\w+)(?:\s+ORDER\s+BY\s+(\w+))?(?:\s+WHERE\s+(\w+)\s*=\s*([\w\s\"]+))?;$", comando)
        if match:
            select_columns = match.group(1)
            table_name = match.group(2)
            order_by_column = match.group(3)
            where_column = match.group(4)
            where_value = match.group(5)
            print("Executando comando SELECT:")
            if select_columns == "*":
                print(f"Selecionar todas as colunas da tabela '{table_name}'")
            else:
                selected_columns = select_columns.split(", ")
                print(f"Selecionar as colunas:")
                for column in selected_columns:
                    print(f"- {column}")
            print(f"Da tabela '{table_name}'")
            if order_by_column:
                print(f"Ordenar por coluna: {order_by_column}")
            if where_column and where_value:
                print(f"Condição WHERE: {where_column} = {where_value}")
        else:
            print("Comando inválido")

    elif token == "UPDATE":
        match = re.match(r"^UPDATE\s+(\w+)\s+SET\s+(\w+)\s+=\s+([\w\s\"]+)\s+WHERE\s+(\w+)\s+=\s+([\w\s\"]+);$", comando)
        if match:
            table_name = match.group(1)
            set_column = match.group(2)
            set_value = match.group(3)
            where_column = match.group(4)
            where_value = match.group(5)
            print(f"Executando comando UPDATE na tabela '{table_name}':")
            print(f"Definir coluna '{set_column}' como '{set_value}'")
            print(f"Condição WHERE: {where_column} = {where_value}")
        else:
            print("Comando inválido")

    elif token == "DELETE":
        match = re.match(r"^DELETE\s+FROM\s+(\w+)\s+WHERE\s+(\w+)\s+=\s+([\w\s\"]+);$", comando)
        if match:
            table_name = match.group(1)
            where_column = match.group(2)
            where_value = match.group(3)
            print(f"Executando comando DELETE na tabela '{table_name}':")
            print(f"Condição WHERE: {where_column} = {where_value}")
        else:
            print("Comando inválido")

    elif token == "TRUNCATE TABLE":
        match = re.match(r"^TRUNCATE\s+TABLE\s+(\w+);$", comando)
        if match:
            table_name = match.group(1)
            print(f"Executando comando TRUNCATE TABLE na tabela '{table_name}'")
        else:
            print("Comando inválido")

    else:
        print("Comando inválido")

# Função principal (main)
def main():
    while True:
        comando = input("Digite um comando SQL: ")
        if comando == "sair":
            break
        parse_command(comando)

# Executar a função principal
main()
