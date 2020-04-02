from random import randint

class Ave():
    #Atributos da classe
    ave_especie = "ave"
    ave_cobertura = "penas"

    #Métodos da classe
    #--Método que gera um número inteiro aleatório de 1 a 5
    def botarOvo(self):
        return "Botando {} ovos.".format(randint(0,5))

class Mamifero():
    #Atributos da classe
    mamifero_especie = "mamifero"
    mamifero_cobertura = "pelos"

    #Métodos da classe
    def beberLeite(self):
        return "Bebendo leite."

class animalEstimacao():
    #Atributos da classe

    #Atributos dos objetos
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
        if tipo == "mamifero":
            self.especie = Mamifero.mamifero_especie
            self.cobertura = Mamifero.mamifero_cobertura
            
        else:
            self.especie = Ave.ave_especie
            self.cobertura = Ave.ave_cobertura

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

gato = animalEstimacao("Fido", 5, "mamifero")
cacatua = animalEstimacao("Cacá", 3, "ave")

print(gato.descricao())
#print(gato.falar("Eu sou um gato"))
#todos os objetos criados podem usar métodos das classes pai
#print("{} está {}".format(gato.nome, gato.botarOvo()))
#print("Mas gato não bota ovo...")
print()
#
print(cacatua.descricao())
#print(cacatua.falar("Eu sou uma calopsita"))
print("{} está {}".format(cacatua.nome, cacatua.botarOvo()))

#print(animalEstimacao.mro())