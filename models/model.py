class Notbook():
    def __init__(self, marca, preco, imagem, resenhas, estrelas, descricao):
        self.marca = marca
        self.imagem = imagem
        self.preco = preco
        self.descricao = descricao
        self.resenhas = resenhas
        self.estrelas = estrelas

    def getMarca(self):
        return self.marca

    def getPreco(self):
        return self.preco

    def getDescricao(self):
        return self.descricao
    
    def getResenhas(self):
        return self.resenhas

    def getImagem(self):
        return self.imagem

    def getEstrelas(self):
        return self.estrelas
