from data import db
from config import USER, PSWD, HOST, DB_NAME

from misc import app

import handlers

def main():
    db.global_init(USER, PSWD, HOST, DB_NAME)
    app.run()


if __name__ == '__main__':
    main()


