import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class TelaFiado(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Dividas dos clientes'
        self.left = 300
        self.top = 100
        self.width = 600
        self.height = 600 
        
        self.initUI()

    def initUI(self):
        
        self.lbBuscarCliente = QPushButton('Buscar cliente ', self)
        self.lbTotal = QLabel(' DÍVIDA TOTAL R$: 00,00 ', self)
        self.lbTotal.setStyleSheet('QLabel {font: bold; font: 20px; background-color: #26C281; border-radius: 5px}')
        self.lbBuscarCliente.setStyleSheet('QPushButton {font: bold; font: 20px;}')

        self.campoBuscaCliente = QLineEdit(self)
        #self.campoBuscaCliente.setGeometry(0,0,200,50)

        self.tabela = self.createTable()

        self.widget = QWidget(self)
        layout = QGridLayout()
        self.widget.setLayout(layout)
        layout.addWidget(self.tabela,2,0,20,15)
        layout.addWidget(self.lbBuscarCliente,0,1)
        layout.addWidget(self.campoBuscaCliente,0,2)
        layout.addWidget(self.lbTotal,1,1)
        
        

        self.setCentralWidget(self.widget)

        

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
    
    def createTable(self):
        self.tableDividas = QTableWidget(self)
        self.tableDividas.setRowCount(15)
        self.tableDividas.setColumnCount(5)
        self.tableDividas.setItem(0,0,QTableWidgetItem('NOME'))
        self.tableDividas.setItem(0,1,QTableWidgetItem('PRODUTO'))
        self.tableDividas.setItem(0,2,QTableWidgetItem('QTDE'))
        self.tableDividas.setItem(0,3,QTableWidgetItem('DATA DA COMPRA'))
        self.tableDividas.setItem(0,4,QTableWidgetItem('TOTAL R$'))

        self.tableDividas.setEditTriggers(QTableWidget.NoEditTriggers) #bloqueia todas as celulas

        self.tableDividas.setStyleSheet('QTableWidget {font: 15px; font: bold}')
        
        return self.tableDividas

if __name__ == '__main__':
    app = QApplication(sys.argv)
    telaFiado = TelaFiado()
    sys.exit(app.exec_())



        