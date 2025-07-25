"""
Quick Template Fix for Primary 5 Word Problems
This adds the correct template for the main Word Problems route
"""

from flask import Blueprint, render_template, request

# Import the main generated blueprint and add this specific fix
from flask_learn_all_generated import flask_learn_all_bp, FlaskLearnHandler

# Override the main Word Problems route with correct template
@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Whole-Numbers/Word-Problems-Solving-Model-Method')
def p5_word_problems_model_method_fixed():
    """Fixed: Main Word Problems page with correct template"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    
    try:
        # Use the existing Word-Problems.html template
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems.html', **context)
    except Exception as e:
        return f"<h1>Word Problems - Model Method - Primary 5</h1><p>Template error: {str(e)}</p><p><a href='/Learn/Primary_Grade_5_Mathematics'>← Back</a></p>"

# Add a test route to verify template loading
@flask_learn_all_bp.route('/test-primary5-templates')
def test_primary5_templates():
    """Test which Primary 5 templates are working"""
    
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    
    # Test a few templates that we know exist
    test_results = []
    
    templates_to_test = [
        ('Word-Problems.html', 'Notes/Primary5/WholeNumbers/Word-Problems.html'),
        ('Figures-to-Words.html', 'Notes/Primary5/WholeNumbers/Figures-to-Words.html'), 
        ('Words-to-Figures.html', 'Notes/Primary5/WholeNumbers/Words-to-Figures.html'),
        ('Decimal - Multiply.html', 'Notes/Primary5/Decimal/multiplying-decimal-numbers-by-10s-100s-1000s.html'),
    ]
    
    for name, template_path in templates_to_test:
        try:
            # Try to render the template
            render_template(template_path, **context)
            test_results.append(f'✅ {name}: Template exists and renders')
        except Exception as e:
            test_results.append(f'❌ {name}: {str(e)[:50]}')
    
    html = '<h1>Primary 5 Template Test Results</h1><ul>'
    for result in test_results:
        html += f'<li>{result}</li>'
    html += '</ul>'
    
    html += '''
    <h3>Test Links:</h3>
    <ul>
        <li><a href="/Learn/Primary-Grade-5/Whole-Numbers/Word-Problems-Solving-Model-Method">Word Problems (Fixed)</a></li>
        <li><a href="/Learn/Primary-Grade-5/WholeNumbers/Figures-to-Words">Figures to Words</a></li>
    </ul>
    <p><a href="/Learn">← Back to Learn</a></p>
    '''
    
    return html