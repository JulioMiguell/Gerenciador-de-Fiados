from model.DTO.ClienteDTO import ClienteDTO
from model.DAO.ClienteDAO import ClienteDAO

class clienteCTR:

    def buscarCliente(nome, id = False):
        clienteDAO = ClienteDAO
        return clienteDAO.buscarCliente(nome, id)

    def cadastrarCliente(nome):
        clienteDTO = ClienteDTO()
        clienteDTO.Nome = nome

        clienteDAO = ClienteDAO
        clienteDAO.cadastrarCliente(clienteDTO)

    def excluirCliente(nome):
        clienteDTO = ClienteDTO()
        ClienteDTO.Nome = nome

        clienteDAO = ClienteDAO
        clienteDAO.excluirCliente(clienteDTO)