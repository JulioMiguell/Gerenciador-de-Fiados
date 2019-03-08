import sqlite3
from DataBase.ConexaoSQL import ConexaoSQL


class ProdutoDAO:
    
    def cadastrarProduto(produto):

        con = ConexaoSQL.conexaoBd()
        cur = con.cursor()

        query = """
        INSERT INTO produtos (nome, valor)
        VALUES ('{}', '{}')
        """.format(produto.Nome, produto.Valor)

        cur.execute(query)
        con.commit()
        print('Produtos cadastrados com sucesso')

        
        