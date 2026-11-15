# Cast IA

**Plateforme intelligente de gestion et d'évaluation des auditions.**

## Présentation

Cast IA est une plateforme web destinée à faciliter l'organisation des castings. Elle permet aux directeurs de casting de publier des scénarios et aux candidats de participer aux auditions.

Le projet prévoit également l'intégration de méthodes d'intelligence artificielle afin d'assister l'analyse des performances des candidats.

## Technologies

### Backend
- Python
- Django 5.2
- Django REST Framework
- SQLite
- Redis (configuration prévue pour les traitements asynchrones)

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

## Fonctionnalités implémentées

- Gestion des utilisateurs avec l'authentification Django.
- Gestion des profils avec deux rôles : directeur de casting et candidat.
- Création automatique d'un profil lors de la création d'un utilisateur.
- Modèle de données pour les scénarios de casting.
- Consultation des scénarios par les utilisateurs authentifiés.
- Création de scénarios réservée aux directeurs de casting.
- Modèles de données pour les auditions et les évaluations.
- API REST pour la consultation et la création des scénarios.

## Fonctionnalités en cours de développement

- Interface utilisateur React dédiée à Cast IA.
- Soumission et gestion des vidéos d'audition via une API.
- Traitement automatique des auditions.
- Intégration des fonctionnalités d'intelligence artificielle.
- Analyse et génération de retours sur les performances.

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

Copier la clé générée dans le fichier `.env`, à la place de la valeur d'exemple :

```env
DJANGO_SECRET_KEY=ta_cle_secrete_generee
```

Appliquer les migrations et lancer le serveur :

```powershell
python manage.py migrate
python manage.py runserver
```

Le backend sera disponible à l'adresse : http://127.0.0.1:8000/

### 2. Frontend

Depuis le dossier `frontend` :

```powershell
npm install
npm run dev
```

Le frontend sera disponible à l'adresse : http://localhost:5173/

### 3. Redis (facultatif pour le démarrage de base)

Si tu souhaites lancer Redis avec Docker, exécute la commande depuis le dossier `backend`, où se trouve le fichier `docker-compose.yml` :

```powershell
docker compose up -d
```

## État du projet

Cast IA est actuellement au stade de prototype en développement.

Le backend dispose d'une première base fonctionnelle pour la gestion des profils et des scénarios. L'interface React et les fonctionnalités avancées de gestion et d'analyse des auditions restent à développer.

## Auteur

Projet académique et technique — Cast IA.
