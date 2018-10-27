
from flask_script import Manager

from flask_migrate import Migrate, MigrateCommand
from news import app,db, create_app

# define the manager
manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)


@app.route('/index')
def index():
    return 'index'


# develop app for development or production
app = create_app('development')


if __name__ == '__main__':
    manager.run()