from random import randint

class Ave:
    #Atributos da classe
    ave_especie = "ave"
    ave_cobertura = "penas"

    #Métodos da classe
    #--Método que gera um número inteiro aleatório de 1 a 5
    def botarOvo(self):
        return "Botando {} ovos.".format(randint(0,5))


class Mamifero:
    #Atributos da classe
    mamifero_especie = "mamifero"
    mamifero_cobertura = "pelos"


class animalEstimacao(Mamifero,Ave):
    #Atributos da classe

    #Atributos dos objetos
    def __init__(self,nome,idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
        if tipo == "mamifero":
            self.especie = self.mamifero_especie
            self.cobertura = self.mamifero_cobertura
        
        else:
            self.especie = self.ave_especie
            self.cobertura = self.ave_cobertura

    #Métodos dos atributos
    #--Método que descreve o objeto
    def descricao(self):
        if self.tipo == "mamifero":
            return "{} é um {} de {} anos de idade que tem o corpo coberto por {}.".format(self.nome,self.tipo,self.idade, self.cobertura)
        else:
            return "{} é uma {} de {} anos de idade que tem o corpo coberto por {}.".format(self.nome,self.tipo,self.idade, self.cobertura)

    #--Método que printa uma frase como se fosse o objeto falando
    def falar(self, fala):
        return "{} diz: {}.".format(self.nome, fala)

fido = animalEstimacao("Fido", 5, "mamifero")
caca = animalEstimacao("Cacá", 3, "ave")

print(fido.descricao())
print(fido.falar("Eu sou um gato"))
#todos os objetos criados podem usar métodos das classes pai
print("{} está {}".format(fido.nome, fido.botarOvo()))

print("Mas gato não bota ovo...")
#print(caca.descricao())
#print(caca.falar("Eu sou uma calopsita"))