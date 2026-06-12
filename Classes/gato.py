class Gato:
    def __init__(self,raca:str,cor:str,tipo_pelo:str,idade:int,nome:str):
        """
        Docstring for __init__
        
        :param self: Comando que faz os atributos e métodos olharem para a classe
        :param raca: Digite a raça do Gato
        :type raca: str
        :param cor: Digite a cor do gato
        :type cor: str
        :param tipo_pelo: Digite o tipo do pelo(Sem pelo, Pelo longo, Pelo curto)
        :type tipo_pelo: str
        :param idade: Digite a idade do gato com o número inteiro
        :type idade: int
        :param nome: Digite o nome do gato
        :type nome: str
        """
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.cor = cor
        self.tipo_pelo = tipo_pelo

    def miar(self):
        print(f"A {self.nome} miou")


meu_gato = Gato("Bombain","Preto","Pelo Curto",15,"Preta")

meu_gato.miar()