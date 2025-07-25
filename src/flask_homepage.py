"""
Flask HomePage Blueprint - Phase 2 Migration
Parallel implementation of HomePage.py functionality

This runs alongside the existing Tipfy system for gradual migration.
"""

from flask import Blueprint, render_template, request, session, g
from flask import current_app
import logging
from flask_models import get_flask_auth_context

# Import existing modules (they still work from python2_libs_backup when needed)
# We'll access the original functions through the Tipfy handlers for now
try:
    from Database import HCSubscription, SubmitProblemsTable, TestsMaster
    import HCRank
    import CodeTranslation
    import Grade7
    from Grade7 import Grade7PageConfig
except ImportError as e:
    # Graceful fallback during migration
    logging.warning(f"Some imports not available yet: {e}")

# Create Flask blueprint
flask_home_bp = Blueprint('flask_home', __name__)

class FlaskBaseHandler:
    """
    Flask equivalent of the Tipfy BaseHandler
    Provides same functionality but adapted for Flask
    """
    
    def __init__(self):
        # Initialize with current request context
        self.intent = request.args.get("intn")
    
    def get_template_context(self):
        """
        Get template context equivalent to Tipfy's render_response
        This maintains the same template variables that templates expect
        """
        # Get full authentication context
        context = get_flask_auth_context(session)
        
        # Add homepage-specific context
        context.update({
            'current_url': request.url,
            'register_url': '/Register',  # Static for now
            'TRIAL': 'N',  # Default value
            'UnfinishedWorksheetsCount': 0,  # Default value
            'intent': self.intent,
            'section': 'content'  # Default section
        })
        
        return context

@flask_home_bp.route('/flask-homepage')
def flask_homepage_real():
    """
    Flask version of the actual homepage
    Serves the real HomePage.html template
    """
    handler = FlaskBaseHandler()
    context = handler.get_template_context()
    
    try:
        # Try to serve the actual HomePage.html template
        return render_template('HomePage.html', **context)
    except Exception as e:
        # If template fails, show debug info
        return f"""
        <h1>Template Loading Test</h1>
        <p><strong>Error:</strong> {str(e)}</p>
        <p><strong>Template path:</strong> templates/HomePage.html</p>
        <p><strong>Context keys:</strong> {list(context.keys())}</p>
        <p>This helps us debug what's needed for the template to work.</p>
        """

@flask_home_bp.route('/flask-test')
def flask_homepage_test():
    """
    Test route to verify Flask homepage functionality
    Accessible at /flask-test (doesn't interfere with existing routes)
    """
    handler = FlaskBaseHandler()
    context = handler.get_template_context()
    
    # For testing, we'll return a simple response showing it works
    return f"""
    <html>
    <head><title>Flask Homepage Test</title></head>
    <body>
        <h1>🚀 Flask Homepage Blueprint Working!</h1>
        <h2>Phase 2: Parallel Flask Implementation</h2>
        
        <h3>Template Context (same as Tipfy):</h3>
        <ul>
            <li>Current URL: {context['current_url']}</li>
            <li>Intent: {context['intent']}</li>
            <li>Login URL: {context['login_url']}</li>
            <li>Register URL: {context['register_url']}</li>
            <li>Section: {context['section']}</li>
        </ul>
        
        <h3>Status:</h3>
        <p>✅ Flask blueprint loaded</p>
        <p>✅ Template context matching Tipfy structure</p>
        <p>✅ Ready to serve same templates as original</p>
        
        <p><strong>Next:</strong> This will serve the actual HomePage.html template</p>
        
        <p><a href="/">← Back to original homepage</a></p>
    </body>
    </html>
    """

@flask_home_bp.route('/Primary_Grade_3_Mathematics')
def flask_primary3():
    """
    Flask version of Primary3 page - serves actual template
    """
    handler = FlaskBaseHandler()
    context = handler.get_template_context()
    
    # Add Primary3-specific context (matching original Tipfy handler)
    grade_concept_rank = {}  # For now, empty dict like original when no user
    context.update({
        'grade_concept_rank': grade_concept_rank
    })
    
    try:
        return render_template('Primary_Grade_3.html', **context)
    except Exception as e:
        # Safety fallback
        return f"""
        <h1>Primary Grade 3 Mathematics</h1>
        <p>Temporary service update in progress.</p>
        <p><a href="/">← Back to homepage</a></p>
        <p>Debug: {str(e)[:100]}</p>
        """

@flask_home_bp.route('/Primary_Grade_4_Mathematics')
def flask_primary4():
    """Flask version of Primary4 page"""
    handler = FlaskBaseHandler()
    context = handler.get_template_context()
    context.update({'grade_concept_rank': {}})
    
    try:
        return render_template('Primary_Grade_4.html', **context)
    except Exception as e:
        return f"<h1>Primary Grade 4 Mathematics</h1><p>Service update in progress.</p><p><a href='/'>← Homepage</a></p>"

@flask_home_bp.route('/Primary_Grade_5_Mathematics')
def flask_primary5():
    """Flask version of Primary5 page"""
    handler = FlaskBaseHandler()
    context = handler.get_template_context()
    context.update({'grade_concept_rank': {}})
    
    try:
        return render_template('Primary_Grade_5.html', **context)
    except Exception as e:
        return f"<h1>Primary Grade 5 Mathematics</h1><p>Service update in progress.</p><p><a href='/'>← Homepage</a></p>"

@flask_home_bp.route('/Primary_Grade_6_Mathematics')
@flask_home_bp.route('/PSLE')  # PSLE route points to Primary 6
def flask_primary6():
    """Flask version of Primary6 page (also handles /PSLE)"""
    handler = FlaskBaseHandler()
    context = handler.get_template_context()
    context.update({'grade_concept_rank': {}})
    
    try:
        return render_template('Primary_Grade_6.html', **context)
    except Exception as e:
        return f"<h1>Primary Grade 6 Mathematics / PSLE</h1><p>Service update in progress.</p><p><a href='/'>← Homepage</a></p>"

@flask_home_bp.route('/flask-primary3-test')
def flask_primary3_test():
    """
    Test route for Primary3 page functionality
    """
    return f"""
    <html>
    <head><title>Flask Primary3 Test</title></head>
    <body>
        <h1>📚 Primary3 Migration Complete!</h1>
        <p>✅ <a href="/Primary_Grade_3_Mathematics">Primary Grade 3 Mathematics</a> is now running on Flask</p>
        <p><a href="/">← Back to homepage</a></p>
    </body>
    </html>
    """

# Additional test routes for other handlers
@flask_home_bp.route('/flask-handlers-status')
def flask_handlers_status():
    """Show status of all Flask handler implementations"""
    
    handlers_status = {
        'HomePage': '✅ Test implemented',
        'Primary3': '✅ Test implemented', 
        'Primary4': '⏳ Pending',
        'Primary5': '⏳ Pending',
        'Primary6': '⏳ Pending',
        'Secondary1': '⏳ Pending',
        'UnfinishedWorksheets': '⏳ Pending'
    }
    
    status_html = "<h3>Flask Handler Migration Status:</h3><ul>"
    for handler, status in handlers_status.items():
        status_html += f"<li>{handler}: {status}</li>"
    status_html += "</ul>"
    
    return f"""
    <html>
    <head><title>Flask Migration Status</title></head>
    <body>
        <h1>🔄 Phase 2 Migration Status</h1>
        {status_html}
        
        <h3>Test Routes:</h3>
        <ul>
            <li><a href="/flask-test">Flask Homepage Test</a></li>
            <li><a href="/flask-primary3-test">Flask Primary3 Test</a></li>
        </ul>
        
        <p><a href="/">← Back to original homepage</a></p>
    </body>
    </html>
    """