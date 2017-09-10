from database.Config import app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from database.All import *
# from database.tables.UrlShortnerTable import UrlShortner

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
	manager.run()