# Cast IA

**Plateforme d'aide à la présélection des candidats pour les castings.**

## Présentation

Cast IA est une plateforme destinée aux producteurs et aux directeurs de casting. Son objectif est de faciliter le tri d'un grand nombre de candidatures et l'identification des profils les plus adaptés à chaque rôle.

Le fonctionnement cible est le suivant :

1. Le producteur ou le directeur de casting définit un projet et ses rôles.
2. Les candidats déposent leur profil et leur audition pour un rôle.
3. Les auditions sont analysées selon des critères définis pour ce rôle.
4. Chaque candidature reçoit une note accompagnée, à terme, d'éléments explicatifs.
5. Pour chaque rôle, Cast IA met en avant les **15 candidats les mieux notés**.
6. Le producteur consulte les auditions et conserve la décision finale.

L'intelligence artificielle est un outil d'aide à la présélection : elle ne remplace pas le jugement du producteur et ses évaluations doivent pouvoir être contrôlées.

## Technologies

### Backend
- Python
- Django 5.2
- Django REST Framework
- SQLite
- Redis (configuration prévue pour les traitements asynchrones)
- librosa (choix retenu pour l'extraction des caractéristiques audio)

### Frontend
- React 19
- Vite
- JavaScript
- Axios
- React Router

## Architecture

```text
cast-ia/
├── backend/
│   ├── ai/
│   ├── applicants/
│   ├── casting/
│   ├── evaluations/
│   ├── config/
│   ├── manage.py
│   └── docker-compose.yml
│
├── frontend/
│   ├── public/
│   ├── src/
│   └── package.json
│
├── .gitignore
└── README.md
```

## Fonctionnalités actuellement présentes dans le backend

- Authentification Django.
- Profils avec deux types de comptes : directeur de casting et candidat.
- Création automatique d'un profil lors de la création d'un utilisateur.
- Modèle de données pour les scénarios de casting.
- Consultation des scénarios par les utilisateurs authentifiés.
- Création de scénarios réservée aux directeurs de casting.
- Modèles de données pour les auditions vidéo et les évaluations.
- Champ de note globale associé à une évaluation.

## Interface actuelle et fonctionnalités à développer

L'interface React présente le concept Cast IA et un aperçu interactif de classements par rôle. Les noms et les notes affichés dans cet aperçu sont **des données fictives de démonstration** : ils ne proviennent pas encore du backend.

Les éléments suivants restent à implémenter pour obtenir le fonctionnement réel :

- Modèle de données des rôles, rattachés aux projets/castings.
- Association de chaque audition au rôle concerné.
- Dépôt et consultation des vidéos d'audition via l'API.
- Définition des critères de notation par rôle.
- Analyse automatique des auditions et génération de notes justifiables.
- API de classement qui retourne les 15 meilleures candidatures pour chaque rôle.
- Interface producteur connectée aux données réelles, avec consultation des auditions et validation humaine.

**Important :** le classement automatique et le Top 15 réel ne sont pas encore opérationnels. L'aperçu de la page d'accueil sert uniquement à illustrer le résultat attendu.

## Installation et lancement

### 1. Backend

Depuis le dossier `backend` :

Créer et activer un environnement virtuel :

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Installer les dépendances :

```powershell
pip install -r requirements.txt
```

Configurer les variables d'environnement :

```powershell
Copy-Item .env.example .env
```

Générer une clé secrète Django :

```powershell
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copier la clé générée dans le fichier `.env`, puis appliquer les migrations et lancer le serveur :

```powershell
python manage.py migrate
python manage.py runserver
```

Backend : http://127.0.0.1:8000/

### 2. Frontend

Depuis le dossier `frontend` :

```powershell
npm install
npm run dev
```

Frontend : http://localhost:5173/

### 3. Redis (facultatif pour le démarrage de base)

Pour lancer Redis avec Docker, depuis le dossier `backend` :

```powershell
docker compose up -d
```

## État du projet

Cast IA est un prototype en développement. La base Django contient les premiers modèles de profils, scénarios, auditions et évaluations. L'interface présente désormais la vision produit centrée sur la présélection et le Top 15 par rôle. Le modèle métier complet des rôles, l'analyse IA et le classement réel restent à construire.

## Auteur

Projet académique et technique — Cast IA.
