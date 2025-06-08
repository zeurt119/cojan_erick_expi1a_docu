"""Gestion des formulaires avec WTF pour les films
Fichier : gestion_films_wtf_forms.py
Auteur : OM 2022.04.11

"""
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, NumberRange, DataRequired, Email
from wtforms.validators import Regexp
from wtforms.widgets import TextArea


class FormWTFAddFilm(FlaskForm):
    nom_client_add_wtf = StringField("Nom", validators=[Length(min=2, max=50), DataRequired()])
    prenom_client_add_wtf = StringField("Prénom", validators=[Length(min=2, max=50), DataRequired()])
    email_client_add_wtf = StringField("Email", validators=[Email(), DataRequired()])
    entreprise_client_add_wtf = StringField("Entreprise", validators=[Length(max=100)])
    telephone_client_add_wtf = StringField("Téléphone", validators=[Length(min=6, max=20)])
    submit = SubmitField("Ajouter client")


class FormWTFUpdateFilm(FlaskForm):
    nom_client_update_wtf = StringField("Nom", validators=[DataRequired(), Length(min=2, max=50)])
    prenom_client_update_wtf = StringField("Prénom", validators=[DataRequired(), Length(min=2, max=50)])
    email_client_update_wtf = StringField("Email", validators=[Email(), DataRequired()])
    entreprise_client_update_wtf = StringField("Entreprise", validators=[Length(max=100)])
    telephone_client_update_wtf = StringField("Téléphone", validators=[Length(min=6, max=20)])
    submit = SubmitField("Mettre à jour")


class FormWTFDeleteFilm(FlaskForm):
    nom_film_delete_wtf = StringField("Nom du client à supprimer", render_kw={'readonly': True})
    submit_btn_del_film = SubmitField("Effacer client")
    submit_btn_conf_del_film = SubmitField("Êtes-vous sûr d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")

