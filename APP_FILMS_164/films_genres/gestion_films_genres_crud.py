"""
    Fichier : gestion_films_genres_crud.py
    Auteur : OM 2021.05.01
    Gestions des "routes" FLASK et des données pour l'association entre les films et les genres.
"""
from pathlib import Path

from flask import redirect
from flask import request
from flask import session
from flask import url_for

from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *

"""
    Nom : films_genres_afficher
    Auteur : OM 2021.05.01
    Définition d'une "route" /films_genres_afficher
    
    But : Afficher les films avec les genres associés pour chaque film.
    
    Paramètres : id_genre_sel = 0 >> tous les films.
                 id_genre_sel = "n" affiche le film dont l'id est "n"
                 
"""


@app.route("/films_genres_afficher/<int:id_film_sel>", methods=['GET', 'POST'])
def films_genres_afficher(id_film_sel):
    print(" films_genres_afficher id_film_sel ", id_film_sel)
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                # Requête adaptée pour afficher les utilisateurs au lieu des films
                strsql_genres_films_afficher_data = """SELECT id_client, nom, prenom, email, entreprise, telephone
                                                       FROM t_client"""
                if id_film_sel == 0:
                    mc_afficher.execute(strsql_genres_films_afficher_data)
                else:
                    valeur_id_utilisateur_selected_dictionnaire = {"value_id_film_selected": id_film_sel}
                    strsql_genres_films_afficher_data += " WHERE id_client = %(value_id_film_selected)s"
                    mc_afficher.execute(strsql_genres_films_afficher_data, valeur_id_utilisateur_selected_dictionnaire)

                data_genres_films_afficher = mc_afficher.fetchall()
                print("data_genres ", data_genres_films_afficher, " Type : ", type(data_genres_films_afficher))

                if not data_genres_films_afficher and id_film_sel == 0:
                    flash("""La table "t_client" est vide. !""", "warning")
                elif not data_genres_films_afficher and id_film_sel > 0:
                    flash(f"Le client {id_film_sel} demandé n'existe pas !!", "warning")


        except Exception as Exception_films_genres_afficher:
            raise Exception(f"fichier : {Path(__file__).name}  ;  {films_genres_afficher.__name__} ;"
                            f"{Exception_films_genres_afficher}")

    print("films_genres_afficher  ", data_genres_films_afficher)
    return render_template("films_genres/films_genres_afficher.html", data=data_genres_films_afficher)



"""
    nom: edit_genre_film_selected
    On obtient un objet "objet_dumpbd"

    Récupère la liste de tous les genres du film sélectionné par le bouton "MODIFIER" de "films_genres_afficher.html"
    
    Dans une liste déroulante particulière (tags-selector-tagselect), on voit :
    1) Tous les genres contenus dans la "t_genre".
    2) Les genres attribués au film selectionné.
    3) Les genres non-attribués au film sélectionné.

    On signale les erreurs importantes

"""


@app.route("/edit_genre_film_selected", methods=['GET', 'POST'])
def edit_genre_film_selected():
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                # Récupère tous les utilisateurs
                strsql_utilisateurs_afficher = """SELECT id_utilisateur, nom FROM t_utilisateur ORDER BY id_utilisateur ASC"""
                mc_afficher.execute(strsql_utilisateurs_afficher)
                data_utilisateurs_all = mc_afficher.fetchall()
                print("Tous les utilisateurs :", data_utilisateurs_all)

            # Récupère l'ID du client sélectionné depuis le bouton "Modifier"
            id_client_edit = request.values['id_film_genres_edit_html']
            session['session_id_client_edit'] = id_client_edit

            dict_id_client = {"value_id_film_selected": id_client_edit}

            # Récupère les infos du client et les utilisateurs associés/non associés
            data_client, data_utilisateurs_non_attribues, data_utilisateurs_attribues = \
                genres_films_afficher_data(dict_id_client)

            # Enregistre dans la session les ID utilisateurs attribués et non attribués
            session['session_lst_utilisateurs_non_attribues'] = [item['id_utilisateur'] for item in data_utilisateurs_non_attribues]
            session['session_lst_utilisateurs_attribues'] = [item['id_utilisateur'] for item in data_utilisateurs_attribues]

            print("Client sélectionné :", data_client)
            print("Utilisateurs non attribués :", data_utilisateurs_non_attribues)
            print("Utilisateurs attribués :", data_utilisateurs_attribues)

        except Exception as e:
            raise ExceptionEditGenreFilmSelected(
                f"fichier : {Path(__file__).name} ; fonction : {edit_genre_film_selected.__name__} ; erreur : {e}"
            )

        return render_template("films_genres/films_genres_modifier_tags_dropbox.html",
                               data_genres=data_utilisateurs_all,
                               data_film_selected=data_client,
                               data_genres_attribues=data_utilisateurs_attribues,
                               data_genres_non_attribues=data_utilisateurs_non_attribues)




"""
    nom: update_genre_film_selected

    Récupère la liste de tous les genres du film sélectionné par le bouton "MODIFIER" de "films_genres_afficher.html"
    
    Dans une liste déroulante particulière (tags-selector-tagselect), on voit :
    1) Tous les genres contenus dans la "t_genre".
    2) Les genres attribués au film selectionné.
    3) Les genres non-attribués au film sélectionné.

    On signale les erreurs importantes
"""


@app.route("/update_genre_film_selected", methods=['GET', 'POST'])
def update_genre_film_selected():
    if request.method == "POST":
        try:
            # Récupère l'id du film sélectionné
            id_film_selected = session['session_id_film_genres_edit']
            print("session['session_id_film_genres_edit'] ", session['session_id_film_genres_edit'])

            # Récupère la liste des genres qui ne sont pas associés au film sélectionné.
            old_lst_data_genres_films_non_attribues = session['session_lst_data_genres_films_non_attribues']
            print("old_lst_data_genres_films_non_attribues ", old_lst_data_genres_films_non_attribues)

            # Récupère la liste des genres qui sont associés au film sélectionné.
            old_lst_data_genres_films_attribues = session['session_lst_data_genres_films_old_attribues']
            print("old_lst_data_genres_films_old_attribues ", old_lst_data_genres_films_attribues)

            # Effacer toutes les variables de session.
            session.clear()

            # Récupère ce que l'utilisateur veut modifier comme genres dans le composant "tags-selector-tagselect"
            # dans le fichier "genres_films_modifier_tags_dropbox.html"
            new_lst_str_genres_films = request.form.getlist('name_select_tags')
            print("new_lst_str_genres_films ", new_lst_str_genres_films)

            # OM 2021.05.02 Exemple : Dans "name_select_tags" il y a ['4','65','2']
            # On transforme en une liste de valeurs numériques. [4,65,2]
            new_lst_int_genre_film_old = list(map(int, new_lst_str_genres_films))
            print("new_lst_genre_film ", new_lst_int_genre_film_old, "type new_lst_genre_film ",
                  type(new_lst_int_genre_film_old))

            # Pour apprécier la facilité de la vie en Python... "les ensembles en Python"
            # https://fr.wikibooks.org/wiki/Programmation_Python/Ensembles
            # OM 2021.05.02 Une liste de "id_genre" qui doivent être effacés de la table intermédiaire "t_genre_film".
            lst_diff_genres_delete_b = list(set(old_lst_data_genres_films_attribues) -
                                            set(new_lst_int_genre_film_old))
            print("lst_diff_genres_delete_b ", lst_diff_genres_delete_b)

            # Une liste de "id_genre" qui doivent être ajoutés à la "t_genre_film"
            lst_diff_genres_insert_a = list(
                set(new_lst_int_genre_film_old) - set(old_lst_data_genres_films_attribues))
            print("lst_diff_genres_insert_a ", lst_diff_genres_insert_a)

            # SQL pour insérer une nouvelle association entre
            # "fk_film"/"id_film" et "fk_genre"/"id_genre" dans la "t_genre_film"
            strsql_insert_genre_film = """INSERT INTO t_genre_film (id_genre_film, fk_genre, fk_film)
                                                    VALUES (NULL, %(value_fk_genre)s, %(value_fk_film)s)"""

            # SQL pour effacer une (des) association(s) existantes entre "id_film" et "id_genre" dans la "t_genre_film"
            strsql_delete_genre_film = """DELETE FROM t_genre_film WHERE fk_genre = %(value_fk_genre)s AND fk_film = %(value_fk_film)s"""

            with DBconnection() as mconn_bd:
                # Pour le film sélectionné, parcourir la liste des genres à INSÉRER dans la "t_genre_film".
                # Si la liste est vide, la boucle n'est pas parcourue.
                for id_genre_ins in lst_diff_genres_insert_a:
                    # Constitution d'un dictionnaire pour associer l'id du film sélectionné avec un nom de variable
                    # et "id_genre_ins" (l'id du genre dans la liste) associé à une variable.
                    valeurs_film_sel_genre_sel_dictionnaire = {"value_fk_film": id_film_selected,
                                                               "value_fk_genre": id_genre_ins}

                    mconn_bd.execute(strsql_insert_genre_film, valeurs_film_sel_genre_sel_dictionnaire)

                # Pour le film sélectionné, parcourir la liste des genres à EFFACER dans la "t_genre_film".
                # Si la liste est vide, la boucle n'est pas parcourue.
                for id_genre_del in lst_diff_genres_delete_b:
                    # Constitution d'un dictionnaire pour associer l'id du film sélectionné avec un nom de variable
                    # et "id_genre_del" (l'id du genre dans la liste) associé à une variable.
                    valeurs_film_sel_genre_sel_dictionnaire = {"value_fk_film": id_film_selected,
                                                               "value_fk_genre": id_genre_del}

                    # Du fait de l'utilisation des "context managers" on accède au curseur grâce au "with".
                    # la subtilité consiste à avoir une méthode "execute" dans la classe "DBconnection"
                    # ainsi quand elle aura terminé l'insertion des données le destructeur de la classe "DBconnection"
                    # sera interprété, ainsi on fera automatiquement un commit
                    mconn_bd.execute(strsql_delete_genre_film, valeurs_film_sel_genre_sel_dictionnaire)

        except Exception as Exception_update_genre_film_selected:
            raise ExceptionUpdateGenreFilmSelected(f"fichier : {Path(__file__).name}  ;  "
                                                   f"{update_genre_film_selected.__name__} ; "
                                                   f"{Exception_update_genre_film_selected}")

    # Après cette mise à jour de la table intermédiaire "t_genre_film",
    # on affiche les films et le(urs) genre(s) associé(s).
    return redirect(url_for('films_genres_afficher', id_film_sel=id_film_selected))


"""
    nom: genres_films_afficher_data

    Récupère la liste de tous les genres du film sélectionné par le bouton "MODIFIER" de "films_genres_afficher.html"
    Nécessaire pour afficher tous les "TAGS" des genres, ainsi l'utilisateur voit les genres à disposition

    On signale les erreurs importantes
"""


def genres_films_afficher_data(valeur_id_film_selected_dict):
    print("valeur_id_film_selected_dict...", valeur_id_film_selected_dict)
    try:

        strsql_film_selected = """SELECT id_film, nom_film, duree_film, description_film, cover_link_film, date_sortie_film, GROUP_CONCAT(id_genre) as GenresFilms FROM t_genre_film
                                        INNER JOIN t_film ON t_film.id_film = t_genre_film.fk_film
                                        INNER JOIN t_genre ON t_genre.id_genre = t_genre_film.fk_genre
                                        WHERE id_film = %(value_id_film_selected)s"""

        strsql_genres_films_non_attribues = """SELECT id_genre, intitule_genre FROM t_genre WHERE id_genre not in(SELECT id_genre as idGenresFilms FROM t_genre_film
                                                    INNER JOIN t_film ON t_film.id_film = t_genre_film.fk_film
                                                    INNER JOIN t_genre ON t_genre.id_genre = t_genre_film.fk_genre
                                                    WHERE id_film = %(value_id_film_selected)s)"""

        strsql_genres_films_attribues = """SELECT id_film, id_genre, intitule_genre FROM t_genre_film
                                            INNER JOIN t_film ON t_film.id_film = t_genre_film.fk_film
                                            INNER JOIN t_genre ON t_genre.id_genre = t_genre_film.fk_genre
                                            WHERE id_film = %(value_id_film_selected)s"""

        # Du fait de l'utilisation des "context managers" on accède au curseur grâce au "with".
        with DBconnection() as mc_afficher:
            # Envoi de la commande MySql
            mc_afficher.execute(strsql_genres_films_non_attribues, valeur_id_film_selected_dict)
            # Récupère les données de la requête.
            data_genres_films_non_attribues = mc_afficher.fetchall()
            # Affichage dans la console
            print("genres_films_afficher_data ----> data_genres_films_non_attribues ", data_genres_films_non_attribues,
                  " Type : ",
                  type(data_genres_films_non_attribues))

            # Envoi de la commande MySql
            mc_afficher.execute(strsql_film_selected, valeur_id_film_selected_dict)
            # Récupère les données de la requête.
            data_film_selected = mc_afficher.fetchall()
            # Affichage dans la console
            print("data_film_selected  ", data_film_selected, " Type : ", type(data_film_selected))

            # Envoi de la commande MySql
            mc_afficher.execute(strsql_genres_films_attribues, valeur_id_film_selected_dict)
            # Récupère les données de la requête.
            data_genres_films_attribues = mc_afficher.fetchall()
            # Affichage dans la console
            print("data_genres_films_attribues ", data_genres_films_attribues, " Type : ",
                  type(data_genres_films_attribues))

            # Retourne les données des "SELECT"
            return data_film_selected, data_genres_films_non_attribues, data_genres_films_attribues

    except Exception as Exception_genres_films_afficher_data:
        raise ExceptionGenresFilmsAfficherData(f"fichier : {Path(__file__).name}  ;  "
                                               f"{genres_films_afficher_data.__name__} ; "
                                               f"{Exception_genres_films_afficher_data}")
