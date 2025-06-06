"""Gestion des "routes" FLASK et des données pour les genres.
Fichier : gestion_genres_crud.py
Auteur : OM 2021.03.16
"""
from pathlib import Path

from flask import redirect
from flask import request
from flask import session
from flask import url_for

from APP_FILMS_164 import app
from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *
from APP_FILMS_164.genres.gestion_genres_wtf_forms import FormWTFAjouterGenres
from APP_FILMS_164.genres.gestion_genres_wtf_forms import FormWTFDeleteGenre
from APP_FILMS_164.genres.gestion_genres_wtf_forms import FormWTFUpdateGenre

"""
    Auteur : OM 2021.03.16
    Définition d'une "route" /genres_afficher
    
    Test : ex : http://127.0.0.1:5575/genres_afficher
    
    Paramètres : order_by : ASC : Ascendant, DESC : Descendant
                id_genre_sel = 0 >> tous les genres.
                id_genre_sel = "n" affiche le genre dont l'id est "n"
"""


@app.route("/genres_afficher/<string:order_by>/<int:id_genre_sel>", methods=['GET', 'POST'])
def genres_afficher(order_by, id_genre_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_genre_sel == 0:
                    strsql_genres_afficher = """SELECT * FROM t_docclients ORDER BY id_doc ASC"""
                    mc_afficher.execute(strsql_genres_afficher)
                elif order_by == "ASC":
                    # C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
                    # la commande MySql classique est "SELECT * FROM t_genre"
                    # Pour "lever"(raise) une erreur s'il y a des erreurs sur les noms d'attributs dans la table
                    # donc, je précise les champs à afficher
                    # Constitution d'un dictionnaire pour associer l'id du genre sélectionné avec un nom de variable
                    valeur_id_genre_selected_dictionnaire = {"value_id_genre_selected": id_genre_sel}
                    strsql_genres_afficher = """SELECT * FROM t_docclients WHERE id_doc = %(value_id_genre_selected)s"""

                    mc_afficher.execute(strsql_genres_afficher, valeur_id_genre_selected_dictionnaire)
                else:
                    strsql_genres_afficher = """SELECT * FROM t_docclients ORDER BY id_doc DESC"""

                    mc_afficher.execute(strsql_genres_afficher)

                data_genres = mc_afficher.fetchall()

                print("data_genres ", data_genres, " Type : ", type(data_genres))

                # Différencier les messages si la table est vide.
                if not data_genres and id_genre_sel == 0:
                    flash("""La table "t_genre" est vide. !!""", "warning")
                elif not data_genres and id_genre_sel > 0:
                    # Si l'utilisateur change l'id_genre dans l'URL et que le genre n'existe pas,
                    flash(f"Le genre demandé n'existe pas !!", "warning")
                else:
                    # Dans tous les autres cas, c'est que la table "t_genre" est vide.
                    # OM 2020.04.09 La ligne ci-dessous permet de donner un sentiment rassurant aux utilisateurs.
                    flash(f"Données genres affichés !!", "success")

        except Exception as Exception_genres_afficher:
            raise ExceptionGenresAfficher(f"fichier : {Path(__file__).name}  ;  "
                                          f"{genres_afficher.__name__} ; "
                                          f"{Exception_genres_afficher}")

    # Envoie la page "HTML" au serveur.
    return render_template("genres/genres_afficher.html", data=data_genres)


"""
    Auteur : OM 2021.03.22
    Définition d'une "route" /genres_ajouter
    
    Test : ex : http://127.0.0.1:5575/genres_ajouter
    
    Paramètres : sans
    
    But : Ajouter un genre pour un film
    
    Remarque :  Dans le champ "name_genre_html" du formulaire "genres/genres_ajouter.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/genres_ajouter", methods=['GET', 'POST'])
def genres_ajouter_wtf():
    form = FormWTFAjouterGenres()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                name_genre_wtf = form.nom_genre_wtf.data
                name_genre = name_genre_wtf.lower()
                valeurs_insertion_dictionnaire = {"value_intitule_genre": name_genre}
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_genre = """INSERT INTO t_docclients (id_doc,titre) VALUES (NULL,%(value_intitule_genre)s) """
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_genre, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                # Pour afficher et constater l'insertion de la valeur, on affiche en ordre inverse. (DESC)
                return redirect(url_for('genres_afficher', order_by='DESC', id_genre_sel=0))

        except Exception as Exception_genres_ajouter_wtf:
            raise ExceptionGenresAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                            f"{genres_ajouter_wtf.__name__} ; "
                                            f"{Exception_genres_ajouter_wtf}")

    return render_template("genres/genres_ajouter_wtf.html", form=form)


"""
    Auteur : OM 2021.03.29
    Définition d'une "route" /genre_update
    
    Test : ex cliquer sur le menu "genres" puis cliquer sur le bouton "EDIT" d'un "genre"
    
    Paramètres : sans
    
    But : Editer(update) un genre qui a été sélectionné dans le formulaire "genres_afficher.html"
    
    Remarque :  Dans le champ "nom_genre_update_wtf" du formulaire "genres/genre_update_wtf.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/genre_update", methods=['GET', 'POST'])
def genre_update_wtf():
    try:
        try:
            id_doc_update = int(request.values['id_genre_btn_edit_html'])
        except (ValueError, KeyError):
            flash("Identifiant invalide ou manquant.", "danger")
            return redirect(url_for("genres_afficher", order_by="ASC", id_genre_sel=0))

        form_update = FormWTFUpdateGenre()

        if request.method == "POST" and form_update.submit.data and form_update.validate():
            titre_update = form_update.titre.data
            contenu_update = form_update.contenu.data
            date_ajout_update = form_update.date_ajout.data

            valeur_update_dictionnaire = {
                "value_id_doc": id_doc_update,
                "value_titre": titre_update,
                "value_contenu": contenu_update,
                "value_date_ajout": date_ajout_update
            }

            str_sql_update_docclient = """
                UPDATE t_docclients 
                SET titre = %(value_titre)s, 
                    contenu = %(value_contenu)s,
                    date_ajout = %(value_date_ajout)s
                WHERE id_doc = %(value_id_doc)s
            """

            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_docclient, valeur_update_dictionnaire)

            flash("Document mis à jour !", "success")
            return redirect(url_for('genres_afficher', order_by="ASC", id_genre_sel=id_doc_update))

        elif request.method == "GET":
            str_sql_select_docclient = """
                SELECT id_doc, titre, contenu, date_ajout 
                FROM t_docclients 
                WHERE id_doc = %(value_id_doc)s
            """
            valeur_select_dictionnaire = {"value_id_doc": id_doc_update}

            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_select_docclient, valeur_select_dictionnaire)
                data_docclient = mybd_conn.fetchone()

            if data_docclient is None:
                flash("Aucun document trouvé avec cet identifiant.", "warning")
                return redirect(url_for("genres_afficher", order_by="ASC", id_genre_sel=0))

            form_update.titre.data = data_docclient["titre"]
            form_update.contenu.data = data_docclient["contenu"]
            form_update.date_ajout.data = data_docclient["date_ajout"]

    except Exception as e:
        raise ExceptionGenreUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{genre_update_wtf.__name__} ; "
                                      f"{e}")

    return render_template("genres/genre_update_wtf.html", form_update=form_update)



"""
    Auteur : OM 2021.04.08
    Définition d'une "route" /genre_delete
    
    Test : ex. cliquer sur le menu "genres" puis cliquer sur le bouton "DELETE" d'un "genre"
    
    Paramètres : sans
    
    But : Effacer(delete) un genre qui a été sélectionné dans le formulaire "genres_afficher.html"
    
    Remarque :  Dans le champ "nom_genre_delete_wtf" du formulaire "genres/genre_delete_wtf.html",
                le contrôle de la saisie est désactivée. On doit simplement cliquer sur "DELETE"
"""


@app.route("/genre_delete", methods=['GET', 'POST'])
def genre_delete_wtf():
    data_docclient_delete = None
    btn_submit_del = None

    try:
        # Récupération sécurisée de l'ID du document
        id_doc_delete = int(request.values.get('id_genre_btn_delete_html', 0))

        form_delete = FormWTFDeleteGenre()
        print("on submit", form_delete.validate_on_submit())

        if request.method == "POST" and form_delete.validate_on_submit():

            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("genres_afficher", order_by="ASC", id_genre_sel=0))

            elif form_delete.submit_btn_conf_del.data:
                data_docclient_delete = session.get('data_docclient_delete')
                print("data_docclient_delete :", data_docclient_delete)

                flash("Effacer le document de façon définitive de la BD !!!", "danger")
                btn_submit_del = True

            elif form_delete.submit_btn_del.data:
                valeur_delete_dictionnaire = {"value_id_doc": id_doc_delete}
                print("valeur_delete_dictionnaire", valeur_delete_dictionnaire)

                str_sql_delete_docclient = """
                    DELETE FROM t_docclients 
                    WHERE id_doc = %(value_id_doc)s
                """
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_docclient, valeur_delete_dictionnaire)

                flash("Document définitivement effacé !!", "success")
                print("Document définitivement effacé !!")

                return redirect(url_for("genres_afficher", order_by="ASC", id_genre_sel=0))

        elif request.method == "GET":
            valeur_select_dictionnaire = {"value_id_doc": id_doc_delete}
            print("ID document (GET):", id_doc_delete, type(id_doc_delete))

            str_sql_select_docclient = """
                SELECT id_doc, titre
                FROM t_docclients
                WHERE id_doc = %(value_id_doc)s
            """

            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_select_docclient, valeur_select_dictionnaire)
                data_docclient_delete = mydb_conn.fetchall()
                print("data_docclient_delete...", data_docclient_delete)

                session['data_docclient_delete'] = data_docclient_delete

                if data_docclient_delete:
                    data_doc = data_docclient_delete[0]
                    print("data_doc", data_doc)
                    form_delete.nom_genre_delete_wtf.data = data_doc["titre"]
                else:
                    flash("Document non trouvé. Impossible de le supprimer.", "warning")
                    return redirect(url_for("genres_afficher", order_by="ASC", id_genre_sel=0))

            btn_submit_del = False

    except ValueError:
        flash("ID document invalide.", "danger")
        return redirect(url_for("genres_afficher", order_by="ASC", id_genre_sel=0))
    except Exception as Exception_genre_delete_wtf:
        raise ExceptionGenreDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{genre_delete_wtf.__name__} ; "
                                      f"{Exception_genre_delete_wtf}")

    return render_template("genres/genre_delete_wtf.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del,
                           data_films_associes=data_docclient_delete)
