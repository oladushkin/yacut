from .error_handlers import InvalidAPIUsage
from .models import URLMap
import string


def validators_url(data):
    if 'url' not in data or data['url'] is None:
        raise InvalidAPIUsage('\"url\" является обязательным полем!')


def validators_castom_id(data):
    if len(data['custom_id']) > 16:
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    if URLMap.query.filter_by(short=data['custom_id']).first():
        raise InvalidAPIUsage(f'Имя "{data["custom_id"]}" уже занято.')
    letters_and_digits = string.ascii_letters + string.digits
    for i in data['custom_id']:
        if i in letters_and_digits:
            continue
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
