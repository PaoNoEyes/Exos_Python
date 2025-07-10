class Eleve():


    def __init__(self,nom,prenom):
        self.nom = nom
        self.prenom = prenom

    def id(self):
        return str(self.nom)+" "+str(self.prenom)
    
    def changer_nom(self,nom):
        self.nom = nom




    
def nouvel_eleve(nom,prenom):
    a = Eleve(nom,prenom)
    return a    
    
Gelly = Eleve("GELLY","Kieran")
Biolley = nouvel_eleve("Gab","l'Adjudant")


print()
print(Gelly)                                        #<_main__.Eleve object at 0x00000290F9CF2D90>
print()                                             #
print(Gelly.prenom)                                 #Kieran
print()                                             #
print(Gelly.nom)                                    #GELLY
print()                                             #
print(Gelly.id())                                   #GELLY Kieran
print()                                             #
print(Biolley.id())                                 #Gab l'Adjudant
print()                                             #
Biolley.changer_nom("Mr")                           #
print(Biolley.id())                                 #Mr l'Adjudant
print()                                             #

