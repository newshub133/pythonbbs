from flask import Flask
import config
from exts import db
from blueprints.cms import bp as cms_bp
from blueprints.front import bp as front_bp
from blueprints.user import bp as user_bp
from flask_migrate import Migrate
from models import user
import commands

app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)
db.init_app(app)
app.register_blueprint(cms_bp)
app.register_blueprint(front_bp)
app.register_blueprint(user_bp)
migrate = Migrate(app, db)
app.cli.command("create-permission")(commands.create_permission)
app.cli.command("create-role")(commands.create_role)
app.cli.command("create-test-user")(commands.create_test_user)
app.cli.command("create-admin")(commands.create_admin)






if __name__ == '__main__':
    app.run()
