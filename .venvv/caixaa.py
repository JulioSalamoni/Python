# ==================================================================== CRIAÇÃO JANELA ================================================================================================
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTableWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from sys import argv 

class Caixa(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Caixa da Padaria")
        self.setGeometry(150,50,1600,900)


# ===================================================================== CRIAÇÃO LAYOUTS ======================================================================================
        # Criar o layout horizontal ---------------------------------------------------------------------------------------
        self.layout_horizontal = QHBoxLayout()


        # Vamos criar as duas colunas: Esquerda e Direita
        # e alterar as cores de fundo de cada uma:

        self.label_col_esquerda = QLabel()
        self.label_col_esquerda.setStyleSheet("QLabel{background-color:#071D4A}")

        self.label_col_direita = QLabel()
        self.label_col_direita.setStyleSheet("QLabel{background-color:#356BDA}")
        self.label_col_esquerda.setFixedWidth(800)


# ========================================================================= COLUNA ESQUERDA ========================================================================================
        # Criar o layout dos elementos da coluna da esquerda. Este layout é vertical --------------------------------------------------------------------------------------
        self.layout_vert_col_esq = QVBoxLayout()


        # vamos criar uma label para adicionar o logo 
        self.label_logo = QLabel()
        # Vamos setar o Pixmap à label para carregar a imagem
        self.label_logo.setPixmap(QPixmap("BlueLogo.jpg"))
        # Ajustar a imagem à label
        self.label_logo.setScaledContents(True)

        
        # criar a label do codigo do produto ----------------------------------------------------------------------------------
        self.label_cod_produto = QLabel("Código do Produto")
        self.label_cod_produto.setStyleSheet("QLabel {font-weight:bold; font-size:15pt; color:#61B8FF}")
        self.edit_cod_produto = QLineEdit()
        self.edit_cod_produto.setStyleSheet("QLineEdit{font-size:15pt; color:#61B8FF; background-color:#0E45B7}")


        # criar a label e o edit do nome do produto ----------------------------------------------------------------------------------
        self.label_nome_produto = QLabel("Nome do Produto")
        self.label_nome_produto.setStyleSheet("QLabel {font-weight:bold; font-size:15pt; color:#61B8FF}")
        self.edit_nome_produto = QLineEdit()
        self.edit_nome_produto.setStyleSheet("QLineEdit{font-size:15pt; color:#61B8FF; background-color:#0E45B7}")


        # criar a label e o edit da descrição do produto ----------------------------------------------------------------------------------
        self.label_descricao_produto = QLabel("Descrição do Produto")
        self.label_descricao_produto.setStyleSheet("QLabel {font-weight:bold; font-size:15pt; color:#61B8FF}")
        self.edit_descricao_produto = QLineEdit()
        self.edit_descricao_produto.setStyleSheet("QLineEdit{font-size:15pt; color:#61B8FF; background-color:#0E45B7}")
        self.edit_descricao_produto.setFixedHeight(88)


        # criar a label e o edit da Quantidade do produto ----------------------------------------------------------------------------------
        self.label_quantidade_produto = QLabel("Quantidade do Produto")
        self.label_quantidade_produto.setStyleSheet("QLabel {font-weight:bold; font-size:15pt; color:#61B8FF}")
        self.edit_quantidade_produto = QLineEdit()
        self.edit_quantidade_produto.setStyleSheet("QLineEdit{font-size:15pt; color:#61B8FF; background-color:#0E45B7}")
        self.edit_quantidade_produto.setFixedHeight(40)


        # criar a label e o edit do preço unitario do produto ----------------------------------------------------------------------------------
        self.label_preco_produto = QLabel("Preço Unitário do Produto")
        self.label_preco_produto.setStyleSheet("QLabel {font-weight:bold; font-size:15pt; color:#61B8FF}")
        self.edit_preco_produto = QLineEdit()
        self.edit_preco_produto.setStyleSheet("QLineEdit{font-size:15p; color:#61B8FF; background-color:#0E45B7}")
        self.edit_preco_produto.setFixedHeight(40)


        # criar a label e o edit do subtotal do produto ----------------------------------------------------------------------------------
        self.label_subtotal_produto = QLabel("Sub Total:")
        self.label_subtotal_produto.setStyleSheet("QLabel {font-weight:bold; font-size:15pt; color:#61B8FF}")
        self.edit_subtotal_produto = QLineEdit("Tecle F3 para calcular o Subtotal")
        self.edit_subtotal_produto.setStyleSheet("QLineEdit{font-size:15pt; color:#61B8FF; background-color:#0E45B7}")
        self.edit_subtotal_produto.setFixedHeight(40)
        self.edit_subtotal_produto.setEnabled(False)



        # Adicionando os elementos á coluna da esquerda --------------------------------------------------------------------------------------------------------
        # Adicionar o logo ao layout vertical
        self.layout_vert_col_esq.addWidget(self.label_logo)

        # Adicionar o codigo do produto
        self.layout_vert_col_esq.addWidget(self.label_cod_produto)
        self.layout_vert_col_esq.addWidget(self.edit_cod_produto)

        # Adicionar o nome do produto
        self.layout_vert_col_esq.addWidget(self.label_nome_produto)
        self.layout_vert_col_esq.addWidget(self.edit_nome_produto)

        # Adicionar a descrição do produto
        self.layout_vert_col_esq.addWidget(self.label_descricao_produto)
        self.layout_vert_col_esq.addWidget(self.edit_descricao_produto)

        # Adicionar a quantidade do produto
        self.layout_vert_col_esq.addWidget(self.label_quantidade_produto)
        self.layout_vert_col_esq.addWidget(self.edit_quantidade_produto)

        # Adicionar o preço do produto
        self.layout_vert_col_esq.addWidget(self.label_preco_produto)
        self.layout_vert_col_esq.addWidget(self.edit_preco_produto)

        # Adicionar o subtotal
        self.layout_vert_col_esq.addWidget(self.label_subtotal_produto)
        self.layout_vert_col_esq.addWidget(self.edit_subtotal_produto)



        # Setar o layout vertical à label coluna esquerda
        self.label_col_esquerda.setLayout(self.layout_vert_col_esq)

# ========================================================================== FIM COLUNA ESQUERDA ===============================================================================



# =========================================================================== COLUNA DIREITA =====================================================================================================

        # Criar o layout vertical da coluna da direita para os elementos:
        # QTableWidget, QLabel, QLineEdit
        self.layout_vert_col_dir = QVBoxLayout()
        
        self.tabel_produtos = QTableWidget()
        # Criar os itens do cabeçalho da tabela
        cabecalho = ["Cod.Produto", "Nome Produto", "Quantidade", "Preço", "Sub total"]
        # Definir a quantidade de colunas da nossa tabela
        self.tabel_produtos.setColumnCount(5)
        # Adicionar o cabecalho a tabela
        self.tabel_produtos.setHorizontalHeaderLabels(cabecalho)
        # Editar a tabela
        self.tabel_produtos.setStyleSheet("QTableWidget{background-color: #071D4A}")
        # Adicionar algumas linhas
        self.tabel_produtos.setRowCount(20)


        self.label_total_pagar = QLabel("Total a Pagar")
        self.label_total_pagar.setStyleSheet("QLabel{font-weight:bold; font-size:40pt; color:#071D4A; background-color:#356BDA}")

        self.edit_total_pagar = QLineEdit("0,00")
        self.edit_total_pagar.setStyleSheet("QLineEdit{font-weight:bold; font-size:50pt; color:#61B8FF; background-color:#071D4A}")
        self.edit_total_pagar.setEnabled(False)


        # adicionando os controles ao layout vertical da coluna da direita -------------------------------------------------------------------------------------------
        self.layout_vert_col_dir.addWidget(self.tabel_produtos)
        self.layout_vert_col_dir.addWidget(self.label_total_pagar)
        self.layout_vert_col_dir.addWidget(self.edit_total_pagar)

        # Setar o layout vertical da col direita na coluna da direita
        self.label_col_direita.setLayout(self.layout_vert_col_dir)



# ======================================================================= FIM COLUNA DIREITA ====================================================================================


# ================================================================== ADICIONAR OS LAYOUTS NA JANELA ==============================================================
        # Adicionar as colunas da esqerda e direita ao layout horizontal
        # lembrar que essa parte tem que sempre ficar depois de ter alterado todos
        # os detalhes doque irá ficar dentro
        self.layout_horizontal.addWidget(self.label_col_esquerda)
        self.layout_horizontal.addWidget(self.label_col_direita)

        # Setar o layout horizontal à nossa janela
        self.setLayout(self.layout_horizontal)

# ==================================================================== keyPress =========================================================================
        # Vamos usar a função keyPress para fazer a janela observar as teclas que estão sendo digitadas
        # e assim, capturar a tecla específica e executar uma ação
        self.keyPressEvent = self.keyPressEvent

    def keyPressEvent(self, e):
        if(e.key()==Qt.Key.Key_F3):
            print("Você digitou a tecla f3")




# ========================================================================================================================================
app = QApplication(argv)
janela = Caixa()
janela.show()
app.exec()