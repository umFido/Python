#Herança é o processo pelo qual uma classe pega atributos e métodos de outra
#Uma classe formada a partir de outra é chamada de classe Filha
#A classe a partir da qual foi criada é a classe Pai

import ClasseGatos as CG

#Criando uma nova classe que herdará atributos da classe Gato do arquivo ClasseGatos
class GatoPreto(CG.Gato):
    
    def dorme(self, tempo):
        return "{} dorme {} horas.".format(self.nome, tempo)

##Classes filhas herdam atributos da classe pai, como .nome() e .idade()
chomuske = GatoPreto("Chomuske", "3", "Gato Demonho")
##tambem herdam metodos da classe pai, como .descricao()
print(chomuske.descricao())

#Alem de possuirem metodos proprios de suas classe que nao sao acessadas pela classe pai
print(chomuske.dorme(10))

#print()
#print(isinstance(chomuske, GatoPreto))
#print(isinstance(chomuske, CG.Gato))