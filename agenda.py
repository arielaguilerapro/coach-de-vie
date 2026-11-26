import json

def sauvegarder(agenda, chemin):
    with open(chemin, 'w', encoding='utf-8') as fichier_json:
        json.dump(agenda, fichier_json)

def charger(chemin):
    """
    Permet de charger un agenda
    Paramètre : le chemin vers le fichier json qui contient l'agenda
    Retour : 
             La liste présente dans le fichier json
             SI le fichier est introuvable, renvoie une liste vide
             SI le fichier est abîmé, ne touche à rien, renvoie None

    """
    chargement = []
    try:
        with open(chemin, encoding='utf-8') as fichier_json:
            chargement = json.load(fichier_json)
            return chargement
    except FileNotFoundError:
        print("Fichier introuvable")
        return chargement
    except json.decoder.JSONDecodeError:
        print("Fichier abîmé")
        

def debut(entree):
    return entree["debut"]

def ajouter_entree(agenda, titre, type_entree, debut, pour_qui, ressources=None, duree_min=None):
    """
    Permet d'ajouter une entrée à l'agenda
    Paramètres : l'agenda, le titre de l'entrée, le type d'entrée, la date et l'heure du début, pour qui, les ressources nécessaires et la durée de l'entrée
    Ne retourne rien.
    """
    if ressources is None:
        ressources = []
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
        print(f"{entree['debut'][10:]} {entree['titre']} ({entree['type']}, {entree['pour_qui']})", end=" ")
        for ress in entree['ressources']:
            print(f"{ress['nom']}  {ress['quantite']}")
            

def reste(agenda, ressource, date_limite, reserve_depart):
    """
    Renvoie ce qui reste d'une ressource à la fin de date_limite
    Paramètre : l'agenda, la ressource, la date limite et la réserve de départ
    Retourne : ce qu'il reste de la ressource à la date limite
    """
    reserve = reserve_depart
    for entree in agenda:
        if entree['debut'][:10] <= date_limite:
            for ress in entree["ressources"]:
                if ress['nom'] == ressource:
                    reserve += ress['quantite']
    return reserve



agenda = charger("donnees/agenda.json")


if agenda is not None:
    afficher_semaine(agenda, "2024-06-01", "2024-06-07")
    sauvegarder(agenda, "donnees/agenda.json")