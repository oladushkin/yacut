from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, regexp

from settings import CUSTOM_ID_RE


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле')]
    )
    custom_id = URLField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(1, 16),
            Optional(),
            regexp(CUSTOM_ID_RE, message='Указано недопустимое имя для короткой ссылки')
        ]
    )
    submit = SubmitField('Добавить')
