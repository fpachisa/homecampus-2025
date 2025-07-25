"""
Flask Authentication Blueprint - Phase 2 Migration
Handles all authentication routes: login, register, logout, etc.

This runs alongside the existing Tipfy system for gradual migration.
"""

from flask import Blueprint, render_template, request, session, redirect, url_for, flash
import logging

# Create Flask blueprint for authentication
flask_auth_bp = Blueprint('flask_auth', __name__)

class FlaskAuthHandler:
    """
    Flask equivalent of the Tipfy authentication handlers
    For now, provides basic structure - authentication logic will be added gradually
    """
    
    def __init__(self):
        self.intent = request.args.get("intn")
    
    def get_template_context(self):
        """Get template context for auth pages"""
        context = {
            'auth_session': None,  # Will implement proper auth later
            'current_user': None,
            'login_url': '/SignIn',
            'logout_url': '/auth/logout',
            'current_url': request.url,
            'register_url': '/Register',
            'TRIAL': 'N',
            'UnfinishedWorksheetsCount': 0,
            'intent': self.intent,
        }
        return context

@flask_auth_bp.route('/SignIn')
@flask_auth_bp.route('/auth/login')
def flask_signin():
    """Flask version of login page"""
    handler = FlaskAuthHandler()
    context = handler.get_template_context()
    
    try:
        return render_template('LoginPage.html', **context)
    except Exception as e:
        return f"""
        <h1>Sign In - HomeCampus</h1>
        <p>Sign in functionality is being updated.</p>
        <p><a href="/">← Back to homepage</a></p>
        <p>Debug: {str(e)[:50]}</p>
        """

@flask_auth_bp.route('/Register') 
@flask_auth_bp.route('/auth/register')
def flask_register():
    """Flask version of registration page"""
    handler = FlaskAuthHandler()
    context = handler.get_template_context()
    
    try:
        return render_template('RegisterPage.html', **context)
    except Exception as e:
        return f"""
        <h1>Register - HomeCampus</h1>
        <p>Registration functionality is being updated.</p>
        <p><a href="/">← Back to homepage</a></p>
        <p>Debug: {str(e)[:50]}</p>
        """

@flask_auth_bp.route('/ForgotPassword')
def flask_forgot_password():
    """Flask version of forgot password page"""
    handler = FlaskAuthHandler()
    context = handler.get_template_context()
    
    try:
        return render_template('ForgotPasswordPage.html', **context)
    except Exception as e:
        return f"""
        <h1>Forgot Password - HomeCampus</h1>
        <p>Password reset functionality is being updated.</p>
        <p><a href="/SignIn">← Back to sign in</a></p>
        <p>Debug: {str(e)[:50]}</p>
        """

@flask_auth_bp.route('/ResetPassword')
def flask_reset_password():
    """Flask version of reset password page"""
    handler = FlaskAuthHandler()
    context = handler.get_template_context()
    
    try:
        return render_template('ResetPasswordPage.html', **context)
    except Exception as e:
        return f"""
        <h1>Reset Password - HomeCampus</h1>
        <p>Password reset functionality is being updated.</p>
        <p><a href="/SignIn">← Back to sign in</a></p>
        <p>Debug: {str(e)[:50]}</p>
        """

@flask_auth_bp.route('/AddChild')
def flask_add_child():
    """Flask version of add child page"""
    handler = FlaskAuthHandler()
    context = handler.get_template_context()
    
    try:
        return render_template('AddChildPage.html', **context)
    except Exception as e:
        return f"""
        <h1>Add Child - HomeCampus</h1>
        <p>Add child functionality is being updated.</p>
        <p><a href="/">← Back to homepage</a></p>
        <p>Debug: {str(e)[:50]}</p>
        """

@flask_auth_bp.route('/auth/logout')
def flask_logout():
    """Flask version of logout - simple redirect for now"""
    # Clear any session data (will implement proper logout later)
    session.clear()
    return redirect('/')

# Test route to show auth migration status
@flask_auth_bp.route('/flask-auth-status')
def flask_auth_status():
    """Show status of authentication route migration"""
    
    auth_routes_status = {
        '/SignIn': '✅ Template loading implemented',
        '/Register': '✅ Template loading implemented',
        '/ForgotPassword': '✅ Template loading implemented', 
        '/ResetPassword': '✅ Template loading implemented',
        '/AddChild': '✅ Template loading implemented',
        '/auth/logout': '✅ Basic logout implemented',
        'Authentication Logic': '⏳ Phase 3 - Full auth implementation'
    }
    
    status_html = "<h3>Authentication Routes Migration Status:</h3><ul>"
    for route, status in auth_routes_status.items():
        status_html += f"<li><strong>{route}</strong>: {status}</li>"
    status_html += "</ul>"
    
    return f"""
    <html>
    <head><title>Authentication Migration Status</title></head>
    <body>
        <h1>🔐 Authentication Routes Migration</h1>
        {status_html}
        
        <h3>Test Auth Routes:</h3>
        <ul>
            <li><a href="/SignIn">Sign In Page</a></li>
            <li><a href="/Register">Register Page</a></li>
            <li><a href="/ForgotPassword">Forgot Password</a></li>
        </ul>
        
        <p><strong>Note:</strong> These routes now load templates but full authentication logic will be implemented in Phase 3.</p>
        <p><a href="/">← Back to homepage</a></p>
    </body>
    </html>
    """