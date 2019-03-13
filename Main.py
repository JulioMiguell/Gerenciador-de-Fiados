from Views.TelaPrincipal import *

if __name__ == "__main__":

    app = QApplication(sys.argv)
    telaPrincipal = TelaPrincipal()
    sys.exit(app.exec_())