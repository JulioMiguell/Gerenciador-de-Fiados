from model.DTO.DividaDTO import DividaDTO
from model.DAO.DividaDAO import DividaDAO
from controller.ClienteCTR import clienteCTR
from controller.ProdutoCTR import ProdutoCTR

class DividaCTR:

    def cadastrarDivida(cliente, produto, qtde, data, total):
        
        dividaDTO = DividaDTO()
        idCliente = clienteCTR.buscarCliente(cliente, True)
        idProduto = ProdutoCTR.buscarProduto(produto, True)
        dividaDTO.idCliente = idCliente
        dividaDTO.idProduto = idProduto
        dividaDTO.qtdeProdutos = qtde
        print('dividaDTO {}'.format(dividaDTO.totalCompras))
        dividaDTO.dataCompra = data
        dividaDTO.totalCompras = total

        dividaDAO = DividaDAO
        dividaDAO.cadastrarDivida(dividaDTO)