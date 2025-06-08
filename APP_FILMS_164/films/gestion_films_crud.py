"""Gestion des "routes" FLASK et des données pour les films.
Fichier : gestion_films_crud.py
Auteur : OM 2022.04.11
"""
from pathlib import Path

from flask import redirect
from flask import request
from flask import session
from flask import url_for

from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *
from APP_FILMS_164.films.gestion_films_wtf_forms import FormWTFUpdateFilm, FormWTFAddFilm, FormWTFDeleteFilm

"""Ajouter un film grâce au formulaire "film_add_wtf.html"
Auteur : OM 2022.04.11
Définition d'une "route" /film_add

Test : exemple: cliquer sur le menu "Films/Genres" puis cliquer sur le bouton "ADD" d'un "film"

Paramètres : sans


Remarque :  Dans le champ "nom_film_update_wtf" du formulaire "films/films_update_wtf.html",
            le contrôle de la saisie s'effectue ici en Python dans le fichier ""
            On ne doit pas accepter un champ vide.
"""


@app.route("/film_add", methods=['GET', 'POST'])
def film_add_wtf():
    # Objet formulaire pour AJOUTER un client
    form_add_film = FormWTFAddFilm()
    if request.method == "POST":
        try:
            if form_add_film.validate_on_submit():
                # Récupérer les valeurs du formulaire avec les bons noms de champs
                nom_utilisateur = form_add_film.nom_client_add_wtf.data
                prenom_utilisateur = form_add_film.prenom_client_add_wtf.data
                email_utilisateur = form_add_film.email_client_add_wtf.data
                entreprise_utilisateur = form_add_film.entreprise_client_add_wtf.data
                telephone_utilisateur = form_add_film.telephone_client_add_wtf.data

                valeurs_insertion_dictionnaire = {
                    "nom": nom_utilisateur,
                    "prenom": prenom_utilisateur,
                    "email": email_utilisateur,
                    "entreprise": entreprise_utilisateur,
                    "telephone": telephone_utilisateur
                }
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                # Requête SQL pour insérer dans la table t_client
                strsql_insert_utilisateur = """
                    INSERT INTO t_client (nom, prenom, email, entreprise, telephone)
                    VALUES (%(nom)s, %(prenom)s, %(email)s, %(entreprise)s, %(telephone)s)
                """
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_utilisateur, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                # Rediriger vers la page d'affichage (adapte si besoin)
                return redirect(url_for('films_genres_afficher', id_film_sel=0))

        except Exception as Exception_genres_ajouter_wtf:
            raise ExceptionGenresAjouterWtf(
                f"fichier : {Path(__file__).name}  ;  "
                f"{film_add_wtf.__name__} ; "
                f"{Exception_genres_ajouter_wtf}"
            )

    return render_template("films/film_add_wtf.html", form_add_film=form_add_film)





"""Editer(update) un film qui a été sélectionné dans le formulaire "films_genres_afficher.html"
Auteur : OM 2022.04.11
Définition d'une "route" /film_update

Test : exemple: cliquer sur le menu "Films/Genres" puis cliquer sur le bouton "EDIT" d'un "film"

Paramètres : sans

But : Editer(update) un genre qui a été sélectionné dans le formulaire "genres_afficher.html"

Remarque :  Dans le champ "nom_film_update_wtf" du formulaire "films/films_update_wtf.html",
            le contrôle de la saisie s'effectue ici en Python.
            On ne doit pas accepter un champ vide.
"""


@app.route("/film_update", methods=['GET', 'POST'])
def film_update_wtf():
    # Récupérer l'id client à modifier (anciennement id_film_btn_edit_html)
    id_client_update = request.values['id_film_btn_edit_html']

    # Formulaire pour la mise à jour (FormWTFUpdateFilm doit contenir les bons champs)
    form_update_client = FormWTFUpdateFilm()  # Renommer si tu veux, ici on garde le même nom

    try:
        if request.method == "POST" and form_update_client.submit.data:
            # Récupérer les champs modifiables
            nom_update = form_update_client.nom_client_update_wtf.data
            prenom_update = form_update_client.prenom_client_update_wtf.data
            email_update = form_update_client.email_client_update_wtf.data
            entreprise_update = form_update_client.entreprise_client_update_wtf.data
            telephone_update = form_update_client.telephone_client_update_wtf.data

            valeur_update_dictionnaire = {
                "value_id_client": id_client_update,
                "value_nom": nom_update,
                "value_prenom": prenom_update,
                "value_email": email_update,
                "value_entreprise": entreprise_update,
                "value_telephone": telephone_update
            }

            str_sql_update_client = """
                UPDATE t_client
                SET nom = %(value_nom)s,
                    prenom = %(value_prenom)s,
                    email = %(value_email)s,
                    entreprise = %(value_entreprise)s,
                    telephone = %(value_telephone)s
                WHERE id_client = %(value_id_client)s
            """

            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_client, valeur_update_dictionnaire)

            flash("Client mis à jour !!", "success")

            # Rediriger vers la page d'affichage après mise à jour
            return redirect(url_for('films_genres_afficher', id_film_sel=id_client_update))

        elif request.method == "GET":
            # Récupérer les données client pour préremplir le formulaire
            str_sql_id_client = "SELECT * FROM t_client WHERE id_client = %(value_id_client)s"
            valeur_select_dictionnaire = {"value_id_client": id_client_update}

            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_client, valeur_select_dictionnaire)
                data_client = mybd_conn.fetchone()

            form_update_client.nom_client_update_wtf.data = data_client["nom"]
            form_update_client.prenom_client_update_wtf.data = data_client["prenom"]
            form_update_client.email_client_update_wtf.data = data_client["email"]
            form_update_client.entreprise_client_update_wtf.data = data_client["entreprise"]
            form_update_client.telephone_client_update_wtf.data = data_client["telephone"]

    except Exception as e:
        raise ExceptionFilmUpdateWtf(
            f"fichier : {Path(__file__).name}  ;  "
            f"{film_update_wtf.__name__} ; "
            f"{e}"
        )

    return render_template("films/film_update_wtf.html", form_update_film=form_update_client)



"""Effacer(delete) un film qui a été sélectionné dans le formulaire "films_genres_afficher.html"
Auteur : OM 2022.04.11
Définition d'une "route" /film_delete
    
Test : ex. cliquer sur le menu "film" puis cliquer sur le bouton "DELETE" d'un "film"
    
Paramètres : sans

Remarque :  Dans le champ "nom_film_delete_wtf" du formulaire "films/film_delete_wtf.html"
            On doit simplement cliquer sur "DELETE"
"""


@app.route("/film_delete", methods=['GET', 'POST'])
def film_delete_wtf():
    data_film_delete = None
    btn_submit_del = None
    id_film_delete = request.values['id_film_btn_delete_html']

    form_delete_film = FormWTFDeleteFilm()
    try:
        if form_delete_film.submit_btn_annuler.data:
            return redirect(url_for("films_genres_afficher", id_film_sel=0))

        if form_delete_film.submit_btn_conf_del_film.data:
            data_film_delete = session['data_film_delete']
            flash(f"Effacer le client de façon définitive de la BD !!!", "danger")
            btn_submit_del = True

        if form_delete_film.submit_btn_del_film.data:
            valeur_delete_dictionnaire = {"value_id_film": id_film_delete}

            # Suppression dans la table t_client
            str_sql_delete_client = """DELETE FROM t_client WHERE id_client = %(value_id_film)s"""

            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_delete_client, valeur_delete_dictionnaire)

            flash(f"Client définitivement effacé !!", "success")
            return redirect(url_for('films_genres_afficher', id_film_sel=0))

        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_film": id_film_delete}

            str_sql_select_client = """SELECT * FROM t_client WHERE id_client = %(value_id_film)s"""

            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_select_client, valeur_select_dictionnaire)
                data_film_delete = mydb_conn.fetchall()
                session['data_film_delete'] = data_film_delete

            btn_submit_del = False

    except Exception as Exception_film_delete_wtf:
        raise ExceptionFilmDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                     f"{film_delete_wtf.__name__} ; "
                                     f"{Exception_film_delete_wtf}")

    return render_template("films/film_delete_wtf.html",
                           form_delete_film=form_delete_film,
                           btn_submit_del=btn_submit_del,
                           data_film_del=data_film_delete)

