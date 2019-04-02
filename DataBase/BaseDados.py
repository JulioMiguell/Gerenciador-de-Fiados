import sqlite3

class BaseDados:

    def gerarBaseDados():

        try:
            con = sqlite3.connect('DataBase/baseDados.db')

            cur = con.cursor()

            sqlClientes = """
            CREATE TABLE clientes (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE)
                """

            cur.execute(sqlClientes)
            con.commit()

            sqlProdutos = """
            CREATE TABLE produtos (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, 
            valor REAL NOT NULL)
                """
            cur.execute(sqlProdutos)
            con.commit()

            sqlDividas = """
	    CREATE TABLE dividas (
	    "nome_cliente"	TEXT NOT NULL,
	    "nome_produto"	TEXT NOT NULL,
	    "qtde"	INTEGER NOT NULL,
	    "data"	TEXT NOT NULL,
	    "total"	INTEGER NOT NULL
	
        )
        """

            cur.execute(sqlDividas)
            con.commit()

            con.close()
        except sqlite3.OperationalError:
            print('A base já existe')
            return False

if __name__ == '__main__':
    baseDados = BaseDados
    baseDados.gerarBaseDados()
