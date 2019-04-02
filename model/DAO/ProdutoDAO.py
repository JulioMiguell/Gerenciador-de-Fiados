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
    
    def listarProdutos():
        con = ConexaoSQL.conexaoBd()
        cur = con.cursor()

        query = """
        SELECT nome, id
        FROM produtos
        """

        cur.execute(query)

        data = cur.fetchall()
        
        return data
    
    def buscarProduto(nome):
        try:
            con = ConexaoSQL.conexaoBd()
            cur = con.cursor()

            query = """
            SELECT nome
            FROM produtos
            WHERE nome = '{}'
            """.format(nome)
            cur.execute(query)
            data = cur.fetchone()
            print(data[1])
            
            return data[0]
        except TypeError:
            print('Retorno da funcao buscarProdutos() vazio')
    
    def obterValor(nome):
        con = ConexaoSQL.conexaoBd()
        cur = con.cursor()

        query = """
        SELECT valor
        from produtos
        where nome = '{}'
        """.format(nome)

        cur.execute(query)

        data = cur.fetchone()
        print(data)
        
        return data[0]

        
        