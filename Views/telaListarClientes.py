import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from controller.ClienteCTR import clienteCTR

class TelaListarClientes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Lista de clientes cadastrados'
        self.left = 300
        self.top = 100
        self.width = 300
        self.height = 500

        self.nomeDigitado = None
        
        self.initUI()

    def initUI(self):

        self.tabela = self.createTable()
        self.listarClientes()

        self.widget = QWidget(self)
        layout = QGridLayout()
        self.widget.setLayout(layout)
        layout.addWidget(self.tabela,3,0,20,25)
        self.setCentralWidget(self.widget)

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
    
    def createTable(self):
        self.tableDividas = QTableWidget(self)
        self.tableDividas.setRowCount(30)
        self.tableDividas.setColumnCount(2)
        self.tableDividas.setItem(0,0,QTableWidgetItem('Id'))
        self.tableDividas.setItem(0,1,QTableWidgetItem('Nome'))
        
        self.tableDividas.setEditTriggers(QTableWidget.NoEditTriggers) #bloqueia todas as celulas

        self.tableDividas.setStyleSheet('QTableWidget {font: 14px; font: bold}')
        
        return self.tableDividas

    def listarClientes(self):
        clientes = clienteCTR.listaClientes()

        for linha in range(len(clientes)):
            for coluna in range(2):
                self.tabela.setItem((linha+1), coluna, QTableWidgetItem('{}'.format(clientes[linha][coluna])) )

if __name__ == '__main__':
    app = QApplication(sys.argv)
    telaFiado = TelaFiado()
    sys.exit(app.exec_())
