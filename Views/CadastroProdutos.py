import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class CadastroProdutos(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.title = 'Tela de cadastro de Clientes'
        self.left = 600
        self.top = 200
        self.width = 400
        self.height = 350 

        self.initUI()
    
    def initUI(self):

        self.labelTitle = QLabel('Cadastrar produtos', self)
        self.labelTitle.setGeometry(70, 10, 300, 50)
        self.labelTitle.setStyleSheet('QLabel {font: 30px; font: bold}')

        self.lbNome = QLabel('Nome', self)
        self.lbNome.setGeometry(20, 80, 100, 50)
        self.lbNome.setStyleSheet('QLabel {font: 20px; font: bold}')

        self.campoNome = QLineEdit(self)
        self.campoNome.setGeometry(100, 93, 210, 30)

        self.lbValor = QLabel('Valor R$:', self)
        self.lbValor.setGeometry(20, 142, 100, 50)
        self.lbValor.setStyleSheet('QLabel {font: 20px; font: bold}')

        self.campoValor = QDoubleSpinBox(self)
        self.campoValor.setGeometry(130, 150, 100, 40)
        self.campoValor.setStyleSheet('QDoubleSpinBox {font: 20px; font: bold}')

        

        self.bntCadastrar = QPushButton('Cadastrar', self)
        self.bntCadastrar.setStyleSheet('QPushButton {font: 20px; font: bold}')
        self.bntCadastrar.setGeometry(126,250,160,50)

        self.setFixedSize(self.width, self.height)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    telaCadastroClientes = CadastroProdutos()
    sys.exit(app.exec_())