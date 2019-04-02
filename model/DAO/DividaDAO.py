import sqlite3
from DataBase.ConexaoSQL import ConexaoSQL

class DividaDAO:

    def cadastrarDivida(divida):

        con = ConexaoSQL.conexaoBd()
        cur = con.cursor()

        query = """
        INSERT INTO dividas (nome_cliente, nome_produto, qtde, data, total)
        VALUES ('{}', '{}','{}', '{}', '{}')
        """.format(divida.nomeCliente, divida.nomeProduto, divida.qtdeProdutos, divida.dataCompra, divida.totalCompras)

        cur.execute(query)
        con.commit()
        print('Divida cadastrada com sucesso!')
    
    def buscarDivida(divida):
        
        con = ConexaoSQL.conexaoBd()
        cur = con.cursor()

        query = """
        SELECT* 
        FROM dividas
        WHERE nome_cliente = '{}'
        """.format(divida.nomeCliente)

        cur.execute(query)
        data = cur.fetchall()

        return data

    def obterDividaTotal(divida):
        con = ConexaoSQL.conexaoBd()
        cur = con.cursor()

        query = """
        SELECT SUM(total)
        FROM dividas
        WHERE nome_cliente = '{}'
        """.format(divida.nomeCliente)

        cur.execute(query)
        data = cur.fetchone()

        return data[0]

    def quitarDivida(divida):
        con = ConexaoSQL.conexaoBd()
        cur = con.cursor()

        query = """
        DELETE
        FROM dividas
        WHERE nome_cliente = '{}'
        """.format(divida.nomeCliente)

        cur.execute(query)
        con.commit()

        