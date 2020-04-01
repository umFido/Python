#Classes são como formulários ou modelos que exigem determinadas informações.
#Quando os requisitos da classe são preenchidos é possível criar um objeto a partir do modelo da classe


#Definindo uma classe
class Gato:

    #Atributos da classe
    especie = "mamifero"

    #Atributos dos objetos
    def __init__(self, nome, idade, raca):
            self.nome = nome
            self.idade = idade
            self.raca = raca
            self.barriga_status = False

    #Métodos dos objetos
    def descricao(self):
        return"{} tem {} anos de idade.".format(self.nome, self.idade)
    
    def fala(self, som):
        return "{} diz {}".format(self.nome, som)

    ##Método que altera o status inicial de um dos atributos
    def encher_barriga(self):
        self.barriga_status = True


#Instanciando objetos a partir da classe
fido = Gato("Fido", 18, "Siames")
nega = Gato("Nega", 10, "Vira-lata")
brida = Gato("Brida", 7, "Vira-lata")

#Acessando atributos dos objetos usando nome_do_objeto.atributo
#print("{1} tem {3} anos.  {0} tem {2} anos".format(nega.nome, fido.nome, nega.idade, fido.idade))

#if fido.especie == "mamifero" and nega.especie == "mamifero":
#    print("Ambos são {}".format(fido.especie))

#Função que recebe qualquer número de elementos e retorna o maior valor
def gato_mais_velho(*idades):
    return max(idades)

#print("O gato mais velho tem", gato_mais_velho(nega.idade, fido.idade, brida.idade), "anos.")

#Utilizando os métodos criados anteriormente
#print(fido.descricao())
#print(fido.fala("Meau"))

#Função que verifica o status do atributo barriga_status
def fome_fido():
    if fido.barriga_status == False:
        print("{} está com a barriga vazia.".format(fido.nome))
    else:
        print("{} está com a barriga cheia.".format(fido.nome))

#fome_fido()
##atualiza o atributo barriga_status para True
#print("Alimentando o gato...")
#fido.encher_barriga()
#fome_fido()