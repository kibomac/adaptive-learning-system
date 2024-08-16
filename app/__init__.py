from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # Basic configuration
    app.config.from_object('app.config.Config')
    
    # Initialize plugins
    db.init_app(app)
    CORS(app)
    migrate.init_app(app, db)
    
    # Register Blueprints
    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app