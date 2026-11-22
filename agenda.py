def debut(entree):
        return entree["debut"]

def ajouter_entree(agenda, titre, type_entree, debut, pour_qui, ressources=None, duree_min=None):
    """
    Permet d'ajouter une entrée à l'agenda
    Paramètres : l'agenda, le titre de l'entrée, le type d'entrée, la date et l'heure du début, pour qui, les ressources nécéssaires et la durée de l'entrée
    Ne retourne rien.
    """
    entree = {
        'titre': titre,
        'type': type_entree,
        'debut': debut, 
        'duree_min': duree_min,
        'pour_qui': pour_qui,
        'ressources': ressources,
        }
    agenda.append(entree)
    
def afficher_journee(agenda, jour):
    """
    Affiche les entrées d'un jour, triées par heure
    Paramètres : l'agenda et le jour demandé
    Ne retourne rien
    """
    planning = []
    for entree in agenda:
        if entree['debut'][:10] == jour:
            planning.append(entree)

    planning.sort(key=debut)
    print(planning)

def afficher_semaine(agenda, premier_jour, dernier_jour):
    """
    Affiche chaque jour qui a des entrées, dans l'ordre
    Paramètre: l'agenda, le premier jour, le dernier jour
    """
    print(f"Semaine du {premier_jour} au {dernier_jour}")
    semaine = []
    jour = ""
    for entree in agenda:
        if entree['debut'][:10] >= premier_jour and entree['debut'][:10] <= dernier_jour:
            semaine.append(entree)
    semaine.sort(key=debut)
    for entree in semaine:
        if(entree['debut'][:10] != jour):
            print(f"- {entree['debut'][:10]}")
            jour = entree['debut'][:10]
        if entree['ressources'] != None:
            for ress in entree['ressources']:
                print(f"{entree['debut'][10:]} {entree['titre']} ({entree['type']}, {entree['pour_qui']})  {ress['nom']}  {ress['quantite']}")


def reste(agenda, ressource, date_limite, reserve_depart):
    """
    Renvoie ce qui reste d'une ressource à la fin de date_limite
    Paramètre : l'agenda, la ressource, la date limite et la réserve de départ
    Retourne : ce qu'il reste de la ressource à la date limite
    """
    reserve = reserve_depart
    for entree in agenda:
        if entree['debut'][:10] <= date_limite:
            if entree['ressources'] != None:
                for ress in entree["ressources"]:
                    if ress['nom'] == ressource:
                        reserve += ress['quantite']
    return reserve

    


    




agenda = []

ajouter_entree(agenda, "Dentiste", "rendez-vous", "2026-11-24 15:00", "moi", [{'nom': "argent", 'quantite': -25, 'statut': "estimée"},], 30)
ajouter_entree(agenda, "Sport", "séance", "2026-11-24 18:00", "moi", [{'nom': "énergie", 'quantite': -10, 'statut': "estimée"},], 60)
ajouter_entree(agenda, "Courses", "tâche", "2026-11-25", "foyer", [{'nom': "argent", 'quantite': -85, 'statut': "estimée"},], None)
ajouter_entree(agenda, "Cinéma", "rendez-vous", "2026-11-27 20:30", "foyer", [{'nom': "argent", 'quantite': -24, 'statut': "estimée"},], 120)
ajouter_entree(agenda, "Salaire", "revenu", "2026-11-28", "foyer", [{'nom': "argent", 'quantite': 1450, 'statut': "confirmée"},], None)
ajouter_entree(agenda, "Loyer", "dépense", "2026-12-05", "foyer", [{'nom': "argent", 'quantite': -650, 'statut': "estimée"},], None)
ajouter_entree(agenda, "Courses", "tâche", "2026-11-28", "foyer", [{'nom': "argent", 'quantite': -110, 'statut': "estimée"},], None)
ajouter_entree(agenda, "Électricité", "dépense", "2026-12-02", "foyer", [{'nom': "argent", 'quantite': -72, 'statut': "confirmée"},], None)
#afficher_semaine(agenda, "2026-11-23", "2026-11-29")

assert reste(agenda, "argent", "2026-11-24", 420) == 395
assert reste(agenda, "argent", "2026-11-27", 420) == 286
assert reste(agenda, "argent", "2026-11-28", 420) == 1626
assert reste(agenda, "argent", "2026-12-05", 420) == 904

ajouter_entree(agenda, "Pharmacie", "dépense", "2026-11-26", "foyer", [{'nom': "argent", 'quantite': -12, 'statut': "estimée"}], None)
assert reste(agenda, "argent", "2026-11-27", 420) == 274

"""
for entree in agenda:
    
    if entree["debut"][:10] == "2026-11-24":
        print(entree)    

argent_total = 420

for entree in agenda:
    for ressource in entree["ressources"]:
        if ressource["nom"] == "argent":
            argent_total += ressource["quantite"]
        
print(argent_total)

argent_total = 420

for entree in agenda:
    if entree["debut"][:10] <= "2026-11-27":
        for ressource in entree["ressources"]:
            if ressource["nom"] == "argent":
                argent_total += ressource["quantite"]
        
print(argent_total)

"""

