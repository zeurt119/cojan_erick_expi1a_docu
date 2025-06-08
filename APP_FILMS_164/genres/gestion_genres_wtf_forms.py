"""
    Fichier : gestion_genres_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, DataRequired
from wtforms.validators import Regexp


class FormWTFAjouterGenres(FlaskForm):
    entreprise = StringField("Entreprise", validators=[DataRequired(), Length(min=2, max=100)])
    titre = StringField("Titre", validators=[DataRequired(), Length(min=2, max=200)])
    contenu = TextAreaField("Contenu", validators=[DataRequired(), Length(min=2, max=2000)])
    date_ajout = StringField("Date ajout (YYYY-MM-DD)", validators=[DataRequired()])
    submit = SubmitField("Ajouter")



class FormWTFUpdateGenre(FlaskForm):
    entreprise = StringField("Entreprise", validators=[DataRequired(), Length(min=2, max=200)])
    titre = StringField("Titre", validators=[DataRequired(), Length(min=2, max=200)])
    contenu = TextAreaField("Contenu", validators=[DataRequired(), Length(min=2, max=2000)])
    date_ajout = StringField("Date ajout (YYYY-MM-DD)", validators=[DataRequired()])
    submit = SubmitField("Mettre à jour")


class FormWTFDeleteGenre(FlaskForm):
    """
        Dans le formulaire "genre_delete_wtf.html"

        nom_genre_delete_wtf : Champ qui reçoit la valeur du genre, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "genre".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_genre".
    """
    nom_genre_delete_wtf = StringField("Effacer cette doc")
    submit_btn_del = SubmitField("Effacer")
    submit_btn_conf_del = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
