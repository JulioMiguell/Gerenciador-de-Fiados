import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Views.CadastroClientes import CadastroClientes
from Views.CadastroProdutos import CadastroProdutos
from Views.TelaFiado import TelaFiado
from Views.telaListarClientes import TelaListarClientes
from controller.ProdutoCTR import ProdutoCTR
from controller.ClienteCTR import clienteCTR
from controller.DividaCTR import DividaCTR
import threading

class TelaPrincipal(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.title = 'Tela Principal | Bem-vindo'
        self.left = 300
        self.top = 100
        self.width = 840
        self.height = 480 

        self.flagAcesso = 0
        self.clienteLocalizado = False

        self.initUI()

    def initUI(self):

        self.labelTitle = QLabel('Fiados', self)
        self.labelTitle.setGeometry(330,10,200,70)
        self.labelTitle.setStyleSheet('QLabel {font: 60px; font: bold}')

        self.campoBuscaCliente = QLineEdit(self)
        self.campoBuscaCliente.setGeometry(280,100,300,40)

        self.bntBuscarCliente = QPushButton('Buscar Cliente ', self)
        self.bntBuscarCliente.setGeometry(120,100,130,40)
        self.bntBuscarCliente.setStyleSheet('QPushButton {font: bold; font: 16px}')
        self.bntBuscarCliente.clicked.connect(self.bntBuscarClienteClicked)


        self.bntAddProdutos = QPushButton(' Add Produto', self)
        self.bntAddProdutos.setGeometry(120,170,130,40)
        self.bntAddProdutos.setStyleSheet('QPushButton {font: bold; font: 16px;}')
        self.bntAddProdutos.clicked.connect(self.bntAddProdutosClicked)
        
        self.boxProdutos = QComboBox(self)
        self.boxProdutos.setGeometry(280,170,140,40)
        self.boxProdutos.setStyleSheet('QComboBox {font: bold; font: 15px;}')
        self.listaProdutos()
        
        self.lbQtde = QLabel('Qtde:', self)
        self.lbQtde.setGeometry(460,170,50,40)
        self.lbQtde.setStyleSheet('QLabel {font: bold; font: 16px; border-radius: 5px; background: #D2D7D3}')

        self.spinQtde = QSpinBox(self)
        self.spinQtde.setGeometry(520,170,60,40)
        self.spinQtde.setStyleSheet('QSpinBox {font: bold; font: 16px;}')

        self.boxData = QDateEdit(self)
        self.boxData.setGeometry(280,240,300,40)
        self.boxData.setStyleSheet('QDateEdit {font: 16px; font: bold}')
        self.boxData.setDisplayFormat('dd-MMM-yyyy')   

        self.boxData.setDate(QDate.currentDate())

        self.lbDataCompra = QLabel('Data da compra', self)
        self.lbDataCompra.setGeometry(120,240,130,40)
        self.lbDataCompra.setStyleSheet('QLabel {font: bold; font: 17px; border-radius: 5px; background: #D2D7D3}')

        self.lbTotal = QLabel('Valor a receber: R$ 00,00', self)
        self.lbTotal.setStyleSheet('QLabel {color: white; font: bold; font: 25px; background: #26C281; border-radius: 10px}')
        self.lbTotal.setGeometry(280,310,300,60)

        self.bntVender = QPushButton('Realizar Venda', self)
        self.bntVender.setStyleSheet('QPushButton {font: 20px; font: bold}')
        self.bntVender.setGeometry(350,400,160,50)
        self.bntVender.clicked.connect(self.bntVenderClicked)

        #Linha vertical (apenas para manter organizado)
        self.line =QLabel('', self)
        self.line.setGeometry(650, 0, 5, 480)
        self.line.setStyleSheet('QLabel { background: #22313F}')

        self.imagemLabel = QLabel(self)
        pixmap = QPixmap('Views/imagens/money.png')
        self.imagemLabel.setPixmap(pixmap)
        self.imagemLabel.setGeometry(675,10,147,152)

        self.bntVerQuitarFiados = QPushButton('Ver|Quitar Fiados', self)
        self.bntVerQuitarFiados.setStyleSheet('QPushButton {font: 16px; font: bold}')
        self.bntVerQuitarFiados.setGeometry(665,155,165,50)
        self.bntVerQuitarFiados.clicked.connect(self.bntVerQuitarFiadosClicked)

        self.bntListarClientes = QPushButton('Listar clientes', self)
        self.bntListarClientes.setStyleSheet('QPushButton {font: 16px; font: bold}')
        self.bntListarClientes.setGeometry(690,230,120,50)
        self.bntListarClientes.clicked.connect(self.bntListarClientesClicked)

        #Seção de cadastrar clientes e produtos
        self.lbCadastrar = QLabel(' Cadastrar/Alterar: ', self)
        self.lbCadastrar.setStyleSheet('QLabel {font: 18px; font: bold; background: #4B77BE; border-radius: 5px}')
        self.lbCadastrar.setGeometry(665,310,170,40)
        
        self.bntClientes = QPushButton('Clientes', self)
        self.bntClientes.setStyleSheet('QPushButton {font: 20px; font: bold}')
        self.bntClientes.setGeometry(690,360,120,50)
        self.bntClientes.clicked.connect(self.bntCadastrarClientesClicked)
        
        self.bntProdutos = QPushButton('Produtos', self)
        self.bntProdutos.setGeometry(690,420,120,50)
        self.bntProdutos.setStyleSheet('QPushButton {font: 20px; font: bold}')
        self.bntProdutos.clicked.connect(self.bntCadastrarProdutosClicked)
        
        self.setFixedSize(self.width, self.height)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
    
    def bntVerQuitarFiadosClicked(self):
        self.telaFiados = TelaFiado()


    def bntCadastrarClientesClicked(self):
        self.telaCadastrocliente = CadastroClientes()
        
    def bntListarClientesClicked(self):
        self.telaListarClientes = TelaListarClientes()

    def bntBuscarClienteClicked(self):
        self.nomeDigitado = self.campoBuscaCliente.text().lower()
        if(self.nomeDigitado == clienteCTR.buscarCliente(self.nomeDigitado)):
            self.clienteLocalizado = True
            aviso = QMessageBox.information(self, '', 'Cliente {}, localizado '.format(self.nomeDigitado))
            self.campoBuscaCliente.setStyleSheet('QLineEdit {background: #2ECC71}')
        else:
            aviso = QMessageBox.information(self, 'Atenção!', 'Cliente {} NÃO localizado '.format(self.nomeDigitado))
            self.campoBuscaCliente.setStyleSheet('QLineEdit {background: #F22613}')

    def bntAddProdutosClicked(self):
        self.boxProdutos.setStyleSheet('QComboBox{background: #26A65B}')
        self.nomeProduto = self.boxProdutos.currentText()
        self.qtdeProdutos = self.spinQtde.value()
        self.valorProduto = ProdutoCTR.obterValor(self.nomeProduto)
        self.lbTotal.setText('Valor a receber: R$ {:0.2f}'.format(self.qtdeProdutos*self.valorProduto))
        aviso = QMessageBox.information(self, 'Aviso: ', 'Produto {} adicionado!'.format(self.boxProdutos.currentText()))
        

    def bntVenderClicked(self):

        aviso = QMessageBox.question(self, 'Atenção', 'Você deseja realmente registrar esta venda?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if (aviso == QMessageBox.Yes):

            if(self.clienteLocalizado == True and self.spinQtde.value() != 0):
                self.nomeCliente = self.campoBuscaCliente.text().lower()
                self.nomeProduto = self.boxProdutos.currentText()
                print(self.nomeProduto)
                self.qtdeProdutos = self.spinQtde.value()
                print('Quantidade produtos {}'.format(self.qtdeProdutos))
                self.dataCompra = self.boxData.date().toString('dd-MMM-yyyy')
                #self.dataCompra = self.dataCompra.toString("dd-MMM-yyyy")
                print(self.dataCompra)
                self.valorProduto = ProdutoCTR.obterValor(self.nomeProduto)
                self.totalCompras = self.qtdeProdutos * self.valorProduto
                DividaCTR.cadastrarDivida(self.nomeCliente, self.nomeProduto, self.qtdeProdutos, self.dataCompra, self.totalCompras )

                aviso = QMessageBox.information(self, 'Aviso: ', 'A venda foi registrada com sucesso')
            else:
                aviso = QMessageBox.information(self, 'Aviso: ', 'Verificar os campos antes de realizar venda')
    def bntCadastrarProdutosClicked(self):
        telaCadastroProdutos = CadastroProdutos()
        telaCadastroProdutos.exec_()
        print(telaCadastroProdutos.bntCadastrarClickedStatus)
        if(telaCadastroProdutos.bntCadastrarClickedStatus):
            self.listaProdutos()


    def listaProdutos(self):
        self.produtos = ProdutoCTR.listarProdutos()
        self.tamListaProdutos = len(ProdutoCTR.listarProdutos())
        
        if (self.flagAcesso == 0):
            for i in self.produtos:
                self.boxProdutos.addItem(i[0])
            
            self.flagAcesso += 1
        
        else:
            self.boxProdutos.addItem(self.produtos[self.tamListaProdutos-1][0])
         
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    telaPrincipal = TelaPrincipal()
    sys.exit(app.exec_())