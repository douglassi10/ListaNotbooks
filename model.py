class Notbook():
    def __init__(self, marca, imagem, preco, descricao, resenhas, estrelas):
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
        return self.preco
    
    def getResenhas(self):
        return self.descricao

    def getImagem(self):
        return self.resenhas

    def getEstrelas(self):
        return self.estrelas
