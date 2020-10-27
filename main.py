from flask import Flask
from data import db
from data.__all_models import Short_url, Long_url, Pair

app = Flask(__name__)
app.config['SECRET_KEY'] = 'short_links_service_BAZINGA_key'


def main():
    db.global_init("short_urls_db")

#    short = Short_url()
#    short.url = "http://127.0.0.1/sramo.ta"
#    long = Long_url()
#    long.url = "http://ya.ru"

    session = db.create_session()


    pair = session.query(Pair).first()
    print(pair)
    print(pair.short)
    print(pair.long)

 #   pair = Pair()
 #   pair.long = long
 #   pair.short = short

#    session.add(pair)
#    session.commit()
    #    app.run()


if __name__ == '__main__':
    main()


