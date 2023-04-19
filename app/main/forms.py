from flask_wtf import FlaskForm
from govuk_frontend_wtf.wtforms_widgets import GovRadioInput, GovSubmitInput, GovTextInput, GovDateInput
from wtforms.fields import RadioField, SubmitField, StringField, DateField
from wtforms.validators import InputRequired, Length, Optional, DataRequired

class CookiesForm(FlaskForm):
    functional = RadioField(
        "Do you want to accept functional cookies?",
        widget=GovRadioInput(),
        validators=[InputRequired(message="Select yes if you want to accept functional cookies")],
        choices=[("no", "No"), ("yes", "Yes")],
        default="no",
    )
    analytics = RadioField(
        "Do you want to accept analytics cookies?",
        widget=GovRadioInput(),
        validators=[InputRequired(message="Select yes if you want to accept analytics cookies")],
        choices=[("no", "No"), ("yes", "Yes")],
        default="no",
    )
    save = SubmitField("Save cookie settings", widget=GovSubmitInput())

class CircuitsForm(FlaskForm):


    circuits_date = DateField(
                "Please enter the start date for the period you need data for",
                widget=GovDateInput(),
                format = "%d %m %Y",
                validators=[
                    InputRequired()
                ]
            )
    choose_session_effort = RadioField(
        "Choose session tpe",
        widget=GovRadioInput(),
        validators=[InputRequired(message="Choose an session you want to do")],
        choices=[("easy", "Easy set"), ("medium", "Medium effort"), ("challenging", "Challenging")],
        default="no",
    )
    choose_session_type = RadioField(
        "Choose session tpe",
        widget=GovRadioInput(),
        validators=[InputRequired(message="Choose an session you want to do")],
        choices=[("hiit", "HIIT"), ("twelve", "12 by 12 by 6"), ("oneby6", "One min by 6 by 3")],
        default="no",
    )

    submit = SubmitField("Continue", widget=GovSubmitInput())

