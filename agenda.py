dentiste = {
    "titre": "Dentiste",
    "type": "rendez-vous",
    "debut": "2026-11-24 15:00",
    "duree_min": 30,
    "pour_qui": "moi",
    "ressources": [
        {"nom": "argent", "quantite": -25, "statut": "estimée"},
    ],
}


sport = {
    "titre": "Sport",
    "type": "séance",
    "debut": "2026-11-24 18:00",
    "duree_min": 60,
    "pour_qui": "moi",
    "ressources": [
        {"nom": "énergie", "quantite": -10, "statut": "estimée"},
    ],
}

courses = {
    "titre": "Courses",
    "type": "tâche",
    "debut": "2026-11-25",
    "duree_min": None,
    "pour_qui": "foyer",
    "ressources": [
        {"nom": "argent", "quantite": -85, "statut": "estimée"},
    ],
}

cinema = {
    "titre": "Cinéma",
    "type": "rendez-vous",
    "debut": "2026-11-27 20:30",
    "duree_min": 120,
    "pour_qui": "foyer",
    "ressources": [
        {"nom": "argent", "quantite": -24, "statut": "estimée"},
    ],
}

salaire = {
    "titre": "Salaire",
    "type": "revenu",
    "debut": "2026-11-28",
    "duree_min": None,
    "pour_qui": "foyer",
    "ressources": [
        {"nom": "argent", "quantite": 1450, "statut": "confirmée"},
    ],
}

loyer = {
    "titre": "Loyer",
    "type": "dépense",
    "debut": "2026-12-05",
    "duree_min": None,
    "pour_qui": "foyer",
    "ressources": [
        {"nom": "argent", "quantite": -650, "statut": "confirmée"},
    ],
}

courses_1 = {
    "titre": "Courses",
    "type": "tâche",
    "debut": "2026-11-28",
    "duree_min": None,
    "pour_qui": "foyer",
    "ressources": [
        {"nom": "argent", "quantite": -110, "statut": "estimée"},
    ],
}

electricite = {
    "titre": "Électricité",
    "type": "dépense",
    "debut": "2026-12-02",
    "duree_min": None,
    "pour_qui": "foyer",
    "ressources": [
        {"nom": "argent", "quantite": -72, "statut": "confirmée"},
    ],
}


agenda = [electricite, courses_1, courses, cinema, salaire, sport, dentiste, loyer]

for entree in agenda:
    print(entree)

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



