import random
import sys
import os
import platform
import time
import webbrowser
from colorama import init,Fore, Back, Style
import pickle
from tqdm import tqdm


def clear_aff():
    os.system('cls' if os.name=='nt' else 'clear')


def printsave():
    print("-----------------------------------------------------\n | Appuyez sur | s - Pour Sauvegarder | q - Pour quitter | ")

def menusave(player):
    printsave()
    val = input()
    if val == 's':
        pickle.dump(player, open("save.p", "wb"))
    if val == 'q':
        sys.exit()
    else:
        return val

def menu():
    print("---------------------Mokepon RPG---------------------")
    print("-----------------------------------------------------")
    print("          1 : Crée une nouvelle partie               ")
    print("          2 : Charger votre partie                   ")
    print("          3 : A propos du jeu                        ")
    print("          4 : Fermer le jeu                          ")
    chx = input()
    if chx == '1':
        progress = 0
        player = creationJoueurs()
        game(player,progress)
    elif chx == '2':
        player = pickle.load(open("save.p", "rb"))
        progress = player["position"]
        #barre
        blc = tqdm(total = 69420, position=0, leave=False)
        for j in range(69420):
            blc.set_description("... Votre partie charge ...".format(j))
            blc.update(1)
        blc.close()
        #fin barre
        game(player,progress)
    elif chx == '3':
        about()
    elif chx == '4':
        sys.exit()
    else:
        print("error")

def print_slow(txt):
    for x in txt:
        print(x, end='', flush=True) #affiche lettre par letre le str
        time.sleep(0.015)
    print() #retour a la ligne

def about():
    print_slow("Ce jeu est developpé par Antoine Azevedo Da Silva et Stanley Jamais dans le cadre du projet python pour l'école Hetic. Il reprend les bases que les jeux pokémons on pu introduire, surtout ceux de gameboy. \n L'histoire est assez comique nous essayerons de vous faire venir à bout du Covid avec des monstres aux noms comiques.\n Si jamais vous voulez nous faire savoir votre retour n'hésitez pas à nous contacter par le mail étudiant de l'école.\n Nous vous souhaitons une agréable partie et une bonne dose de rire :).")
    sys.stdout.flush()
    menu()

def maping(player,val):

    if val == 1:

        map1(player)  # changer player pos a chaques map
        menusave(player)
    elif val == 2:
        map2(player)
    elif val == 3:
        map3(player)
    elif val == 4:
        print("Bienvenue a Honk Ponk, une boutique est disponible souhaitez vous y  aller \n o - Oui n - Non//")
        chx = int(input())
        # if chx == "o":
        map4(player)
    elif val == 5:
        map5(player)
    elif val == 6:
        map6(player)
    elif val == 7:
        boss(player)

    elif val !=1 or val !=2 or val !=3 or val !=4 or val !=5 or val !=6 or val !=7:
        print("error 404")

def game(player,progress):


    if progress == 0:
        auberge(player)  # a mettre toute les 2maps + b4 boss
        magasinChoix(player)  # a mettre entre r3/r4 + r7/r8 avec un message pour le dernier shop
        maping(player,1)

    else:
        maping(player,progress)

def random_area():
    value=["Vous pénétrez dans la foret attention à vos miches","Vous y trouver un tunnel et vous y glissez !",
           "Vous appercevez une silhouette au loin, vous décidez de la rattraper",
           "Cette coline semble donner un point de vue interessant, allez y.",
           "Cette sombre crevasse semble dangeureuse, j'espère pour vous qu'il n'y a pas de pythons en bas",
           "Une ville abandonnée du nom de Woolhanne se dresse devant vous, faites attention !",
           "Un pont suspendu est droit devant faites gaffe a vos pas pour pas faire craquer le pont",
           "Une incroyable cascade d'eau vous apparait, ne glissez pas sur les rochers"]
    i=random.randint(0,6)
    print(value[i])
    print("---------------------------")
    time.sleep(1)

def intro(name):  # OK
    print("Bienvenue à toi", name,
          "!\nTon aventure ne fais que de commencer et pourtant nous comptons déjà sur toi car aujourd'hui dans le monde des moképon sévis une atroce maladie véhiculé par un bandit de la région, l'horrible Corvid.\nPour t'aider dans ta quête afin de sauver notre monde, je vais t'offrir ton premier moképon ! \nChoisis le bien, ils ont tous leurs forces et faiblesses et tu ne pourra pas le changer une fois ton choix fait.")
    time.sleep(1)


# Inventaire Du joueur

def creationJoueurs():  # Crée le joueur, donne son nom, son argent, son inventaire, son mokepon (via la fct mokeponChoice)
    player = {}
    mokepon = {}
    player["argent"] = 1000
    player["inventaire"] = {}
    player["inventaire"]["soin"] = 5
    player["inventaire"]["attaque"] = 5
    player["inventaire"]["defense"] = 5
    player["position"] = 0
    player["name"] = str(input("Quel est ton nom ?"))
    intro(player.get("name"))
    player["mokepon"] = mokeponChoice(mokepon)
    print("Wow! Tu as choisi", mokepon.get("name"), "très bon choix!")
    return player


# Inventaire Du joueur
def playerInventory(player):  # Affiche les objets dans l'inventaire du joueur, et lui demande si il veux en use une
    verificationKey = 0
    potion = ' '
    testvie = " "
    while verificationKey == 0:
        print("Vous possedez dans votre inventaire:\n", player["inventaire"]["soin"], "potion de soin,\n",
              player["inventaire"]["attaque"], "potion d'attaque,\net ", player["inventaire"]["defense"],
              "potion de defense\n")
        playerChoiceInventory = input("Que desirez-vous faire  ?\na - Prendre une potion de soin\nb - Prendre une potion d'attaque\nc - Prendre une potion de défense\nd - Sortir\n")

        if playerChoiceInventory == 'a':
            potion = "soin"
            testvie = inventory(player, potion)
            verificationKey = 1
        elif playerChoiceInventory == 'b':
            potion = "attaque"
            testvie ="attaque"
            inventory(player,  potion)
            verificationKey = 1
        elif playerChoiceInventory == 'c':
            potion = "defense"
            testvie = "defense"
            inventory(player, potion)
            verificationKey = 1
        elif playerChoiceInventory == 'd':
            return False
        elif playerChoiceInventory!='a' or playerChoiceInventory!='b' or playerChoiceInventory!='c' or playerChoiceInventory!='d':
            verificationKey = 0
            print("Tu n'as pas entrée une valeur correcte!")

        if (testvie == 'soinerror'):
            verificationKey = 0
    return player


def inventory(player, potion):  # Enleve l'objet de l'inventaire et ajoute la stat en plus
    if (player["inventaire"][potion] >= 1):
        if potion == "soin":
            if (player["mokepon"]["hp"] != player["mokepon"]["hpmax"]):
                player["inventaire"][potion] = player["inventaire"][potion] - 1
                player["mokepon"]["hp"] = soin(player["mokepon"]["hp"], player["mokepon"]["hpmax"])
                print("Votre", player["mokepon"]["name"], " a desormais", player["mokepon"]["hp"], "pv!")
            else:
                print("Impossible, Il possede déja toute sa vie !")
                return 'soinerror'

        else:
            player["inventaire"][potion] = player["inventaire"][potion] - 1
            player["mokepon"][potion] = player["mokepon"][potion] + 5
            print("Votre", player["mokepon"]["name"], " a desormais", player["mokepon"][potion], " points", potion, '.')
    elif (player["inventaire"][potion] < 1):
        print("Vous n'avez pas l'item en stock !")
    else:
        print("Compris ! Retour a l'inventaire")
    return player


# Soin base
def soin(vie, vieMax):  # Ajoute les pv en plus au mokepon si possible
    hp = vie
    hpMax = vieMax
    hpTmp = 0
    if hp < hpMax:
        hpTmp = hp + 20
        if hpTmp < hpMax:
            return hpTmp
    return hpMax


def rickroll():
    print('Ho non ! Un cul-de-sac !')
    website="https://destroykeaum.alwaysdata.net/assets/other/addon/rickroll.mp4"
    webbrowser.open_new_tab(website)
    
    
def briller():
    print('Perdu lol enjoy')
    website = "https://destroykeaum.alwaysdata.net/assets/other/addon/briller.mp4"
    webbrowser.open_new_tab(website)
  
def felicitation():
    print("Félicitation tu as vaincu le grand Corvid !")
    website = "https://destroykeaum.alwaysdata.net/assets/other/addon/victory.mp4"
    webbrowser.open_new_tab(website)


def interactionEnnemi():  # Genere un phrase de provoque de l'ia adverse
    nomDres = ['P-A', 'Joao-vc, le canard', 'Julien laperceuse', 'Anthoriz, le fils du soleil levant', 'Ouati bé',
               'Maitre Pims le tenor', 'John Weak, le surpuissant', 'Jean Damien le rapide', 'NekFat, le rapide',
               'Manu Micron, le bon eleve', 'Cyril Hamdoula, animateur', 'Meerajh Kalifa, la spéléologue']
    MiseEnGardeDres = ["J'aime les shorts, ça garde mes genoux bien au frais",
                       "Ha ha ! Je crois que tu as besoin d'un peu d'échauffement !", "C'que t'es faible! Hahaha!",
                       "Tiens? Quelle bonne surprise, tu es là aussi?! Eh ben... Allez, viens prendre ta baffe, minable!",
                       "j'vais t'casser en deux minab'. Ta maman te reconnaîtra qu'à la couleur de ton p'tit cartable!",
                       "Oh, toi. Je vais t'en faire baver!"]
    print(nomDres[random.randint(0, (len(nomDres) - 1))], '- "',
          MiseEnGardeDres[random.randint(0, (len(MiseEnGardeDres) - 1))], '"')



# magasin (base) & auberge

# auberge
def auberge(player):  # Soigne le pokemon de 20pv
    player["mokepon"]["hp"] = soin(player["mokepon"]["hp"], player["mokepon"]["hpmax"])
    print("Votre", player["mokepon"]["name"], "s'est bien reposé, il a desormais", player["mokepon"]["hp"], "pv!")
    return player


# magasin
# Initiation du magasin
def magasinChoix(player):  # Propose l'achat de potion
    verificationKey2 = 0
    potion = "none"
    print(
        "La potion de vie redonne 20 HP a ton mokepon, son prix est de 200 MokeDollars !\nLa potion d'attaque donne 5 points d'attaque temporaire en plus a ton mokepon, son prix est de 200 MokeDollars !\nLa potion de défense donne 5 points de defense temporaire en plus a ton mokepon, son prix est de 200 MokeDollars !\nQue desirez-vous faire  ?")
    achatPotion(player, choixPotion())
    while verificationKey2 == 0:
        rachat = input("Ce sera tout ? o - oui / n - non\n")
        if rachat == 'n':
            magasinChoix(player)
        elif rachat == 'o':
            verificationKey2 = 1
            return player
        else:
            verificationKey2 = 0


# Choix de la potion a acheter
def choixPotion():  # Fait choisir au joueur quelle type de potion, il veux se servir ou acheter
    potion = 'none'
    verificationKey = 0
    while verificationKey == 0:
        playerChoiceInventory = input(
            "\na - Acheter une potion de soin\nb - Acheter une potion d'attaque\nc - Acheter une potion de défense\nd - Sortir\n")
        if playerChoiceInventory == 'a':
            verificationKey = 1
            potion = "soin"
        elif playerChoiceInventory == 'b':
            verificationKey = 1
            potion = "attaque"
        elif playerChoiceInventory == 'c':
            verificationKey = 1
            potion = "defense"
        elif playerChoiceInventory == 'd':
            verificationKey = 1
        else:
            verificationKey = 0
            print("Tu n'as pas entrée une valeur correcte!")
    return potion


# Achat de la potion
def achatPotion(player, potion):  # Retire le prix de la potion a la monnaie du joueurs
    verificationMoney = player.get("argent") - 200
    if verificationMoney >= 0 and potion != "none":
        player["argent"] = verificationMoney
        ajoutPotion(player, potion)
        print("Achat réussi !")
    elif verificationMoney < 0:
        print("tu n'as pas assez de MokeDollars !")
    return player


def ajoutPotion(player, potion):  # Ajoute la potion a l'inventaire du joueur
    player["inventaire"][potion] = int(player["inventaire"][potion]) + 1
    return player


# Annulation du bonus de dégats/défense
def annulationBonus(player):  # Remet les stats du mokepon a la normale
    if (player["mokepon"]["attaque"] > player["mokepon"]["attaquemax"]) or (
            player["mokepon"]["defense"] > player["mokepon"]["defensemax"]):
        if (player["mokepon"]["attaque"] > player["mokepon"]["attaquemax"]):
            player["mokepon"]["attaque"] = player["mokepon"]["attaquemax"]
        if (player["mokepon"]["defense"] > player["mokepon"]["defensemax"]):
            player["mokepon"]["defense"] = player["mokepon"]["defensemax"]
    return player


# choix du moképon
def mokeponChoice(mokepon):  # Ajoute le nom, et les stats du mokepon du joueur
    verificationKey = 0
    listeDeNomMkpn = ["Andynosaur", "Abysscyan", "Cagdosse"]
    print("Laisse mon te présenter ton futur compagnon,")
    print("Andynosaur, le mokepon dinosaure !")
    print("Abysscyan, le mokepon flottant !")
    print("Cagdosse, le pokemon calcium !")
    while verificationKey == 0:
        playerChoiceMkpnCh = input("Lequel choisis-tu ?\na - Andynosaur\nb - Abysscyan\nc - Cagdosse\n")
        if ((playerChoiceMkpnCh == 'a') or (playerChoiceMkpnCh == 'b') or (playerChoiceMkpnCh == 'c')):
            if (playerChoiceMkpnCh == 'a'):
                mokepon["name"] = listeDeNomMkpn[0]
            if (playerChoiceMkpnCh == 'b'):
                mokepon["name"] = listeDeNomMkpn[1]
            if (playerChoiceMkpnCh == 'c'):
                mokepon["name"] = listeDeNomMkpn[2]
            mokepon["hp"] = 39
            mokepon["attaque"] = 52
            mokepon["vitesse"] = 65
            mokepon["vitessemax"] = 65
            mokepon["attaquemax"] = 53
            mokepon["defense"] = 43
            mokepon["defensemax"] = 45
            mokepon["hpmax"] = 39
            mokepon["niveau"] = 5
            mokepon["niveaumax"] = 100
            mokepon["xp"] = 125
            mokepon["xpmax"] = 216
            verificationKey = 1
            return mokepon
        else:
            verificationKey = 0
            print("Tu n'as pas entrée une valeur correcte!")


# Creation mokepon adverse
def CreaMokeponEnnemi(mokeponEnnemi, niveauMonde):  # Crée un mokepon ennemi, un nom, ses stats
    listeDeNom = ["bajineganne", "Pouikpouik", "melanchiron", "logipeck", "Wumpus", "Closcasque", "Chiamommy",
                  "Teteanos", "psyorisk", "Jeremimique", "fouini", "pytonne", "sarcamouche", "Maskarpe", "Hydroalcolo",
                  "Linuksse", "Gel'Os"]
    listeHp = [45, 50, 60, 70, 80]  # 80
    listeAttaque = [49, 50, 62, 70, 82]  # 100
    listeDefense = [49, 59, 63, 78, 83]  # 123
    listeVitesse = [45, 50, 60, 70, 80]  # 80
    listeNiveauMax = [11, 16, 24, 32, 38]  # 50
    niveauMin = 6
    mokeponEnnemi["name"] = listeDeNom[random.randint(0, (len(listeDeNom) - 1))]
    if(niveauMonde == 0):
        mokeponEnnemi["hp"] = 45
        mokeponEnnemi["hpmax"] = mokeponEnnemi["hp"]
        mokeponEnnemi["attaque"] = 49
        mokeponEnnemi["vitesse"] = 45
        mokeponEnnemi["defense"] = 49
    else:
        mokeponEnnemi["hp"] = random.randint(listeHp[niveauMonde-1], listeHp[niveauMonde])
        mokeponEnnemi["hpmax"] = mokeponEnnemi["hp"]
        mokeponEnnemi["attaque"] = random.randint(listeAttaque[niveauMonde-1], listeAttaque[niveauMonde])
        mokeponEnnemi["vitesse"] = random.randint(listeVitesse[niveauMonde-1], listeVitesse[niveauMonde])
        mokeponEnnemi["defense"] = random.randint(listeDefense[niveauMonde-1], listeDefense[niveauMonde])

    mokeponEnnemi["niveau"] = random.randint(niveauMin, (random.randint((niveauMin + 1), listeNiveauMax[niveauMonde])))
    mokeponEnnemi["xp"] = mokeponEnnemi["niveau"] * mokeponEnnemi["niveau"] * mokeponEnnemi["niveau"]
    return mokeponEnnemi


def monnaieGagner(player):  # Donne une quantité aleatoire d'argent au joueur
    ajout = random.randint(90, 120)
    player["argent"] = player["argent"] + ajout
    return ajout


def calculXpGagner(mokeponEnnemi):  # Calcul l'xp gagnée par le joueurs suite au combat
    exp = int(mokeponEnnemi["xp"] * (mokeponEnnemi["niveau"] / 7))
    print("Felicitation, ton moképon à gagner", exp, "points d'experience !")
    return exp


def addXp(player, mokeponEnnemi):  # Ajoute l'xp au mokepon
    player["mokepon"]["xp"] = player["mokepon"]["xp"] + calculXpGagner(mokeponEnnemi)
    print("Il a désormais", player["mokepon"]["xp"], "point d'xp !")
    while (player["mokepon"]["xp"] >= player["mokepon"]["xpmax"]):
        monteeXp(player)
        print("Super! ton", player["mokepon"]["name"], "est passé niveau", player["mokepon"]["niveau"], "!")


def monteeXp(player):  # Fait evoluer le mokepon du joueurs
    if (player["mokepon"]["xp"] >= player["mokepon"]["xpmax"]):
        player["mokepon"]["xpmax"] = (player["mokepon"]["niveau"] + 1) * (player["mokepon"]["niveau"] + 1) * (
                    player["mokepon"]["niveau"] + 1)
        player["mokepon"]["niveau"] = player["mokepon"]["niveau"] + 1


def augmentationStats(player, evo):  # Amelioration des stats du mokepon suite a une evolution
    listeAtk = [64, 84, 130]
    listDfs = [58, 78, 111]
    listHp = [58, 78, 78]
    listVit = [80, 100, 78]
    player["mokepon"]["hp"] = listHp[evo]
    player["mokepon"]["hpmax"] = listHp[evo]
    player["mokepon"]["attaque"] = listeAtk[evo]
    player["mokepon"]["attaquemax"] = listeAtk[evo]
    player["mokepon"]["vitesse"] = listVit[evo]
    player["mokepon"]["vitessemax"] = listVit[evo]
    player["mokepon"]["defense"] = listDfs[evo]
    player["mokepon"]["defensemax"] = listDfs[evo]


def attaqueMokepon(mokeponCible, valAttaque, valDefense,
                   nameAttaquant):  # Lance l'attaque du personnage, et affiche le nmb de point enlever, gere les CRIT et les MISS
    percentOne = random.randint(3, 25)
    rnd = random.randint(0, 100)
    if ((rnd >= 0) and (rnd <= 5)):
        puissanceAtk = int(critique(valAttaque, percentOne) - valDefense)
        mokeponCible = int(mokeponCible - puissanceAtk)
        print("COUP CRITIQUE !", nameAttaquant, " attaque de ", puissanceAtk, " points !")
    elif ((rnd >= 95) and (rnd <= 100)):
        print("L'attaque a échoué !")
        return mokeponCible
    else:
        puissanceAtk = int(valAttaque - valDefense)
        mokeponCible = int(mokeponCible - puissanceAtk)
        print(nameAttaquant, " attaque de ", puissanceAtk, " points !")
    return mokeponCible


def critique(atk, mult):  # Fct de calcul du coup critique
    return atk + (atk * ((mult / 100)))


def attaqueIa(mokeponEnnemi, player):  # Si l'ennemi attaque, enleve les pts au mokepon du joueurs ou se soigne
    rndCombat = random.randint(1, 100)
    if rndCombat <= 95 and rndCombat > 0:
        player["mokepon"]["hp"] = attaqueMokepon(player["mokepon"]["hp"], mokeponEnnemi["attaque"],
                                                 player["mokepon"]["defense"], mokeponEnnemi["name"])
    elif rndCombat <= 100 and rndCombat > 95:
        mokeponEnnemi["hp"] = soin(mokeponEnnemi["hp"], mokeponEnnemi["hpmax"])
        print(mokeponEnnemi["name"], " s'est soigné de 20 PV, il a désormais ", mokeponEnnemi["hp"],
              "pv !")
    else:
        print("error")
    if player["mokepon"]["hp"] <= 0:
        return "G-0"
    else:
        return "good"


def choixCombatJoueurs(boss):  # Dis le choix du joueurs pour son action de combat
    verificationKeyA = 1
    while verificationKeyA == 1:
        print("Que souhaitez vous faire?")
        playerChoice = input("\na - Attaquer\nb - Voir inventaire\nc - Fuir !\n")
        if playerChoice == 'a':
            verificationKeyA = 0
            return 'atk'
        elif playerChoice == 'b':
            verificationKeyA = 0
            return 'inv'
        elif (playerChoice == 'c') and (boss == False):
            verificationKeyA = 0
            return 'run'
        else:
            verificationKeyA = 1
            print("Tu n'as pas entrée une valeur correcte!")



def attaqueJoueurs(player,
                   mokeponEnnemi):  # Si le joueurs attaque, enleve les pts de vie au mokepon adverse, et fait evoluer le mokepon si passage de palier
    mokeponEnnemi["hp"] = attaqueMokepon(mokeponEnnemi["hp"], player["mokepon"]["attaque"],
                                         mokeponEnnemi["defense"], player["mokepon"]["name"])
    if mokeponEnnemi["hp"] <= 0:
        if ((player["mokepon"]["niveau"] + 1) <= player["mokepon"]["niveaumax"]):
            addXp(player, mokeponEnnemi)
            if (player["mokepon"]["niveau"] >= 16):
                augmentationStats(player, 0)
            if (player["mokepon"]["niveau"] >= 36):
                augmentationStats(player, 1)
            if (player["mokepon"]["niveau"] >= 40):
                augmentationStats(player, 2)
            print("Ce combat t'as fait gagné", monnaieGagner(player), "Mokedollars !")
        return "IA-Dead"
    else:
        return "good"


def textApparitionEnnemi(mokeponEnnemi):  # Texte aleatoire d'appartiton dennemi
    texteMiseEnGarde = ['Attention', 'Prend garde', 'Mefie toi', 'Sois fort', 'Prepare tes attaques', 'Fait gaffe']
    texteCorpUn = ['sauvage', 'terrifiant', 'monstrueux', 'immonde']
    texteCorpDeux = ['apparait', 'surgis', 'debarque', 'est la']

    print(texteMiseEnGarde[random.randint(0, (len(texteMiseEnGarde) - 1))], 'un', mokeponEnnemi['name'], "niveau",
          mokeponEnnemi['niveau'], texteCorpUn[random.randint(0, (len(texteCorpUn) - 1))],
          texteCorpDeux[random.randint(0, (len(texteCorpDeux) - 1))], '!')


def affichagePV(player, mokeponEnnemi, ia):  # Affiche les pv restant du mokepon (ennemi ou kjpueur)
    if (ia):
        if (player["mokepon"]["hp"] < 0):
            player["mokepon"]["hp"] = 0
        if (player["mokepon"]["hp"] > 0):
            print("Il reste à ton", player["mokepon"]["name"], ",", player["mokepon"]["hp"], "PV")
    else:
        if (mokeponEnnemi["hp"] <= 0):
            print("Super, tu as térrassé le", mokeponEnnemi["name"], "!")
            mokeponEnnemi["hp"] = 0
        if (mokeponEnnemi["hp"] > 0):
            print("Il reste au", mokeponEnnemi["name"], "ennemi,", mokeponEnnemi["hp"], "PV")


def roulementDesTours(player, niv, boss,mobBoss):  # Fct qui declenche un combat, en fct de la vitesse du mokepon, celui ci attk en 1er ou pas.
    death = "start"
    tours = 1
    verificationKeyCJ = 1
    mokeponEnnemi = {}
    if (boss):
        listeDeNom = ["bajineganne", "Pouikpouik", "melanchiron"]
        listeHp = [75, 80, 85]  # 80
        listeAttaque = [90, 100, 95]  # 100
        listeDefense = [123, 100, 115]  # 123
        listeVitesse = [80, 90, 80]  # 80
        niveauBoss = 50  # 50
        mokeponEnnemi["name"] = listeDeNom[mobBoss]
        mokeponEnnemi["hp"] = listeHp[mobBoss]
        mokeponEnnemi["hpmax"] = mokeponEnnemi["hp"]
        mokeponEnnemi["attaque"] = listeAttaque[mobBoss]
        mokeponEnnemi["vitesse"] = listeVitesse[mobBoss]
        mokeponEnnemi["defense"] = listeDefense[mobBoss]
        mokeponEnnemi["niveau"] = niveauBoss
        mokeponEnnemi["xp"] = mokeponEnnemi["niveau"] * mokeponEnnemi["niveau"] * mokeponEnnemi["niveau"]
        return mokeponEnnemi
    else:
        CreaMokeponEnnemi(mokeponEnnemi, niv)

    if (player["mokepon"]["vitesse"] < mokeponEnnemi["vitesse"]):
        tours = 2
        verificationKeyCJ = 0
    elif (player["mokepon"]["vitesse"] == mokeponEnnemi["vitesse"]):
        tours = 1
        verificationKeyCJ = 1
    else:
        tours = 1

    if (boss):
        print("afficher ici phrase du boss et ses mokepon")
    else:
        interactionEnnemi()
        textApparitionEnnemi(mokeponEnnemi)
    affichagePV(player, mokeponEnnemi, False)

    while death != "G-0" and death != "IA-Dead" and death != 'run':

        # Roulement des tours
        if (tours % 2) == 0:  # Si pair -> Ennemi joue
            print(Style.RESET_ALL)
            print('\033[34m')
            death = attaqueIa(mokeponEnnemi, player)
            affichagePV(player, mokeponEnnemi, True)
            verificationKeyCJ = 1
            if death == "G-0":
                print(Style.RESET_ALL)
                return "G-0"
        else:  # Si impair -> joueur attaque
            # Menu du choix de l'action du joueur
            while verificationKeyCJ == 1:
                print(Style.RESET_ALL)
                choix = choixCombatJoueurs(boss)
                if (choix == 'inv'):
                    if (playerInventory(player) == False):
                        verificationKeyCJ = 1
                    else:
                        verificationKeyCJ = 0
                elif (choix == 'atk'):
                    print('\033[31m')
                    death = attaqueJoueurs(player, mokeponEnnemi)
                    affichagePV(player, mokeponEnnemi, False)
                    verificationKeyCJ = 0
                elif (choix == 'run'):
                    annulationBonus(player)
                    print('Vous fuyez le combat !')
                    death = 'run'
                    verificationKeyCJ = 0
                else:
                    print("Error !")
                    verificationKeyCJ = 1
            verificationKeyCJ = 0
            if death == "IA-Dead":
                annulationBonus(player)
                print(Style.RESET_ALL)
                return "good"
        tours = tours + 1


def MenuDirection(n, s, e, w):
    print("Ou voulez vous vous dirigez ?")
    if n == True:
        print("1 : Haut")
    if s == True:
        print("2 : Bas")
    if e == True:
        print("3 : Droite")
    if w == True:
        print("4 : Gauche")

    print("---------------------------")
    direc = input()

    if n == False and direc == '1':
        print("Evite de foncer dans les murs !")
        direc = MenuDirection(n, s, e, w)
        return direc
    elif s == False and direc == '2':
        print("Evite de foncer dans les murs !")
        direc = MenuDirection(n, s, e, w)
        return direc
    elif e == False and direc == '3':
        print("Evite de foncer dans les murs !")
        direc = MenuDirection(n, s, e, w)
        return direc
    elif w == False and direc == '4':
        print("Evite de foncer dans les murs !")
        direc = MenuDirection(n, s, e, w)
        return direc

    elif direc != '1' and direc != '2' and direc != '3' and direc != '4':
        print("erreur de frappe ? Recommencez donc")
        direc = MenuDirection(n, s, e, w)  # Recursivité ta vu ;p
        return direc

    else:
        return direc


#########################################################   MAP1

def a11(player):
    clear_aff()
    random_area()
    MenuDirection(False, False, True, False)


def a12(player):
    clear_aff()
    random_area()
    gm=roulementDesTours(player,0,False,0)
    if gm=="G-0":
        print("Game Over - Trop faible pour ce jeu ?")
        briller()
        sys.exit()
    acc = MenuDirection(False, False, True, True)
    if acc == '4':
        a11(player)
        a12(player)


def a13(player):
    clear_aff()
    random_area()
    ajoutPotion(player, "soin")

    acc = MenuDirection(False, True, False, True)
    if acc == '4':
        a12(player)
        a13(player)


def b13(player):
    clear_aff()
    random_area()
    # event ?
    acc = MenuDirection(True, True, False, False)
    if acc == '1':
        a13(player)
        b13(player)


def c13(player):
    clear_aff()
    random_area()
    gm=roulementDesTours(player,0,False,0)
    if gm=="G-0":
        print("Game Over - Trop faible pour ce jeu ?")
        briller()
        sys.exit()
    acc = MenuDirection(True, False, True, False)
    if acc == '1':
        b13(player)
        c13(player)


def c14(player):
    clear_aff()
    random_area()
    # event ?
    acc = MenuDirection(False, False, True, True)
    if acc == '4':
        c13(player)
        c14(player)


def c15(player):
    clear_aff()
    random_area()
    gm=roulementDesTours(player,0,False,0)
    if gm=="G-0":
        print("Game Over - Trop faible pour ce jeu ?")
        briller()
        sys.exit()
    acc = MenuDirection(False, False, True, True)
    if acc == '4':
        c14(player)
        c15(player)
    else:
        return True


def map1(player):
    success = False
    player["position"]=1
    while success == False:
        a11(player)
        a12(player)
        a13(player)
        b13(player)
        c13(player)
        c14(player)
        success = c15(player)


#########################################################   MAP2

def b21(player):
    clear_aff()
    random_area()
    gm=roulementDesTours(player,1,False,0)
    if gm=="G-0":
        print("Game Over - Trop faible pour ce jeu ?")
        briller()
        sys.exit()
    MenuDirection(False, False, True, False)  # droite


def b22(player):
    clear_aff()
    random_area()
    # event ?
    acc = MenuDirection(False, False, True, True)  # gauche droite
    if acc == '4':
        b21(player)
        b22(player)


def b23(player):
    clear_aff()
    random_area()
    gm=roulementDesTours(player,1,False,0)
    if gm=="G-0":
        print("Game Over - Trop faible pour ce jeu ?")
        briller()
        sys.exit()
    acc = MenuDirection(False, True, False, True)  # gauche bas
    if acc == '4':
        b22(player)
        b23(player)


def c23(player):
    clear_aff()
    random_area()
    # event ?
    acc = MenuDirection(True, True, False, False)  # haut bas
    if acc == '1':
        b23(player)
        c23(player)


def d23(player):
    clear_aff()
    random_area()
    ajoutPotion(player, "soin")
    acc = MenuDirection(True, False, True, False)  # haut droite
    if acc == '1':
        c23(player)
        d23(player)


def d24(player):
    clear_aff()
    random_area()
    # event ?
    acc = MenuDirection(False, False, True, True)  # gauche droite
    if acc == '4':
        d23(player)
        d24(player)


def d25(player):
    clear_aff()
    random_area()
    # event ?
    acc = MenuDirection(True, False, False, True)  # haut gauche
    if acc == '4':
        d24(player)
        d25(player)


def c25(player):
    clear_aff()
    random_area()
    gm=roulementDesTours(player,1,False,0)
    if gm=="G-0":
        print("Game Over - Trop faible pour ce jeu ?")
        briller()
        sys.exit()
    acc = MenuDirection(True, True, False, False)  # haut bas
    if acc == '2':
        d25(player)
        c25(player)


def b25(player):
    clear_aff()
    random_area()
    # event ?
    acc = MenuDirection(True, True, False, False)  # haut bas
    if acc == '2':
        c25(player)
        b25(player)


def a25(player):  # end of road
    clear_aff()
    random_area()
    gm=roulementDesTours(player,1,False,0)
    if gm=="G-0":
        print("Game Over - Trop faible pour ce jeu ?")
        briller()
        sys.exit()
    acc = MenuDirection(True, True, False, False)  # haut bas
    if acc == '2':
        b25(player)
        a25(player)
    else:
        return True


def map2(player):
    success = False
    player["position"] = 2
    while success == False:
        b21(player)
        b22(player)
        b23(player)
        c23(player)
        d23(player)
        d24(player)
        d25(player)
        c25(player)
        b25(player)
        success = a25(player)


#########################################################   MAP3

def c31(player):
    clear_aff()
    random_area()
    gm=roulementDesTours(player,2,False,0)
    if gm=="G-0":
        print("Game Over - Trop faible pour ce jeu ?")
        briller()
        sys.exit()
    MenuDirection(False, False, True, False)


def c32(player):
    clear_aff()
    random_area()
    # event ?
    acc = MenuDirection(False, False, True, True)
    if acc == '4':
        c31(player)
        c32(player)


def c33(player):
    clear_aff()
    random_area()
    # event
    acc = MenuDirection(True, False, False, True)
    if acc == '4':
        c32(player)
        c33(player)


def b33(player):
    clear_aff()
    random_area()
    ajoutPotion(player, "soin")
    acc = MenuDirection(True, True, False, False)
    if acc == '2':
        c33(player)
        b33(player)


def a33(player):
    clear_aff()
    random_area()
    gm=roulementDesTours(player,2,False,0)
    if gm=="G-0":
        print("Game Over - Trop faible pour ce jeu ?")
        briller()
        sys.exit()
    acc = MenuDirection(True, True, False, False)
    if acc == '2':
        b33(player)
        a33(player)
    else:
        return True


def map3(player):
    success = False
    player["position"] = 3
    while success == False:
        c31(player)
        c32(player)
        c33(player)
        b33(player)
        success = a33(player)


#########################################################   MAP4

def b41(player):
    clear_aff()
    random_area()
    gm=roulementDesTours(player,3,False,0)
    if gm=="G-0":
        print("Game Over - Trop faible pour ce jeu ?")
        briller()
        sys.exit()
    MenuDirection(False, False, True, False)  # droite


def b42(player):
    clear_aff()
    random_area()
    # event ?
    acc = MenuDirection(False, False, True, True)  # gauche droite
    if acc == '4':
        b41(player)
        b42(player)


def b43(player):
    clear_aff()
    random_area()
    # event
    acc = MenuDirection(False, False, True, True)  # gauche droite
    if acc == '4':
        b42(player)
        b43(player)


def b44(player):
    clear_aff()
    random_area()
    gm=roulementDesTours(player,3,False,0)
    if gm=="G-0":
        print("Game Over - Trop faible pour ce jeu ?")
        briller()
        sys.exit()
    acc = MenuDirection(True, True, False, True)  # haut bas gauche
    if acc == '4':
        b43(player)
        b44(player)
    elif acc == '1':
        a44(player)


def a44(player):
    random_area()
    rickroll()
    MenuDirection(False, True, False, False)  # bas
    b44(player)


def c44(player):
    clear_aff()
    random_area()
    gm=roulementDesTours(player,3,False,0)
    if gm=="G-0":
        print("Game Over - Trop faible pour ce jeu ?")
        briller()
        sys.exit()
    acc = MenuDirection(True, True, False, False)  # haut bas
    if acc == '1':
        b44(player)
        c44(player)


def d44(player):
    clear_aff()
    random_area()
    ajoutPotion(player, "soin")
    acc = MenuDirection(True, True, False, False)  # haut bas
    if acc == '1':
        c44(player)
        d44(player)


def e44(player):  # end of road
    clear_aff()
    random_area()
    # event3
    acc = MenuDirection(True, True, False, False)  # haut bas
    if acc == '1':
        d44(player)
        e44(player)
    else:
        return True


def map4(player):
    success = False
    player["position"] = 4
    while success == False:
        b41(player)
        b42(player)
        b43(player)
        b44(player)
        c44(player)
        d44(player)
        success = e44(player)


#########################################################   MAP5

def b51(player):
    clear_aff()
    random_area()
    # event
    MenuDirection(False, False, True, False)  # droite


def b52(player):
    clear_aff()
    random_area()
    gm=roulementDesTours(player,4,False,0)
    if gm=="G-0":
        print("Game Over - Trop faible pour ce jeu ?")
        briller()
        sys.exit()
    acc = MenuDirection(False, False, True, True)  # gauche droite
    if acc == '4':
        b51(player)
        b52(player)


def b53(player):
    clear_aff()
    random_area()
    # event
    acc = MenuDirection(False, False, True, True)  # gauche droite
    if acc == '4':
        b52(player)
        b53(player)


def b54(player):
    clear_aff()
    random_area()
    gm=roulementDesTours(player,4,False,0)
    if gm=="G-0":
        print("Game Over - Trop faible pour ce jeu ?")
        briller()
        sys.exit()
    acc = MenuDirection(False, False, True, True)  # gauche droite
    if acc == '4':
        b53(player)
        b54(player)


def b55(player):
    clear_aff()
    random_area()
    ajoutPotion(player, "soin")
    acc = MenuDirection(True, False, False, True)  # gauche haut
    if acc == '4':
        b54(player)
        b55(player)


def a55(player):
    clear_aff()
    random_area()
    gm=roulementDesTours(player,4,False,0)
    if gm=="G-0":
        print("Game Over - Trop faible pour ce jeu ?")
        briller()
        sys.exit()
    acc = MenuDirection(True, True, False, False)  # haut bas
    if acc == '2':
        b55(player)
        a55(player)


def mb55(player):  # end of road
    clear_aff()
    random_area()
    gm=roulementDesTours(player,4,False,0)
    if gm=="G-0":
        print("Game Over - Trop faible pour ce jeu ?")
        briller()
        sys.exit()
    acc = MenuDirection(True, True, False, False)  # haut bas
    if acc == '2':
        a55(player)
        mb55(player)
    else:
        return True


def map5(player):
    success = False
    player["position"] = 5
    while success == False:
        b51(player)
        b52(player)
        b53(player)
        b54(player)
        b55(player)
        a55(player)
        success = mb55(player)


#########################################################   MAP6

def c61(player):
    clear_aff()
    random_area()
    # event
    MenuDirection(True, False, False, False)


def b61(player):
    clear_aff()
    random_area()
    gm=roulementDesTours(player,4,False,0)
    if gm=="G-0":
        print("Game Over - Trop faible pour ce jeu ?")
        briller()
        sys.exit()

    acc = MenuDirection(False, True, True, False)
    if acc == '2':
        c61(player)
        b61(player)


def b62(player):
    clear_aff()
    random_area()
    # event
    acc = MenuDirection(False, False, True, True)
    if acc == '4':
        b61(player)
        b62(player)


def b63(player):
    clear_aff()
    random_area()
    gm=roulementDesTours(player,4,False,0)
    if gm=="G-0":
        print("Game Over - Trop faible pour ce jeu ?")
        briller()
        sys.exit()
    acc = MenuDirection(False, True, False, True)
    if acc == '4':
        b62(player)
        b63(player)


def c63(player):
    clear_aff()
    random_area()
    # event
    acc = MenuDirection(True, True, False, False)
    if acc == '1':
        b63(player)
        c63(player)


def d63(player):
    clear_aff()
    random_area()
    gm=roulementDesTours(player,4,False,0)
    if gm=="G-0":
        print("Game Over - Trop faible pour ce jeu ?")
        briller()
        sys.exit()
    acc = MenuDirection(True, True, True, False)
    if acc == '1':
        c63(player)
        d63(player)
    elif acc == '2':
        e63(player)


def e63(player):  # special path
    clear_aff()
    random_area()
    ajoutPotion(player, "soin")
    MenuDirection(True, False, False, False)
    d63(player)


def d64(player):
    clear_aff()
    random_area()
    gm=roulementDesTours(player,4,False,0)
    if gm=="G-0":
        print("Game Over - Trop faible pour ce jeu ?")
        briller()
        sys.exit()
    acc = MenuDirection(False, False, True, True)
    if acc == '4':
        d63(player)
        d64(player)


def d65(player):
    clear_aff()
    random_area()
    # event
    acc = MenuDirection(True, True, False, True)
    if acc == '4':
        d64(player)
        d65(player)
    elif acc == '2':
        e65(player)


def e65(player):  # special path
    clear_aff()
    random_area()
    gm=roulementDesTours(player,4,False,0)
    if gm=="G-0":
        print("Game Over - Trop faible pour ce jeu ?")
        briller()
        sys.exit()
    MenuDirection(True, False, False, False)
    d65(player)


def c65(player):
    clear_aff()
    random_area()
    # event
    acc = MenuDirection(True, True, False, False)
    if acc == '2':
        d65(player)
        c65(player)


def b65(player):
    clear_aff()
    random_area()
    ajoutPotion(player, "soin")
    acc = MenuDirection(True, True, False, False)
    if acc == '2':
        c65(player)
        b65(player)


def a65(player):
    clear_aff()
    random_area()
    gm=roulementDesTours(player,4,False,0)
    if gm=="G-0":
        print("Game Over - Trop faible pour ce jeu ?")
        briller()
        sys.exit()
    acc = MenuDirection(False, True, True, False)
    if acc == '2':
        b65(player)
        a65(player)


def a66(player):
    clear_aff()
    random_area()
    acc = MenuDirection(False, False, True, True)
    if acc == '4':
        a65(player)
        a66(player)
    else:
        return True


def map6(player):
    success = False
    player["position"] = 6
    while success == False:
        c61(player)
        b61(player)
        b62(player)
        b63(player)
        c63(player)
        d63(player)
        d64(player)
        d65(player)
        c65(player)
        b65(player)
        a65(player)
        success = a66(player)


def boss(player):
    i=0
    print("Devant vous se présente le grand fléau de 2020, l'Horrible Corvid et il vous agresse, préparez vous a riposter !")
    while i<3:
        gm=roulementDesTours(player, 4, True, i)
        if gm=="G-0":
            print("Game Over - Trop faible pour ce jeu ?")
            briller()
            sys.exit()
        i+=1
    felicitation()

menu()
