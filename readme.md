# 📁 Gestion doc des clients avec Flask et MySQL

## 📝 Description du projet

Ce projet est une application web développée avec **Flask (Python)** permettant de gérer des **clients**, des **documents** associés à ces clients, ainsi que des **utilisateurs internes**. Il vise à fournir une solution simple, claire et efficace pour organiser et centraliser tous les documents liés aux relations clients d'une entreprise.

## 🧾 Objectifs

- Permettre la création, modification et suppression de clients, documents et utilisateurs.
- Stocker tous les éléments dans une base de données MySQL relationnelle.
- Offrir une interface web ergonomique avec HTML, Bootstrap et Jinja2.
- Faciliter la navigation, l'accès et la gestion des données.

## 🗃️ Structure de la base de données

- `t_client` : stocke les données personnelles des clients (nom, prénom, entreprise, email, téléphone, commentaire).
- `t_docclients` : documents associés à des clients (titre, contenu, date).
- `t_utilisateur` : collaborateurs internes gérant les documents ou les clients.

## 📂 Fonctionnalités

- Affichage et recherche des clients.
- Ajout, édition, suppression de clients.
- Ajout, visualisation, modification, suppression de documents.
- Gestion des utilisateurs.
- Interface responsive (Bootstrap 5).

## 🛠️ Technologies utilisées

| Technologie | Usage |
|-------------|-------|
| Python / Flask | Application web, logique métier |
| MySQL | Base de données relationnelle |
| HTML / CSS / Bootstrap | Front-end et mise en page |
| Jinja2 | Moteur de templates |
| JavaScript | Interactivité de la page |
| HeidiSQL | Gestionnaire de base de données MySQL |

## 🚀 Lancement de l'application

1. Cloner le projet
2. Configurer votre environnement Python (Flask, pymysql...)
3. Importer le fichier SQL dans MySQL
4. Lancer `app.py`
5. Ouvrir le navigateur à `http://127.0.0.1:5000`

## 🎯 Améliorations futures

- Association des documents aux clients et utilisateurs via des clés étrangères.
- Ajout de l’authentification des utilisateurs avec rôles.
- Téléversement de fichiers PDF/docx.
- Tableau de bord statistiques.
- Déploiement en ligne.

## 👥 Public cible

- PME, indépendants, associations, cabinets de conseil ou de transport.
- Toute structure souhaitant organiser ses documents clients facilement.

---

Développé par **Erick Cojan** – Informaticien en infrastructure.
