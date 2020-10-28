from flask import Flask
from data import db
from config import USER, PSWD, HOST, DB_NAME, SECRET_KEY

import handlers

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY



def main():
    db.global_init(USER, PSWD, HOST, DB_NAME)
    app.run()


if __name__ == '__main__':
    main()


