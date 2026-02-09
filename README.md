🎓 EduNotes - Gestionnaire de Notes Étudiant

EduNotes est une application web moderne et intuitive développée avec Flask (Python) permettant aux étudiants de gérer leurs résultats scolaires, calculer leur moyenne générale et suivre leur progression académique.

(Remplacer par une capture d'écran réelle)

✨ Fonctionnalités Principales

📊 Tableau de Bord Interactif : Visualisation immédiate de la moyenne générale, du statut d'admission (Admis/Ajourné) et graphique de répartition des notes.

📝 Gestion Complète (CRUD) : Ajouter, modifier et supprimer des notes et des matières facilement.

📈 Suivi de Progression : Barres de progression visuelles pour chaque matière et indicateurs de couleur (Vert/Rouge) selon la performance.

🔍 Recherche & Filtres : Filtrage dynamique instantané des matières dans les listes.

💾 Persistance des Données : Utilisation de SQLite pour sauvegarder les notes de manière fiable.

📂 Export CSV : Téléchargement du relevé de notes complet au format CSV pour Excel ou autres tableurs.

🎨 Interface Moderne : Design réactif et élégant conçu avec Tailwind CSS, incluant des animations fluides et un mode sombre léger (Slate).

🛠️ Stack Technique

Backend : Python 3, Flask

Base de données : SQLite3 (Native)

Frontend : HTML5, Jinja2 Templating

Styles : Tailwind CSS (via CDN)

Icônes : FontAwesome 6

Graphiques : Chart.js

🚀 Installation et Démarrage

Suivez ces étapes pour lancer le projet localement.

Prérequis

Python 3.x installé sur votre machine.

1. Cloner ou télécharger le projet

Placez tous les fichiers (app.py et le dossier templates/) dans un répertoire.

2. Créer un environnement virtuel (recommandé)

python -m venv venv
# Sur Windows
venv\Scripts\activate
# Sur macOS/Linux
source venv/bin/activate


3. Installer les dépendances

Ce projet ne nécessite que Flask comme dépendance externe majeure.

pip install flask


4. Lancer l'application

python app.py


5. Accéder à l'application

Ouvrez votre navigateur et allez à l'adresse suivante :
http://127.0.0.1:5000

La base de données edunotes.db sera créée automatiquement lors du premier lancement.

📂 Structure du Projet

EduNotes/
│
├── app.py                # Point d'entrée, logique serveur et routes
├── edunotes.db           # Base de données SQLite (générée automatiquement)
├── README.md             # Documentation du projet
│
└── templates/            # Dossier des fichiers HTML
    ├── index.html        # Page d'accueil (Tableau de bord)
    ├── releve.html       # Liste complète des notes (Relevé)
    ├── ajouter.html      # Formulaire d'ajout
    └── modifier.html     # Formulaire de modification


📖 Guide d'Utilisation

Ajouter une note : Cliquez sur "Nouvelle Note", entrez le nom de la matière, la note (/20) et le coefficient.

Voir le Dashboard : La page d'accueil affiche votre moyenne pondérée. Le statut "ADMIS" s'affiche si la moyenne est >= 10.

Modifier une entrée : Depuis la page "Mon Relevé", cliquez sur l'icône crayon ✏️ pour corriger une erreur.

Supprimer une note : Depuis la page "Mon Relevé", cliquez sur la corbeille 🗑️. Une fenêtre de confirmation apparaîtra pour éviter les erreurs.

Exporter : Utilisez le bouton "Exporter" sur la page Relevé pour obtenir un fichier .csv de vos résultats.

🛡️ Sécurité

Les entrées utilisateur sont protégées contre les injections SQL grâce à l'utilisation des paramètres de requête SQLite (?).

Une validation côté serveur assure que les notes restent entre 0 et 20.

🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou une Pull Request pour suggérer des améliorations.

Fait avec ❤️ pour les étudiants.