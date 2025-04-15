from app.routes.auth import auth_bp
from app.routes.users import users_bp
from app.routes.messages import messages_bp

# Import blueprints to make them available when importing from routes
__all__ = ['auth_bp', 'users_bp', 'messages_bp']
