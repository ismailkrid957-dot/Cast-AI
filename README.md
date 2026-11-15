<div align="center">
  <img src="docs/assets/banner.svg" alt="Cast AI — Présélection artistique multimodale, objective et explicable" width="100%" />

  <p>
    <strong>Plateforme de casting multimodal propulsée par une IA éthique, transparente et explicable.</strong><br />
    <em>Prototype officiel — Hackathon IA Éthique 360 (JEI INSAT × OIF • Mandat 2026/2027)</em>
  </p>

  <p>
    <a href="#-architecture--pipeline-multimodal">Architecture</a> •
    <a href="#-éthique-xai--radar-dévaluation">Éthique &amp; XAI</a> •
    <a href="#-stack-technique">Stack</a> •
    <a href="#-démarrage-rapide">Démarrage rapide</a> •
    <a href="LICENSE">Licence MIT</a>
  </p>
</div>

---

## 🎯 Pourquoi Cast AI ?

La présélection manuelle de centaines d'auditions vidéo expose les jurys à la fatigue décisionnelle et aux biais inconscients, tout en laissant les candidats sans retour objectif.

**Cast AI** assiste les directeurs de casting en analysant de manière asynchrone les performances vidéo et vocales afin d'établir un **Top 15 argumenté par rôle**. L'algorithme ne remplace jamais le regard artistique : chaque score est décomposé visuellement pour éclairer la **validation finale par un jury humain**.

---

## ⚙️ Architecture & Pipeline Multimodal

<div align="center">
  <img src="docs/assets/pipeline-flow.svg" alt="Pipeline de traitement asynchrone Cast AI : Capture, File Async, Extraction IA et Décision XAI" width="100%" />
</div>

1. **Capture & Dépôt (`frontend/` → `backend/`) :** Le candidat soumet son audition vidéo pour un rôle précis via l'interface React reliée à l'API Django REST Framework.
2. **Traitement Asynchrone (`Redis` + `Celery`) :** Chaque vidéo est placée en file d'attente afin de découpler l'ingestion web des calculs lourds d'extraction multimodale.
3. **Extraction Multimodale :**
   * **Expressivité faciale (`DeepFace`) :** Cohérence émotionnelle et dynamique des expressions au fil de la scène.
   * **Posture & Langage corporel (`MediaPipe`) :** Présence scénique, ancrage et gestuelle.
   * **Prosodie & Diction (`Librosa`) :** Rythme, intonation, clarté vocale et variations d'énergie.
4. **Aide à la Décision (`Top 15` & `XAI`) :** Génération d'un classement transparent par rôle accompagné d'un profil radar explicable soumis au jury.

---

## 🛡️ Éthique, XAI & Radar d'Évaluation

<div align="center">
  <img src="docs/assets/cast-ai-radar.svg" alt="Radar d'évaluation explicable à 6 axes et principes IA Éthique 360" width="100%" />
</div>

Conçu selon les principes du **Hackathon IA Éthique 360 (JEI INSAT × OIF)**, le moteur d'évaluation repose sur trois garanties :

* **Neutralisation des biais démographiques :** Les métriques portent exclusivement sur des signaux artistiques et techniques (prosodie, posture, expressivité, diction, adéquation au rôle), sans attributs d'âge, de genre ou d'origine.
* **Explicabilité native (XAI) :** Aucun score « boîte noire » — le jury visualise la contribution exacte de chacun des **6 axes du radar** pour chaque profil du Top 15.
* **Supervision humaine (*Human-in-the-Loop*) :** Cast AI filtre et structure la présélection ; le jury conserve le contrôle total sur les ajustements et la sélection finale.

---

## 🛠️ Stack Technique

| Couche | Technologies | Rôle |
| :--- | :--- | :--- |
| **Backend & API** | Python, Django 5.2, Django REST Framework | Gestion des rôles, auditions, authentification et endpoints REST |
| **Asynchrone** | Celery, Redis | Exécution en arrière-plan des pipelines vidéo et audio |
| **IA Multimodale** | MediaPipe, DeepFace, Librosa | Extraction des repères posturaux, émotionnels et acoustiques |
| **Frontend** | React 19, Vite | Espace candidat et tableau de bord jury (Top 15 & graphiques XAI) |
| **Base de données** | SQLite | Persistance légère pour le prototypage rapide |

---

## 📁 Structure du dépôt

```text
spider-el-3ankabout/
├── backend/          # API Django 5.2, modèles, tâches Celery et analyseurs IA
├── frontend/         # Application React 19 + Vite (interfaces Candidat & Jury)
├── docs/
│   └── assets/       # Bannières et schémas SVG locaux (banner, pipeline-flow, cast-ai-radar)
├── LICENSE           # Licence MIT
└── README.md

🚀 Démarrage rapide
git clone [https://github.com/ismailkrid957-dot/spider-el-3ankabout.git](https://github.com/ismailkrid957-dot/spider-el-3ankabout.git)
cd spider-el-3ankabout

Lancer le Backend & le Worker Celery:
cd backend
python -m venv .venv
source .venv/bin/activate        # Sur Windows : .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


Démarrez le worker Celery:
cd backend
celery -A config worker -l info

Lancer le Frontend:
cd frontend
npm install
npm run dev

📄 Licence:
### Vérification rapide pour que les 3 SVG s'affichent sans erreur

Avant de valider le commit de `README.md` sur `main` :
1. **Assurez-vous que `banner.svg`, `cast-ai-radar.svg` et `pipeline-flow.svg` sont bien tous les trois sur `main` dans `docs/assets/`**[cite: 3].
2. **Vérifiez l'absence de `&` isolé dans `cast-ai-radar.svg` et `pipeline-flow.svg` :** si vous avez copié d'anciennes versions contenant `Équité & Auditabilité`, `Broker & Workers` ou `Top 15 & Radar`, remplacez `&` par `&amp;` (ou `+`) — sinon le proxy d'images de GitHub bloquera leur affichage dans le README.
