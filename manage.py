from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell

from app import AppFactory, db
from app.models import User

app = AppFactory()
migrate = Migrate(app=app, db=db)
manager = Manager(app)
def make_shell_context():
    return dict(app=app, db=db, User=User)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()

