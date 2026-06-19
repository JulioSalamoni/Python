# ==================================================================== CRIAÇÃO JANELA ================================================================================================
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt
from sys import argv 


class Pet(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pet")
        self.setGeometry(150,50,1600,900)

        self.setStyleSheet("background-color:#323A4B")

        # colocando o ícona na janela
        self.setWindowIcon(QIcon("PretaIcon"))

# ==============================================================================================================================================================================
    # Criar o layout horizontal ---------------------------------------------------------------------------------------
        self.layout_horizontal = QHBoxLayout()
        self.layout_horizontal.setSpacing(0)


    # Criar a coluna da esquerda
        self.label_col_esquerda = QLabel()
        self.label_col_esquerda.setStyleSheet("QLabel{background-color:#D6DDF5}")
    # Criar a coluna da esquerda
        self.label_col_direita = QLabel()
        self.label_col_direita.setStyleSheet("QLabel{background-color:#D6DDF5}")
        self.label_col_esquerda.setFixedWidth(800)


# =================================================================== COLUNA ESQUERDA ===============================================================================================
        # Criando layout para os elementos da coluna da esquerda
        self.layout_vert_col_esq = QVBoxLayout()


        # vamos criar uma label para adicionar o logo 
        self.label_logo = QLabel()
        # Vamos setar o Pixmap à label para carregar a imagem
        self.label_logo.setPixmap(QPixmap("PretaLogo.png"))
        # Ajustar a imagem à label
        self.label_logo.setScaledContents(True)

        # Adicionando os elementos -------------------------------------------------------------------------
        # Adicionar o logo ao layout vertical
        self.layout_vert_col_esq.addWidget(self.label_logo)

        # Setar o layout vertical à label coluna esquerda
        self.label_col_esquerda.setLayout(self.layout_vert_col_esq)

# =================================================================== FIM COLUNA ESQUERDA ==============================================================================================

# ===================================================================== COLUNA DIREITA ==========================================================================================

        self.layout_vert_col_dir = QVBoxLayout()

        # 1
        self.label_voluntario = QLabel("Seja Voluntário,")
        self.label_voluntario.setStyleSheet("QLabel {font-weight:bold; font-size:25pt; color:#323A4B}")

        # 2
        self.label_miaumigo = QLabel("e ajude um miaumigo a encontrar um lar")
        self.label_miaumigo.setStyleSheet("QLabel {font-weight:bold; font-size:14pt; color:#000000}")

        # 3
        self.label_seunome = QLabel("Seu Nome:")
        self.label_seunome.setStyleSheet("QLabel{font-size:15pt;color:#000000}")  
        self.edit_seunome = QLineEdit()
        self.edit_seunome.setStyleSheet("QLineEdit{font-size:15pt; color:#000000; background-color:#ffffff}")
        self.edit_seunome.setFixedHeight(50)

        # 4
        self.label_seuemail = QLabel("Seu Email:")
        self.label_seuemail.setStyleSheet("QLabel{font-size:15pt;color:#000000}")  
        self.edit_seuemail = QLineEdit()
        self.edit_seuemail.setStyleSheet("QLineEdit{font-size:15pt; color:#000000; background-color:#ffffff}")
        self.edit_seuemail.setFixedHeight(50)

        # 5
        self.label_suasenha = QLabel("Sua Senha:")
        self.label_suasenha.setStyleSheet("QLabel{font-size:15pt;color:#000000}")  
        self.edit_suasenha = QLineEdit()
        self.edit_suasenha.setStyleSheet("QLineEdit{font-size:15pt; color:#000000; background-color:#ffffff}")
        self.edit_suasenha.setFixedHeight(50)

        # 6
        self.button_cadastrar = QPushButton("Cadastrar")
        self.button_cadastrar.setStyleSheet("background-color:#323A4B; color:#ffffff") 
        self.button_cadastrar.setFixedHeight(50)

        # 7
        self.button_cadastrargoogle = QPushButton("Cadastrar com Google")
        self.button_cadastrargoogle.setStyleSheet("background-color:#FA4E3E; color:#ffffff") 
        self.button_cadastrargoogle.setFixedHeight(50)

        # 8
        self.button_cadastrarfacebook = QPushButton("Cadastrar com Facebook")
        self.button_cadastrarfacebook.setStyleSheet("background-color:#23599B; color:#ffffff") 
        self.button_cadastrarfacebook.setFixedHeight(50)



# Adicionando os elementos ---------------------------------------------------------------------------------
        # 1
        self.layout_vert_col_dir.addWidget(self.label_voluntario)
        # 2
        self.layout_vert_col_dir.addWidget(self.label_miaumigo)
        # 3
        self.layout_vert_col_dir.addWidget(self.label_seunome)
        self.layout_vert_col_dir.addWidget(self.edit_seunome)    
        # 4
        self.layout_vert_col_dir.addWidget(self.label_seuemail)
        self.layout_vert_col_dir.addWidget(self.edit_seuemail)    
        # 5
        self.layout_vert_col_dir.addWidget(self.label_suasenha)
        self.layout_vert_col_dir.addWidget(self.edit_suasenha)    
        # 6
        self.layout_vert_col_dir.addWidget(self.button_cadastrar)
        # 7
        self.layout_vert_col_dir.addWidget(self.button_cadastrargoogle)
        #8
        self.layout_vert_col_dir.addWidget(self.button_cadastrarfacebook)



        # Setar o layout vertical da col direita na coluna da direita
        self.label_col_direita.setLayout(self.layout_vert_col_dir)


# ================================================================== ADICIONAR OS LAYOUTS NA JANELA ================================================================================
 
        # Adicionar as colunas da esquerda e direita ao layout horizontal
        self.layout_horizontal.addWidget(self.label_col_esquerda)
        self.layout_horizontal.addWidget(self.label_col_direita)

        # Setar o layout horizontal à nossa janela
        self.setLayout(self.layout_horizontal)


# ===========================================================================================================================================================================
app = QApplication(argv)
janela = Pet()
janela.show()
app.exec()

