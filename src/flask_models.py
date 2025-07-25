"""
Flask User Models - Compatible with existing GAE NDB system
Maintains compatibility with original HomeCampusUser model from Models.py
"""

from google.cloud import ndb
import hashlib
import secrets
import datetime
import logging

class FlaskHomeCampusUser(ndb.Model):
    """
    Flask-compatible user model that mirrors the original HomeCampusUser
    Maintains all original fields for zero user-visible changes
    """
    
    # Original fields from Models.py HomeCampusUser
    auth_id = ndb.StringProperty(required=True)
    username = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    password_hash = ndb.StringProperty(required=False)  # Hashed password
    
    # Original HomeCampusUser fields
    authorized = ndb.BooleanProperty(default=False)
    active = ndb.BooleanProperty(default=True)
    IsParent = ndb.BooleanProperty(default=False)
    first_name = ndb.StringProperty(required=False)
    last_name = ndb.StringProperty(required=False)
    parent_first_name = ndb.StringProperty(required=False)
    parent_last_name = ndb.StringProperty(required=False)
    skill = ndb.StringProperty(required=False)
    IsTeacher = ndb.BooleanProperty(default=False)
    school_code = ndb.StringProperty(required=False)
    
    # Additional fields for Flask authentication
    created = ndb.DateTimeProperty(auto_now_add=True)
    last_login = ndb.DateTimeProperty()
    email_verified = ndb.BooleanProperty(default=False)
    password_reset_token = ndb.StringProperty()
    password_reset_expires = ndb.DateTimeProperty()
    
    @classmethod
    def create_user(cls, username, email, password=None, **kwargs):
        """
        Create a new user with password hashing
        Compatible with original user creation flow
        """
        try:
            # Generate auth_id in the same format as original system
            auth_id = f"own|{username}"
            
            # Check if user already exists
            existing_user = cls.query(cls.username == username).get()
            if existing_user:
                return None, "User already exists"
            
            existing_email = cls.query(cls.email == email).get()
            if existing_email:
                return None, "Email already registered"
            
            # Create user entity
            user_data = {
                'auth_id': auth_id,
                'username': username,
                'email': email,
                **kwargs  # Include any additional fields
            }
            
            # Hash password if provided
            if password:
                user_data['password_hash'] = cls._hash_password(password)
            
            user = cls(**user_data)
            user.put()
            
            logging.info(f"Created new user: {username}")
            return user, None
            
        except Exception as e:
            logging.error(f"Error creating user {username}: {str(e)}")
            return None, f"Registration failed: {str(e)}"
    
    @classmethod
    def authenticate(cls, username, password):
        """
        Authenticate user with username/email and password
        Returns user entity if successful, None if failed
        """
        try:
            # Try to find user by username or email
            user = cls.query(cls.username == username).get()
            if not user:
                user = cls.query(cls.email == username).get()
            
            if not user or not user.active:
                return None
            
            # Verify password
            if user.password_hash and cls._verify_password(password, user.password_hash):
                # Update last login
                user.last_login = datetime.datetime.now()
                user.put()
                return user
            
            return None
            
        except Exception as e:
            logging.error(f"Authentication error for {username}: {str(e)}")
            return None
    
    @classmethod
    def get_by_auth_id(cls, auth_id):
        """Get user by auth_id (for social login compatibility)"""
        return cls.query(cls.auth_id == auth_id).get()
    
    @classmethod
    def get_by_email(cls, email):
        """Get user by email"""
        return cls.query(cls.email == email).get()
    
    @staticmethod
    def _hash_password(password):
        """Hash password using secure method"""
        salt = secrets.token_hex(32)
        pwdhash = hashlib.pbkdf2_hmac('sha256', 
                                      password.encode('utf-8'), 
                                      salt.encode('utf-8'), 
                                      100000)
        return salt + pwdhash.hex()
    
    @staticmethod
    def _verify_password(password, stored_hash):
        """Verify password against stored hash"""
        try:
            salt = stored_hash[:64]
            stored_password = stored_hash[64:]
            pwdhash = hashlib.pbkdf2_hmac('sha256',
                                          password.encode('utf-8'),
                                          salt.encode('utf-8'),
                                          100000)
            return pwdhash.hex() == stored_password
        except:
            return False
    
    def set_password(self, password):
        """Set new password for user"""
        self.password_hash = self._hash_password(password)
    
    def generate_reset_token(self):
        """Generate password reset token"""
        self.password_reset_token = secrets.token_urlsafe(32)
        self.password_reset_expires = datetime.datetime.now() + datetime.timedelta(hours=1)
        return self.password_reset_token
    
    def verify_reset_token(self, token):
        """Verify password reset token"""
        if not self.password_reset_token or not self.password_reset_expires:
            return False
        
        if datetime.datetime.now() > self.password_reset_expires:
            return False
        
        return self.password_reset_token == token
    
    def to_dict(self):
        """Convert user to dictionary (for session storage)"""
        return {
            'id': self.key.id(),
            'auth_id': self.auth_id,
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'IsParent': self.IsParent,
            'IsTeacher': self.IsTeacher,
            'authorized': self.authorized,
            'active': self.active,
            'school_code': self.school_code
        }

class FlaskUserSession:
    """
    Helper class to manage user sessions in Flask
    Compatible with original Tipfy auth session format
    """
    
    def __init__(self, flask_session):
        self.session = flask_session
    
    def login_user(self, user):
        """Log in user and store in session"""
        self.session['user_id'] = user.key.id()
        self.session['auth_id'] = user.auth_id
        self.session['username'] = user.username
        self.session['user_data'] = user.to_dict()
        self.session.permanent = True
        logging.info(f"User logged in: {user.username}")
    
    def logout_user(self):
        """Log out user and clear session"""
        username = self.session.get('username', 'unknown')
        self.session.clear()
        logging.info(f"User logged out: {username}")
    
    def get_current_user(self):
        """Get current logged-in user"""
        user_id = self.session.get('user_id')
        if not user_id:
            print("get_current_user: No user_id in session")
            return None
        
        try:
            print(f"get_current_user: Fetching user with ID {user_id}")
            with ndb.Client().context():
                user_key = ndb.Key(FlaskHomeCampusUser, user_id)
                user = user_key.get()
                print(f"get_current_user: Retrieved user: {user}")
                return user
        except Exception as e:
            print(f"get_current_user: Exception: {str(e)}")
            return None
    
    def is_logged_in(self):
        """Check if user is logged in"""
        return 'user_id' in self.session and self.session.get('user_id') is not None
    
    def get_user_data(self):
        """Get user data from session (for template context)"""
        return self.session.get('user_data', {})

# Utility functions for backward compatibility
def get_flask_auth_context(flask_session):
    """
    Generate authentication context for templates
    Compatible with original Tipfy auth context
    """
    user_session = FlaskUserSession(flask_session)
    current_user = user_session.get_current_user()
    
    context = {
        'auth_session': user_session.session if user_session.is_logged_in() else None,
        'current_user': current_user,
        'login_url': '/SignIn',
        'logout_url': '/auth/logout',
        'register_url': '/Register',
        'user_data': user_session.get_user_data(),
        'is_logged_in': user_session.is_logged_in()
    }
    
    return context