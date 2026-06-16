from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
import sys

class janela2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Minha Janela")
        # Largura, Altura e Posição da Janela, (X, Y, Largura, Altura)
        self.setGeometry(10,20,800,400)
        # O QLabel é usado para mostrar informações na tela, geralmente textos, mas também pode exibir imagens.
        # O QPushButton cria um botão clicável.
        self.texto = QLabel("Clique no botão abaixo")
        self.botao = QPushButton("Clique Aqui")
        # para organizar os controles(label, pushbutton) usaremos o comando
        # QVboxLayout, para distribuir os controles de forma vertical na tela
        # o Vbox é porque é na vertical, se fosse na horizontal seria o Hbox
        layout_vertical = QVBoxLayout()
        layout_vertical.addWidget(self.texto)
        layout_vertical.addWidget(self.botao)
        # Adicionar o layout vertical a tela
        self.setLayout(layout_vertical)

app = QApplication(sys.argv)
tela = janela2()
tela.show()
app.exec()
