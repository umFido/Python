#Herança é o processo pelo qual uma classe pega atributos e métodos de outra
#Uma classe formada a partir de outra é chamada de classe Filha
#A classe a partir da qual foi criada é a classe Pai

import ClasseGatos as CG

#Criando uma nova classe que herdará atributos da classe Gato do arquivo ClasseGatos
class GatoPreto(CG.Gato):
    #É possível sobrescrever atributos da classe pai na classe filho
    especie = "Demonio Carmesim"

    def dorme(self, tempo):
        return "{} dorme {} horas por dia.".format(self.nome, tempo)

##Classes filhas herdam atributos da classe pai, como .nome() e .idade()
chomuske = GatoPreto("Chomuske", "3", "Gato")
##tambem herdam metodos da classe pai, como .descricao()
print(chomuske.descricao())
print("{} é um {}".format(chomuske.nome, chomuske.especie))

#Alem de possuirem metodos proprios de suas classe que nao sao acessadas pela classe pai
print(chomuske.dorme(10))

#print()

#A função isinstance() determina se uma instância pertence a uma determinada classe
#print(isinstance(chomuske, GatoPreto)) #True, chomuske foi criado a partir da classe GatoPreto
#print(isinstance(chomuske, CG.Gato)) #True, chomuske foi criado a partir da classe CG.Gato, pois GatoPreto a chama

