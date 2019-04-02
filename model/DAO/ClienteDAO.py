import sqlite3
import os
from DataBase.ConexaoSQL import ConexaoSQL

class ClienteDAO:

    def buscarCliente(nome):
        try:
            con = ConexaoSQL.conexaoBd()
            cur = con.cursor()

            query = """
            SELECT id, nome
            FROM clientes
            WHERE nome = '{}'
            """.format(nome)
            cur.execute(query)
            data = cur.fetchone()
    
            return data[1]
        except TypeError:
            print('Retorno da funcao buscarCliente() vazio')

    def cadastrarCliente(cliente):
        con = ConexaoSQL.conexaoBd()
        cur = con.cursor()

        query = """
        INSERT INTO clientes (nome)
        VALUES ('{}')
        """.format(cliente.Nome)

        cur.execute(query)
        con.commit()
        print('Dados cadastrados com sucesso')

    def excluirCliente(nome):
        con = ConexaoSQL.conexaoBd()
        cur = con.cursor()

        query = """
        DELETE
        FROM clientes
        WHERE nome = '{}'
        """.format(nome)

        cur.execute(query)
        con.commit()

    def listarClientes():
        try:
            con = ConexaoSQL.conexaoBd()
            cur = con.cursor()

            query = """
            SELECT id, nome
            FROM clientes
            """
            cur.execute(query)
            data = cur.fetchall()
    
            return data
        except TypeError:
            print('Retorno da funcao buscarCliente() vazio')

    

