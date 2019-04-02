import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from controller.ClienteCTR import clienteCTR

class CadastroClientes(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.title = 'Tela de cadastro de Clientes'
        self.left = 600
        self.top = 200
        self.width = 450
        self.height = 300
        self.initUI()
    
    def initUI(self):

        self.labelTitle = QLabel('Cadastrar Clientes', self)
        self.labelTitle.setGeometry(70, 10, 400, 50)
        self.labelTitle.setStyleSheet('QLabel {font: 30px; font: bold}')

        self.lbNome = QLabel('Nome', self)
        self.lbNome.setGeometry(20, 90, 100, 50)
        self.lbNome.setStyleSheet('QLabel {font: 23px; font: bold}')

        self.campoNome = QLineEdit(self)
        self.campoNome.setGeometry(100, 93, 270, 40)
        self.campoNome.setStyleSheet('QLineEdit {font: 20px;}')

        self.bntCadastrar = QPushButton('Cadastrar', self)
        self.bntCadastrar.setStyleSheet('QPushButton {font: 20px; font: bold}')
        self.bntCadastrar.setGeometry(50,200,160,50)
        self.bntCadastrar.clicked.connect(self.bntCadastrarClicked)

        self.bntExcluir = QPushButton('Excluir', self)
        self.bntExcluir.setStyleSheet('QPushButton {font: 20px; font: bold}')
        self.bntExcluir.setGeometry(250,200,160,50)
        self.bntExcluir.clicked.connect(self.bntExcluirClicked)


        self.setFixedSize(self.width, self.height)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def bntCadastrarClicked(self):
        self.nomeDigitado = self.campoNome.text()

        if (self.nomeDigitado != ''):
            clienteCTR.cadastrarCliente(self.nomeDigitado.lower())
            avisoCadastro = QMessageBox.information(self, 'Aviso', 'Cliente: {} cadastrado com sucesso!'.format(self.nomeDigitado))
        else:
            aviso = QMessageBox.information(self, 'Atenção!', 'Registro em branco, favor inserir um nome a ser cadastrado')
        

    def bntExcluirClicked(self):
        self.nomeDigitado = self.campoNome.text()
        
        if(self.nomeDigitado == ''):
            aviso = QMessageBox.information(self, 'Atenção!', 'Registro em branco! \n É necessário inserir o nome a ser excluído')
        
        if(clienteCTR.buscarCliente(self.nomeDigitado) == self.nomeDigitado):
            avisoExlusão = QMessageBox.question(self, 'Atenção', 'Você deseja realmente excluir o cliente: {}'.format(self.nomeDigitado), QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if (avisoExlusão == QMessageBox.Yes):
                idCliente = clienteCTR.buscarCliente(self.nomeDigitado)
                print(idCliente)
                clienteCTR.excluirCliente(self.nomeDigitado)

        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    telaCadastroClientes = CadastroClientes()
    sys.exit(app.exec_())