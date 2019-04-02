import sqlite3
from DataBase.ConexaoSQL import ConexaoSQL

class DividaDAO:

    def cadastrarDivida(divida):

        con = ConexaoSQL.conexaoBd()
        cur = con.cursor()

        query = """
        INSERT INTO dividas (id_cliente_fk, id_produto_fk, qtde, data, total)
        VALUES ('{}', '{}','{}', '{}', '{}')
        """.format(divida.idCliente, divida.idProduto, divida.qtdeProdutos, divida.dataCompra, divida.totalCompras)

        cur.execute(query)
        con.commit()
        print('Divida cadastrada com sucesso!')