from flask import jsonify, request
from hashids import Hashids
from data.__all_models import Short_url, Long_url

from data import db
from main import app

@app.route('/long_to_short/')
def long_to_short():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in ['long_url']):
        return jsonify({'error': 'Bad request'})

    hashids = Hashids(min_length=8)
    session = db.create_session()

    long = Long_url(url=request.json['long_url'])
    last_one = session.query(Long_url).order_by(Long_url.id.desc()).first()

    short_url = hashids.encode(last_one.id + 1) if last_one else 1
    short = Short_url(url=f'https://localhost:5000/{short_url}')
    short.long = [long]

    session.add(short)
    session.commit()

    return jsonify({'short_link': short_url})


def test_create():
    from requests import get
    api_server = "http://localhost:5000"
    params = {"long_url": "http://yandexlyceum.ru"}
    response = get(f'{api_server}/long_to_short/', json=params)
    assert response.status_code != 200
