from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit
import sys
class CadastroProduto(QWidget):
    # Método init para inicializar a nossa janela
    def __init__(self):
        super().__init__()
        # Vamos setar um texto para o título da janela
        self.setWindowTitle("Cadastro de Produtos")
        # Setar a posição e o tamanho da janela (X, Y, Largura, Altura)
        self.setGeometry(750,250,300,400)

        self.setStyleSheet("background-color:#1D0047")


        # o QLineEdit cria uma caixinha que podemos escrever dentro, nesse caso deixamos um qlabel acima
        # que não pode ser editado, deixando um rótulo nessa caixa editável
        self.nome_label = QLabel("Nome do Produto")
        # vamos aplicar uma formatação na label utilizando comandos
        # de CSS(Cascade Style Sheet - Folha de Estilo em cascata)
        self.nome_label.setStyleSheet("QLabel{font-size:20pt;color:#7445F2;font-weight:bold}")
        self.nome_edit = QLineEdit()
        #também iremos aplicar a formatação na
        self.nome_edit.setStyleSheet("QLineEdit{border-radius:5px; background-color:#9272F2; font-size:20pt}")

        # aplicaremos o mesmo padrão para todas:
        self.tipo_label = QLabel("Tipo")
        self.tipo_label.setStyleSheet("QLabel{font-size:20pt;color:#7445F2;font-weight:bold}")  
        self.tipo_edit = QLineEdit()
        self.tipo_edit.setStyleSheet("QLineEdit{border-radius:5px; background-color:#9272F2; font-size:20pt}")


        self.preco_label = QLabel("Preço")
        self.preco_label.setStyleSheet("QLabel{font-size:20pt;color:#7445F2;font-weight:bold}")  
        self.preco_Edit = QLineEdit()
        self.preco_Edit.setStyleSheet("QLineEdit{border-radius:5px; background-color:#9272F2; font-size:20pt}")


        self.cadastrar_button = QPushButton("Cadastrar")
        self.cadastrar_button.setStyleSheet("background-color:#9272F2") 

        self.layout_vertical = QVBoxLayout()


        # adicionar os controles no layout
        self.layout_vertical.addWidget(self.nome_label)
        self.layout_vertical.addWidget(self.nome_edit)

        self.layout_vertical.addWidget(self.tipo_label)
        self.layout_vertical.addWidget(self.tipo_edit)

        self.layout_vertical.addWidget(self.preco_label)
        self.layout_vertical.addWidget(self.preco_Edit)

        self.layout_vertical.addWidget(self.cadastrar_button)

        # adicionar o layout vertical com todos os controles a nossa tela
        self.setLayout(self.layout_vertical)

# apresentar a janela
app = QApplication (sys.argv)
cad = CadastroProduto()
cad.show()
app.exec()
