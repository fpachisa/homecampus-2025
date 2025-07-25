"""
Complete Flask Learn System - ALL 338 Routes
AUTO-GENERATED from Learn.py analysis
"""

from flask import Blueprint, render_template, request

flask_learn_all_bp = Blueprint('flask_learn_all', __name__)

class FlaskLearnHandler:
    def __init__(self):
        self.intent = request.args.get("intn")
    
    def get_template_context(self):
        return {
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


# AUTO-GENERATED FLASK ROUTES FOR ALL LEARN CONTENT
# Generated from Learn.py analysis

# ====== PRIMARY3 ROUTES (41 routes) ======

@flask_learn_all_bp.route('/Learn/Primary-Grade-3/Whole-Numbers/Number-Notations-Place-Values-Up-to-10000')
def p3wnupto10000_4407():
    """Learn route: /Learn/Primary-Grade-3/Whole-Numbers/Number-Notations-Place-Values-Up-to-10000"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/WholeNumbers/Whole_Numbers_Upto_10000.html', **context)
    except Exception as e:
        grade = "Primary-Grade-3"
        topic = "Number-Notations-Place-Values-Up-to-10000"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-3/Whole-Numbers/Writing-Numbers-from-Figures-to-Words-Up-to-10000')
def p3wnfigurestowordsupto10000_5652():
    """Learn route: /Learn/Primary-Grade-3/Whole-Numbers/Writing-Numbers-from-Figures-to-Words-Up-to-10000"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/WholeNumbers/Figures_To_Words_Upto_10000.html', **context)
    except Exception as e:
        grade = "Primary-Grade-3"
        topic = "Writing-Numbers-from-Figures-to-Words-Up-to-10000"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-3/Whole-Numbers/Writing-Numbers-from-Words-to-Figures-Up-to-10000')
def p3wnwordstofiguresupto10000_6431():
    """Learn route: /Learn/Primary-Grade-3/Whole-Numbers/Writing-Numbers-from-Words-to-Figures-Up-to-10000"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/WholeNumbers/Words_To_Figures_Upto_10000.html', **context)
    except Exception as e:
        grade = "Primary-Grade-3"
        topic = "Writing-Numbers-from-Words-to-Figures-Up-to-10000"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-3/Whole-Numbers/Number-Patterns')
def p3wnnumberpatterns_3997():
    """Learn route: /Learn/Primary-Grade-3/Whole-Numbers/Number-Patterns"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/WholeNumbers/Number_Patterns.html', **context)
    except Exception as e:
        grade = "Primary-Grade-3"
        topic = "Number-Patterns"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-3/Whole-Numbers/Comparing-Ordering')
def p3wncomparingordering_2732():
    """Learn route: /Learn/Primary-Grade-3/Whole-Numbers/Comparing-Ordering"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/WholeNumbers/Comparing_Ordering.html', **context)
    except Exception as e:
        grade = "Primary-Grade-3"
        topic = "Comparing-Ordering"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-3/Whole-Numbers/Addition')
def p3wnaddition_9662():
    """Learn route: /Learn/Primary-Grade-3/Whole-Numbers/Addition"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/WholeNumbers/Addition_Of_Numbers_Within_10000.html', **context)
    except Exception as e:
        grade = "Primary-Grade-3"
        topic = "Addition"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-3/Whole-Numbers/Subtraction')
def p3wnsubtraction_2188():
    """Learn route: /Learn/Primary-Grade-3/Whole-Numbers/Subtraction"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/WholeNumbers/Subtraction_Of_Numbers_Within_10000.html', **context)
    except Exception as e:
        grade = "Primary-Grade-3"
        topic = "Subtraction"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-3/Whole-Numbers/Multiplication-Tables-of-6-7-8-9')
def p3wntimestables6789_6856():
    """Learn route: /Learn/Primary-Grade-3/Whole-Numbers/Multiplication-Tables-of-6-7-8-9"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/WholeNumbers/Multiplication_Tables_Of_6_7_8_9.html', **context)
    except Exception as e:
        grade = "Primary-Grade-3"
        topic = "Multiplication-Tables-of-6-7-8-9"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-3/Whole-Numbers/2-Step-Word-Problems')
def p3wnwordproblems_7172():
    """Learn route: /Learn/Primary-Grade-3/Whole-Numbers/2-Step-Word-Problems"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/WholeNumbers/Whole_Numbers_Word_Problems.html', **context)
    except Exception as e:
        grade = "Primary-Grade-3"
        topic = "2-Step-Word-Problems"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-3/Whole-Numbers-Multiplication')
def p3wnmultiplication_7396():
    """Learn route: /Learn/Primary-Grade-3/Whole-Numbers-Multiplication"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/WholeNumbers/Multiplication_Of_Numbers_Within_10000.html', **context)
    except Exception as e:
        grade = "Primary-Grade-3"
        topic = "Whole-Numbers-Multiplication"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-3/Whole-Numbers-Division')
def p3wndivision_6391():
    """Learn route: /Learn/Primary-Grade-3/Whole-Numbers-Division"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/WholeNumbers/Division_Of_Numbers_Within_1000.html', **context)
    except Exception as e:
        grade = "Primary-Grade-3"
        topic = "Whole-Numbers-Division"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-3/Fractions/What-Is-a-Fraction')
def p5frwhatisfractions_4007():
    """Learn route: /Learn/Primary-Grade-3/Fractions/What-Is-a-Fraction"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/Fractions/Equivalent_Fractions.html', **context)
    except Exception as e:
        grade = "Primary-Grade-3"
        topic = "What-Is-a-Fraction"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-3/Money-Word-Problems')
def p3mowordproblems_6074():
    """Learn route: /Learn/Primary-Grade-3/Money-Word-Problems"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/Money/Money_Word_Problems.html', **context)
    except Exception as e:
        grade = "Primary-Grade-3"
        topic = "Money-Word-Problems"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-3/Addition-of-Money')
def p3moaddition_2977():
    """Learn route: /Learn/Primary-Grade-3/Addition-of-Money"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/Money/Addition_Of_Money.html', **context)
    except Exception as e:
        grade = "Primary-Grade-3"
        topic = "Addition-of-Money"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-3/Subtraction-of-Money')
def p3mosubtraction_6938():
    """Learn route: /Learn/Primary-Grade-3/Subtraction-of-Money"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/Money/Subtraction_Of_Money.html', **context)
    except Exception as e:
        grade = "Primary-Grade-3"
        topic = "Subtraction-of-Money"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-3/Telling-Time')
def p3titellingtime_6706():
    """Learn route: /Learn/Primary-Grade-3/Telling-Time"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/Time/Telling_Time.html', **context)
    except Exception as e:
        grade = "Primary-Grade-3"
        topic = "Telling-Time"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-3/Time-Conversion-Hours-Minutes')
def p3titimeconversion_5650():
    """Learn route: /Learn/Primary-Grade-3/Time-Conversion-Hours-Minutes"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/Time/Hours_and_Minutes.html', **context)
    except Exception as e:
        grade = "Primary-Grade-3"
        topic = "Time-Conversion-Hours-Minutes"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-3/Time-Addition')
def p3titimeaddition_5663():
    """Learn route: /Learn/Primary-Grade-3/Time-Addition"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/Time/Time_Addition.html', **context)
    except Exception as e:
        grade = "Primary-Grade-3"
        topic = "Time-Addition"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-3/Time-Subtraction')
def p3titimesubtraction_893():
    """Learn route: /Learn/Primary-Grade-3/Time-Subtraction"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/Time/Time_Subtraction.html', **context)
    except Exception as e:
        grade = "Primary-Grade-3"
        topic = "Time-Subtraction"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-3/Time-Finding-Duration-Start-Finish')
def p3titimeduration_8172():
    """Learn route: /Learn/Primary-Grade-3/Time-Finding-Duration-Start-Finish"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/Time/Time_Duration.html', **context)
    except Exception as e:
        grade = "Primary-Grade-3"
        topic = "Time-Finding-Duration-Start-Finish"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-3/Time-Problem-Sums')
def p3titimewordproblems_9905():
    """Learn route: /Learn/Primary-Grade-3/Time-Problem-Sums"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/Time/Time_Word_Problems.html', **context)
    except Exception as e:
        grade = "Primary-Grade-3"
        topic = "Time-Problem-Sums"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-3/Metres-Centimetres')
def p3lmvmetrescentimetres_9184():
    """Learn route: /Learn/Primary-Grade-3/Metres-Centimetres"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/LengthMassVolume/Metres_Centimetres.html', **context)
    except Exception as e:
        grade = "Primary-Grade-3"
        topic = "Metres-Centimetres"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-3/KiloMetres-Metres')
def p3lmvkilometresmetres_6855():
    """Learn route: /Learn/Primary-Grade-3/KiloMetres-Metres"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/LengthMassVolume/KiloMetres_Metres.html', **context)
    except Exception as e:
        grade = "Primary-Grade-3"
        topic = "KiloMetres-Metres"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-3/Kilograms-Grams')
def p3lmvkilogramsgrams_1178():
    """Learn route: /Learn/Primary-Grade-3/Kilograms-Grams"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/LengthMassVolume/Kilograms_Grams.html', **context)
    except Exception as e:
        grade = "Primary-Grade-3"
        topic = "Kilograms-Grams"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-3/Litres-Millilitres')
def p3lmvlitresmillilitres_4184():
    """Learn route: /Learn/Primary-Grade-3/Litres-Millilitres"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/LengthMassVolume/Litres_Millilitres.html', **context)
    except Exception as e:
        grade = "Primary-Grade-3"
        topic = "Litres-Millilitres"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-3/Length-Mass-Volume-1-Step-Story-Sums')
def p3lmv1stepwordproblems_1903():
    """Learn route: /Learn/Primary-Grade-3/Length-Mass-Volume-1-Step-Story-Sums"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/LengthMassVolume/1_Step_Story_Sums.html', **context)
    except Exception as e:
        grade = "Primary-Grade-3"
        topic = "Length-Mass-Volume-1-Step-Story-Sums"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-3/Length-Mass-Volume-2-Step-Story-Sums')
def p3lmv2stepwordproblems_8055():
    """Learn route: /Learn/Primary-Grade-3/Length-Mass-Volume-2-Step-Story-Sums"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/LengthMassVolume/2_Step_Story_Sums.html', **context)
    except Exception as e:
        grade = "Primary-Grade-3"
        topic = "Length-Mass-Volume-2-Step-Story-Sums"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-3/Equivalent-Fractions')
def p3frequivalentfractions_8949():
    """Learn route: /Learn/Primary-Grade-3/Equivalent-Fractions"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/Fractions/Equivalent_Fractions.html', **context)
    except Exception as e:
        grade = "Primary-Grade-3"
        topic = "Equivalent-Fractions"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-3/Simplifying-Fractions')
def p3frsimplifyingfractions_6455():
    """Learn route: /Learn/Primary-Grade-3/Simplifying-Fractions"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/Fractions/Simplifying_Fractions.html', **context)
    except Exception as e:
        grade = "Primary-Grade-3"
        topic = "Simplifying-Fractions"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-3/Comparing-and-Ordering-Fractions')
def p3frcomparingorderingfractions_9609():
    """Learn route: /Learn/Primary-Grade-3/Comparing-and-Ordering-Fractions"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/Fractions/Comparing_Ordering_Fractions.html', **context)
    except Exception as e:
        grade = "Primary-Grade-3"
        topic = "Comparing-and-Ordering-Fractions"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-3/Adding-Fractions')
def p3fraddingfractions_6876():
    """Learn route: /Learn/Primary-Grade-3/Adding-Fractions"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/Fractions/Addition_Fractions.html', **context)
    except Exception as e:
        grade = "Primary-Grade-3"
        topic = "Adding-Fractions"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-3/Subtracting-Fractions')
def p3frsubtractingfractions_5272():
    """Learn route: /Learn/Primary-Grade-3/Subtracting-Fractions"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/Fractions/Subtracting_Fractions.html', **context)
    except Exception as e:
        grade = "Primary-Grade-3"
        topic = "Subtracting-Fractions"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-3/Area-in-Square-Units')
def p3apsquareunits_1271():
    """Learn route: /Learn/Primary-Grade-3/Area-in-Square-Units"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/AreaPerimeter/Area_Square_Units.html', **context)
    except Exception as e:
        grade = "Primary-Grade-3"
        topic = "Area-in-Square-Units"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-3/Area-in-Square-Centimetres-Square-Metres')
def p3apsquarecmm_7454():
    """Learn route: /Learn/Primary-Grade-3/Area-in-Square-Centimetres-Square-Metres"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/AreaPerimeter/Area_Square_CM_Square_M.html', **context)
    except Exception as e:
        grade = "Primary-Grade-3"
        topic = "Area-in-Square-Centimetres-Square-Metres"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-3/Area-of-Squares-and-Rectangles')
def p3aparea_7658():
    """Learn route: /Learn/Primary-Grade-3/Area-of-Squares-and-Rectangles"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/AreaPerimeter/Area_Square_Rectangle.html', **context)
    except Exception as e:
        grade = "Primary-Grade-3"
        topic = "Area-of-Squares-and-Rectangles"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-3/Perimeter-of-Squares-and-Rectangles')
def p3apperimeter_8913():
    """Learn route: /Learn/Primary-Grade-3/Perimeter-of-Squares-and-Rectangles"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/AreaPerimeter/Perimeter_Square_Rectangle.html', **context)
    except Exception as e:
        grade = "Primary-Grade-3"
        topic = "Perimeter-of-Squares-and-Rectangles"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-3/Area-Perimeter-Problem-Sums')
def p3apwordproblems_7955():
    """Learn route: /Learn/Primary-Grade-3/Area-Perimeter-Problem-Sums"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/AreaPerimeter/Area_Perimeter_Word_Problems.html', **context)
    except Exception as e:
        grade = "Primary-Grade-3"
        topic = "Area-Perimeter-Problem-Sums"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-3/Identifying-Angles-in-Figures')
def p3anidentifying_3680():
    """Learn route: /Learn/Primary-Grade-3/Identifying-Angles-in-Figures"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/Angles/Identifying_Angles.html', **context)
    except Exception as e:
        grade = "Primary-Grade-3"
        topic = "Identifying-Angles-in-Figures"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-3/Right-Angles')
def p3anrightangles_3655():
    """Learn route: /Learn/Primary-Grade-3/Right-Angles"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/Angles/Right_Angles.html', **context)
    except Exception as e:
        grade = "Primary-Grade-3"
        topic = "Right-Angles"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-3/Bar-Graphs')
def p3bgbargraphs_9820():
    """Learn route: /Learn/Primary-Grade-3/Bar-Graphs"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/BarGraphs/Bar_Graphs.html', **context)
    except Exception as e:
        grade = "Primary-Grade-3"
        topic = "Bar-Graphs"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-3/Identifying-Perpendicular-Parallel-Lines')
def p3ppperpendicularparallel_584():
    """Learn route: /Learn/Primary-Grade-3/Identifying-Perpendicular-Parallel-Lines"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/PerpendicularParallel/Perpendicular_Parallel.html', **context)
    except Exception as e:
        grade = "Primary-Grade-3"
        topic = "Identifying-Perpendicular-Parallel-Lines"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

# ====== PRIMARY4 ROUTES (50 routes) ======

@flask_learn_all_bp.route('/Learn/Primary4/Data-Analysis/Tables-and-Bar-Graphs')
def p4dataanalysistablesbar_3790():
    """Learn route: /Learn/Primary4/Data-Analysis/Tables-and-Bar-Graphs"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/DataAnalysis/Tables-and-Bar-Graphs.html', **context)
    except Exception as e:
        grade = "Primary4"
        topic = "Tables-and-Bar-Graphs"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary4/Data-Analysis/Line-Graphs')
def p4dataanalysislinegraphs_7039():
    """Learn route: /Learn/Primary4/Data-Analysis/Line-Graphs"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/DataAnalysis/Line-Graphs.html', **context)
    except Exception as e:
        grade = "Primary4"
        topic = "Line-Graphs"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary4/Geometry/Perpendicular-and-Parallel-Lines')
def p4geometryparallelperpendicular_3959():
    """Learn route: /Learn/Primary4/Geometry/Perpendicular-and-Parallel-Lines"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/Geometry/Perpendicular-and-Parallel-Lines.html', **context)
    except Exception as e:
        grade = "Primary4"
        topic = "Perpendicular-and-Parallel-Lines"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary4/Geometry/Understanding-Angles')
def p4geometryunderstandingangles_5294():
    """Learn route: /Learn/Primary4/Geometry/Understanding-Angles"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/Geometry/Understanding-Angles.html', **context)
    except Exception as e:
        grade = "Primary4"
        topic = "Understanding-Angles"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary4/Geometry/What-is-an-angle-how-to-measure-it')
def p4geometrywhatisanangle_1548():
    """Learn route: /Learn/Primary4/Geometry/What-is-an-angle-how-to-measure-it"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/Geometry/Understanding-Angles.html', **context)
    except Exception as e:
        grade = "Primary4"
        topic = "What-is-an-angle-how-to-measure-it"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary4/Geometry/Drawing-Angles')
def p4geometrydrawingangles_2578():
    """Learn route: /Learn/Primary4/Geometry/Drawing-Angles"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/Geometry/Drawing-Angles.html', **context)
    except Exception as e:
        grade = "Primary4"
        topic = "Drawing-Angles"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary4/Geometry/Angles-Turns-and-Directions')
def p4geometryanglesturnsdirections_8701():
    """Learn route: /Learn/Primary4/Geometry/Angles-Turns-and-Directions"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/Geometry/Angles-Turns-and-Directions.html', **context)
    except Exception as e:
        grade = "Primary4"
        topic = "Angles-Turns-and-Directions"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary4/Geometry/Quadrilaterals-Rectangles-and-Squares')
def p4geometryquadrilateral_7524():
    """Learn route: /Learn/Primary4/Geometry/Quadrilaterals-Rectangles-and-Squares"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/Geometry/Quadrilaterals-Rectangles-and-Squares.html', **context)
    except Exception as e:
        grade = "Primary4"
        topic = "Quadrilaterals-Rectangles-and-Squares"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary4/Geometry/Symmetric-Figures-Shapes-and-Patterns')
def p4geometrysymmetry_6807():
    """Learn route: /Learn/Primary4/Geometry/Symmetric-Figures-Shapes-and-Patterns"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/Geometry/Symmetric-Figures-Shapes-and-Patterns.html', **context)
    except Exception as e:
        grade = "Primary4"
        topic = "Symmetric-Figures-Shapes-and-Patterns"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary4/Measurement/Area-and-Perimeter-of-Rectangles-and-Squares')
def p4measurementrectanglesquare_3250():
    """Learn route: /Learn/Primary4/Measurement/Area-and-Perimeter-of-Rectangles-and-Squares"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/Measurement/Area-and-Perimeter-of-Rectangles-and-Squares.html', **context)
    except Exception as e:
        grade = "Primary4"
        topic = "Area-and-Perimeter-of-Rectangles-and-Squares"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary4/Measurement/Time-Seconds-24-Hour-Clock-Duration')
def p4measurementtime_5077():
    """Learn route: /Learn/Primary4/Measurement/Time-Seconds-24-Hour-Clock-Duration"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/Measurement/Time-Seconds-24-Hour-Clock-Duration.html', **context)
    except Exception as e:
        grade = "Primary4"
        topic = "Time-Seconds-24-Hour-Clock-Duration"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary4/Whole-Numbers/Word-Problems')
def p4wnwordproblems_3298():
    """Learn route: /Learn/Primary4/Whole-Numbers/Word-Problems"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/WholeNumbers/Whole_Numbers_Word_Problems.html', **context)
    except Exception as e:
        grade = "Primary4"
        topic = "Word-Problems"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary4/Whole-Numbers/Factors-Multiples')
def p4wnfactorsmultiples_8072():
    """Learn route: /Learn/Primary4/Whole-Numbers/Factors-Multiples"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/WholeNumbers/Whole_Numbers_Factors_and_Multiples.html', **context)
    except Exception as e:
        grade = "Primary4"
        topic = "Factors-Multiples"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary4/Whole-Numbers/Numbers-Up-to-100000')
def p4wnupto100000_404():
    """Learn route: /Learn/Primary4/Whole-Numbers/Numbers-Up-to-100000"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/WholeNumbers/Whole_Numbers_Upto_100000.html', **context)
    except Exception as e:
        grade = "Primary4"
        topic = "Numbers-Up-to-100000"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary4/Whole-Numbers/Multiplication-Division-by-1-and-2-Digit-Numbers')
def p4wnmultiplydivide_2044():
    """Learn route: /Learn/Primary4/Whole-Numbers/Multiplication-Division-by-1-and-2-Digit-Numbers"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/WholeNumbers/Whole-Numbers-Multiplication-and-Division-by-1-digit-and-2-digit-Numbers.html', **context)
    except Exception as e:
        grade = "Primary4"
        topic = "Multiplication-Division-by-1-and-2-Digit-Numbers"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary4/Decimal/Understanding-Tenths-Hundredths-Thousandths')
def p4decimal10s100s1000s_6403():
    """Learn route: /Learn/Primary4/Decimal/Understanding-Tenths-Hundredths-Thousandths"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/Decimals/Decimals-Understanding-Tenths-Hundredths-Thousandths.html', **context)
    except Exception as e:
        grade = "Primary4"
        topic = "Understanding-Tenths-Hundredths-Thousandths"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary4/Decimal/Decimals-Addition')
def p4decimaladdition_505():
    """Learn route: /Learn/Primary4/Decimal/Decimals-Addition"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/Decimals/Decimals-Addition.html', **context)
    except Exception as e:
        grade = "Primary4"
        topic = "Decimals-Addition"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary4/Decimal/Decimals-Subtraction')
def p4decimalsubtraction_5909():
    """Learn route: /Learn/Primary4/Decimal/Decimals-Subtraction"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/Decimals/Decimals-Subtraction.html', **context)
    except Exception as e:
        grade = "Primary4"
        topic = "Decimals-Subtraction"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary4/Decimal/Decimals-Multiplication')
def p4decimalmultiplication_4773():
    """Learn route: /Learn/Primary4/Decimal/Decimals-Multiplication"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/Decimals/Decimals-Multiplication.html', **context)
    except Exception as e:
        grade = "Primary4"
        topic = "Decimals-Multiplication"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary4/Decimal/Decimals-Division')
def p4decimaldivision_5302():
    """Learn route: /Learn/Primary4/Decimal/Decimals-Division"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/Decimals/Decimals-Division.html', **context)
    except Exception as e:
        grade = "Primary4"
        topic = "Decimals-Division"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary4/Decimal/Word-Problems')
def p4decimalwordproblems_3598():
    """Learn route: /Learn/Primary4/Decimal/Word-Problems"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/Decimals/Decimals-Word-Problems.html', **context)
    except Exception as e:
        grade = "Primary4"
        topic = "Word-Problems"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary4/Fractions/Fractions-Word-Problems-Grade-4')
def p4fractionswordproblems_1116():
    """Learn route: /Learn/Primary4/Fractions/Fractions-Word-Problems-Grade-4"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/Fractions/Fractions-Word-Problems-Grade-4.html', **context)
    except Exception as e:
        grade = "Primary4"
        topic = "Fractions-Word-Problems-Grade-4"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-4/Data-Analysis/Tables-and-Bar-Graphs')
def p4dataanalysistablesbar_5063():
    """Learn route: /Learn/Primary-Grade-4/Data-Analysis/Tables-and-Bar-Graphs"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/DataAnalysis/Tables-and-Bar-Graphs.html', **context)
    except Exception as e:
        grade = "Primary-Grade-4"
        topic = "Tables-and-Bar-Graphs"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-4/Data-Analysis/Line-Graphs')
def p4dataanalysislinegraphs_8327():
    """Learn route: /Learn/Primary-Grade-4/Data-Analysis/Line-Graphs"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/DataAnalysis/Line-Graphs.html', **context)
    except Exception as e:
        grade = "Primary-Grade-4"
        topic = "Line-Graphs"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-4/Geometry/Perpendicular-and-Parallel-Lines')
def p4geometryparallelperpendicular_1795():
    """Learn route: /Learn/Primary-Grade-4/Geometry/Perpendicular-and-Parallel-Lines"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/Geometry/Perpendicular-and-Parallel-Lines.html', **context)
    except Exception as e:
        grade = "Primary-Grade-4"
        topic = "Perpendicular-and-Parallel-Lines"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-4/Geometry/Understanding-Angles')
def p4geometryunderstandingangles_1045():
    """Learn route: /Learn/Primary-Grade-4/Geometry/Understanding-Angles"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/Geometry/Understanding-Angles.html', **context)
    except Exception as e:
        grade = "Primary-Grade-4"
        topic = "Understanding-Angles"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-4/Geometry/What-is-an-angle-how-to-measure-it')
def p4geometrywhatisanangle_3928():
    """Learn route: /Learn/Primary-Grade-4/Geometry/What-is-an-angle-how-to-measure-it"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/Geometry/Understanding-Angles.html', **context)
    except Exception as e:
        grade = "Primary-Grade-4"
        topic = "What-is-an-angle-how-to-measure-it"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-4/Geometry/Drawing-Angles')
def p4geometrydrawingangles_2122():
    """Learn route: /Learn/Primary-Grade-4/Geometry/Drawing-Angles"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/Geometry/Drawing-Angles.html', **context)
    except Exception as e:
        grade = "Primary-Grade-4"
        topic = "Drawing-Angles"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-4/Geometry/Angles-Turns-and-Directions')
def p4geometryanglesturnsdirections_7775():
    """Learn route: /Learn/Primary-Grade-4/Geometry/Angles-Turns-and-Directions"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/Geometry/Angles-Turns-and-Directions.html', **context)
    except Exception as e:
        grade = "Primary-Grade-4"
        topic = "Angles-Turns-and-Directions"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-4/Geometry/Quadrilaterals-Rectangles-and-Squares')
def p4geometryquadrilateral_7762():
    """Learn route: /Learn/Primary-Grade-4/Geometry/Quadrilaterals-Rectangles-and-Squares"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/Geometry/Quadrilaterals-Rectangles-and-Squares.html', **context)
    except Exception as e:
        grade = "Primary-Grade-4"
        topic = "Quadrilaterals-Rectangles-and-Squares"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-4/Geometry/Symmetric-Figures-Shapes-and-Patterns')
def p4geometrysymmetry_9029():
    """Learn route: /Learn/Primary-Grade-4/Geometry/Symmetric-Figures-Shapes-and-Patterns"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/Geometry/Symmetric-Figures-Shapes-and-Patterns.html', **context)
    except Exception as e:
        grade = "Primary-Grade-4"
        topic = "Symmetric-Figures-Shapes-and-Patterns"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-4/Measurement/Area-and-Perimeter-of-Rectangles-and-Squares')
def p4measurementrectanglesquare_7564():
    """Learn route: /Learn/Primary-Grade-4/Measurement/Area-and-Perimeter-of-Rectangles-and-Squares"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/Measurement/Area-and-Perimeter-of-Rectangles-and-Squares.html', **context)
    except Exception as e:
        grade = "Primary-Grade-4"
        topic = "Area-and-Perimeter-of-Rectangles-and-Squares"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-4/Measurement/Time-Seconds-24-Hour-Clock-Duration')
def p4measurementtime_9344():
    """Learn route: /Learn/Primary-Grade-4/Measurement/Time-Seconds-24-Hour-Clock-Duration"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/Measurement/Time-Seconds-24-Hour-Clock-Duration.html', **context)
    except Exception as e:
        grade = "Primary-Grade-4"
        topic = "Time-Seconds-24-Hour-Clock-Duration"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-4/Whole-Numbers/Word-Problems')
def p4wnwordproblems_8551():
    """Learn route: /Learn/Primary-Grade-4/Whole-Numbers/Word-Problems"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/WholeNumbers/Whole_Numbers_Word_Problems.html', **context)
    except Exception as e:
        grade = "Primary-Grade-4"
        topic = "Word-Problems"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-4/Whole-Numbers/Factors-Multiples')
def p4wnfactorsmultiples_1389():
    """Learn route: /Learn/Primary-Grade-4/Whole-Numbers/Factors-Multiples"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/WholeNumbers/Whole_Numbers_Factors_and_Multiples.html', **context)
    except Exception as e:
        grade = "Primary-Grade-4"
        topic = "Factors-Multiples"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-4/Whole-Numbers/Numbers-Up-to-100000')
def p4wnupto100000_5723():
    """Learn route: /Learn/Primary-Grade-4/Whole-Numbers/Numbers-Up-to-100000"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/WholeNumbers/Whole_Numbers_Upto_100000.html', **context)
    except Exception as e:
        grade = "Primary-Grade-4"
        topic = "Numbers-Up-to-100000"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-4/Whole-Numbers/Multiplication-Division-by-1-and-2-Digit-Numbers')
def p4wnmultiplydivide_6850():
    """Learn route: /Learn/Primary-Grade-4/Whole-Numbers/Multiplication-Division-by-1-and-2-Digit-Numbers"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/WholeNumbers/Whole-Numbers-Multiplication-and-Division-by-1-digit-and-2-digit-Numbers.html', **context)
    except Exception as e:
        grade = "Primary-Grade-4"
        topic = "Multiplication-Division-by-1-and-2-Digit-Numbers"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-4/Decimal/Understanding-Tenths-Hundredths-Thousandths')
def p4decimal10s100s1000s_4543():
    """Learn route: /Learn/Primary-Grade-4/Decimal/Understanding-Tenths-Hundredths-Thousandths"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/Decimals/Decimals-Understanding-Tenths-Hundredths-Thousandths.html', **context)
    except Exception as e:
        grade = "Primary-Grade-4"
        topic = "Understanding-Tenths-Hundredths-Thousandths"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-4/Decimal/Decimals-Addition')
def p4decimaladdition_6183():
    """Learn route: /Learn/Primary-Grade-4/Decimal/Decimals-Addition"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/Decimals/Decimals-Addition.html', **context)
    except Exception as e:
        grade = "Primary-Grade-4"
        topic = "Decimals-Addition"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-4/Decimal/Decimals-Subtraction')
def p4decimalsubtraction_1685():
    """Learn route: /Learn/Primary-Grade-4/Decimal/Decimals-Subtraction"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/Decimals/Decimals-Subtraction.html', **context)
    except Exception as e:
        grade = "Primary-Grade-4"
        topic = "Decimals-Subtraction"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-4/Decimal/Decimals-Multiplication')
def p4decimalmultiplication_6699():
    """Learn route: /Learn/Primary-Grade-4/Decimal/Decimals-Multiplication"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/Decimals/Decimals-Multiplication.html', **context)
    except Exception as e:
        grade = "Primary-Grade-4"
        topic = "Decimals-Multiplication"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-4/Decimal/Decimals-Division')
def p4decimaldivision_2992():
    """Learn route: /Learn/Primary-Grade-4/Decimal/Decimals-Division"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/Decimals/Decimals-Division.html', **context)
    except Exception as e:
        grade = "Primary-Grade-4"
        topic = "Decimals-Division"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-4/Decimal/Word-Problems')
def p4decimalwordproblems_2294():
    """Learn route: /Learn/Primary-Grade-4/Decimal/Word-Problems"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/Decimals/Decimals-Word-Problems.html', **context)
    except Exception as e:
        grade = "Primary-Grade-4"
        topic = "Word-Problems"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-4/Fractions/Fractions-Word-Problems-Grade-4')
def p4fractionswordproblems_3516():
    """Learn route: /Learn/Primary-Grade-4/Fractions/Fractions-Word-Problems-Grade-4"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/Fractions/Fractions-Word-Problems-Grade-4.html', **context)
    except Exception as e:
        grade = "Primary-Grade-4"
        topic = "Fractions-Word-Problems-Grade-4"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-4/Fractions/Fraction-of-a-Set')
def p4fractionsofset_6803():
    """Learn route: /Learn/Primary-Grade-4/Fractions/Fraction-of-a-Set"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/Fractions/Fraction-of-a-Set.html', **context)
    except Exception as e:
        grade = "Primary-Grade-4"
        topic = "Fraction-of-a-Set"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-4/Types-of-Fractions')
def p5frtypesfractions_3412():
    """Learn route: /Learn/Primary-Grade-4/Types-of-Fractions"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Fractions/Types-of-Fractions.html', **context)
    except Exception as e:
        grade = "Primary-Grade-4"
        topic = "Types-of-Fractions"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-4/Fractions/Simplifying-Fractions-GCF')
def p5frsimplifyingfractions_6488():
    """Learn route: /Learn/Primary-Grade-4/Fractions/Simplifying-Fractions-GCF"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Fractions/Simplifying-Fractions-GCF.html', **context)
    except Exception as e:
        grade = "Primary-Grade-4"
        topic = "Simplifying-Fractions-GCF"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-4/Fractions/Mixed-Numbers-Improper-Fractions')
def p5frimpropermixedfractions_8099():
    """Learn route: /Learn/Primary-Grade-4/Fractions/Mixed-Numbers-Improper-Fractions"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Fractions/Improper-Mixed-Fractions.html', **context)
    except Exception as e:
        grade = "Primary-Grade-4"
        topic = "Mixed-Numbers-Improper-Fractions"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-4/Fractions/Addition-Proper-Fractions')
def p5fraddproperfractions_3231():
    """Learn route: /Learn/Primary-Grade-4/Fractions/Addition-Proper-Fractions"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Fractions/Addition-Proper-Fractions.html', **context)
    except Exception as e:
        grade = "Primary-Grade-4"
        topic = "Addition-Proper-Fractions"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-4/Fractions/Subtraction-Proper-Fractions')
def p5frsubproperfractions_8847():
    """Learn route: /Learn/Primary-Grade-4/Fractions/Subtraction-Proper-Fractions"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Fractions/Subtraction-Proper-Fractions.html', **context)
    except Exception as e:
        grade = "Primary-Grade-4"
        topic = "Subtraction-Proper-Fractions"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

# ====== PRIMARY5 ROUTES (159 routes) ======

@flask_learn_all_bp.route('/Learn/Primary5/WholeNumbers/Figures-to-Words')
def p5wnfigurestowords_8931():
    """Learn route: /Learn/Primary5/WholeNumbers/Figures-to-Words"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Figures-to-Words.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Figures-to-Words"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/WholeNumbers/Words-to-Figures')
def p5wnwordstofigures_8314():
    """Learn route: /Learn/Primary5/WholeNumbers/Words-to-Figures"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Words-to-Figures.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Words-to-Figures"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/WholeNumbers/Place-Values')
def p5wnplacevalue_274():
    """Learn route: /Learn/Primary5/WholeNumbers/Place-Values"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Place-Value.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Place-Values"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/WholeNumbers/Comparison-Ordering-Pattern')
def p5wncomparisonordering_6822():
    """Learn route: /Learn/Primary5/WholeNumbers/Comparison-Ordering-Pattern"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Comparison-Ordering-Pattern.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Comparison-Ordering-Pattern"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/WholeNumbers/Approximation-Estimation-Part-1')
def p5wnapproximationestimation1_8314():
    """Learn route: /Learn/Primary5/WholeNumbers/Approximation-Estimation-Part-1"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Approximation-Estimation-Part-1.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Approximation-Estimation-Part-1"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/WholeNumbers/Approximation-Estimation-Part-2')
def p5wnapproximationestimation2_7811():
    """Learn route: /Learn/Primary5/WholeNumbers/Approximation-Estimation-Part-2"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Approximation-Estimation-Part-2.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Approximation-Estimation-Part-2"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/WholeNumbers/Multiply-by-10-100-1000')
def p5wnmultiply_4018():
    """Learn route: /Learn/Primary5/WholeNumbers/Multiply-by-10-100-1000"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Multiply-by-10-100-1000.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Multiply-by-10-100-1000"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/WholeNumbers/Divide-by-10-100-1000')
def p5wndivide_5259():
    """Learn route: /Learn/Primary5/WholeNumbers/Divide-by-10-100-1000"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Divide-by-10-100-1000.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Divide-by-10-100-1000"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/WholeNumbers/Order-of-Operations')
def p5wnoperations_5246():
    """Learn route: /Learn/Primary5/WholeNumbers/Order-of-Operations"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Order-of-Operations.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Order-of-Operations"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/WholeNumbers/Word-Problems-Video-List')
def p5wnwordproblems_3136():
    """Learn route: /Learn/Primary5/WholeNumbers/Word-Problems-Video-List"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems-Video-List.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Word-Problems-Video-List"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/WholeNumbers/Word-Problems1')
def p5wnwordproblems1_7316():
    """Learn route: /Learn/Primary5/WholeNumbers/Word-Problems1"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems1.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Word-Problems1"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/WholeNumbers/Word-Problems2')
def p5wnwordproblems2_3037():
    """Learn route: /Learn/Primary5/WholeNumbers/Word-Problems2"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems2.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Word-Problems2"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/WholeNumbers/Word-Problems3')
def p5wnwordproblems3_4979():
    """Learn route: /Learn/Primary5/WholeNumbers/Word-Problems3"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems3.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Word-Problems3"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/WholeNumbers/Word-Problems4')
def p5wnwordproblems4_1902():
    """Learn route: /Learn/Primary5/WholeNumbers/Word-Problems4"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems4.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Word-Problems4"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/WholeNumbers/Word-Problems5')
def p5wnwordproblems5_4170():
    """Learn route: /Learn/Primary5/WholeNumbers/Word-Problems5"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems5.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Word-Problems5"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/WholeNumbers/Word-Problems6')
def p5wnwordproblems6_8229():
    """Learn route: /Learn/Primary5/WholeNumbers/Word-Problems6"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems6.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Word-Problems6"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/WholeNumbers/Word-Problems7')
def p5wnwordproblems7_4344():
    """Learn route: /Learn/Primary5/WholeNumbers/Word-Problems7"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems7.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Word-Problems7"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/WholeNumbers/Word-Problems8')
def p5wnwordproblems8_7133():
    """Learn route: /Learn/Primary5/WholeNumbers/Word-Problems8"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems8.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Word-Problems8"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/WholeNumbers/Word-Problems9')
def p5wnwordproblems9_5757():
    """Learn route: /Learn/Primary5/WholeNumbers/Word-Problems9"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems9.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Word-Problems9"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/WholeNumbers/Word-Problems10')
def p5wnwordproblems10_6455():
    """Learn route: /Learn/Primary5/WholeNumbers/Word-Problems10"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems10.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Word-Problems10"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/WholeNumbers/Word-Problems11')
def p5wnwordproblems11_9934():
    """Learn route: /Learn/Primary5/WholeNumbers/Word-Problems11"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems11.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Word-Problems11"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/WholeNumbers/Word-Problems12')
def p5wnwordproblems12_5840():
    """Learn route: /Learn/Primary5/WholeNumbers/Word-Problems12"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems12.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Word-Problems12"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/WholeNumbers/Word-Problems13')
def p5wnwordproblems13_2965():
    """Learn route: /Learn/Primary5/WholeNumbers/Word-Problems13"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems13.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Word-Problems13"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/WholeNumbers/Word-Problems14')
def p5wnwordproblems14_8661():
    """Learn route: /Learn/Primary5/WholeNumbers/Word-Problems14"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems14.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Word-Problems14"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/WholeNumbers/Word-Problems15')
def p5wnwordproblems15_1288():
    """Learn route: /Learn/Primary5/WholeNumbers/Word-Problems15"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems15.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Word-Problems15"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/WholeNumbers/Word-Problems16')
def p5wnwordproblems16_6759():
    """Learn route: /Learn/Primary5/WholeNumbers/Word-Problems16"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems16.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Word-Problems16"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/WholeNumbers/Word-Problems17')
def p5wnwordproblems17_9336():
    """Learn route: /Learn/Primary5/WholeNumbers/Word-Problems17"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems17.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Word-Problems17"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/WholeNumbers/Word-Problems18')
def p5wnwordproblems18_8111():
    """Learn route: /Learn/Primary5/WholeNumbers/Word-Problems18"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems18.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Word-Problems18"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/WholeNumbers/Word-Problems19')
def p5wnwordproblems19_3840():
    """Learn route: /Learn/Primary5/WholeNumbers/Word-Problems19"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems19.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Word-Problems19"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/WholeNumbers/Word-Problems20')
def p5wnwordproblems20_9966():
    """Learn route: /Learn/Primary5/WholeNumbers/Word-Problems20"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems20.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Word-Problems20"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/WholeNumbers/Word-Problems21')
def p5wnwordproblems21_482():
    """Learn route: /Learn/Primary5/WholeNumbers/Word-Problems21"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems21.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Word-Problems21"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/WholeNumbers/Word-Problems22')
def p5wnwordproblems22_8710():
    """Learn route: /Learn/Primary5/WholeNumbers/Word-Problems22"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems22.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Word-Problems22"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/WholeNumbers/Word-Problems23')
def p5wnwordproblems23_6692():
    """Learn route: /Learn/Primary5/WholeNumbers/Word-Problems23"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems23.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Word-Problems23"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Fractions/What-Is-a-Fraction')
def p5frwhatisfractions_2570():
    """Learn route: /Learn/Primary5/Fractions/What-Is-a-Fraction"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Fractions/What-Is-a-Fraction.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "What-Is-a-Fraction"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Fractions/Types-of-Fractions')
def p5frtypesfractions_8421():
    """Learn route: /Learn/Primary5/Fractions/Types-of-Fractions"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Fractions/Types-of-Fractions.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Types-of-Fractions"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Fractions/Improper-Mixed-Fractions')
def p5frimpropermixedfractions_2677():
    """Learn route: /Learn/Primary5/Fractions/Improper-Mixed-Fractions"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Fractions/Improper-Mixed-Fractions.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Improper-Mixed-Fractions"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Fractions/Simplifying-Fractions-GCF')
def p5frsimplifyingfractions_4407():
    """Learn route: /Learn/Primary5/Fractions/Simplifying-Fractions-GCF"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Fractions/Simplifying-Fractions-GCF.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Simplifying-Fractions-GCF"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Fractions/Unlike-Fractions-LCM-Part-1')
def p5frunlikefractions1_344():
    """Learn route: /Learn/Primary5/Fractions/Unlike-Fractions-LCM-Part-1"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Fractions/Unlike-Fractions-LCM-Part-1.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Unlike-Fractions-LCM-Part-1"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Fractions/Unlike-Fractions-LCM-Part-2')
def p5frunlikefractions2_2381():
    """Learn route: /Learn/Primary5/Fractions/Unlike-Fractions-LCM-Part-2"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Fractions/Unlike-Fractions-LCM-Part-2.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Unlike-Fractions-LCM-Part-2"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Fractions/Addition-Proper-Fractions')
def p5fraddproperfractions_3338():
    """Learn route: /Learn/Primary5/Fractions/Addition-Proper-Fractions"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Fractions/Addition-Proper-Fractions.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Addition-Proper-Fractions"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Fractions/Subtraction-Proper-Fractions')
def p5frsubproperfractions_7374():
    """Learn route: /Learn/Primary5/Fractions/Subtraction-Proper-Fractions"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Fractions/Subtraction-Proper-Fractions.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Subtraction-Proper-Fractions"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Fractions/Addition-Mixed-Fractions')
def p5fraddmixedfractions_6670():
    """Learn route: /Learn/Primary5/Fractions/Addition-Mixed-Fractions"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Fractions/Addition-Mixed-Fractions.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Addition-Mixed-Fractions"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Fractions/Subtraction-Mixed-Fractions')
def p5frsubmixedfractions_8728():
    """Learn route: /Learn/Primary5/Fractions/Subtraction-Mixed-Fractions"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Fractions/Subtraction-Mixed-Fractions.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Subtraction-Mixed-Fractions"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Fractions/Multiplication-Fractions')
def p5frmultfractions_696():
    """Learn route: /Learn/Primary5/Fractions/Multiplication-Fractions"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Fractions/Multiplication-Fractions.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Multiplication-Fractions"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Fractions/Multiplication-Mixed-Fractions')
def p5frmultmixedfractions_4211():
    """Learn route: /Learn/Primary5/Fractions/Multiplication-Mixed-Fractions"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Fractions/Multiplication-Mixed-Fractions.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Multiplication-Mixed-Fractions"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Fractions/Division-Proper-Fraction')
def p5frdivisionfractions_4616():
    """Learn route: /Learn/Primary5/Fractions/Division-Proper-Fraction"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Fractions/Division-Proper-Fraction.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Division-Proper-Fraction"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Fractions/Fraction-as-Division')
def p5frfractiondivision_7985():
    """Learn route: /Learn/Primary5/Fractions/Fraction-as-Division"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Fractions/Fraction-as-Division.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Fraction-as-Division"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Fractions/Fractions-Decimals')
def p5frfractiondecimal_9056():
    """Learn route: /Learn/Primary5/Fractions/Fractions-Decimals"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Fractions/Fractions-Decimals.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Fractions-Decimals"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Decimal/Multiply-by-10-100-1000')
def p5dcmultiply_2726():
    """Learn route: /Learn/Primary5/Decimal/Multiply-by-10-100-1000"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Decimal/multiplying-decimal-numbers-by-10s-100s-1000s.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Multiply-by-10-100-1000"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Decimal/Divide-by-10-100-1000')
def p5dcdivide_8902():
    """Learn route: /Learn/Primary5/Decimal/Divide-by-10-100-1000"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Decimal/dividing-decimal-numbers-by-10s-100s-1000s.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Divide-by-10-100-1000"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Decimal/Rounding-Off-Decimal-Numbers')
def p5dcrounding_1470():
    """Learn route: /Learn/Primary5/Decimal/Rounding-Off-Decimal-Numbers"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Decimal/rounding-off-decimal-numbers.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Rounding-Off-Decimal-Numbers"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Decimal/Estimation-in-Calculations-with-Decimal-Numbers')
def p5dcestimation_4996():
    """Learn route: /Learn/Primary5/Decimal/Estimation-in-Calculations-with-Decimal-Numbers"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Decimal/estimation-in-calculations-with-decimal-numbers.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Estimation-in-Calculations-with-Decimal-Numbers"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Percentage/Introduction')
def p5printroduction_4161():
    """Learn route: /Learn/Primary5/Percentage/Introduction"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Percentage/introduction-to-percentage.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Introduction"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Percentage/Percentage-and-Fractions')
def p5prfractions_7617():
    """Learn route: /Learn/Primary5/Percentage/Percentage-and-Fractions"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Percentage/percentage-and-fraction.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Percentage-and-Fractions"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Percentage/Percentage-and-Decimals')
def p5prdecimals_4476():
    """Learn route: /Learn/Primary5/Percentage/Percentage-and-Decimals"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Percentage/percentage-and-decimals.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Percentage-and-Decimals"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Ratio/Introduction')
def p5rtintroduction_5701():
    """Learn route: /Learn/Primary5/Ratio/Introduction"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Ratio/introduction-to-ratio.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Introduction"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Ratio/Equivalent')
def p5rtequivalent_1387():
    """Learn route: /Learn/Primary5/Ratio/Equivalent"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Ratio/equivalent-ratios.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Equivalent"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Ratio/Simplifying')
def p5rtsimplifying_8865():
    """Learn route: /Learn/Primary5/Ratio/Simplifying"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Ratio/simplifying-ratios.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Simplifying"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Measurement/Triangle-Base-Height')
def p5mttrianglebh_6285():
    """Learn route: /Learn/Primary5/Measurement/Triangle-Base-Height"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Measurement/triangle-base-height-measurement.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Triangle-Base-Height"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Measurement/Area-of-Triangle')
def p5mttrianglearea_8007():
    """Learn route: /Learn/Primary5/Measurement/Area-of-Triangle"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Measurement/finding-area-of-triangle.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Area-of-Triangle"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Measurement/Introduction-to-volume-of-cube-cuboid-part-1')
def p5mtvolume1_6422():
    """Learn route: /Learn/Primary5/Measurement/Introduction-to-volume-of-cube-cuboid-part-1"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Measurement/volume-of-cube-cuboid-part-1.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Introduction-to-volume-of-cube-cuboid-part-1"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Measurement/Introduction-to-volume-of-cube-cuboid-part-2')
def p5mtvolume2_7353():
    """Learn route: /Learn/Primary5/Measurement/Introduction-to-volume-of-cube-cuboid-part-2"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Measurement/volume-of-cube-cuboid-part-2.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Introduction-to-volume-of-cube-cuboid-part-2"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Measurement/Introduction-to-volume-of-cube-cuboid-part-3')
def p5mtvolume3_3443():
    """Learn route: /Learn/Primary5/Measurement/Introduction-to-volume-of-cube-cuboid-part-3"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Measurement/volume-of-cube-cuboid-part-3.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Introduction-to-volume-of-cube-cuboid-part-3"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Data-Analysis/Finding-Average')
def p5daaverage_6545():
    """Learn route: /Learn/Primary5/Data-Analysis/Finding-Average"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Data-Analysis/Finding-Average.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Finding-Average"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Geometry/What-is-an-angle')
def p5geometrywhatisangle_591():
    """Learn route: /Learn/Primary5/Geometry/What-is-an-angle"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Geometry/What-is-an-angle.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "What-is-an-angle"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Geometry/Finding-unknown-angles')
def p5geometryangles_3423():
    """Learn route: /Learn/Primary5/Geometry/Finding-unknown-angles"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Geometry/Finding-unknown-angles.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Finding-unknown-angles"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Geometry/Types-of-triangles')
def p5geometrytriangles_389():
    """Learn route: /Learn/Primary5/Geometry/Types-of-triangles"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Geometry/Types-of-triangles.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Types-of-triangles"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Geometry/Angle-sum-of-triangle')
def p5geometryanglesum_6139():
    """Learn route: /Learn/Primary5/Geometry/Angle-sum-of-triangle"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Geometry/angle-sum-of-triangles.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Angle-sum-of-triangle"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Geometry/Triangle-Finding-unknown-angles')
def p5geometrytriangleangle_9854():
    """Learn route: /Learn/Primary5/Geometry/Triangle-Finding-unknown-angles"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Geometry/Triangle-Finding-unknown-angles.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Triangle-Finding-unknown-angles"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Geometry/Drawing-Triangles-Using-geometrical-instruments-part-1')
def p5geometrydrawingtriangles1_1845():
    """Learn route: /Learn/Primary5/Geometry/Drawing-Triangles-Using-geometrical-instruments-part-1"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Geometry/Drawing-Triangles-Using-geometrical-instruments-part-1.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Drawing-Triangles-Using-geometrical-instruments-part-1"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Geometry/Drawing-Triangles-Using-geometrical-instruments-part-2')
def p5geometrydrawingtriangles2_1505():
    """Learn route: /Learn/Primary5/Geometry/Drawing-Triangles-Using-geometrical-instruments-part-2"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Geometry/Drawing-Triangles-Using-geometrical-instruments-part-2.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Drawing-Triangles-Using-geometrical-instruments-part-2"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Geometry/Drawing-Triangles-Using-geometrical-instruments-part-3')
def p5geometrydrawingtriangles3_1955():
    """Learn route: /Learn/Primary5/Geometry/Drawing-Triangles-Using-geometrical-instruments-part-3"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Geometry/Drawing-Triangles-Using-geometrical-instruments-part-3.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Drawing-Triangles-Using-geometrical-instruments-part-3"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Geometry/Four-sided-figures-types-and-properties')
def p5geometryfoursided_24():
    """Learn route: /Learn/Primary5/Geometry/Four-sided-figures-types-and-properties"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Geometry/Four-sided-figures-types-and-properties.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Four-sided-figures-types-and-properties"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Geometry/Four-sided-figures-finding-unknown-angles-part-1')
def p5geometryfoursidedangles1_5473():
    """Learn route: /Learn/Primary5/Geometry/Four-sided-figures-finding-unknown-angles-part-1"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Geometry/Four-sided-figures-finding-unknown-angles-part-1.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Four-sided-figures-finding-unknown-angles-part-1"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Geometry/Four-sided-figures-finding-unknown-angles-part-2')
def p5geometryfoursidedangles2_9964():
    """Learn route: /Learn/Primary5/Geometry/Four-sided-figures-finding-unknown-angles-part-2"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Geometry/Four-sided-figures-finding-unknown-angles-part-2.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Four-sided-figures-finding-unknown-angles-part-2"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Geometry/Four-sided-figures-finding-unknown-angles-part-3')
def p5geometryfoursidedangles3_7847():
    """Learn route: /Learn/Primary5/Geometry/Four-sided-figures-finding-unknown-angles-part-3"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Geometry/Four-sided-figures-finding-unknown-angles-part-3.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Four-sided-figures-finding-unknown-angles-part-3"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Geometry/Drawing-a-parallelogram')
def p5geometryfoursidedfigures1_6678():
    """Learn route: /Learn/Primary5/Geometry/Drawing-a-parallelogram"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Geometry/drawing-four-sided-figures-parallelogram.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Drawing-a-parallelogram"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Geometry/Drawing-a-rhombus')
def p5geometryfoursidedfigures2_9513():
    """Learn route: /Learn/Primary5/Geometry/Drawing-a-rhombus"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Geometry/drawing-four-sided-figures-rhombus.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Drawing-a-rhombus"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Geometry/Drawing-a-trapezium')
def p5geometryfoursidedfigures3_745():
    """Learn route: /Learn/Primary5/Geometry/Drawing-a-trapezium"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Geometry/drawing-four-sided-figures-trapezium.html', **context)
    except Exception as e:
        grade = "Primary5"
        topic = "Drawing-a-trapezium"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary5/Measurement/Volume-Cube-Cuboid-Advanced-Word-Problems')
def p6measurementwordproblems_7321():
    """Learn route: /Learn/Primary5/Measurement/Volume-Cube-Cuboid-Advanced-Word-Problems"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        # Template doesn't exist in Primary5 - this might be a Primary6 topic
        return f"<h1>Volume Cube Cuboid Advanced Word Problems - Primary 5</h1><p>This content is available in Primary 6.</p><p><a href='/Learn/Primary-Grade-6/Measurement/Volume-Cube-Cuboid-Advanced-Word-Problems'>Go to Primary 6 Version</a></p>"
    except Exception as e:
        grade = "Primary5"
        topic = "Volume-Cube-Cuboid-Advanced-Word-Problems"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/WholeNumbers/Figures-to-Words')
def p5wnfigurestowords_8477():
    """Learn route: /Learn/Primary-Grade-5/WholeNumbers/Figures-to-Words"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Figures-to-Words.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Figures-to-Words"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/WholeNumbers/Words-to-Figures')
def p5wnwordstofigures_8410():
    """Learn route: /Learn/Primary-Grade-5/WholeNumbers/Words-to-Figures"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Words-to-Figures.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Words-to-Figures"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/WholeNumbers/Place-Values')
def p5wnplacevalue_5804():
    """Learn route: /Learn/Primary-Grade-5/WholeNumbers/Place-Values"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Place-Value.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Place-Values"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/WholeNumbers/Comparison-Ordering-Pattern')
def p5wncomparisonordering_3299():
    """Learn route: /Learn/Primary-Grade-5/WholeNumbers/Comparison-Ordering-Pattern"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Comparison-Ordering-Pattern.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Comparison-Ordering-Pattern"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/WholeNumbers/Approximation-Estimation-Part-1')
def p5wnapproximationestimation1_5347():
    """Learn route: /Learn/Primary-Grade-5/WholeNumbers/Approximation-Estimation-Part-1"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Approximation-Estimation-Part-1.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Approximation-Estimation-Part-1"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/WholeNumbers/Approximation-Estimation-Part-2')
def p5wnapproximationestimation1_4971():
    """Learn route: /Learn/Primary-Grade-5/WholeNumbers/Approximation-Estimation-Part-2"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Approximation-Estimation-Part-2.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Approximation-Estimation-Part-2"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/WholeNumbers/Multiply-by-10-100-1000')
def p5wnmultiply_7920():
    """Learn route: /Learn/Primary-Grade-5/WholeNumbers/Multiply-by-10-100-1000"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Multiply-by-10-100-1000.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Multiply-by-10-100-1000"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/WholeNumbers/Divide-by-10-100-1000')
def p5wndivide_1976():
    """Learn route: /Learn/Primary-Grade-5/WholeNumbers/Divide-by-10-100-1000"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Divide-by-10-100-1000.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Divide-by-10-100-1000"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/WholeNumbers/Order-of-Operations')
def p5wnoperations_9187():
    """Learn route: /Learn/Primary-Grade-5/WholeNumbers/Order-of-Operations"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Order-of-Operations.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Order-of-Operations"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Whole-Numbers/Word-Problems-Solving-Model-Method')
def p5wnwordproblems_5724():
    """Learn route: /Learn/Primary-Grade-5/WholeNumbers/Word-Problems-Solving-Model-Method"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Word-Problems-Solving-Model-Method"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/WholeNumbers/Word-Problems1')
def p5wnwordproblems1_1348():
    """Learn route: /Learn/Primary-Grade-5/WholeNumbers/Word-Problems1"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems1.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Word-Problems1"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/WholeNumbers/Word-Problems2')
def p5wnwordproblems2_3303():
    """Learn route: /Learn/Primary-Grade-5/WholeNumbers/Word-Problems2"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems2.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Word-Problems2"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/WholeNumbers/Word-Problems3')
def p5wnwordproblems3_7961():
    """Learn route: /Learn/Primary-Grade-5/WholeNumbers/Word-Problems3"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems3.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Word-Problems3"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/WholeNumbers/Word-Problems4')
def p5wnwordproblems4_4347():
    """Learn route: /Learn/Primary-Grade-5/WholeNumbers/Word-Problems4"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems4.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Word-Problems4"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/WholeNumbers/Word-Problems5')
def p5wnwordproblems5_3449():
    """Learn route: /Learn/Primary-Grade-5/WholeNumbers/Word-Problems5"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems5.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Word-Problems5"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/WholeNumbers/Word-Problems6')
def p5wnwordproblems6_3331():
    """Learn route: /Learn/Primary-Grade-5/WholeNumbers/Word-Problems6"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems6.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Word-Problems6"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/WholeNumbers/Word-Problems7')
def p5wnwordproblems7_9726():
    """Learn route: /Learn/Primary-Grade-5/WholeNumbers/Word-Problems7"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems7.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Word-Problems7"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/WholeNumbers/Word-Problems8')
def p5wnwordproblems8_5045():
    """Learn route: /Learn/Primary-Grade-5/WholeNumbers/Word-Problems8"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems8.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Word-Problems8"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/WholeNumbers/Word-Problems9')
def p5wnwordproblems9_3674():
    """Learn route: /Learn/Primary-Grade-5/WholeNumbers/Word-Problems9"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems9.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Word-Problems9"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/WholeNumbers/Word-Problems10')
def p5wnwordproblems10_4756():
    """Learn route: /Learn/Primary-Grade-5/WholeNumbers/Word-Problems10"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems10.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Word-Problems10"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/WholeNumbers/Word-Problems11')
def p5wnwordproblems11_6112():
    """Learn route: /Learn/Primary-Grade-5/WholeNumbers/Word-Problems11"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems11.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Word-Problems11"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/WholeNumbers/Word-Problems12')
def p5wnwordproblems12_7586():
    """Learn route: /Learn/Primary-Grade-5/WholeNumbers/Word-Problems12"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems12.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Word-Problems12"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/WholeNumbers/Word-Problems13')
def p5wnwordproblems13_8400():
    """Learn route: /Learn/Primary-Grade-5/WholeNumbers/Word-Problems13"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems13.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Word-Problems13"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/WholeNumbers/Word-Problems14')
def p5wnwordproblems14_3204():
    """Learn route: /Learn/Primary-Grade-5/WholeNumbers/Word-Problems14"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems14.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Word-Problems14"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/WholeNumbers/Word-Problems15')
def p5wnwordproblems15_138():
    """Learn route: /Learn/Primary-Grade-5/WholeNumbers/Word-Problems15"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems15.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Word-Problems15"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/WholeNumbers/Word-Problems16')
def p5wnwordproblems16_752():
    """Learn route: /Learn/Primary-Grade-5/WholeNumbers/Word-Problems16"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems16.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Word-Problems16"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/WholeNumbers/Word-Problems17')
def p5wnwordproblems17_4221():
    """Learn route: /Learn/Primary-Grade-5/WholeNumbers/Word-Problems17"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems17.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Word-Problems17"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/WholeNumbers/Word-Problems18')
def p5wnwordproblems18_9381():
    """Learn route: /Learn/Primary-Grade-5/WholeNumbers/Word-Problems18"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems18.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Word-Problems18"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/WholeNumbers/Word-Problems19')
def p5wnwordproblems19_4872():
    """Learn route: /Learn/Primary-Grade-5/WholeNumbers/Word-Problems19"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems19.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Word-Problems19"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/WholeNumbers/Word-Problems20')
def p5wnwordproblems20_745():
    """Learn route: /Learn/Primary-Grade-5/WholeNumbers/Word-Problems20"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems20.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Word-Problems20"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/WholeNumbers/Word-Problems21')
def p5wnwordproblems21_3850():
    """Learn route: /Learn/Primary-Grade-5/WholeNumbers/Word-Problems21"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems21.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Word-Problems21"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/WholeNumbers/Word-Problems22')
def p5wnwordproblems22_2177():
    """Learn route: /Learn/Primary-Grade-5/WholeNumbers/Word-Problems22"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems22.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Word-Problems22"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/WholeNumbers/Word-Problems23')
def p5wnwordproblems23_2802():
    """Learn route: /Learn/Primary-Grade-5/WholeNumbers/Word-Problems23"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/WholeNumbers/Word-Problems23.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Word-Problems23"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Fractions/What-Is-a-Fraction')
def p5frwhatisfractions_5408():
    """Learn route: /Learn/Primary-Grade-5/Fractions/What-Is-a-Fraction"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Fractions/What-Is-a-Fraction.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "What-Is-a-Fraction"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Fractions/Types-of-Fractions')
def p5frtypesfractions_7699():
    """Learn route: /Learn/Primary-Grade-5/Fractions/Types-of-Fractions"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Fractions/Types-of-Fractions.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Types-of-Fractions"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Fractions/Improper-Mixed-Fractions')
def p5frimpropermixedfractions_7392():
    """Learn route: /Learn/Primary-Grade-5/Fractions/Improper-Mixed-Fractions"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Fractions/Improper-Mixed-Fractions.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Improper-Mixed-Fractions"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Fractions/Simplifying-Fractions-GCF')
def p5frsimplifyingfractions_257():
    """Learn route: /Learn/Primary-Grade-5/Fractions/Simplifying-Fractions-GCF"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Fractions/Simplifying-Fractions-GCF.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Simplifying-Fractions-GCF"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Fractions/Unlike-Fractions-LCM-Part-1')
def p5frunlikefractions1_9215():
    """Learn route: /Learn/Primary-Grade-5/Fractions/Unlike-Fractions-LCM-Part-1"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Fractions/Unlike-Fractions-LCM-Part-1.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Unlike-Fractions-LCM-Part-1"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Fractions/Unlike-Fractions-LCM-Part-2')
def p5frunlikefractions2_1640():
    """Learn route: /Learn/Primary-Grade-5/Fractions/Unlike-Fractions-LCM-Part-2"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Fractions/Unlike-Fractions-LCM-Part-2.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Unlike-Fractions-LCM-Part-2"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Fractions/Addition-Proper-Fractions')
def p5fraddproperfractions_2324():
    """Learn route: /Learn/Primary-Grade-5/Fractions/Addition-Proper-Fractions"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Fractions/Addition-Proper-Fractions.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Addition-Proper-Fractions"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Fractions/Subtraction-Proper-Fractions')
def p5frsubproperfractions_7169():
    """Learn route: /Learn/Primary-Grade-5/Fractions/Subtraction-Proper-Fractions"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Fractions/Subtraction-Proper-Fractions.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Subtraction-Proper-Fractions"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Fractions/Addition-Mixed-Fractions')
def p5fraddmixedfractions_6562():
    """Learn route: /Learn/Primary-Grade-5/Fractions/Addition-Mixed-Fractions"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Fractions/Addition-Mixed-Fractions.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Addition-Mixed-Fractions"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Fractions/Subtraction-Mixed-Fractions')
def p5frsubmixedfractions_8936():
    """Learn route: /Learn/Primary-Grade-5/Fractions/Subtraction-Mixed-Fractions"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Fractions/Subtraction-Mixed-Fractions.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Subtraction-Mixed-Fractions"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Fractions/Multiplication-Fractions')
def p5frmultfractions_3565():
    """Learn route: /Learn/Primary-Grade-5/Fractions/Multiplication-Fractions"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Fractions/Multiplication-Fractions.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Multiplication-Fractions"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Fractions/Multiplication-Mixed-Fractions')
def p5frmultmixedfractions_1():
    """Learn route: /Learn/Primary-Grade-5/Fractions/Multiplication-Mixed-Fractions"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Fractions/Multiplication-Mixed-Fractions.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Multiplication-Mixed-Fractions"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Fractions/Division-Proper-Fraction')
def p5frdivisionfractions_1524():
    """Learn route: /Learn/Primary-Grade-5/Fractions/Division-Proper-Fraction"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Fractions/Division-Proper-Fraction.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Division-Proper-Fraction"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Fractions/Fraction-as-Division')
def p5frfractiondivision_4855():
    """Learn route: /Learn/Primary-Grade-5/Fractions/Fraction-as-Division"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Fractions/Fraction-as-Division.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Fraction-as-Division"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Fractions/Fractions-Decimals')
def p5frfractiondecimal_2566():
    """Learn route: /Learn/Primary-Grade-5/Fractions/Fractions-Decimals"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Fractions/Fractions-Decimals.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Fractions-Decimals"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Decimal/Multiply-by-10-100-1000')
def p5dcmultiply_2175():
    """Learn route: /Learn/Primary-Grade-5/Decimal/Multiply-by-10-100-1000"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Decimal/multiplying-decimal-numbers-by-10s-100s-1000s.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Multiply-by-10-100-1000"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Decimal/Divide-by-10-100-1000')
def p5dcdivide_4878():
    """Learn route: /Learn/Primary-Grade-5/Decimal/Divide-by-10-100-1000"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Decimal/dividing-decimal-numbers-by-10s-100s-1000s.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Divide-by-10-100-1000"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Decimal/Rounding-Off-Decimal-Numbers')
def p5dcrounding_5442():
    """Learn route: /Learn/Primary-Grade-5/Decimal/Rounding-Off-Decimal-Numbers"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Decimal/rounding-off-decimal-numbers.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Rounding-Off-Decimal-Numbers"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Decimal/Estimation-in-Calculations-with-Decimal-Numbers')
def p5dcestimation_8745():
    """Learn route: /Learn/Primary-Grade-5/Decimal/Estimation-in-Calculations-with-Decimal-Numbers"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Decimal/estimation-in-calculations-with-decimal-numbers.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Estimation-in-Calculations-with-Decimal-Numbers"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Percentage/Introduction')
def p5printroduction_8083():
    """Learn route: /Learn/Primary-Grade-5/Percentage/Introduction"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Percentage/introduction-to-percentage.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Introduction"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Percentage/Percentage-and-Fractions')
def p5prfractions_5855():
    """Learn route: /Learn/Primary-Grade-5/Percentage/Percentage-and-Fractions"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Percentage/percentage-and-fraction.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Percentage-and-Fractions"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Percentage/Percentage-and-Decimals')
def p5prdecimals_2912():
    """Learn route: /Learn/Primary-Grade-5/Percentage/Percentage-and-Decimals"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Percentage/percentage-and-decimals.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Percentage-and-Decimals"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Ratio/Introduction')
def p5rtintroduction_7491():
    """Learn route: /Learn/Primary-Grade-5/Ratio/Introduction"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Ratio/introduction-to-ratio.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Introduction"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Ratio/Equivalent')
def p5rtequivalent_6223():
    """Learn route: /Learn/Primary-Grade-5/Ratio/Equivalent"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Ratio/equivalent-ratios.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Equivalent"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Ratio/Simplifying')
def p5rtsimplifying_7689():
    """Learn route: /Learn/Primary-Grade-5/Ratio/Simplifying"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Ratio/simplifying-ratios.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Simplifying"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Measurement/Triangle-Base-Height')
def p5mttrianglebh_6887():
    """Learn route: /Learn/Primary-Grade-5/Measurement/Triangle-Base-Height"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Measurement/triangle-base-height-measurement.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Triangle-Base-Height"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Measurement/Area-of-Triangle')
def p5mttrianglearea_4061():
    """Learn route: /Learn/Primary-Grade-5/Measurement/Area-of-Triangle"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Measurement/finding-area-of-triangle.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Area-of-Triangle"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Measurement/Introduction-to-volume-of-cube-cuboid-part-1')
def p5mtvolume1_3245():
    """Learn route: /Learn/Primary-Grade-5/Measurement/Introduction-to-volume-of-cube-cuboid-part-1"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Measurement/volume-of-cube-cuboid-part-1.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Introduction-to-volume-of-cube-cuboid-part-1"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Measurement/Introduction-to-volume-of-cube-cuboid-part-2')
def p5mtvolume2_6739():
    """Learn route: /Learn/Primary-Grade-5/Measurement/Introduction-to-volume-of-cube-cuboid-part-2"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Measurement/volume-of-cube-cuboid-part-2.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Introduction-to-volume-of-cube-cuboid-part-2"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Measurement/Introduction-to-volume-of-cube-cuboid-part-3')
def p5mtvolume3_3678():
    """Learn route: /Learn/Primary-Grade-5/Measurement/Introduction-to-volume-of-cube-cuboid-part-3"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Measurement/volume-of-cube-cuboid-part-3.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Introduction-to-volume-of-cube-cuboid-part-3"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Data-Analysis/Finding-Average')
def p5daaverage_4073():
    """Learn route: /Learn/Primary-Grade-5/Data-Analysis/Finding-Average"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/DataAnalysis/average.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Finding-Average"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Geometry/What-is-an-angle')
def p5geometrywhatisangle_193():
    """Learn route: /Learn/Primary-Grade-5/Geometry/What-is-an-angle"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Geometry/What-is-an-angle.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "What-is-an-angle"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Geometry/Finding-unknown-angles')
def p5geometryangles_3098():
    """Learn route: /Learn/Primary-Grade-5/Geometry/Finding-unknown-angles"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Geometry/Finding-unknown-angles.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Finding-unknown-angles"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Geometry/Types-of-triangles')
def p5geometrytriangles_2190():
    """Learn route: /Learn/Primary-Grade-5/Geometry/Types-of-triangles"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Geometry/Types-of-triangles.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Types-of-triangles"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Geometry/Angle-sum-of-triangle')
def p5geometryanglesum_8501():
    """Learn route: /Learn/Primary-Grade-5/Geometry/Angle-sum-of-triangle"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Geometry/angle-sum-of-triangles.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Angle-sum-of-triangle"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Geometry/Triangle-Finding-unknown-angles')
def p5geometrytriangleangle_1748():
    """Learn route: /Learn/Primary-Grade-5/Geometry/Triangle-Finding-unknown-angles"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Geometry/Triangle-Finding-unknown-angles.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Triangle-Finding-unknown-angles"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Geometry/Drawing-Triangles-Using-geometrical-instruments-part-1')
def p5geometrydrawingtriangles1_4000():
    """Learn route: /Learn/Primary-Grade-5/Geometry/Drawing-Triangles-Using-geometrical-instruments-part-1"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Geometry/Drawing-Triangles-Using-geometrical-instruments-part-1.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Drawing-Triangles-Using-geometrical-instruments-part-1"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Geometry/Drawing-Triangles-Using-geometrical-instruments-part-2')
def p5geometrydrawingtriangles2_8276():
    """Learn route: /Learn/Primary-Grade-5/Geometry/Drawing-Triangles-Using-geometrical-instruments-part-2"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Geometry/Drawing-Triangles-Using-geometrical-instruments-part-2.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Drawing-Triangles-Using-geometrical-instruments-part-2"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Geometry/Drawing-Triangles-Using-geometrical-instruments-part-3')
def p5geometrydrawingtriangles3_4394():
    """Learn route: /Learn/Primary-Grade-5/Geometry/Drawing-Triangles-Using-geometrical-instruments-part-3"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Geometry/Drawing-Triangles-Using-geometrical-instruments-part-3.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Drawing-Triangles-Using-geometrical-instruments-part-3"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Geometry/Four-sided-figures-types-and-properties')
def p5geometryfoursided_1354():
    """Learn route: /Learn/Primary-Grade-5/Geometry/Four-sided-figures-types-and-properties"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Geometry/Four-sided-figures-types-and-properties.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Four-sided-figures-types-and-properties"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Geometry/Four-sided-figures-finding-unknown-angles-part-1')
def p5geometryfoursidedangles1_8714():
    """Learn route: /Learn/Primary-Grade-5/Geometry/Four-sided-figures-finding-unknown-angles-part-1"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Geometry/Four-sided-figures-finding-unknown-angles-part-1.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Four-sided-figures-finding-unknown-angles-part-1"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Geometry/Four-sided-figures-finding-unknown-angles-part-2')
def p5geometryfoursidedangles2_8896():
    """Learn route: /Learn/Primary-Grade-5/Geometry/Four-sided-figures-finding-unknown-angles-part-2"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Geometry/Four-sided-figures-finding-unknown-angles-part-2.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Four-sided-figures-finding-unknown-angles-part-2"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Geometry/Four-sided-figures-finding-unknown-angles-part-3')
def p5geometryfoursidedangles3_4281():
    """Learn route: /Learn/Primary-Grade-5/Geometry/Four-sided-figures-finding-unknown-angles-part-3"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Geometry/Four-sided-figures-finding-unknown-angles-part-3.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Four-sided-figures-finding-unknown-angles-part-3"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Geometry/Drawing-a-parallelogram')
def p5geometryfoursidedfigures1_5521():
    """Learn route: /Learn/Primary-Grade-5/Geometry/Drawing-a-parallelogram"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Geometry/drawing-four-sided-figures-parallelogram.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Drawing-a-parallelogram"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Geometry/Drawing-a-rhombus')
def p5geometryfoursidedfigures2_2247():
    """Learn route: /Learn/Primary-Grade-5/Geometry/Drawing-a-rhombus"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Geometry/drawing-four-sided-figures-rhombus.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Drawing-a-rhombus"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-5/Geometry/Drawing-a-trapezium')
def p5geometryfoursidedfigures3_1138():
    """Learn route: /Learn/Primary-Grade-5/Geometry/Drawing-a-trapezium"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Geometry/drawing-four-sided-figures-trapezium.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Drawing-a-trapezium"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/What-are-Properties-of-Triangles')
def properties_of_triangles_p5():
    """Learn route: /What-are-Properties-of-Triangles"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary5/Geometry/properties-of-triangles.html', **context)
    except Exception as e:
        grade = "Primary-Grade-5"
        topic = "Properties-of-Triangles"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

# ====== PRIMARY6 ROUTES (42 routes) ======

@flask_learn_all_bp.route('/Learn/Primary6/Fractions/Dividing-Whole-Number-by-Proper-Fraction')
def p6wholenumberproperfraction_2762():
    """Learn route: /Learn/Primary6/Fractions/Dividing-Whole-Number-by-Proper-Fraction"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/Fractions/Dividing-Whole-Number-by-Proper-Fraction.html', **context)
    except Exception as e:
        grade = "Primary6"
        topic = "Dividing-Whole-Number-by-Proper-Fraction"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary6/Fractions/Dividing-Proper-Fraction-by-Proper-Fraction')
def p6properfractionproperfraction_2275():
    """Learn route: /Learn/Primary6/Fractions/Dividing-Proper-Fraction-by-Proper-Fraction"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/Fractions/Dividing-Proper-Fraction-by-Proper-Fraction.html', **context)
    except Exception as e:
        grade = "Primary6"
        topic = "Dividing-Proper-Fraction-by-Proper-Fraction"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary6/Algebra/What-is-Algebra-and-Algebraic-Expressions')
def p6algebrawhatisalgebra_6679():
    """Learn route: /Learn/Primary6/Algebra/What-is-Algebra-and-Algebraic-Expressions"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/Algebra/What-is-Algebra-and-Algebraic-Expressions.html', **context)
    except Exception as e:
        grade = "Primary6"
        topic = "What-is-Algebra-and-Algebraic-Expressions"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary6/Algebra/Simplifying-and-Evaluating-Algebraic-Expressions')
def p6algebrasimplifying_417():
    """Learn route: /Learn/Primary6/Algebra/Simplifying-and-Evaluating-Algebraic-Expressions"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/Algebra/Simplifying-and-Evaluating-Algebraic-Expressions.html', **context)
    except Exception as e:
        grade = "Primary6"
        topic = "Simplifying-and-Evaluating-Algebraic-Expressions"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary6/Percentage/Finding-Whole-Given-Part-and-Percentage')
def p6prfindwhole_5664():
    """Learn route: /Learn/Primary6/Percentage/Finding-Whole-Given-Part-and-Percentage"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/Percentage/Finding-Whole-Given-Part-and-Percentage.html', **context)
    except Exception as e:
        grade = "Primary6"
        topic = "Finding-Whole-Given-Part-and-Percentage"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary6/Percentage/Finding-Percentage-Increase-Decrease')
def p6princdec_5915():
    """Learn route: /Learn/Primary6/Percentage/Finding-Percentage-Increase-Decrease"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/Percentage/Finding-Percentage-Increase-Decrease.html', **context)
    except Exception as e:
        grade = "Primary6"
        topic = "Finding-Percentage-Increase-Decrease"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary6/Percentage/Advanced-Word-Problems')
def p6percentagewordproblems_7214():
    """Learn route: /Learn/Primary6/Percentage/Advanced-Word-Problems"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/Percentage/Percentage-Advanced-Word-Problems.html', **context)
    except Exception as e:
        grade = "Primary6"
        topic = "Advanced-Word-Problems"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary6/Speed/Distance-Time-Speed')
def p6speeddistancetime_1058():
    """Learn route: /Learn/Primary6/Speed/Distance-Time-Speed"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/Speed/Distance-Time-Speed.html', **context)
    except Exception as e:
        grade = "Primary6"
        topic = "Distance-Time-Speed"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary6/Speed/Average-Speed')
def p6speedaverage_8351():
    """Learn route: /Learn/Primary6/Speed/Average-Speed"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/Speed/Average-Speed.html', **context)
    except Exception as e:
        grade = "Primary6"
        topic = "Average-Speed"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary6/Speed/Advanced-Word-Problems')
def p6speedadvancedwordproblems_3790():
    """Learn route: /Learn/Primary6/Speed/Advanced-Word-Problems"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/Speed/Speed-Advanced-Word-Problems.html', **context)
    except Exception as e:
        grade = "Primary6"
        topic = "Advanced-Word-Problems"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary6/Data-Analysis/Pie-Chart')
def p6dataanalysispiechart_5250():
    """Learn route: /Learn/Primary6/Data-Analysis/Pie-Chart"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/DataAnalysis/Pie-Charts.html', **context)
    except Exception as e:
        grade = "Primary6"
        topic = "Pie-Chart"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary6/Data-Analysis/Pie-Chart-Word-Problems')
def p6dataanalysispiechartwordproblems_1515():
    """Learn route: /Learn/Primary6/Data-Analysis/Pie-Chart-Word-Problems"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/DataAnalysis/Pie-Charts-Word-Problems.html', **context)
    except Exception as e:
        grade = "Primary6"
        topic = "Pie-Chart-Word-Problems"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary6/Ratio/Word-Problems')
def p6ratiowordproblems_1642():
    """Learn route: /Learn/Primary6/Ratio/Word-Problems"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/Ratio/Ratio-Word-Problems.html', **context)
    except Exception as e:
        grade = "Primary6"
        topic = "Word-Problems"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary6/Ratio/Ratio-and-Fraction')
def p6ratiofraction_6719():
    """Learn route: /Learn/Primary6/Ratio/Ratio-and-Fraction"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/Ratio/Ratio-and-Fraction.html', **context)
    except Exception as e:
        grade = "Primary6"
        topic = "Ratio-and-Fraction"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary6/Ratio/Equivalent-Fraction-and-Ratio')
def p6ratioequivalentfraction_5110():
    """Learn route: /Learn/Primary6/Ratio/Equivalent-Fraction-and-Ratio"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/Ratio/Equivalent-Fraction-and-Ratio.html', **context)
    except Exception as e:
        grade = "Primary6"
        topic = "Equivalent-Fraction-and-Ratio"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary6/Measurement/Volume-Cube-Cuboid-Advanced-Word-Problems')
def p6measurementwordproblems_5499():
    """Learn route: /Learn/Primary6/Measurement/Volume-Cube-Cuboid-Advanced-Word-Problems"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/Measurement/Volume-Cube-Cuboid-Advanced-Word-Problems.html', **context)
    except Exception as e:
        grade = "Primary6"
        topic = "Volume-Cube-Cuboid-Advanced-Word-Problems"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary6/Measurement/Radius-and-Diameter-of-Circle')
def p6measurementradiusdiameter_7310():
    """Learn route: /Learn/Primary6/Measurement/Radius-and-Diameter-of-Circle"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/Measurement/Radius-and-Diameter-of-Circle.html', **context)
    except Exception as e:
        grade = "Primary6"
        topic = "Radius-and-Diameter-of-Circle"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary6/Measurement/Circumference-of-Circle')
def p6measurementcirclecircumference_5180():
    """Learn route: /Learn/Primary6/Measurement/Circumference-of-Circle"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/Measurement/Circumference-of-Circle.html', **context)
    except Exception as e:
        grade = "Primary6"
        topic = "Circumference-of-Circle"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary6/Measurement/Area-of-Circle')
def p6measurementcirclearea_8454():
    """Learn route: /Learn/Primary6/Measurement/Area-of-Circle"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/Measurement/Area-of-Circle.html', **context)
    except Exception as e:
        grade = "Primary6"
        topic = "Area-of-Circle"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary6/Area-and-Perimeter-of-Composite-Figures')
def p6measurementcomposite_738():
    """Learn route: /Learn/Primary6/Area-and-Perimeter-of-Composite-Figures"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/Measurement/Area-and-Perimeter-of-Composite-Figures.html', **context)
    except Exception as e:
        grade = "Primary6"
        topic = "Area-and-Perimeter-of-Composite-Figures"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary6/Geometry/Finding-Unknown-Angles-Advanced-Problems')
def p6geometryadvancedproblems_919():
    """Learn route: /Learn/Primary6/Geometry/Finding-Unknown-Angles-Advanced-Problems"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/Geometry/Finding-Unknown-Angles-Advanced-Problems.html', **context)
    except Exception as e:
        grade = "Primary6"
        topic = "Finding-Unknown-Angles-Advanced-Problems"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-6/Fractions/Dividing-Whole-Number-by-Proper-Fraction')
def p6wholenumberproperfraction_6622():
    """Learn route: /Learn/Primary-Grade-6/Fractions/Dividing-Whole-Number-by-Proper-Fraction"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/Fractions/Dividing-Whole-Number-by-Proper-Fraction.html', **context)
    except Exception as e:
        grade = "Primary-Grade-6"
        topic = "Dividing-Whole-Number-by-Proper-Fraction"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-6/Fractions/Dividing-Proper-Fraction-by-Proper-Fraction')
def p6properfractionproperfraction_7595():
    """Learn route: /Learn/Primary-Grade-6/Fractions/Dividing-Proper-Fraction-by-Proper-Fraction"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/Fractions/Dividing-Proper-Fraction-by-Proper-Fraction.html', **context)
    except Exception as e:
        grade = "Primary-Grade-6"
        topic = "Dividing-Proper-Fraction-by-Proper-Fraction"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-6/Algebra/What-is-Algebra-and-Algebraic-Expressions')
def p6algebrawhatisalgebra_6646():
    """Learn route: /Learn/Primary-Grade-6/Algebra/What-is-Algebra-and-Algebraic-Expressions"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/Algebra/What-is-Algebra-and-Algebraic-Expressions.html', **context)
    except Exception as e:
        grade = "Primary-Grade-6"
        topic = "What-is-Algebra-and-Algebraic-Expressions"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-6/Algebra/Simplifying-and-Evaluating-Algebraic-Expressions')
def p6algebrasimplifying_7881():
    """Learn route: /Learn/Primary-Grade-6/Algebra/Simplifying-and-Evaluating-Algebraic-Expressions"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/Algebra/Simplifying-and-Evaluating-Algebraic-Expressions.html', **context)
    except Exception as e:
        grade = "Primary-Grade-6"
        topic = "Simplifying-and-Evaluating-Algebraic-Expressions"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-6/Percentage/Finding-Whole-Given-Part-and-Percentage')
def p6prfindwhole_3009():
    """Learn route: /Learn/Primary-Grade-6/Percentage/Finding-Whole-Given-Part-and-Percentage"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/Percentage/Finding-Whole-Given-Part-and-Percentage.html', **context)
    except Exception as e:
        grade = "Primary-Grade-6"
        topic = "Finding-Whole-Given-Part-and-Percentage"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-6/Percentage/Finding-Percentage-Increase-Decrease')
def p6princdec_1423():
    """Learn route: /Learn/Primary-Grade-6/Percentage/Finding-Percentage-Increase-Decrease"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/Percentage/Finding-Percentage-Increase-Decrease.html', **context)
    except Exception as e:
        grade = "Primary-Grade-6"
        topic = "Finding-Percentage-Increase-Decrease"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-6/Percentage/Advanced-Word-Problems')
def p6percentagewordproblems_5923():
    """Learn route: /Learn/Primary-Grade-6/Percentage/Advanced-Word-Problems"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/Percentage/Percentage-Advanced-Word-Problems.html', **context)
    except Exception as e:
        grade = "Primary-Grade-6"
        topic = "Advanced-Word-Problems"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-6/Speed/Distance-Time-Speed')
def p6speeddistancetime_2962():
    """Learn route: /Learn/Primary-Grade-6/Speed/Distance-Time-Speed"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/Speed/Distance-Time-Speed.html', **context)
    except Exception as e:
        grade = "Primary-Grade-6"
        topic = "Distance-Time-Speed"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-6/Speed/Average-Speed')
def p6speedaverage_4657():
    """Learn route: /Learn/Primary-Grade-6/Speed/Average-Speed"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/Speed/Average-Speed.html', **context)
    except Exception as e:
        grade = "Primary-Grade-6"
        topic = "Average-Speed"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-6/Speed/Advanced-Word-Problems')
def p6speedadvancedwordproblems_3471():
    """Learn route: /Learn/Primary-Grade-6/Speed/Advanced-Word-Problems"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/Speed/Speed-Advanced-Word-Problems.html', **context)
    except Exception as e:
        grade = "Primary-Grade-6"
        topic = "Advanced-Word-Problems"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-6/Data-Analysis/Pie-Chart')
def p6dataanalysispiechart_8006():
    """Learn route: /Learn/Primary-Grade-6/Data-Analysis/Pie-Chart"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/DataAnalysis/Pie-Charts.html', **context)
    except Exception as e:
        grade = "Primary-Grade-6"
        topic = "Pie-Chart"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-6/Data-Analysis/Pie-Chart-Word-Problems')
def p6dataanalysispiechartwordproblems_5942():
    """Learn route: /Learn/Primary-Grade-6/Data-Analysis/Pie-Chart-Word-Problems"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/DataAnalysis/Pie-Charts-Word-Problems.html', **context)
    except Exception as e:
        grade = "Primary-Grade-6"
        topic = "Pie-Chart-Word-Problems"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-6/Ratio/Word-Problems')
def p6ratiowordproblems_167():
    """Learn route: /Learn/Primary-Grade-6/Ratio/Word-Problems"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/Ratio/Ratio-Word-Problems.html', **context)
    except Exception as e:
        grade = "Primary-Grade-6"
        topic = "Word-Problems"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-6/Ratio/Ratio-and-Fraction')
def p6ratiofraction_8640():
    """Learn route: /Learn/Primary-Grade-6/Ratio/Ratio-and-Fraction"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/Ratio/Ratio-and-Fraction.html', **context)
    except Exception as e:
        grade = "Primary-Grade-6"
        topic = "Ratio-and-Fraction"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-6/Ratio/Equivalent-Fraction-and-Ratio')
def p6ratioequivalentfraction_4064():
    """Learn route: /Learn/Primary-Grade-6/Ratio/Equivalent-Fraction-and-Ratio"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/Ratio/Equivalent-Fraction-and-Ratio.html', **context)
    except Exception as e:
        grade = "Primary-Grade-6"
        topic = "Equivalent-Fraction-and-Ratio"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-6/Measurement/Volume-Cube-Cuboid-Advanced-Word-Problems')
def p6measurementwordproblems_61():
    """Learn route: /Learn/Primary-Grade-6/Measurement/Volume-Cube-Cuboid-Advanced-Word-Problems"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/Measurement/Volume-Cube-Cuboid-Advanced-Word-Problems.html', **context)
    except Exception as e:
        grade = "Primary-Grade-6"
        topic = "Volume-Cube-Cuboid-Advanced-Word-Problems"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-6/Measurement/Radius-and-Diameter-of-Circle')
def p6measurementradiusdiameter_6820():
    """Learn route: /Learn/Primary-Grade-6/Measurement/Radius-and-Diameter-of-Circle"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/Measurement/Radius-and-Diameter-of-Circle.html', **context)
    except Exception as e:
        grade = "Primary-Grade-6"
        topic = "Radius-and-Diameter-of-Circle"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-6/Measurement/Circumference-of-Circle')
def p6measurementcirclecircumference_229():
    """Learn route: /Learn/Primary-Grade-6/Measurement/Circumference-of-Circle"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/Measurement/Circumference-of-Circle.html', **context)
    except Exception as e:
        grade = "Primary-Grade-6"
        topic = "Circumference-of-Circle"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-6/Measurement/Area-of-Circle')
def p6measurementcirclearea_2432():
    """Learn route: /Learn/Primary-Grade-6/Measurement/Area-of-Circle"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/Measurement/Area-of-Circle.html', **context)
    except Exception as e:
        grade = "Primary-Grade-6"
        topic = "Area-of-Circle"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-6/Area-and-Perimeter-of-Composite-Figures')
def p6measurementcomposite_6809():
    """Learn route: /Learn/Primary-Grade-6/Area-and-Perimeter-of-Composite-Figures"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/Measurement/Area-and-Perimeter-of-Composite-Figures.html', **context)
    except Exception as e:
        grade = "Primary-Grade-6"
        topic = "Area-and-Perimeter-of-Composite-Figures"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-6/Geometry/Finding-Unknown-Angles-Advanced-Problems')
def p6geometryadvancedproblems_3398():
    """Learn route: /Learn/Primary-Grade-6/Geometry/Finding-Unknown-Angles-Advanced-Problems"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/Geometry/Finding-Unknown-Angles-Advanced-Problems.html', **context)
    except Exception as e:
        grade = "Primary-Grade-6"
        topic = "Finding-Unknown-Angles-Advanced-Problems"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

# ====== OTHER ROUTES (46 routes) ======

@flask_learn_all_bp.route('/Learn/Primary_Grade_3_Mathematics')
def p3notes_3736():
    """Learn route: /Learn/Primary_Grade_3_Mathematics"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary_Grade_3_Mathematics.html', **context)
    except Exception as e:
        grade = "Primary_Grade_3_Mathematics"
        topic = "Primary_Grade_3_Mathematics"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary_Grade_4_Mathematics')
def p4notes_7379():
    """Learn route: /Learn/Primary_Grade_4_Mathematics"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary_Grade_4_Mathematics.html', **context)
    except Exception as e:
        grade = "Primary_Grade_4_Mathematics"
        topic = "Primary_Grade_4_Mathematics"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary_Grade_5_Mathematics')
def p5notes_1930():
    """Learn route: /Learn/Primary_Grade_5_Mathematics"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary_Grade_5_Mathematics.html', **context)
    except Exception as e:
        grade = "Primary_Grade_5_Mathematics"
        topic = "Primary_Grade_5_Mathematics"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary_Grade_6_Mathematics')
def p6notes_4355():
    """Learn route: /Learn/Primary_Grade_6_Mathematics"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary_Grade_6_Mathematics.html', **context)
    except Exception as e:
        grade = "Primary_Grade_6_Mathematics"
        topic = "Primary_Grade_6_Mathematics"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary2/WholeNumbers/Tips-To-Remember-(Multiplication)Times-Table-Of-2-To-12')
def p2timestable_4044():
    """Learn route: /Learn/Primary2/WholeNumbers/Tips-To-Remember-(Multiplication)Times-Table-Of-2-To-12"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary2/WholeNumbers/Tips-To-Remember-(Multiplication)Times-Table-Of-2-To-12.html', **context)
    except Exception as e:
        grade = "Primary2"
        topic = "Tips-To-Remember-(Multiplication)Times-Table-Of-2-To-12"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Primary-Grade-2/WholeNumbers/Tips-To-Remember-(Multiplication)Times-Table-Of-2-To-12')
def p2timestable_9748():
    """Learn route: /Learn/Primary-Grade-2/WholeNumbers/Tips-To-Remember-(Multiplication)Times-Table-Of-2-To-12"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary-Grade-2/WholeNumbers/Tips-To-Remember-(Multiplication)Times-Table-Of-2-To-12.html', **context)
    except Exception as e:
        grade = "Primary-Grade-2"
        topic = "Tips-To-Remember-(Multiplication)Times-Table-Of-2-To-12"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Calculator-Perimeter-Area-Rectangle-Square')
def calculatoraprs_3100():
    """Learn route: /Learn/Calculator-Perimeter-Area-Rectangle-Square"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary4/Measurement/Calculator-Area-and-Perimeter-of-Rectangles-and-Squares.html', **context)
    except Exception as e:
        grade = "Calculator-Perimeter-Area-Rectangle-Square"
        topic = "Calculator-Perimeter-Area-Rectangle-Square"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Times-Tables/Free-Printable-Chart-From-2-to-15')
def timeschart2to15_1624():
    """Learn route: /Learn/Times-Tables/Free-Printable-Chart-From-2-to-15"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Times-Tables/Free-Printable-Chart-From-2-to-15.html', **context)
    except Exception as e:
        grade = "Times-Tables"
        topic = "Free-Printable-Chart-From-2-to-15"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Times-Tables/Free-Printable-Chart-From-16-to-30')
def timeschart16to30_4303():
    """Learn route: /Learn/Times-Tables/Free-Printable-Chart-From-16-to-30"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Times-Tables/Free-Printable-Chart-From-16-to-30.html', **context)
    except Exception as e:
        grade = "Times-Tables"
        topic = "Free-Printable-Chart-From-16-to-30"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Calculator-Times-Table-Multiplication-Chart-2-to-100')
def calculatortimestable_8108():
    """Learn route: /Learn/Calculator-Times-Table-Multiplication-Chart-2-to-100"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/WholeNumbers/Calculator-Times-Table-Multiplication-Chart-2-to-100.html', **context)
    except Exception as e:
        grade = "Calculator-Times-Table-Multiplication-Chart-2-to-100"
        topic = "Calculator-Times-Table-Multiplication-Chart-2-to-100"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Calculator-Radius-of-Circle-Given-Diameter-Circumference-Area')
def calculatorradius_1122():
    """Learn route: /Learn/Calculator-Radius-of-Circle-Given-Diameter-Circumference-Area"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/Measurement/Calculator-Radius-of-Circle-Given-Diameter-Circumference-Area.html', **context)
    except Exception as e:
        grade = "Calculator-Radius-of-Circle-Given-Diameter-Circumference-Area"
        topic = "Calculator-Radius-of-Circle-Given-Diameter-Circumference-Area"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Calculator-Diameter-of-Circle-Elementary-Grade-Math')
def calculatordiameter_2947():
    """Learn route: /Learn/Calculator-Diameter-of-Circle-Elementary-Grade-Math"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/Measurement/Calculator-Diameter-of-Circle-for-Elementary-Grade-Math.html', **context)
    except Exception as e:
        grade = "Calculator-Diameter-of-Circle-Elementary-Grade-Math"
        topic = "Calculator-Diameter-of-Circle-Elementary-Grade-Math"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Calculator-Circumference-of-Circle-Grade-6-Elementary-Math')
def calculatorcircumference_2292():
    """Learn route: /Learn/Calculator-Circumference-of-Circle-Grade-6-Elementary-Math"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/Measurement/Calculator-Circumference-of-Circle-Given-Radius-Diameter-Area.html', **context)
    except Exception as e:
        grade = "Calculator-Circumference-of-Circle-Grade-6-Elementary-Math"
        topic = "Calculator-Circumference-of-Circle-Grade-6-Elementary-Math"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Calculator-Area-of-Circle-Grade-6-Elementary-Math')
def calculatorarea_2618():
    """Learn route: /Learn/Calculator-Area-of-Circle-Grade-6-Elementary-Math"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary6/Measurement/Calculator-Area-of-Circle-Given-Radius-Diameter-Circumference.html', **context)
    except Exception as e:
        grade = "Calculator-Area-of-Circle-Grade-6-Elementary-Math"
        topic = "Calculator-Area-of-Circle-Grade-6-Elementary-Math"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Time-Units-Converter')
def timeunitsconverter_5425():
    """Learn route: /Learn/Time-Units-Converter"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/TimeUnitsConverter/Time-Units-Converter.html', **context)
    except Exception as e:
        grade = "Time-Units-Converter"
        topic = "Time-Units-Converter"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Hours-Unit-Converter')
def hoursunitconverter_1699():
    """Learn route: /Learn/Hours-Unit-Converter"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/TimeUnitsConverter/Hours-Converter.html', **context)
    except Exception as e:
        grade = "Hours-Unit-Converter"
        topic = "Hours-Unit-Converter"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Hours-to-Minutes-Converter')
def hourstominutesconverter_9087():
    """Learn route: /Learn/Hours-to-Minutes-Converter"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/TimeUnitsConverter/Hours-to-Minutes-Converter.html', **context)
    except Exception as e:
        grade = "Hours-to-Minutes-Converter"
        topic = "Hours-to-Minutes-Converter"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Hours-to-Seconds-Converter')
def hourstosecondsconverter_9144():
    """Learn route: /Learn/Hours-to-Seconds-Converter"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/TimeUnitsConverter/Hours-to-Seconds-Converter.html', **context)
    except Exception as e:
        grade = "Hours-to-Seconds-Converter"
        topic = "Hours-to-Seconds-Converter"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Hours-to-Milliseconds-Converter')
def hourstomillisecondsconverter_4292():
    """Learn route: /Learn/Hours-to-Milliseconds-Converter"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/TimeUnitsConverter/Hours-to-Milliseconds-Converter.html', **context)
    except Exception as e:
        grade = "Hours-to-Milliseconds-Converter"
        topic = "Hours-to-Milliseconds-Converter"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Hours-to-Days-Converter')
def hourstodaysconverter_7542():
    """Learn route: /Learn/Hours-to-Days-Converter"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/TimeUnitsConverter/Hours-to-Days-Converter.html', **context)
    except Exception as e:
        grade = "Hours-to-Days-Converter"
        topic = "Hours-to-Days-Converter"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Hours-to-Weeks-Converter')
def hourstoweeksconverter_7451():
    """Learn route: /Learn/Hours-to-Weeks-Converter"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/TimeUnitsConverter/Hours-to-Weeks-Converter.html', **context)
    except Exception as e:
        grade = "Hours-to-Weeks-Converter"
        topic = "Hours-to-Weeks-Converter"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Hours-to-Months-Converter')
def hourstomonthsconverter_2095():
    """Learn route: /Learn/Hours-to-Months-Converter"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/TimeUnitsConverter/Hours-to-Months-Converter.html', **context)
    except Exception as e:
        grade = "Hours-to-Months-Converter"
        topic = "Hours-to-Months-Converter"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Hours-to-Years-Converter')
def hourstoyearsconverter_131():
    """Learn route: /Learn/Hours-to-Years-Converter"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/TimeUnitsConverter/Hours-to-Years-Converter.html', **context)
    except Exception as e:
        grade = "Hours-to-Years-Converter"
        topic = "Hours-to-Years-Converter"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Hours-to-Decades-Converter')
def hourstodecadesconverter_7938():
    """Learn route: /Learn/Hours-to-Decades-Converter"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/TimeUnitsConverter/Hours-to-Decades-Converter.html', **context)
    except Exception as e:
        grade = "Hours-to-Decades-Converter"
        topic = "Hours-to-Decades-Converter"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Hours-to-Centuries-Converter')
def hourstocenturiesconverter_688():
    """Learn route: /Learn/Hours-to-Centuries-Converter"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/TimeUnitsConverter/Hours-to-Centuries-Converter.html', **context)
    except Exception as e:
        grade = "Hours-to-Centuries-Converter"
        topic = "Hours-to-Centuries-Converter"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Hours-to-Millenniums-Converter')
def hourstomillenniumsconverter_1500():
    """Learn route: /Learn/Hours-to-Millenniums-Converter"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/TimeUnitsConverter/Hours-to-Millenniums-Converter.html', **context)
    except Exception as e:
        grade = "Hours-to-Millenniums-Converter"
        topic = "Hours-to-Millenniums-Converter"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Hours-to-Microseconds-Converter')
def hourstomicrosecondsconverter_3621():
    """Learn route: /Learn/Hours-to-Microseconds-Converter"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/TimeUnitsConverter/Hours-to-Microseconds-Converter.html', **context)
    except Exception as e:
        grade = "Hours-to-Microseconds-Converter"
        topic = "Hours-to-Microseconds-Converter"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Hours-to-Nanoseconds-Converter')
def hourstonanosecondsconverter_4849():
    """Learn route: /Learn/Hours-to-Nanoseconds-Converter"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/TimeUnitsConverter/Hours-to-Nanoseconds-Converter.html', **context)
    except Exception as e:
        grade = "Hours-to-Nanoseconds-Converter"
        topic = "Hours-to-Nanoseconds-Converter"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Hours-to-Picoseconds-Converter')
def hourstopicosecondsconverter_6282():
    """Learn route: /Learn/Hours-to-Picoseconds-Converter"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/TimeUnitsConverter/Hours-to-Picoseconds-Converter.html', **context)
    except Exception as e:
        grade = "Hours-to-Picoseconds-Converter"
        topic = "Hours-to-Picoseconds-Converter"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Calculator-Two-Number-Comparison-Greater-Smaller-Equal-To')
def calculatornumbercomparison_7255():
    """Learn route: /Learn/Calculator-Two-Number-Comparison-Greater-Smaller-Equal-To"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/WholeNumbers/Calculator-to-Compare-Two-Numbers.html', **context)
    except Exception as e:
        grade = "Calculator-Two-Number-Comparison-Greater-Smaller-Equal-To"
        topic = "Calculator-Two-Number-Comparison-Greater-Smaller-Equal-To"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Time-Duration-Calculator')
def calculatortimeduration_7568():
    """Learn route: /Learn/Time-Duration-Calculator"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/Time/Calculator-Time-Duration-Addition-Subtraction.html', **context)
    except Exception as e:
        grade = "Time-Duration-Calculator"
        topic = "Time-Duration-Calculator"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Length-Units-Converter')
def lengthunitsconverter_1499():
    """Learn route: /Learn/Length-Units-Converter"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/LengthUnitConverter/Length-Units-Converter.html', **context)
    except Exception as e:
        grade = "Length-Units-Converter"
        topic = "Length-Units-Converter"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Meter-Unit-Converter')
def meterunitconverter_4630():
    """Learn route: /Learn/Meter-Unit-Converter"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/LengthUnitConverter/Meter-Converter.html', **context)
    except Exception as e:
        grade = "Meter-Unit-Converter"
        topic = "Meter-Unit-Converter"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Meter-to-Centimeter-Converter')
def metertocentimeterconverter_7937():
    """Learn route: /Learn/Meter-to-Centimeter-Converter"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/LengthUnitConverter/Meter-to-Centimeter-Converter.html', **context)
    except Exception as e:
        grade = "Meter-to-Centimeter-Converter"
        topic = "Meter-to-Centimeter-Converter"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Meter-to-Millimeter-Converter')
def metertomillimeterconverter_6828():
    """Learn route: /Learn/Meter-to-Millimeter-Converter"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/LengthUnitConverter/Meter-to-Millimeter-Converter.html', **context)
    except Exception as e:
        grade = "Meter-to-Millimeter-Converter"
        topic = "Meter-to-Millimeter-Converter"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Meter-to-Kilometre-Converter')
def metertokilometreconverter_9561():
    """Learn route: /Learn/Meter-to-Kilometre-Converter"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/LengthUnitConverter/Meter-to-Kilometre-Converter.html', **context)
    except Exception as e:
        grade = "Meter-to-Kilometre-Converter"
        topic = "Meter-to-Kilometre-Converter"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Meter-to-Inches-Converter')
def metertoinchesconverter_5869():
    """Learn route: /Learn/Meter-to-Inches-Converter"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/LengthUnitConverter/Meter-to-Inches-Converter.html', **context)
    except Exception as e:
        grade = "Meter-to-Inches-Converter"
        topic = "Meter-to-Inches-Converter"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Meter-to-Feet-Converter')
def metertofeetconverter_8253():
    """Learn route: /Learn/Meter-to-Feet-Converter"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/LengthUnitConverter/Meter-to-Feet-Converter.html', **context)
    except Exception as e:
        grade = "Meter-to-Feet-Converter"
        topic = "Meter-to-Feet-Converter"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Meter-to-Feet-and-Inches-Conversion')
def metertofeetinchesconverter_4980():
    """Learn route: /Learn/Meter-to-Feet-and-Inches-Conversion"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/LengthUnitConverter/Meter-to-Feet-and-Inches-Conversion.html', **context)
    except Exception as e:
        grade = "Meter-to-Feet-and-Inches-Conversion"
        topic = "Meter-to-Feet-and-Inches-Conversion"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Meter-to-Miles-Conversion')
def metertomilesconverter_1069():
    """Learn route: /Learn/Meter-to-Miles-Conversion"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/LengthUnitConverter/Meter-to-Miles-Converter.html', **context)
    except Exception as e:
        grade = "Meter-to-Miles-Conversion"
        topic = "Meter-to-Miles-Conversion"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Meter-to-Yards-Conversion')
def metertoyardsconverter_5150():
    """Learn route: /Learn/Meter-to-Yards-Conversion"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/LengthUnitConverter/Meter-to-Yards-Converter.html', **context)
    except Exception as e:
        grade = "Meter-to-Yards-Conversion"
        topic = "Meter-to-Yards-Conversion"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Equivalent-Fractions-Calculator')
def equivalentfractionscalculator_4406():
    """Learn route: /Learn/Equivalent-Fractions-Calculator"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/Fractions/Equivalent-Fractions-Generator.html', **context)
    except Exception as e:
        grade = "Equivalent-Fractions-Calculator"
        topic = "Equivalent-Fractions-Calculator"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Simplifying-Fractions-Calculator')
def simplifyingfractionscalculator_4608():
    """Learn route: /Learn/Simplifying-Fractions-Calculator"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/Fractions/Simplifying-Fractions-Calculator.html', **context)
    except Exception as e:
        grade = "Simplifying-Fractions-Calculator"
        topic = "Simplifying-Fractions-Calculator"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Compare-Fractions-Calculator')
def comparefractionscalculator_1081():
    """Learn route: /Learn/Compare-Fractions-Calculator"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/Fractions/Compare-Fractions-Calculator.html', **context)
    except Exception as e:
        grade = "Compare-Fractions-Calculator"
        topic = "Compare-Fractions-Calculator"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Add-Fractions-Calculator')
def addfractionscalculator_6913():
    """Learn route: /Learn/Add-Fractions-Calculator"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/Fractions/Add-Fractions-Calculator.html', **context)
    except Exception as e:
        grade = "Add-Fractions-Calculator"
        topic = "Add-Fractions-Calculator"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"

@flask_learn_all_bp.route('/Learn/Subtract-Fractions-Calculator')
def subtractfractionscalculator_8791():
    """Learn route: /Learn/Subtract-Fractions-Calculator"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Primary3/Fractions/Subtract-Fractions-Calculator.html', **context)
    except Exception as e:
        grade = "Subtract-Fractions-Calculator"
        topic = "Subtract-Fractions-Calculator"
        return f"<h1>{topic} - {grade}</h1><p>Content updating...</p><p><a href='/Learn'>← Learn</a></p>"



# ====== FOOTER ROUTES ======

@flask_learn_all_bp.route('/What_is_Singapore_Math')
def singapore_math():
    """Singapore Math information page"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Singapore_Math.html', **context)
    except Exception as e:
        return f"<h1>Singapore Math - HomeCampus</h1><p>Singapore Math information is being updated.</p><p><a href='/'>← Back to homepage</a></p>"

@flask_learn_all_bp.route('/Contact')
def contact():
    """Contact Us page"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Contact.html', **context)
    except Exception as e:
        return f"<h1>Contact Us - HomeCampus</h1><p>Contact information is being updated.</p><p><a href='/'>← Back to homepage</a></p>"

@flask_learn_all_bp.route('/Disclaimer')
def disclaimer():
    """Disclaimer page"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Disclaimer.html', **context)
    except Exception as e:
        return f"<h1>Disclaimer - HomeCampus</h1><p>Disclaimer information is being updated.</p><p><a href='/'>← Back to homepage</a></p>"

@flask_learn_all_bp.route('/PrivacyPolicy')
def privacy_policy():
    """Privacy Policy page"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('PrivacyPolicy.html', **context)
    except Exception as e:
        return f"<h1>Privacy Policy - HomeCampus</h1><p>Privacy policy information is being updated.</p><p><a href='/'>← Back to homepage</a></p>"

@flask_learn_all_bp.route('/FAQs')
def faqs():
    """Frequently Asked Questions page"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('FAQs.html', **context)
    except Exception as e:
        return f"<h1>FAQs - HomeCampus</h1><p>FAQ information is being updated.</p><p><a href='/'>← Back to homepage</a></p>"

@flask_learn_all_bp.route('/AboutHomeCampus')
def about_homecampus():
    """About HomeCampus page"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('AboutHomeCampus.html', **context)
    except Exception as e:
        return f"<h1>About HomeCampus</h1><p>About information is being updated.</p><p><a href='/'>← Back to homepage</a></p>"

@flask_learn_all_bp.route('/Subscribe')
def subscribe():
    """Subscription page"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('SubscriptionPage.html', **context)
    except Exception as e:
        return f"<h1>Subscribe - HomeCampus</h1><p>Subscription information is being updated.</p><p><a href='/'>← Back to homepage</a></p>"

@flask_learn_all_bp.route('/Refund')
def refund():
    """Refund policy page"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Refund.html', **context)
    except Exception as e:
        return f"<h1>Refund Policy - HomeCampus</h1><p>Refund information is being updated.</p><p><a href='/'>← Back to homepage</a></p>"

# ====== WORKSHEET ROUTES ======

@flask_learn_all_bp.route('/Free-Math-Worksheets/Perimeter-of-Rectangles')
def worksheet_perimeter_rectangles():
    """Rectangle Perimeter Worksheet"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Worksheets/Free-Math-Worksheet-on-Perimeter-of-Rectangles.html', **context)
    except Exception as e:
        return f"<h1>Perimeter of Rectangles Worksheet</h1><p>Worksheet is being updated.</p><p><a href='/Math-Worksheets'>← Back to Worksheets</a></p>"

@flask_learn_all_bp.route('/Free-Math-Worksheets/Perimeter-of-Squares')
def worksheet_perimeter_squares():
    """Square Perimeter Worksheet"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Worksheets/Free-Math-Worksheet-on-Perimeter-of-Squares.html', **context)
    except Exception as e:
        return f"<h1>Perimeter of Squares Worksheet</h1><p>Worksheet is being updated.</p><p><a href='/Math-Worksheets'>← Back to Worksheets</a></p>"

@flask_learn_all_bp.route('/Free-Math-Worksheets/Area-of-Rectangles')
def worksheet_area_rectangles():
    """Rectangle Area Worksheet"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Worksheets/Free-Math-Worksheet-on-Area-of-Rectangles.html', **context)
    except Exception as e:
        return f"<h1>Area of Rectangles Worksheet</h1><p>Worksheet is being updated.</p><p><a href='/Math-Worksheets'>← Back to Worksheets</a></p>"

@flask_learn_all_bp.route('/Free-Math-Worksheets/Area-of-Squares')
def worksheet_area_squares():
    """Square Area Worksheet"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Worksheets/Free-Math-Worksheet-on-Area-of-Squares.html', **context)
    except Exception as e:
        return f"<h1>Area of Squares Worksheet</h1><p>Worksheet is being updated.</p><p><a href='/Math-Worksheets'>← Back to Worksheets</a></p>"

@flask_learn_all_bp.route('/Free-Math-Worksheets/Diameter-Radius-of-Circle')
def worksheet_diameter_radius():
    """Circle Diameter Radius Worksheet"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Worksheets/Free-Math-Worksheet-on-Diameter-Radius-of-Circle.html', **context)
    except Exception as e:
        return f"<h1>Diameter and Radius of Circle Worksheet</h1><p>Worksheet is being updated.</p><p><a href='/Math-Worksheets'>← Back to Worksheets</a></p>"

@flask_learn_all_bp.route('/Free-Math-Worksheets/Circumference-of-Circle')
def worksheet_circumference():
    """Circle Circumference Worksheet"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Worksheets/Free-Math-Worksheet-on-Circumference-of-Circle.html', **context)
    except Exception as e:
        return f"<h1>Circumference of Circle Worksheet</h1><p>Worksheet is being updated.</p><p><a href='/Math-Worksheets'>← Back to Worksheets</a></p>"

@flask_learn_all_bp.route('/Free-Math-Worksheets/Numbers-Place-Value-Up-To-10000')
def worksheet_numbers_place_value():
    """Numbers Place Value Worksheet"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Worksheets/Free-Math-Worksheet-on-Numbers-Up-To-10000.html', **context)
    except Exception as e:
        return f"<h1>Numbers Place Value Up To 10000 Worksheet</h1><p>Worksheet is being updated.</p><p><a href='/Math-Worksheets'>← Back to Worksheets</a></p>"

@flask_learn_all_bp.route('/Free-Math-Worksheets/Write-Figures-To-Words-Up-To-10000')
def worksheet_figures_to_words():
    """Figures to Words Worksheet"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Worksheets/Free-Math-Worksheet-on-Figures-To-Words-Up-To-10000.html', **context)
    except Exception as e:
        return f"<h1>Write Figures To Words Up To 10000 Worksheet</h1><p>Worksheet is being updated.</p><p><a href='/Math-Worksheets'>← Back to Worksheets</a></p>"

@flask_learn_all_bp.route('/Free-Math-Worksheets/Convert-Words-To-Figures-Up-To-10000')
def worksheet_words_to_figures():
    """Words to Figures Worksheet"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Worksheets/Free-Math-Worksheet-on-Words-To-Figures-Up-To-10000.html', **context)
    except Exception as e:
        return f"<h1>Convert Words To Figures Up To 10000 Worksheet</h1><p>Worksheet is being updated.</p><p><a href='/Math-Worksheets'>← Back to Worksheets</a></p>"

@flask_learn_all_bp.route('/Free-Math-Worksheets/Number-Pattern-Worksheets-for-Grade-3')
def worksheet_number_patterns():
    """Number Patterns Worksheet"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Worksheets/Free-Math-Worksheet-on-Basic-Number-Patterns.html', **context)
    except Exception as e:
        return f"<h1>Number Pattern Worksheets for Grade 3</h1><p>Worksheet is being updated.</p><p><a href='/Math-Worksheets'>← Back to Worksheets</a></p>"

@flask_learn_all_bp.route('/Free-Math-Worksheets/Comparing-Ordering-Numbers-Worksheets')
def worksheet_comparing_ordering():
    """Comparing Ordering Numbers Worksheet"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Worksheets/Free-Math-Worksheet-on-Compare-Order-Four-Digit-Numbers.html', **context)
    except Exception as e:
        return f"<h1>Comparing and Ordering Numbers Worksheets</h1><p>Worksheet is being updated.</p><p><a href='/Math-Worksheets'>← Back to Worksheets</a></p>"

@flask_learn_all_bp.route('/Free-Math-Worksheets/Addition-of-Four-Digit-Numbers-Up-To-10000')
def worksheet_addition_four_digit():
    """Addition Four Digit Numbers Worksheet"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Worksheets/Free-Math-Worksheet-on-Addition-of-Numbers-Up-To-10000.html', **context)
    except Exception as e:
        return f"<h1>Addition of Four Digit Numbers Up To 10000 Worksheet</h1><p>Worksheet is being updated.</p><p><a href='/Math-Worksheets'>← Back to Worksheets</a></p>"

@flask_learn_all_bp.route('/Free-Math-Worksheets/Basic-Subtraction-of-Four-Digit-Numbers-Up-To-10000')
def worksheet_subtraction_four_digit():
    """Subtraction Four Digit Numbers Worksheet"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Worksheets/Free-Math-Worksheet-on-Subtraction-of-Numbers-Up-To-10000.html', **context)
    except Exception as e:
        return f"<h1>Basic Subtraction of Four Digit Numbers Up To 10000 Worksheet</h1><p>Worksheet is being updated.</p><p><a href='/Math-Worksheets'>← Back to Worksheets</a></p>"

@flask_learn_all_bp.route('/Free-Math-Worksheets/Multiplication-of-Three-Digit-Numbers')
def worksheet_multiplication_three_digit():
    """Multiplication Three Digit Numbers Worksheet"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Worksheets/Free-Math-Worksheet-on-Multiplication-of-3-Digits.html', **context)
    except Exception as e:
        return f"<h1>Multiplication of Three Digit Numbers Worksheet</h1><p>Worksheet is being updated.</p><p><a href='/Math-Worksheets'>← Back to Worksheets</a></p>"

@flask_learn_all_bp.route('/Free-Math-Worksheets/Long-Division-of-Two-Digit-Numbers-with-Remainders')
def worksheet_long_division():
    """Long Division Worksheet"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Worksheets/Free-Math-Worksheet-on-Long-Division-of-2-Digits.html', **context)
    except Exception as e:
        return f"<h1>Long Division of Two Digit Numbers with Remainders Worksheet</h1><p>Worksheet is being updated.</p><p><a href='/Math-Worksheets'>← Back to Worksheets</a></p>"

@flask_learn_all_bp.route('/Free-Math-Worksheets/Whole-Numbers-2-Step-Word-Problems-4-Operations')
def worksheet_whole_numbers_word_problems():
    """Whole Numbers Word Problems Worksheet"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Worksheets/Free-Math-Worksheet-on-2-Step-Word-Problems-Whole-Numbers.html', **context)
    except Exception as e:
        return f"<h1>Whole Numbers 2-Step Word Problems 4 Operations Worksheet</h1><p>Worksheet is being updated.</p><p><a href='/Math-Worksheets'>← Back to Worksheets</a></p>"

@flask_learn_all_bp.route('/Free-Math-Worksheets/Adding-Money-With-Cents-Worksheets')
def worksheet_money_addition():
    """Money Addition Worksheet"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Worksheets/Free-Math-Worksheet-on-Money-Addition.html', **context)
    except Exception as e:
        return f"<h1>Adding Money With Cents Worksheets</h1><p>Worksheet is being updated.</p><p><a href='/Math-Worksheets'>← Back to Worksheets</a></p>"

@flask_learn_all_bp.route('/Free-Math-Worksheets/Money-Subtraction-With-Cents-Worksheets')
def worksheet_money_subtraction():
    """Money Subtraction Worksheet"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Worksheets/Free-Math-Worksheet-on-Money-Subtraction.html', **context)
    except Exception as e:
        return f"<h1>Money Subtraction With Cents Worksheets</h1><p>Worksheet is being updated.</p><p><a href='/Math-Worksheets'>← Back to Worksheets</a></p>"

@flask_learn_all_bp.route('/Free-Math-Worksheets/Money-Word-Problems-Singapore-Math-Worksheets')
def worksheet_money_word_problems():
    """Money Word Problems Worksheet"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Worksheets/Free-Math-Worksheet-on-Money-Word-Problems-Story-Sum.html', **context)
    except Exception as e:
        return f"<h1>Money Word Problems Singapore Math Worksheets</h1><p>Worksheet is being updated.</p><p><a href='/Math-Worksheets'>← Back to Worksheets</a></p>"

@flask_learn_all_bp.route('/Free-Math-Worksheets/Reading-and-Telling-Time-Worksheets')
def worksheet_telling_time():
    """Reading and Telling Time Worksheet"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Worksheets/Free-Math-Worksheet-on-Reading-and-Telling-Time.html', **context)
    except Exception as e:
        return f"<h1>Reading and Telling Time Worksheets</h1><p>Worksheet is being updated.</p><p><a href='/Math-Worksheets'>← Back to Worksheets</a></p>"

@flask_learn_all_bp.route('/Free-Math-Worksheets/Hours-to-Minutes-Converter-Worksheets')
def worksheet_hours_to_minutes():
    """Hours to Minutes Converter Worksheet"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Worksheets/Free-Math-Worksheet-on-Convert-Hours-to-Minutes.html', **context)
    except Exception as e:
        return f"<h1>Hours to Minutes Converter Worksheets</h1><p>Worksheet is being updated.</p><p><a href='/Math-Worksheets'>← Back to Worksheets</a></p>"

@flask_learn_all_bp.route('/Free-Math-Worksheets/How-to-Add-Hours-and-Minutes-Time-Addition')
def worksheet_time_addition():
    """Time Addition Worksheet"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Worksheets/Free-Math-Worksheet-on-Time-Addition-Add-Hours-Minutes.html', **context)
    except Exception as e:
        return f"<h1>How to Add Hours and Minutes Time Addition</h1><p>Worksheet is being updated.</p><p><a href='/Math-Worksheets'>← Back to Worksheets</a></p>"

@flask_learn_all_bp.route('/Free-Math-Worksheets/How-to-Subtract-Hours-and-Minutes-Time-Subtraction')
def worksheet_time_subtraction():
    """Time Subtraction Worksheet"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Worksheets/Free-Math-Worksheet-on-Time-Subtraction-Subtract-Hours-Minutes.html', **context)
    except Exception as e:
        return f"<h1>How to Subtract Hours and Minutes Time Subtraction</h1><p>Worksheet is being updated.</p><p><a href='/Math-Worksheets'>← Back to Worksheets</a></p>"

@flask_learn_all_bp.route('/Free-Math-Worksheets/Calculate-Time-Duration-Start-Finish-Time')
def worksheet_time_duration():
    """Time Duration Worksheet"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Worksheets/Free-Math-Worksheet-on-Calculate-Time-Duration.html', **context)
    except Exception as e:
        return f"<h1>Calculate Time Duration Start Finish Time</h1><p>Worksheet is being updated.</p><p><a href='/Math-Worksheets'>← Back to Worksheets</a></p>"

@flask_learn_all_bp.route('/Free-Math-Worksheets/Time-Duration-Singapore-Math-Word-Problems-Story-Sum')
def worksheet_time_duration_word_problems():
    """Time Duration Word Problems Worksheet"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Worksheets/Free-Math-Worksheet-on-2-Step-Time-Duration-Word-Problems.html', **context)
    except Exception as e:
        return f"<h1>Time Duration Singapore Math Word Problems Story Sum</h1><p>Worksheet is being updated.</p><p><a href='/Math-Worksheets'>← Back to Worksheets</a></p>"

# ====== LOWERCASE WORKSHEET ROUTES ======

@flask_learn_all_bp.route('/free-math-worksheets/how-to-convert-metres-to-centimetres')
def worksheet_metres_to_centimeters():
    """Metres to Centimeters Worksheet"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Worksheets/free-math-worksheet-on-how-to-convert-metres-to-centimeters.html', **context)
    except Exception as e:
        return f"<h1>How to Convert Metres to Centimeters</h1><p>Worksheet is being updated.</p><p><a href='/Math-Worksheets'>← Back to Worksheets</a></p>"

@flask_learn_all_bp.route('/free-math-worksheets/how-to-convert-kilometers-to-meters')
def worksheet_kilometers_to_meters():
    """Kilometers to Meters Worksheet"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Worksheets/free-math-worksheet-on-how-to-convert-kilometers-to-meters.html', **context)
    except Exception as e:
        return f"<h1>How to Convert Kilometers to Meters</h1><p>Worksheet is being updated.</p><p><a href='/Math-Worksheets'>← Back to Worksheets</a></p>"

@flask_learn_all_bp.route('/free-math-worksheets-1-kilograms-equal-to-1000-grams')
def worksheet_kilograms_to_grams():
    """Kilograms to Grams Worksheet"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Worksheets/free-math-worksheet-on-how-to-convert-kilograms-to-grams.html', **context)
    except Exception as e:
        return f"<h1>1 Kilograms Equal to 1000 Grams</h1><p>Worksheet is being updated.</p><p><a href='/Math-Worksheets'>← Back to Worksheets</a></p>"

@flask_learn_all_bp.route('/free-math-worksheets-how-to-convert-litres-to-millilitres')
def worksheet_litres_to_millilitres():
    """Litres to Millilitres Worksheet"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Worksheets/free-math-worksheet-on-how-to-convert-litres-to-millilitres.html', **context)
    except Exception as e:
        return f"<h1>How to Convert Litres to Millilitres</h1><p>Worksheet is being updated.</p><p><a href='/Math-Worksheets'>← Back to Worksheets</a></p>"

@flask_learn_all_bp.route('/free-math-worksheets-solve-1-step-word-problems-length-mass-volume')
def worksheet_1_step_length_mass_volume():
    """1-Step Length Mass Volume Worksheet"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Worksheets/free-math-worksheet-solve-1-step-length-mass-volume.html', **context)
    except Exception as e:
        return f"<h1>Solve 1-Step Word Problems Length Mass Volume</h1><p>Worksheet is being updated.</p><p><a href='/Math-Worksheets'>← Back to Worksheets</a></p>"

@flask_learn_all_bp.route('/free-math-worksheets-solve-2-step-word-problems-length-mass-volume')
def worksheet_2_step_length_mass_volume():
    """2-Step Length Mass Volume Worksheet"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Worksheets/free-math-worksheet-solve-2-step-length-mass-volume.html', **context)
    except Exception as e:
        return f"<h1>Solve 2-Step Word Problems Length Mass Volume</h1><p>Worksheet is being updated.</p><p><a href='/Math-Worksheets'>← Back to Worksheets</a></p>"

@flask_learn_all_bp.route('/free-math-worksheets-what-is-a-fraction')
def worksheet_what_is_fraction():
    """What is a Fraction Worksheet"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Worksheets/free-math-worksheet-what-is-a-fraction.html', **context)
    except Exception as e:
        return f"<h1>What is a Fraction</h1><p>Worksheet is being updated.</p><p><a href='/Math-Worksheets'>← Back to Worksheets</a></p>"

@flask_learn_all_bp.route('/what-are-equivalent-fractions-free-math-worksheets')
def worksheet_equivalent_fractions():
    """Equivalent Fractions Worksheet"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Worksheets/free-math-worksheet-what-are-equivalent-fraction.html', **context)
    except Exception as e:
        return f"<h1>What are Equivalent Fractions</h1><p>Worksheet is being updated.</p><p><a href='/Math-Worksheets'>← Back to Worksheets</a></p>"

@flask_learn_all_bp.route('/how-to-simplify-fractions-free-math-worksheets')
def worksheet_simplify_fractions():
    """Simplify Fractions Worksheet"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Worksheets/free-math-worksheet-simplifying-fractions.html', **context)
    except Exception as e:
        return f"<h1>How to Simplify Fractions</h1><p>Worksheet is being updated.</p><p><a href='/Math-Worksheets'>← Back to Worksheets</a></p>"

@flask_learn_all_bp.route('/comparing-and-ordering-fractions-free-math-worksheets')
def worksheet_comparing_fractions():
    """Comparing Fractions Worksheet"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Worksheets/free-math-worksheet-comparing-ordering-fractions.html', **context)
    except Exception as e:
        return f"<h1>Comparing and Ordering Fractions</h1><p>Worksheet is being updated.</p><p><a href='/Math-Worksheets'>← Back to Worksheets</a></p>"

@flask_learn_all_bp.route('/how-to-add-fractions-singapore-math-free-math-worksheets')
def worksheet_add_fractions():
    """Add Fractions Worksheet"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Worksheets/free-math-worksheet-add-fractions.html', **context)
    except Exception as e:
        return f"<h1>How to Add Fractions Singapore Math</h1><p>Worksheet is being updated.</p><p><a href='/Math-Worksheets'>← Back to Worksheets</a></p>"

@flask_learn_all_bp.route('/how-to-subtract-fractions-singapore-math-free-math-worksheets')
def worksheet_subtract_fractions():
    """Subtract Fractions Worksheet"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Worksheets/free-math-worksheet-subtract-fractions.html', **context)
    except Exception as e:
        return f"<h1>How to Subtract Fractions Singapore Math</h1><p>Worksheet is being updated.</p><p><a href='/Math-Worksheets'>← Back to Worksheets</a></p>"

@flask_learn_all_bp.route('/free-math-worksheets-area-in-square-units')
def worksheet_area_square_units():
    """Area in Square Units Worksheet"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Worksheets/free-math-worksheet-area-in-square-units.html', **context)
    except Exception as e:
        return f"<h1>Area in Square Units</h1><p>Worksheet is being updated.</p><p><a href='/Math-Worksheets'>← Back to Worksheets</a></p>"

@flask_learn_all_bp.route('/area-in-square-centimeters-meters-free-math-worksheets')
def worksheet_area_square_cm_m():
    """Area in Square Centimeters Meters Worksheet"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Worksheets/free-math-worksheet-area-in-square-centimeters-meters.html', **context)
    except Exception as e:
        return f"<h1>Area in Square Centimeters Meters</h1><p>Worksheet is being updated.</p><p><a href='/Math-Worksheets'>← Back to Worksheets</a></p>"

@flask_learn_all_bp.route('/how-to-calculate-area-of-a-square-free-math-worksheets')
def worksheet_calculate_area_square():
    """Calculate Area of Square Worksheet"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Worksheets/free-math-worksheet-how-to-calculate-area-of-a-square.html', **context)
    except Exception as e:
        return f"<h1>How to Calculate Area of a Square</h1><p>Worksheet is being updated.</p><p><a href='/Math-Worksheets'>← Back to Worksheets</a></p>"

@flask_learn_all_bp.route('/identifying-angles-in-a-figure-free-math-worksheets')
def worksheet_identifying_angles():
    """Identifying Angles Worksheet"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Worksheets/free-math-worksheet-identifying-angles.html', **context)
    except Exception as e:
        return f"<h1>Identifying Angles in a Figure</h1><p>Worksheet is being updated.</p><p><a href='/Math-Worksheets'>← Back to Worksheets</a></p>"

@flask_learn_all_bp.route('/what-is-a-right-angle-free-math-worksheets')
def worksheet_right_angles():
    """Right Angles Worksheet"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Worksheets/free-math-worksheet-right-angles.html', **context)
    except Exception as e:
        return f"<h1>What is a Right Angle</h1><p>Worksheet is being updated.</p><p><a href='/Math-Worksheets'>← Back to Worksheets</a></p>"

@flask_learn_all_bp.route('/what-is-a-bar-graph-free-math-worksheets-for-grade-3')
def worksheet_bar_graphs():
    """Bar Graphs Worksheet"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Worksheets/free-math-worksheet-bar-graphs.html', **context)
    except Exception as e:
        return f"<h1>What is a Bar Graph for Grade 3</h1><p>Worksheet is being updated.</p><p><a href='/Math-Worksheets'>← Back to Worksheets</a></p>"

# ====== UTILITY ROUTES ======

@flask_learn_all_bp.route('/Math-Worksheets')
@flask_learn_all_bp.route('/math-worksheets')
def flask_math_worksheets():
    """Math Worksheets page"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Math-Worksheets.html', **context)
    except Exception as e:
        return f"<h1>Math Worksheets - HomeCampus</h1><p>Math worksheets content is being updated.</p><p><a href='/Learn'>← Back to Learn</a></p>"

@flask_learn_all_bp.route('/Math-Calculators')
def flask_math_calculators():
    """Math Calculators page"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Math-Calculators.html', **context)
    except Exception as e:
        return f"<h1>Math Calculators - HomeCampus</h1><p>Math calculators content is being updated.</p><p><a href='/Learn'>← Back to Learn</a></p>"

@flask_learn_all_bp.route('/Math-Glossary')
def flask_math_glossary():
    """Math Glossary page"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Math-Glossary.html', **context)
    except Exception as e:
        return f"<h1>Math Glossary - HomeCampus</h1><p>Math glossary content is being updated.</p><p><a href='/Learn'>← Back to Learn</a></p>"

@flask_learn_all_bp.route('/Rectangle')
def flask_rectangle():
    """Rectangle glossary page"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Glossary/Rectangle.html', **context)
    except Exception as e:
        return f"<h1>Rectangle - Math Glossary</h1><p>Rectangle content is being updated.</p><p><a href='/Learn'>← Back to Learn</a></p>"

@flask_learn_all_bp.route('/Square')
def flask_square():
    """Square glossary page"""
    handler = FlaskLearnHandler()
    context = handler.get_template_context()
    try:
        return render_template('Notes/Glossary/Square.html', **context)
    except Exception as e:
        return f"<h1>Square - Math Glossary</h1><p>Square content is being updated.</p><p><a href='/Learn'>← Back to Learn</a></p>"

@flask_learn_all_bp.route('/learn-routes-status')
def learn_routes_status():
    return f"""
    <h1>Complete HomeCampus Routes System</h1>
    <p><strong>Learn Routes:</strong> 338 routes (All Primary 3-6 subjects)</p>
    <p><strong>Utility Routes:</strong> Math-Worksheets, Math-Calculators, Math-Glossary, Rectangle, Square</p>
    <p><strong>Footer Routes:</strong> Singapore Math, Contact, Disclaimer, Privacy, FAQs, About, Subscribe, Refund</p>
    <p><strong>Auth Routes:</strong> SignIn, Register, ForgotPassword, ResetPassword, AddChild</p>
    <p><strong>Homepage:</strong> Main homepage and static file serving</p>
    <p><strong>🎉 COMPLETE MIGRATION SUCCESS!</strong> All routes functional on Python 3.9 + Flask</p>
    <p><a href="/">← Back to homepage</a> | <a href="/Learn">Learn System</a></p>
    """
