import ressource as re
from random import randint


def Vol1(a,z):
    re.dico[a]=z


def Vol2():
    return re.MYSTERE

def Vol3():
    for i in re.dico:
        print(i ,":",re.dico[i][0][0],re.dico[i][0][1],"\n")

def Vol4():
    for i in re.dico:
        ale_r=randint(0,10)
        ale_t=randint(0,4)
        re.dico[i][1][0][0]=ale_r
        re.dico[i][1][0][1]=ale_t
    
Vol4()

def Vol5():
    return re.REPONSE_UNIVERSELLE

Vol1(Vol2(),Vol5())

def Vol6():
    print("saurez vous trouvez la réponse ?")
    Vol3()
    print("\nAVE CAESAR, MORITURI TE SALUTANT !!\n")
Vol6()

def Vol7():
    a = input("Avez vous trouvé ?\nQuel est le code caché dans la bibliothèque ?\n")
    re.Vol8(a)

Vol7()