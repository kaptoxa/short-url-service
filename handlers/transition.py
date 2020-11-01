from flask import jsonify, redirect
from data.__all_models import ShortUrl

from data import db
from misc import app

from config import API_URL


@app.route('/<link>', methods=['GET'])
def transition(link):
    session = db.create_session()
    short = session.query(ShortUrl).filter(ShortUrl.url == link).first()
    if short:
        short.jumps_count += 1
        session.commit()
        return redirect(short.long.url)
    else:
        return jsonify({'error': f'Sorry. We don not have created \'{link}\' short link.'})


from requests import get, post
link = 'null'

def test_create():
    global link
    params = {"long_url": "http://dirty.ru"}
    response = post(f'{API_URL}/long_to_short/', json=params)
    print(response.json())
    link = response.json()['short_link']
    assert response.status_code == 200 and link != 'null'


def test_transition():
    global link
    response = get(f'{API_URL}/{link}')
    assert response.status_code == 200

