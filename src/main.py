"""
HomeCampus Flask Application
Python 3.9 migration from Tipfy framework

This is the main entry point for the HomeCampus mathematics education platform.
Migrated from Tipfy RequestHandler pattern to Flask application structure.
"""

import os
import logging
from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from flask_wtf.csrf import CSRFProtect
from google.cloud import ndb

# Import configuration
from flask_config import get_config

def create_app():
    """Flask application factory"""
    
    # Initialize Flask app with static files configuration
    app = Flask(__name__, 
                static_folder='.',  # Serve static files from current directory
                static_url_path='/static')
    app.config.from_object(get_config())
    
    # Initialize extensions - only if CSRF is enabled in config
    if app.config.get('WTF_CSRF_ENABLED', True):
        csrf = CSRFProtect(app)
    
    # Initialize Google Cloud NDB
    if not os.getenv('GAE_ENV', '').startswith('standard'):
        # Local development
        ndb_client = ndb.Client(project=app.config.get('GOOGLE_CLOUD_PROJECT'))
    else:
        # Production GAE
        ndb_client = ndb.Client()
    
    # Set up logging
    if not app.debug and not app.testing:
        # Production logging configuration
        logging.basicConfig(level=logging.INFO)
        app.logger.setLevel(logging.INFO)
        app.logger.info('HomeCampus startup')
    
    # Register Flask blueprints (Phase 2 - parallel implementation)
    from flask_homepage import flask_home_bp
    from flask_auth import flask_auth_bp
    from flask_learn_all_generated import flask_learn_all_bp
    from flask_practice_all_generated import flask_practice_all_bp
    
    app.register_blueprint(flask_home_bp)
    app.register_blueprint(flask_auth_bp)
    app.register_blueprint(flask_learn_all_bp)
    app.register_blueprint(flask_practice_all_bp)
    
    # Add static file routes that match original app.yaml structure
    from flask import send_from_directory
    
    @app.route('/stylesheets/<path:filename>')
    def serve_stylesheets(filename):
        return send_from_directory('stylesheets', filename)
    
    @app.route('/images/<path:filename>')
    def serve_images(filename):
        return send_from_directory('images', filename)
    
    @app.route('/js/<path:filename>')
    def serve_js(filename):
        return send_from_directory('js', filename)
    
    @app.route('/Home_Campus_User_Guide.pdf')
    def serve_user_guide():
        return send_from_directory('.', 'Home_Campus_User_Guide.pdf')
    
    @app.route('/download-worksheets/<path:filename>')
    def serve_worksheet_pdfs_lowercase(filename):
        """Serve PDF worksheets from Worksheets folder (lowercase)"""
        return send_from_directory('Worksheets', filename)
    
    @app.route('/Download-Worksheets/<path:filename>')
    def serve_worksheet_pdfs_capital(filename):
        """Serve PDF worksheets from Worksheets folder (capital D)"""
        return send_from_directory('Worksheets', filename)
    
    # Main homepage route - now using Flask (Phase 2)
    @app.route('/')
    def index():
        """Main homepage - migrated from Tipfy to Flask"""
        # Use the same logic as our tested flask_homepage route
        from flask_homepage import FlaskBaseHandler
        
        handler = FlaskBaseHandler()
        context = handler.get_template_context()
        
        try:
            return render_template('HomePage.html', **context)
        except Exception as e:
            # Safety fallback - log error and show simple page
            app.logger.error(f'Homepage template error: {str(e)}')
            return f"""
            <h1>HomeCampus - Temporary Service Message</h1>
            <p>We're performing system updates. Please try refreshing the page.</p>
            <p><a href="/flask-homepage">Alternative homepage link</a></p>
            <p>Error reference: {str(e)[:100]}</p>
            """
    
    # Keep backup route for testing
    @app.route('/phase1-test')
    def phase1_backup():
        """Backup of Phase 1 test page"""
        return '''
        <h1>Phase 1 Backup - Flask Working</h1>
        <p>This is the original Phase 1 test page for reference.</p>
        <p><a href="/">← Back to main homepage</a></p>
        '''
    
    @app.route('/health')
    def health_check():
        """Health check endpoint for monitoring"""
        return jsonify({
            'status': 'healthy',
            'version': '3.0.0-migration-phase1',
            'python_version': '3.9',
            'framework': 'Flask'
        })
    
    @app.route('/test-flask-post', methods=['POST'])
    def test_flask_post():
        """Test if Flask can handle POST requests"""
        logging.info(f"FLASK POST TEST - Method: {request.method}, Form: {dict(request.form)}, Args: {dict(request.args)}")
        return jsonify({'status': 'Flask POST working', 'method': request.method})
    
    @app.route('/test-db')
    def test_database():
        """Test database connectivity"""
        try:
            # Simple NDB test
            with ndb_client.context():
                return jsonify({
                    'database': 'connected', 
                    'ndb_client': 'initialized',
                    'status': 'ready_for_model_migration'
                })
        except Exception as e:
            app.logger.error(f'Database connection failed: {str(e)}')
            return jsonify({'database': 'error', 'message': str(e)}), 500
    
    # Error handlers
    @app.errorhandler(404)
    def not_found_error(error):
        return '<h1>404 - Page Not Found</h1><p>This route will be migrated in Phase 2</p>', 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return '<h1>500 - Internal Server Error</h1><p>Error during migration testing</p>', 500
    
    return app

# Create the Flask application instance
app = create_app()

# For GAE Python 3.9, the app instance needs to be available at module level
if __name__ == '__main__':
    # Local development server
    app.run(host='127.0.0.1', port=8080, debug=True)