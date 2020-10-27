from flask import Flask
from data import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'short_links_service_BAZINGA_key'


def main():
    db.global_init("short_urls_db")
#    app.run()


if __name__ == '__main__':
    main()


