import sqlite3
from DataBase.BaseDados import BaseDados

class ConexaoSQL:

    def conexaoBd():
        BaseDados.gerarBaseDados()
        con = sqlite3.connect('DataBase/baseDados.db')
        print('Conexão com o banco de dados foi estabelecida')
        return con

