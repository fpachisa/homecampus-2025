"""
Flask Learn Blueprint - Phase 2 Migration
Handles the massive Learn system (393+ routes)

Strategy: Start with main Learn pages, then systematically add content routes
"""

from flask import Blueprint, render_template, request
import logging

# Create Flask blueprint for Learn system
flask_learn_bp = Blueprint('flask_learn', __name__)

class FlaskLearnHandler:
    """Flask equivalent of the Tipfy Learn handlers"""
    
    def __init__(self):
        self.intent = request.args.get("intn")
    
    def get_template_context(self):
        """Get template context for Learn pages"""
        context = {
            'auth_session': None,
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

# Main Learn page
@flask_learn_bp.route('/Learn')
@flask_learn_bp.route('/Learn/')
def flask_learn_main():
    """Main Learn page"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    
    try:
        return render_template('LearnPage.html', **context)
    except Exception as e:
        return f"""
        <h1>Learn Mathematics - HomeCampus</h1>
        <p>Learning content is being updated.</p>
        <p><a href="/">← Back to homepage</a></p>
        <p>Debug: {str(e)[:50]}</p>
        """

# Primary Grade Learn pages
@flask_learn_bp.route('/Learn/Primary_Grade_3_Mathematics')
def flask_learn_p3():
    """Primary Grade 3 Learn page"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    
    try:
        return render_template('NotesPage.html', **context)
    except Exception as e:
        return f"<h1>Grade 3 Mathematics - Learn</h1><p>Content updating...</p><p><a href='/Learn'>← Back to Learn</a></p>"

@flask_learn_bp.route('/Learn/Primary_Grade_4_Mathematics')
def flask_learn_p4():
    """Primary Grade 4 Learn page"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    
    try:
        return render_template('NotesPage.html', **context)
    except Exception as e:
        return f"<h1>Grade 4 Mathematics - Learn</h1><p>Content updating...</p><p><a href='/Learn'>← Back to Learn</a></p>"

@flask_learn_bp.route('/Learn/Primary_Grade_5_Mathematics')
def flask_learn_p5():
    """Primary Grade 5 Learn page"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    
    try:
        return render_template('NotesPage.html', **context)
    except Exception as e:
        return f"<h1>Grade 5 Mathematics - Learn</h1><p>Content updating...</p><p><a href='/Learn'>← Back to Learn</a></p>"

@flask_learn_bp.route('/Learn/Primary_Grade_6_Mathematics')
def flask_learn_p6():
    """Primary Grade 6 Learn page"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    
    try:
        return render_template('NotesPage.html', **context)
    except Exception as e:
        return f"<h1>Grade 6 Mathematics - Learn</h1><p>Content updating...</p><p><a href='/Learn'>← Back to Learn</a></p>"

# Special Learn routes from app.yaml
@flask_learn_bp.route('/Math-Worksheets')
@flask_learn_bp.route('/math-worksheets')
def flask_math_worksheets():
    """Math Worksheets page - serves the actual template"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    
    try:
        # This is the correct template from the original Learn.py
        return render_template('Notes/Math-Worksheets.html', **context)
    except Exception as e:
        return f"""
        <h1>Math Worksheets - HomeCampus</h1>
        <p>Math worksheets content is being updated.</p>
        <p><a href="/Learn">← Back to Learn main page</a></p>
        <p>Debug: {str(e)[:100]}</p>
        """

@flask_learn_bp.route('/Math-Calculators')
@flask_learn_bp.route('/What-are-Properties-of-Triangles')
@flask_learn_bp.route('/Math-Glossary')
@flask_learn_bp.route('/Rectangle')
@flask_learn_bp.route('/Square')
def flask_learn_special_pages():
    """Other special Learn pages from app.yaml"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    
    # Determine which template based on URL
    path = request.path
    if 'Calculator' in path:
        template_name = 'Notes/Math-Calculators.html'
        page_title = 'Math Calculators'
    elif 'Triangle' in path:
        template_name = 'Notes/Glossary/Triangles.html'
        page_title = 'Properties of Triangles'
    elif 'Glossary' in path:
        template_name = 'Notes/Math-Glossary.html'  
        page_title = 'Math Glossary'
    elif 'Rectangle' in path:
        template_name = 'Notes/Glossary/Rectangle.html'
        page_title = 'Rectangle'
    elif 'Square' in path:
        template_name = 'Notes/Glossary/Square.html'
        page_title = 'Square'
    else:
        template_name = 'LearnPage.html'
        page_title = 'Learn Mathematics'
    
    try:
        return render_template(template_name, **context)
    except Exception as e:
        return f"""
        <h1>{page_title} - HomeCampus</h1>
        <p>This learning content is being updated.</p>
        <p><a href="/Learn">← Back to Learn main page</a></p>
        <p>Debug: {str(e)[:50]}</p>
        """

# Learn migration status
@flask_learn_bp.route('/flask-learn-status')
def flask_learn_status():
    """Show Learn system migration status"""
    
    learn_status = {
        'Main Learn Pages': {
            '/Learn': '✅ Implemented',
            '/Learn/Primary_Grade_3_Mathematics': '✅ Implemented',
            '/Learn/Primary_Grade_4_Mathematics': '✅ Implemented', 
            '/Learn/Primary_Grade_5_Mathematics': '✅ Implemented',
            '/Learn/Primary_Grade_6_Mathematics': '✅ Implemented',
        },
        'Special Learn Pages': {
            '/Math-Calculators': '✅ Implemented',
            '/Math-Worksheets': '✅ Implemented',
            '/What-are-Properties-of-Triangles': '✅ Implemented',
            '/Math-Glossary': '✅ Implemented',
            '/Rectangle': '✅ Implemented',
            '/Square': '✅ Implemented',
        },
        'Content Routes': {
            'Primary 5 WholeNumbers (50+ routes)': '⏳ Next phase',
            'Primary 5 Fractions (40+ routes)': '⏳ Next phase',
            'Primary 5 Decimals (30+ routes)': '⏳ Next phase',
            'Primary 5 Other topics (100+ routes)': '⏳ Next phase',
            'Primary 3,4,6 Content (200+ routes)': '⏳ Future phases',
        }
    }
    
    html = '<h1>📚 Learn System Migration Status</h1>'
    
    for category, routes in learn_status.items():
        html += f'<h3>{category}:</h3><ul>'
        for route, status in routes.items():
            html += f'<li><strong>{route}</strong>: {status}</li>'
        html += '</ul>'
    
    html += '''
    <h3>Next Steps:</h3>
    <p>The Learn system has <strong>393 content routes</strong>. We're implementing them systematically:</p>
    <ol>
        <li>✅ Main Learn pages (completed)</li>
        <li>⏳ High-traffic content routes (in progress)</li>
        <li>⏳ Bulk content migration (planned)</li>
    </ol>
    
    <h3>Test Learn Pages:</h3>
    <ul>
        <li><a href="/Learn">Main Learn Page</a></li>
        <li><a href="/Learn/Primary_Grade_5_Mathematics">Grade 5 Learn</a></li>
        <li><a href="/Math-Calculators">Math Calculators</a></li>
    </ul>
    
    <p><a href="/">← Back to homepage</a></p>
    '''
    
    return html