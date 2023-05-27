from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Ваш адрес',
        validators=[DataRequired('Обязательное поле')]
    )
    custom_id = URLField(
        'Короткий адрес',
        validators=[Length(1, 6), Optional()]
    )
    submit = SubmitField('Добавить')
