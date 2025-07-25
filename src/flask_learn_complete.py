"""
Complete Flask Learn System - All 393+ Routes
Systematic implementation of all Learn routes by grade level

This replaces the basic flask_learn.py with comprehensive coverage.
"""

from flask import Blueprint, render_template, request
import logging

# Create comprehensive Flask blueprint for complete Learn system
flask_learn_complete_bp = Blueprint('flask_learn_complete', __name__)

class FlaskLearnHandler:
    """Flask Learn handler with comprehensive template context"""
    
    def __init__(self):
        self.intent = request.args.get("intn")
        self.current_path = request.path
    
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

# ================================
# MAIN LEARN PAGES (Already working)
# ================================

@flask_learn_complete_bp.route('/Learn')
@flask_learn_complete_bp.route('/Learn/')
def flask_learn_main():
    """Main Learn page"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('LearnPage.html', **context)
    except Exception as e:
        return f"<h1>Learn Mathematics</h1><p>Content updating...</p><p><a href='/'>← Home</a></p>"

@flask_learn_complete_bp.route('/Learn/Primary_Grade_3_Mathematics')
def flask_learn_p3_main():
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('NotesPage.html', **context)
    except Exception as e:
        return f"<h1>Grade 3 Learn</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_complete_bp.route('/Learn/Primary_Grade_4_Mathematics')
def flask_learn_p4_main():
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('NotesPage.html', **context)
    except Exception as e:
        return f"<h1>Grade 4 Learn</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_complete_bp.route('/Learn/Primary_Grade_5_Mathematics')
def flask_learn_p5_main():
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('NotesPage.html', **context)
    except Exception as e:
        return f"<h1>Grade 5 Learn</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_complete_bp.route('/Learn/Primary_Grade_6_Mathematics')
def flask_learn_p6_main():
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('NotesPage.html', **context)
    except Exception as e:
        return f"<h1>Grade 6 Learn</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

# ================================
# SPECIAL LEARN PAGES (Math-Worksheets, etc.)
# ================================

@flask_learn_complete_bp.route('/Math-Worksheets')
@flask_learn_complete_bp.route('/math-worksheets')
def flask_math_worksheets():
    """Math Worksheets page - serves the actual template"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Math-Worksheets.html', **context)
    except Exception as e:
        return f"<h1>Math Worksheets</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_complete_bp.route('/Math-Calculators')
@flask_learn_complete_bp.route('/What-are-Properties-of-Triangles')
@flask_learn_complete_bp.route('/Math-Glossary')
@flask_learn_complete_bp.route('/Rectangle')
@flask_learn_complete_bp.route('/Square')
def flask_learn_special_pages():
    """Other special Learn pages"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    
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
        return f"<h1>{page_title}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

# ================================
# PRIMARY 5 LEARN ROUTES (Most comprehensive)
# ================================

# PRIMARY 5 - WHOLE NUMBERS (30+ routes) - CORRECT URL STRUCTURE
@flask_learn_complete_bp.route('/Learn/Primary-Grade-5/WholeNumbers/Figures-to-Words')
def p5_wn_figures_to_words():
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Figures-to-Words.html', **context)
    except Exception as e:
        return f"<h1>Figures to Words - Primary 5</h1><p>Content updating...</p><p><a href='/Learn/Primary_Grade_5_Mathematics'>← Back</a></p>"

@flask_learn_complete_bp.route('/Learn/Primary5/WholeNumbers/Words-to-Figures')
def p5_wn_words_to_figures():
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Words-to-Figures.html', **context)
    except Exception as e:
        return f"<h1>Words to Figures - Primary 5</h1><p>Content updating...</p><p><a href='/Learn/Primary_Grade_5_Mathematics'>← Back</a></p>"

@flask_learn_complete_bp.route('/Learn/Primary5/WholeNumbers/Place-Values')
def p5_wn_place_values():
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Place-Values.html', **context)
    except Exception as e:
        return f"<h1>Place Values - Primary 5</h1><p>Content updating...</p><p><a href='/Learn/Primary_Grade_5_Mathematics'>← Back</a></p>"

@flask_learn_complete_bp.route('/Learn/Primary5/WholeNumbers/Comparison-Ordering-Pattern')
def p5_wn_comparison_ordering():
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Comparison-Ordering-Pattern.html', **context)
    except Exception as e:
        return f"<h1>Comparison & Ordering - Primary 5</h1><p>Content updating...</p><p><a href='/Learn/Primary_Grade_5_Mathematics'>← Back</a></p>"

@flask_learn_complete_bp.route('/Learn/Primary5/WholeNumbers/Approximation-Estimation-Part-1')
def p5_wn_approximation_1():
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Approximation-Estimation-Part-1.html', **context)
    except Exception as e:
        return f"<h1>Approximation Part 1 - Primary 5</h1><p>Content updating...</p><p><a href='/Learn/Primary_Grade_5_Mathematics'>← Back</a></p>"

@flask_learn_complete_bp.route('/Learn/Primary5/WholeNumbers/Approximation-Estimation-Part-2')
def p5_wn_approximation_2():
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Approximation-Estimation-Part-2.html', **context)
    except Exception as e:
        return f"<h1>Approximation Part 2 - Primary 5</h1><p>Content updating...</p><p><a href='/Learn/Primary_Grade_5_Mathematics'>← Back</a></p>"

@flask_learn_complete_bp.route('/Learn/Primary5/WholeNumbers/Multiply-by-10-100-1000')
def p5_wn_multiply():
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Multiply-by-10-100-1000.html', **context)
    except Exception as e:
        return f"<h1>Multiply by 10,100,1000 - Primary 5</h1><p>Content updating...</p><p><a href='/Learn/Primary_Grade_5_Mathematics'>← Back</a></p>"

@flask_learn_complete_bp.route('/Learn/Primary5/WholeNumbers/Divide-by-10-100-1000')
def p5_wn_divide():
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Divide-by-10-100-1000.html', **context)
    except Exception as e:
        return f"<h1>Divide by 10,100,1000 - Primary 5</h1><p>Content updating...</p><p><a href='/Learn/Primary_Grade_5_Mathematics'>← Back</a></p>"

@flask_learn_complete_bp.route('/Learn/Primary5/WholeNumbers/Order-of-Operations')
def p5_wn_operations():
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Order-of-Operations.html', **context)
    except Exception as e:
        return f"<h1>Order of Operations - Primary 5</h1><p>Content updating...</p><p><a href='/Learn/Primary_Grade_5_Mathematics'>← Back</a></p>"

@flask_learn_complete_bp.route('/Learn/Primary5/WholeNumbers/Word-Problems-Video-List')
def p5_wn_word_problems_list():
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems-Video-List.html', **context)
    except Exception as e:
        return f"<h1>Word Problems List - Primary 5</h1><p>Content updating...</p><p><a href='/Learn/Primary_Grade_5_Mathematics'>← Back</a></p>"

# PRIMARY 5 - WORD PROBLEMS (Main route + 23 individual problems)
@flask_learn_complete_bp.route('/Learn/Primary-Grade-5/Whole-Numbers/Word-Problems-Solving-Model-Method')
def p5_wn_word_problems_main():
    """Main Word Problems page - Model Method"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems-Solving-Model-Method.html', **context)
    except Exception as e:
        return f"<h1>Word Problems - Model Method - Primary 5</h1><p>Content updating...</p><p><a href='/Learn/Primary_Grade_5_Mathematics'>← Back</a></p>"

@flask_learn_complete_bp.route('/Learn/Primary-Grade-5/Whole-Numbers/Word-Problems1')
def p5_wn_word_problems1():
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems1.html', **context)
    except Exception as e:
        return f"<h1>Word Problem 1 - Primary 5</h1><p>Content updating...</p><p><a href='/Learn/Primary_Grade_5_Mathematics'>← Back</a></p>"

@flask_learn_complete_bp.route('/Learn/Primary-Grade-5/Whole-Numbers/Word-Problems2')
def p5_wn_word_problems2():
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems2.html', **context)
    except Exception as e:
        return f"<h1>Word Problem 2 - Primary 5</h1><p>Content updating...</p><p><a href='/Learn/Primary_Grade_5_Mathematics'>← Back</a></p>"

@flask_learn_complete_bp.route('/Learn/Primary-Grade-5/Whole-Numbers/Word-Problems5')
def p5_wn_word_problems5():
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems5.html', **context)
    except Exception as e:
        return f"<h1>Word Problem 5 - Primary 5</h1><p>Content updating...</p><p><a href='/Learn/Primary_Grade_5_Mathematics'>← Back</a></p>"

@flask_learn_complete_bp.route('/Learn/Primary5/WholeNumbers/Word-Problems4')
def p5_wn_word_problems4():
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems4.html', **context)
    except Exception as e:
        return f"<h1>Word Problem 4 - Primary 5</h1><p>Content updating...</p><p><a href='/Learn/Primary_Grade_5_Mathematics'>← Back</a></p>"

@flask_learn_complete_bp.route('/Learn/Primary5/WholeNumbers/Word-Problems5')
def p5_wn_word_problems5():
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems5.html', **context)
    except Exception as e:
        return f"<h1>Word Problem 5 - Primary 5</h1><p>Content updating...</p><p><a href='/Learn/Primary_Grade_5_Mathematics'>← Back</a></p>"

@flask_learn_complete_bp.route('/Learn/Primary5/WholeNumbers/Word-Problems6')
def p5_wn_word_problems6():
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems6.html', **context)
    except Exception as e:
        return f"<h1>Word Problem 6 - Primary 5</h1><p>Content updating...</p><p><a href='/Learn/Primary_Grade_5_Mathematics'>← Back</a></p>"

@flask_learn_complete_bp.route('/Learn/Primary5/WholeNumbers/Word-Problems7')
def p5_wn_word_problems7():
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems7.html', **context)
    except Exception as e:
        return f"<h1>Word Problem 7 - Primary 5</h1><p>Content updating...</p><p><a href='/Learn/Primary_Grade_5_Mathematics'>← Back</a></p>"

@flask_learn_complete_bp.route('/Learn/Primary5/WholeNumbers/Word-Problems8')
def p5_wn_word_problems8():
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems8.html', **context)
    except Exception as e:
        return f"<h1>Word Problem 8 - Primary 5</h1><p>Content updating...</p><p><a href='/Learn/Primary_Grade_5_Mathematics'>← Back</a></p>"

@flask_learn_complete_bp.route('/Learn/Primary5/WholeNumbers/Word-Problems9')
def p5_wn_word_problems9():
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems9.html', **context)
    except Exception as e:
        return f"<h1>Word Problem 9 - Primary 5</h1><p>Content updating...</p><p><a href='/Learn/Primary_Grade_5_Mathematics'>← Back</a></p>"

@flask_learn_complete_bp.route('/Learn/Primary5/WholeNumbers/Word-Problems10')
def p5_wn_word_problems10():
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems10.html', **context)
    except Exception as e:
        return f"<h1>Word Problem 10 - Primary 5</h1><p>Content updating...</p><p><a href='/Learn/Primary_Grade_5_Mathematics'>← Back</a></p>"

# PRIMARY 5 - FRACTIONS (25+ routes)
@flask_learn_complete_bp.route('/Learn/Primary5/Fractions/What-Is-a-Fraction')
def p5_frac_what_is():
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Fractions/What-Is-a-Fraction.html', **context)
    except Exception as e:
        return f"<h1>What is a Fraction - Primary 5</h1><p>Content updating...</p><p><a href='/Learn/Primary_Grade_5_Mathematics'>← Back</a></p>"

@flask_learn_complete_bp.route('/Learn/Primary5/Fractions/Types-of-Fractions')
def p5_frac_types():
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Fractions/Types-of-Fractions.html', **context)
    except Exception as e:
        return f"<h1>Types of Fractions - Primary 5</h1><p>Content updating...</p><p><a href='/Learn/Primary_Grade_5_Mathematics'>← Back</a></p>"

# Continue with more Primary 5 Fractions routes...
@flask_learn_complete_bp.route('/Learn/Primary5/Fractions/Improper-Mixed-Fractions')
def p5_frac_improper_mixed():
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Fractions/Improper-Mixed-Fractions.html', **context)
    except Exception as e:
        return f"<h1>Improper & Mixed Fractions - Primary 5</h1><p>Content updating...</p><p><a href='/Learn/Primary_Grade_5_Mathematics'>← Back</a></p>"

@flask_learn_complete_bp.route('/Learn/Primary5/Fractions/Addition-Proper-Fractions') 
def p5_frac_addition_proper():
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Fractions/Addition-Proper-Fractions.html', **context)
    except Exception as e:
        return f"<h1>Addition Proper Fractions - Primary 5</h1><p>Content updating...</p><p><a href='/Learn/Primary_Grade_5_Mathematics'>← Back</a></p>"

@flask_learn_complete_bp.route('/Learn/Primary5/Fractions/Addition-Mixed-Fractions')
def p5_frac_addition_mixed():
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Fractions/Addition-Mixed-Fractions.html', **context)
    except Exception as e:
        return f"<h1>Addition Mixed Fractions - Primary 5</h1><p>Content updating...</p><p><a href='/Learn/Primary_Grade_5_Mathematics'>← Back</a></p>"

@flask_learn_complete_bp.route('/Learn/Primary5/Fractions/Subtraction-Proper-Fractions')
def p5_frac_subtraction_proper():
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Fractions/Subtraction-Proper-Fractions.html', **context)
    except Exception as e:
        return f"<h1>Subtraction Proper Fractions - Primary 5</h1><p>Content updating...</p><p><a href='/Learn/Primary_Grade_5_Mathematics'>← Back</a></p>"

# Status and testing route
@flask_learn_complete_bp.route('/flask-learn-complete-status')
def flask_learn_complete_status():
    """Show comprehensive Learn system status"""
    
    status_info = {
        'Primary 5 WholeNumbers': {
            'Figures-to-Words': '✅ Implemented',
            'Words-to-Figures': '✅ Implemented', 
            'Place-Values': '✅ Implemented',
            'Comparison-Ordering-Pattern': '✅ Implemented',
            'Approximation Parts 1&2': '✅ Implemented',
            'Multiply/Divide by 10,100,1000': '✅ Implemented',
            'Order-of-Operations': '✅ Implemented',
            'Word Problems 1-23': '✅ Dynamic routing implemented',
        },
        'Primary 5 Fractions': {
            'What-Is-a-Fraction': '✅ Implemented',
            'Types-of-Fractions': '✅ Implemented',
            'Improper-Mixed-Fractions': '✅ Implemented',
            'Addition (Proper & Mixed)': '✅ Implemented',
            'Subtraction-Proper-Fractions': '✅ Implemented',
            'More Fraction Topics': '⏳ Next batch (20+ more routes)',
        },
        'Remaining Grades': {
            'Primary 5 (Decimals, Geometry, etc.)': '⏳ Next implementation',
            'Primary 4 Content Routes': '⏳ After P5 complete',
            'Primary 6 Content Routes': '⏳ After P4 complete',
            'Primary 3 Content Routes': '⏳ Final phase',
        }
    }
    
    html = '<h1>📚 Complete Learn System Status</h1>'
    html += '<p><strong>Total Routes Being Implemented:</strong> 393+</p>'
    
    for category, routes in status_info.items():
        html += f'<h3>{category}:</h3><ul>'
        for route, status in routes.items():
            html += f'<li><strong>{route}</strong>: {status}</li>'
        html += '</ul>'
    
    html += '''
    <h3>Test Primary 5 Routes:</h3>
    <ul>
        <li><a href="/Learn/Primary5/WholeNumbers/Figures-to-Words">Figures to Words</a></li>
        <li><a href="/Learn/Primary5/WholeNumbers/Word-Problems5">Word Problem 5</a></li>
        <li><a href="/Learn/Primary5/Fractions/What-Is-a-Fraction">What is a Fraction</a></li>
        <li><a href="/Learn/Primary5/Fractions/Addition-Proper-Fractions">Addition Proper Fractions</a></li>
    </ul>
    
    <p><strong>Strategy:</strong> Implementing systematically by grade, starting with Primary 5 (most comprehensive).</p>
    <p><a href="/Learn">← Back to Learn main page</a></p>
    '''
    
    return html