# 🐍 Backend Django — Guide d’installation et de démarrage

## ⚙️ 1. Création et activation de l’environnement virtuel

```bash
python -m venv env
```

Crée un **environnement virtuel** Python afin d’isoler les dépendances du projet.  
Cela évite les conflits entre les paquets utilisés par différents projets.

Activation de l’environnement virtuel :

- **Linux / macOS :**
  ```bash
  source env/bin/activate
  ```
- **Windows :**
  ```bash
  env\Scripts\activate
  ```

---

## 📦 2. Installation des dépendances principales

```bash
pip install django djangorestframework
pip install django-cors-headers
```

- `django` : framework principal pour le développement web.
- `djangorestframework` : extension pour créer facilement des **API REST**.
- `django-cors-headers` : permet d’autoriser les appels depuis d’autres domaines (ex : autoriser une application **React** à communiquer avec notre backend Django).

---

## 🚀 3. Initialisation du projet

```bash
django-admin startproject backend .
```

Crée un nouveau projet Django nommé **backend**.  
Ce dossier contient les fichiers de configuration principaux du projet.

---

## 🧩 4. Création d’une application

Django est un framework modulaire : un projet peut contenir plusieurs **applications** (par exemple : `authentification`, `commande`, `produits`, etc.).

Créons une première application nommée **api** :

```bash
django-admin startapp api
```

---

## ⚙️ 5. Configuration du projet (`settings.py`)

Le fichier `backend/settings.py` contient la configuration globale du projet.

1. **Déclarer l’application crée :**

   ```python
   INSTALLED_APPS = [
       ...,
       'rest_framework',
       'corsheaders',
       'api.apps.ApiConfig',
   ]
   ```

2. **Base de données :**
   Par défaut, Django utilise **SQLite3**, une base locale adaptée au développement.
   Vous pouvez la modifier plus tard pour utiliser PostgreSQL, MySQL, etc.

3. **CORS (Cross-Origin Resource Sharing) :**
   Ajouter les paramètres nécessaires pour autoriser les appels depuis le frontend :

   ```python
   MIDDLEWARE = [
       'corsheaders.middleware.CorsMiddleware',
       ...,
   ]

   CORS_ALLOW_ALL_ORIGINS = True  # à restreindre en production
   ```

---

## 🌐 6. Gestion des routes (`urls.py`)

Le fichier `backend/urls.py` gère les **routes principales** du projet.

Exemple de base :

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # accès à l’interface d’administration
    path('api/', include('api.urls')),  # inclusion des routes de l’application "api"
]
```

Créer également un fichier `urls.py` dans le dossier `api` pour y définir les routes propres à l’application.

---

## 🧠 7. Structure de l’application

Chaque fichier a un rôle spécifique :

- `models.py` : définition des **modèles de données** (ex : `Transaction`, `User`, etc.)
- `views.py` : logique métier (ce que fait l’API : création, suppression, filtrage…)
- `serializers.py` : conversion des objets Python ⇄ JSON
- `admin.py` : enregistrement des modèles pour qu’ils soient visibles dans l’interface admin
- `tests.py` : tests unitaires

---

## 🗃️ 8. Migrations de la base de données

Après avoir défini vos modèles :

```bash
python manage.py makemigrations
python manage.py migrate
```

- `makemigrations` : crée les fichiers de migration décrivant les changements à appliquer.
- `migrate` : applique ces changements à la base de données (création des tables, etc.).

---

## 🧩 9. Sérialisation

Créer un fichier `serializers.py` dans l’application `api` :

Ce fichier sert à **sérialiser** les objets Python (modèles) en JSON, afin qu’ils puissent être transmis via l’API.

---

## ▶️ 10. Lancer le serveur

```bash
python manage.py runserver
```

Le serveur de développement démarre sur [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## 💡 11. Astuce : différence entre PUT et PATCH

| Méthode   | Description                                                                        |
| --------- | ---------------------------------------------------------------------------------- |
| **PUT**   | Met à jour **l’ensemble** d’un objet. Toutes les propriétés doivent être fournies. |
| **PATCH** | Met à jour **partiellement** un objet (une seule propriété, par exemple).          |
