from flask import jsonify, redirect
from data.__all_models import Short_url, Transition

from data import db
from misc import app


@app.route('/<link>', methods=['GET'])
def transition(link):
    session = db.create_session()
    query = session.query(Short_url).filter(Short_url.url == link)
    if query.scalar():
        short = query.one()
        t = Transition(short=short)
        short.transitions.append(t)
        session.commit()
        return redirect(short.long[-1].url)
    else:
        return jsonify({'error': f'Sorry. We don not have created \'{link}\' short link.'})


from requests import get
api_server = "http://127.0.0.1:5000"
link = 'null'

def test_create():
    global link
    params = {"long_url": "http://dirty.ru"}
    response = get(f'{api_server}/long_to_short/', json=params)
    link = response.json()['short_link']
    assert response.status_code == 200 and link


def test_transition():
    global link
    response = get(f'{api_server}/{link}')
    assert response.status_code == 200

