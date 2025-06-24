from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from server.config import Config
# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app(config_class=Config):
    """Application factory function"""
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    # Import and register blueprints
    from server.controllers.auth_controller import auth_bp
    from server.controllers.episode_controller import episodes_bp
    from server.controllers.guest_controller import guests_bp
    from server.controllers.appearance_controller import appearances_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(episodes_bp)
    app.register_blueprint(guests_bp)
    app.register_blueprint(appearances_bp)
    
    return app

# Create the app instance
app = create_app()

# Import models at the bottom to avoid circular imports
from server.models.user import User
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance