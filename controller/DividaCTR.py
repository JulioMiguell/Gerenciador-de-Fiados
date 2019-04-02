from model.DTO.DividaDTO import DividaDTO
from model.DAO.DividaDAO import DividaDAO
from controller.ClienteCTR import clienteCTR
from controller.ProdutoCTR import ProdutoCTR

class DividaCTR:

    def cadastrarDivida(cliente, produto, qtde, data, total):
        
        dividaDTO = DividaDTO()
        dividaDTO.nomeCliente = cliente
        dividaDTO.nomeProduto = produto
        dividaDTO.qtdeProdutos = qtde
        print('dividaDTO {}'.format(dividaDTO.totalCompras))
        dividaDTO.dataCompra = data
        dividaDTO.totalCompras = total

        dividaDAO = DividaDAO
        dividaDAO.cadastrarDivida(dividaDTO)

    def buscarDivida(cliente):
        dividaDTO = DividaDTO()
        dividaDTO.nomeCliente = cliente
        
        dividaDAO = DividaDAO

        return dividaDAO.buscarDivida(dividaDTO)
    
    def obterDividaTotal(cliente):
        dividaDTO = DividaDTO()
        dividaDTO.nomeCliente = cliente

        dividaDAO = DividaDAO

        return dividaDAO.obterDividaTotal(dividaDTO)
    
    def quitarDivida(cliente):
        dividaDTO = DividaDTO()
        dividaDTO.nomeCliente = cliente

        dividaDAO = DividaDAO

        dividaDAO.quitarDivida(dividaDTO)

        