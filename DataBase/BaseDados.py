import sqlite3

class BaseDados:

    def gerarBaseDados():

        try:
            con = sqlite3.connect('DataBase/baseDados.db')

            cur = con.cursor()

            sql = """
            CREATE TABLE clientes (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE)
                """

            cur.execute(sql)
            con.commit()
            con.close()
        except sqlite3.OperationalError:
            print('A base já existe')
            return False

if __name__ == '__main__':
    baseDados = BaseDados
    baseDados.gerarBaseDados()
