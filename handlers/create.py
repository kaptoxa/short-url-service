from flask import jsonify, request
from data.__all_models import LongUrl, SchemaLongUrl, SchemaShortUrl
from marshmallow import ValidationError

from data import db
from misc import app

from config import API_URL

from pprint import pprint

long_schema = SchemaLongUrl()
short_schema = SchemaShortUrl(only=('url',))

@app.route('/long_to_short/', methods=['POST'])
def long_to_short():
    json_data = request.get_json()
    try:
        data = long_schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 422

    session = db.create_session()
    long = session.query(LongUrl).filter_by(url=data['url']).first()
    if long is None:
        long = LongUrl(url=data['url'])
        session.add(long)
        session.commit()

        session.add(short_schema.load({'short_link': long.id}))
        session.commit()

    return short_schema.dumps(long.short[-1])


def test_create():
    from requests import get, post
    params = {"long_url": "http://yandexlyceum.ru"}
    response = post(f'{API_URL}/long_to_short/', json=params)
    assert response.status_code == 200 and response.json()['short_link']


def test_empty_request():
    from requests import get, post
    response = post(f'{API_URL}/long_to_short/', json={})
    assert response.status_code == 422


def test_bad_request():
    from requests import get, post
    response = post(f'{API_URL}/long_to_short/', json={'a': 1})
    assert response.status_code == 422
