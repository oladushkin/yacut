from flask import jsonify, request
from http import HTTPStatus
from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .views import get_unique_short_id
from .validators_api import validators_castom_id, validators_url


@app.route('/api/id/', methods=['POST'])
def post_url():
    data = request.get_json()
    if data is None:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    validators_url(data)
    if 'custom_id' not in data:
        data['custom_id'] = get_unique_short_id()
    if not data['custom_id']:
        data['custom_id'] = get_unique_short_id()
    validators_castom_id(data)
    url = URLMap(
        original=data['url'],
        short=data['custom_id']
    )
    db.session.add(url)
    db.session.commit()
    return jsonify(url.post_to_dict()), HTTPStatus.CREATED


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_url(short_id):
    url = URLMap.query.filter_by(short=short_id).first()
    if url is None:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    return jsonify(url.get_to_dict()), HTTPStatus.OK
