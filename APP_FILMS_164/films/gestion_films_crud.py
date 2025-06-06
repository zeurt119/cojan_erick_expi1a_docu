from pathlib import Path

from flask import redirect
from flask import request
from flask import session
from flask import url_for
from flask import flash
from flask import render_template

from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *
from APP_FILMS_164.films.gestion_films_wtf_forms import FormWTFUpdateFilm, FormWTFAddFilm, FormWTFDeleteFilm


@app.route("/film_add", methods=['GET', 'POST'])
def film_add_wtf():
    form_add_film = FormWTFAddFilm()
    if request.method == "POST":
        try:
            if form_add_film.validate_on_submit():
                nom_film_add = form_add_film.nom_film_add_wtf.data

                valeurs_insertion_dictionnaire = {"value_nom_film": nom_film_add}
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_film = """INSERT INTO t_filme (id_filme, nom_film) VALUES (NULL,%(value_nom_film)s) """
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_film, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                return redirect(url_for('films_genres_afficher', id_film_sel=0))

        except Exception as Exception_genres_ajouter_wtf:
            raise ExceptionGenresAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                            f"{film_add_wtf.__name__} ; "
                                            f"{Exception_genres_ajouter_wtf}")

    return render_template("films/film_add_wtf.html", form_add_film=form_add_film)


@app.route("/film_update", methods=['GET', 'POST'])
def film_update_wtf():
    id_film_update = request.values['id_film_btn_edit_html']

    form_update_film = FormWTFUpdateFilm()
    try:
        if request.method == "POST" and form_update_film.submit.data:
            nom_film_update = form_update_film.nom_film_update_wtf.data
            duree_film_update = form_update_film.duree_film_update_wtf.data
            description_film_update = form_update_film.description_film_update_wtf.data
            cover_link_film_update = form_update_film.cover_link_film_update_wtf.data
            datesortie_film_update = form_update_film.datesortie_film_update_wtf.data

            valeur_update_dictionnaire = {
                "value_id_filme": id_film_update,
                "value_nom_film": nom_film_update,
                "value_duree_film": duree_film_update,
                "value_description_film": description_film_update,
                "value_cover_link_film": cover_link_film_update,
                "value_datesortie_film": datesortie_film_update
            }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_nom_film = """UPDATE t_filme SET nom_film = %(value_nom_film)s,
                                                            duree_film = %(value_duree_film)s,
                                                            description_film = %(value_description_film)s,
                                                            cover_link_film = %(value_cover_link_film)s,
                                                            date_sortie_film = %(value_datesortie_film)s
                                                            WHERE id_filme = %(value_id_filme)s"""
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_nom_film, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            print(f"Donnée mise à jour !!")

            return redirect(url_for('films_genres_afficher', id_film_sel=id_film_update))
        elif request.method == "GET":
            str_sql_id_film = "SELECT * FROM t_filme WHERE id_filme = %(value_id_filme)s"
            valeur_select_dictionnaire = {"value_id_filme": id_film_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_film, valeur_select_dictionnaire)
                data_film = mybd_conn.fetchone()
            print("data_film ", data_film, " type ", type(data_film), " genre ", data_film["nom_film"])

            form_update_film.nom_film_update_wtf.data = data_film["nom_film"]
            form_update_film.duree_film_update_wtf.data = data_film["duree_film"]
            print(f" duree film  ", data_film["duree_film"], "  type ", type(data_film["duree_film"]))
            form_update_film.description_film_update_wtf.data = data_film["description_film"]
            form_update_film.cover_link_film_update_wtf.data = data_film["cover_link_film"]
            form_update_film.datesortie_film_update_wtf.data = data_film["date_sortie_film"]

    except Exception as Exception_film_update_wtf:
        raise ExceptionFilmUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                     f"{film_update_wtf.__name__} ; "
                                     f"{Exception_film_update_wtf}")

    return render_template("films/film_update_wtf.html", form_update_film=form_update_film)


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
            print("data_film_delete ", data_film_delete)

            flash(f"Effacer le film de façon définitive de la BD !!!", "danger")
            btn_submit_del = True

        if form_delete_film.submit_btn_del_film.data:
            valeur_delete_dictionnaire = {"value_id_filme": id_film_delete}
            print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

            str_sql_delete_fk_film_genre = """DELETE FROM t_genre_film WHERE fk_filme = %(value_id_filme)s"""
            str_sql_delete_film = """DELETE FROM t_filme WHERE id_filme = %(value_id_filme)s"""
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_delete_fk_film_genre, valeur_delete_dictionnaire)
                mconn_bd.execute(str_sql_delete_film, valeur_delete_dictionnaire)

            flash(f"Film définitivement effacé !!", "success")
            print(f"Film définitivement effacé !!")

            return redirect(url_for('films_genres_afficher', id_film_sel=0))
        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_filme": id_film_delete}
            print(id_film_delete, type(id_film_delete))

            str_sql_genres_films_delete = """SELECT * FROM t_filme WHERE id_filme = %(value_id_filme)s"""

            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_genres_films_delete, valeur_select_dictionnaire)
                data_film_delete = mydb_conn.fetchall()
                print("data_film_delete...", data_film_delete)

                session['data_film_delete'] = data_film_delete

            btn_submit_del = False

    except Exception as Exception_film_delete_wtf:
        raise ExceptionFilmDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                     f"{film_delete_wtf.__name__} ; "
                                     f"{Exception_film_delete_wtf}")

    return render_template("films/film_delete_wtf.html",
                           form_delete_film=form_delete_film,
                           btn_submit_del=btn_submit_del,
                           data_film_del=data_film_delete
                           )
