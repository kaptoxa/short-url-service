from flask import jsonify
from data.__all_models import ShortUrl, SchemaShortUrl

from data import db
from misc import app

from config import API_URL


short_schema = SchemaShortUrl(only=('jumps_count',))

@app.route('/statistics/<link>', methods=['GET'])
def statistics(link):
    session = db.create_session()
    short = session.query(ShortUrl).filter(ShortUrl.url == link).first()
    if short:
        return short_schema.dumps(short)
    else:
        return jsonify({'error': f'Sorry. We don not have created \'{link}\' short link.'})


from requests import get, post
link = 'null'

def test_create():
    global link
    params = {"long_url": "http://dirty.ru"}
    response = post(f'{API_URL}/long_to_short/', json=params)
    link = response.json()['short_link']
    assert response.status_code == 200 and link != 'null'


def test_transition():
    global link
    response = get(f'{API_URL}/{link}')
    assert response.status_code == 200


def test_stats():
    global link
    response = get(f'{API_URL}/statistics/{link}')
    assert response.status_code == 200

