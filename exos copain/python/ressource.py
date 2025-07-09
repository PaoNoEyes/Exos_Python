dico = {"1984" : [["George","Orwell"],[[0,0],'']],
"le_meilleur_des_mondes" : [["Aldous","Huxley"],[[0,0],'']],
"fahrenheit_451" : [["Ray","Bradbury"],[[0,0],'']],
"dune" : [["Frank","Herbert"],[[0,0],'']],
"la_ferme_des_animaux" : [["George","Orwell"],[[0,0],'']],
"neuromancien" : [["William","Gibson"],[[0,0],'']],
"fondation" : [["Isaac","Asimov"],[[0,0],'']],
"je_suis_une_legende" : [["Richard","Matheson"],[[0,0],'']],
"le_meilleur_des_mondes_revisite" : [["Aldous","Huxley"],[[0,0],'']],
"le_cycle_des_robots" : [["Isaac","Asimov"],[[0,0],'']],
"hypérion" : [["Dan","Simmons"],[[0,0],'']],
"les_androides_revent_ils_de_moutons_electriques" : [["Philip K.","Dick"],[[0,0],'']],
"ubik" : [["Philip K.","Dick"],[[0,0],'']],
"le_maitre_du_haut_chateau" : [["Philip K.","Dick"],[[0,0],'']],
"solaris" : [["Stanislaw","Lem"],[[0,0],'']],
"le_meilleur_des_mondes" : [["Aldous","Huxley"],[[0,0],'']],
"ravage" : [["René","Barjavel"],[[0,0],'']],
"la_nuit_des_temps" : [["René","Barjavel"],[[0,0],'']],
"malevil" : [["Robert","Merle"],[[0,0],'']],
"le_fléau" : [["Stephen","King"],[[0,0],'']],
"la_route" : [["Cormac","McCarthy"],[[0,0],'']],
"le_passeur" : [["Lois","Lowry"],[[0,0],'']],
"les_hommes_proies" : [["Pierre","Bordage"],[[0,0],'']],
"l_enchâssement" : [["Ian","Watson"],[[0,0],'']],
"le_cycle_de_dune" : [["Frank","Herbert"],[[0,0],'']],
"le_monde_d_edena" : [["Moebius",""],[[0,0],'']],
"le_problème_a_trois_corps" : [["Liu","Cixin"],[[0,0],'']],
"spin" : [["Robert","Wilson"],[[0,0],'']],
"en_remake" : [["Michel","Pagel"],[[0,0],'']],
"les_désastreuses_aventures_des_orphelins_baudelaire" : [["Lemony","Snicket"],[[0,0],'']],
"la_machine_a_explorer_le_temps" : [["H.G.","Wells"],[[0,0],'']],
"la_guerre_des_mondes" : [["H.G.","Wells"],[[0,0],'']],
"le_meilleur_des_mondes" : [["Aldous","Huxley"],[[0,0],'']],
"metro_2033" : [["Dmitry","Glukhovsky"],[[0,0],'']],
"les_jeux_de_la_faim" : [["Suzanne","Collins"],[[0,0],'']],
"divergente" : [["Veronica","Roth"],[[0,0],'']],
"le_labyrinthe" : [["James","Dashner"],[[0,0],'']],
"ready_player_one" : [["Ernest","Cline"],[[0,0],'']],
"un_bonheur_insoutenable" : [["Ira","Levin"],[[0,0],'']],
"la_zone_du_dehors" : [["Alain","Damasio"],[[0,0],'']],
"la_horde_du_contrevent" : [["Alain","Damasio"],[[0,0],'']],
"oxygen" : [["Carl","Djerassi"],[[0,0],'']],
"les_monades_urbaines" : [["Robert","Silverberg"],[[0,0],'']],
"les_voix_du_crepuscule" : [["Joëlle","Wintrebert"],[[0,0],'']],
"l_autre_monde" : [["Maxime","Chattam"],[[0,0],'']],
"le_jeu_des_perles_de_verre" : [["Hermann","Hesse"],[[0,0],'']],
"station_eleven" : [["Emily St.","John Mandel"],[[0,0],'']],
"the_circle" : [["Dave","Eggers"],[[0,0],'']],
"snow_crash" : [["Neal","Stephenson"],[[0,0],'']],
"l'art_de_la_guerre" : [["Sun","Tzu"],[[0,0],'']]}

MYSTERE = "bu_wkytu_tk_leoqwukh_ydjuhwqbqsjygku"
REPONSE_UNIVERSELLE= [["Julius","Caesar"],[[42,42],'42']]

def MaliceTrouvée(a):
    if a : print("le mot de passe est : chiffré !")
    print("TGEgdm9pZSBkZXMgUm9pcw==")
    print("cyberchef est votre ami")

def Vol8(a):
    cpt = 0
    if a == "le_guide_du_voyageur_intergalactique":
        print("Bien joué !\n\n")
        print("Saurez vous retrouvez les titres de ces classiques perdus dans la bibliothèque ?")
        lis = ["BigBrother?","Artyom?","température","guerre_trois_royaumes?",]
        print(lis)
        
        liste = ["1984","metro2033","fahrenheit_451","l'art_de_la_guerre"]
        for i in range(len(liste)):
            print(lis[i],"\n")
            b = input()
            if b == liste[i]:
                cpt = cpt+1
                print("valide\n")
            else : 
                print("erreur\n")
        if cpt == 4:
            print("Felicitations !")
            MaliceTrouvée(True)
        else :
            print("retournez lire vos classique")
    else :
        print("codé ?")

