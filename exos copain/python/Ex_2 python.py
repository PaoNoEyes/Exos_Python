#Ex_2 python
#a=["fraise","pomme","poire","pomme","banane","abricot","fraise","mure","fraise","cerise","peche","pasteque","abricot","melon","cerise","framboise","fraise","pamplemousse","abricot","orange","clementine","ananas","kiwi","easteregg","pomme","ananas","pomme","poire","fraise","fraise","poire","pomme","myrtille","cassis","salade","tomate","avocat","fraise","framboise","ananas","kiwi","orange","poire","pamplemousse","clémentine","pomme","poire","clémentine","ananas","clémentine","pomme","poire","pomme","fraise"]


result={"fraise":6}
ok = False
def fonc1(a,b = "fraise"):
    for x in a :
        if x in result:
            ok = False
            result[x] = result[x]+1
        else : 
            ok = True
            result[x] = 1
    return result
print(fonc1(a))

        

