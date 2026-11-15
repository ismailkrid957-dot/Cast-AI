
# Spider Casting

**Plateforme intelligente de gestion et d'évaluation des auditions.**

## Présentation

Spider Casting est un projet visant à simplifier le processus de casting grâce à une plateforme web permettant aux directeurs de casting de publier des scénarios et aux candidats de participer aux auditions.

Le projet prévoit également l'intégration de méthodes d'intelligence artificielle pour assister l'analyse des performances des candidats.

## Technologies

### Backend
- Python
- Django 5.2
- Django REST Framework
- SQLite
- Redis (configuration pour les traitements asynchrones)

### Frontend
- React 19
- Vite
- JavaScript
- Axios
- React Router

## Architecture

```text
spider-casting/
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

- Interface utilisateur React.
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

Copier la clé générée dans `backend/.env`, à la place de la valeur d'exemple :

```env
DJANGO_SECRET_KEY=ta_cle_secrete_generee
```

Appliquer les migrations :

```powershell
python manage.py migrate
```

Lancer le serveur :

```powershell
python manage.py runserver
```

Le backend sera disponible sur :

http://127.0.0.1:8000/


### 2. Frontend

Depuis le dossier `frontend` :

```bash
npm install
npm run dev
```

Le frontend sera disponible sur :

http://localhost:5173/

### 3. Redis

Pour lancer Redis avec Docker :

```bash
docker compose up -d
```

## État du projet

Spider Casting est actuellement au stade de prototype en développement.

Les fonctionnalités backend de gestion des profils et des scénarios constituent la première base fonctionnelle. L'interface React et les fonctionnalités avancées d'analyse des auditions restent à développer.

## Auteur

Projet académique et technique — Spider Casting.
