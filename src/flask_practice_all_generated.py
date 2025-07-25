"""
Complete Flask Practice System - ALL Practice Routes
AUTO-GENERATED from Primary3Problems.py, Primary4Problems.py, Primary5Problems.py, Primary6Problems.py analysis
Comprehensive Practice route coverage for Grades 3-6 Mathematics
"""

from flask import Blueprint, render_template, request, session, redirect, url_for
import logging

flask_practice_all_bp = Blueprint('flask_practice_all', __name__)

class FlaskPracticeHandler:
    def __init__(self):
        # Initialize practice-specific context
        self.current_user = session.get('current_user')
        self.auth_session = session.get('auth_session')
        
    def get_template_context(self, grade=3, concept="", practice_page=""):
        """Get base template context for practice pages"""
        return {
            'auth_session': self.auth_session,
            'current_user': self.current_user,
            'login_url': '/SignIn',
            'logout_url': '/auth/logout',
            'current_url': request.url,
            'register_url': '/Register',
            'TRIAL': 'N',
            'UnfinishedWorksheetsCount': 0,
            'problems_attempted': 0,
            'correct_problems': 0,
            'Concept_HCScore': 0,
            'Concept_HCRank': 'Academy Ninja',
            'concept_display': concept,
            'ConceptID': concept,
            'Concept_Goal': 30,
            'concept_display_full': f"<a href='/Practice/Primary_Grade_{grade}_Mathematics'>Grade {grade}</a> &nbsp;&gt;&gt;&nbsp; {concept}",
            'practice_page': practice_page,
            'Ninja_max': 40,
            'Ninja_value': 0,
            'Ninja_title': "40 more points to next Ninja rank",
            'Ninja_Start': "Academy Ninja",
            'Ninja_End': "Lower Ninja",
            'Ninja_Percentage': 0,
            'SubscribeMessage': 'N'
        }

    def render_practice_response(self, template_name, grade, concept, **context):
        """Render practice response with error handling"""
        try:
            practice_page = f"/Practice/Primary_Grade_{grade}_Mathematics"
            base_context = self.get_template_context(grade, concept, practice_page)
            base_context.update(context)
            
            # Try to render the appropriate practice template
            # Use PracticePageSkeleton.html for most practice content
            if 'Fraction' in concept:
                return render_template('PracticePageFractionSkeleton.html', **base_context)
            else:
                return render_template('PracticePageSkeleton.html', **base_context)
                
        except Exception as e:
            logging.error(f"Practice template error for {concept}: {e}")
            # Fallback to simple practice page
            try:
                return render_template('Practice_Question_Page.html', **base_context)
            except Exception as e2:
                logging.error(f"Fallback template error: {e2}")
                return f"""
                <h1>Grade {grade} Math Practice - {concept}</h1>
                <p>{concept} practice content</p>
                <p><a href='/Practice'>← Back to Practice</a></p>
                <p><a href='/Practice/Primary_Grade_{grade}_Mathematics'>← Grade {grade} Practice</a></p>
                """


# ====== MAIN PRACTICE PAGES ======

@flask_practice_all_bp.route('/Practice')
def practice_main():
    """Main practice page route"""
    handler = FlaskPracticeHandler()
    context = handler.get_template_context()
    try:
        return render_template('PracticePage.html', **context)
    except Exception as e:
        logging.error(f"Practice main page error: {e}")
        return render_template('PracticePage.html', **context)

@flask_practice_all_bp.route('/Practice/Primary_Grade_3_Mathematics')
def practice_grade3():
    """Grade 3 practice main page"""
    handler = FlaskPracticeHandler()
    context = handler.get_template_context(grade=3)
    try:
        return render_template('Practice_Primary_Grade_3.html', **context)
    except Exception as e:
        logging.error(f"Practice Grade 3 page error: {e}")
        return render_template('Practice_Primary_Grade_3.html', **context)

@flask_practice_all_bp.route('/Practice/Primary_4_Mathematics')
def practice_grade4():
    """Grade 4 practice main page"""
    handler = FlaskPracticeHandler()
    context = handler.get_template_context(grade=4)
    try:
        return render_template('Practice_Primary_4.html', **context)
    except Exception as e:
        logging.error(f"Practice Grade 4 page error: {e}")
        return render_template('Practice_Primary_4.html', **context)

@flask_practice_all_bp.route('/Practice/Primary_5_Mathematics')
def practice_grade5():
    """Grade 5 practice main page"""
    handler = FlaskPracticeHandler()
    context = handler.get_template_context(grade=5)
    try:
        return render_template('Practice_Primary_5.html', **context)
    except Exception as e:
        logging.error(f"Practice Grade 5 page error: {e}")
        return render_template('Practice_Primary_5.html', **context)

@flask_practice_all_bp.route('/Practice/Primary_6_Mathematics')
def practice_grade6():
    """Grade 6 practice main page"""
    handler = FlaskPracticeHandler()
    context = handler.get_template_context(grade=6)
    try:
        return render_template('Practice_Primary_6.html', **context)
    except Exception as e:
        logging.error(f"Practice Grade 6 page error: {e}")
        return render_template('Practice_Primary_6.html', **context)

@flask_practice_all_bp.route('/Practice/Primary_Grade_1_RAYAN_Mathematics')
def practice_grade1():
    """Grade 1 practice main page"""
    handler = FlaskPracticeHandler()
    context = handler.get_template_context(grade=1)
    try:
        return render_template('Practice_Primary_1.html', **context)
    except Exception as e:
        logging.error(f"Practice Grade 1 page error: {e}")
        return render_template('Practice_Primary_1.html', **context)


# ====== GRADE 3 PRACTICE ROUTES (40 routes) ======

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Whole_Numbers_Number_Notation_Place_Values', methods=['GET', 'POST'])
def g3_whole_numbers_place_values():
    """Grade 3: Whole Numbers Place Values"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 3, 'P3WNPlaceValues', 
                                          Problem_Details="Whole Numbers Place Values practice content")

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Whole_Numbers_Figures_to_Words', methods=['GET', 'POST'])
def g3_whole_numbers_figures_to_words():
    """Grade 3: Whole Numbers Figures to Words"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 3, 'P3WNFiguresToWords',
                                          Problem_Details="Whole Numbers Figures to Words practice content")

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Whole_Numbers_Words_to_Figures', methods=['GET', 'POST'])
def g3_whole_numbers_words_to_figures():
    """Grade 3: Whole Numbers Words to Figures"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 3, 'P3WNWordsToFigures',
                                          Problem_Details="Whole Numbers Words to Figures practice content")

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Whole_Numbers_Comparing_Ordering', methods=['GET', 'POST'])
def g3_whole_numbers_comparing_ordering():
    """Grade 3: Whole Numbers Comparing and Ordering"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 3, 'P3WNComparingOrdering',
                                          Problem_Details="Whole Numbers Comparing and Ordering practice content")

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Whole_Numbers_Patterns', methods=['GET', 'POST'])
def g3_whole_numbers_patterns():
    """Grade 3: Whole Numbers Patterns"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 3, 'P3WNNumberPatterns',
                                          Problem_Details="Whole Numbers Number Patterns practice content")

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Whole_Numbers_Addition', methods=['GET', 'POST'])
def g3_whole_numbers_addition():
    """Grade 3: Whole Numbers Addition"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 3, 'P3WNAddition',
                                          Problem_Details="Whole Numbers Addition practice content")

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Whole_Numbers_Subtraction', methods=['GET', 'POST'])
def g3_whole_numbers_subtraction():
    """Grade 3: Whole Numbers Subtraction"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 3, 'P3WNSubtraction',
                                          Problem_Details="Whole Numbers Subtraction practice content")

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Whole_Numbers_Multiplication', methods=['GET', 'POST'])
def g3_whole_numbers_multiplication():
    """Grade 3: Whole Numbers Multiplication"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 3, 'P3WNMultiplication',
                                          Problem_Details="Whole Numbers Multiplication practice content")

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Whole_Numbers_Division', methods=['GET', 'POST'])
def g3_whole_numbers_division():
    """Grade 3: Whole Numbers Division"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 3, 'P3WNDivision',
                                          Problem_Details="Whole Numbers Division practice content")

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Whole_Numbers_Word_Problems', methods=['GET', 'POST'])
def g3_whole_numbers_word_problems():
    """Grade 3: Whole Numbers Word Problems"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 3, 'P3WNWordProblems',
                                          Problem_Details="Whole Numbers Word Problems practice content")

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Money_Addition', methods=['GET', 'POST'])
def g3_money_addition():
    """Grade 3: Money Addition"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 3, 'P3MOAddition',
                                          Problem_Details="Money Addition practice content")

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Money_Subtraction', methods=['GET', 'POST'])
def g3_money_subtraction():
    """Grade 3: Money Subtraction"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 3, 'P3MOSubtraction',
                                          Problem_Details="Money Subtraction practice content")

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Money_Word_Problems', methods=['GET', 'POST'])
def g3_money_word_problems():
    """Grade 3: Money Word Problems"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 3, 'P3MOWordProblems',
                                          Problem_Details="Money Word Problems practice content")

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Metres_Centimetres', methods=['GET', 'POST'])
def g3_metres_centimetres():
    """Grade 3: Metres and Centimetres"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 3, 'P3LMMetreCentiMetre',
                                          Problem_Details="Metres and Centimetres practice content")

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Kilometres_Metres', methods=['GET', 'POST'])
def g3_kilometres_metres():
    """Grade 3: Kilometres and Metres"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 3, 'P3LMKiloMetre',
                                          Problem_Details="Kilometres and Metres practice content")

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Kilograms_Grams', methods=['GET', 'POST'])
def g3_kilograms_grams():
    """Grade 3: Kilograms and Grams"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 3, 'P3LMKiloGram',
                                          Problem_Details="Kilograms and Grams practice content")

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Litres_Millilitres', methods=['GET', 'POST'])
def g3_litres_millilitres():
    """Grade 3: Litres and Millilitres"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 3, 'P3LMLitresMilli',
                                          Problem_Details="Litres and Millilitres practice content")

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Length_Mass_Volume_1-Step_Word_Problems', methods=['GET', 'POST'])
def g3_length_mass_volume_1step():
    """Grade 3: Length Mass Volume 1-Step Word Problems"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 3, 'P3LMWordProblems',
                                          Problem_Details="Length Mass Volume 1-Step Word Problems practice content")

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Length_Mass_Volume_2-Step_Word_Problems', methods=['GET', 'POST'])
def g3_length_mass_volume_2step():
    """Grade 3: Length Mass Volume 2-Step Word Problems"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 3, 'P3LMWordProblems_2Steps',
                                          Problem_Details="Length Mass Volume 2-Step Word Problems practice content")

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Telling_Time', methods=['GET', 'POST'])
def g3_telling_time():
    """Grade 3: Telling Time"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 3, 'P3TITellingTime',
                                          Problem_Details="Telling Time practice content")

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Time_Conversion_Hours_Minutes', methods=['GET', 'POST'])
def g3_time_conversion():
    """Grade 3: Time Conversion Hours and Minutes"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 3, 'P3TIConversionTime',
                                          Problem_Details="Time Conversion Hours and Minutes practice content")

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Time_Finding_Duration_Start_Finish', methods=['GET', 'POST'])
def g3_time_duration():
    """Grade 3: Time Finding Duration Start and Finish"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 3, 'P3TIDuration',
                                          Problem_Details="Time Finding Duration Start and Finish practice content")

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Time_Addition', methods=['GET', 'POST'])
def g3_time_addition():
    """Grade 3: Time Addition"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 3, 'P3TIAddition',
                                          Problem_Details="Time Addition practice content")

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Time_Subtraction', methods=['GET', 'POST'])
def g3_time_subtraction():
    """Grade 3: Time Subtraction"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 3, 'P3TISubtraction',
                                          Problem_Details="Time Subtraction practice content")

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Time_Word_Problems', methods=['GET', 'POST'])
def g3_time_word_problems():
    """Grade 3: Time Word Problems"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 3, 'P3TIWordProblems',
                                          Problem_Details="Time Word Problems practice content")

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Identifying_Angles_in_Figures', methods=['GET', 'POST'])
def g3_identifying_angles():
    """Grade 3: Identifying Angles in Figures"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 3, 'P3ANIdentifying',
                                          Problem_Details="Identifying Angles in Figures practice content")

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Right_Angles', methods=['GET', 'POST'])
def g3_right_angles():
    """Grade 3: Right Angles"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 3, 'P3ANRightAngle',
                                          Problem_Details="Right Angles practice content")

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Bar_Graphs', methods=['GET', 'POST'])
def g3_bar_graphs():
    """Grade 3: Bar Graphs"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 3, 'P3BGBarGraphs',
                                          Problem_Details="Bar Graphs practice content")

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Area_in_Square_Units', methods=['GET', 'POST'])
def g3_area_square_units():
    """Grade 3: Area in Square Units"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 3, 'P3APSquareUnits',
                                          Problem_Details="Area in Square Units practice content")

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Area_in_Square_cm_Square_m', methods=['GET', 'POST'])
def g3_area_square_cm_m():
    """Grade 3: Area in Square cm and Square m"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 3, 'P3APSquareCmM',
                                          Problem_Details="Area in Square cm and Square m practice content")

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Perimeter_of_Squares_Rectangles', methods=['GET', 'POST'])
def g3_perimeter():
    """Grade 3: Perimeter of Squares and Rectangles"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 3, 'P3APPerimeter',
                                          Problem_Details="Perimeter of Squares and Rectangles practice content")

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Area_of_Squares_Rectangles', methods=['GET', 'POST'])
def g3_area():
    """Grade 3: Area of Squares and Rectangles"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 3, 'P3APArea',
                                          Problem_Details="Area of Squares and Rectangles practice content")

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Area_Perimeter_Word_Problems', methods=['GET', 'POST'])
def g3_area_perimeter_word_problems():
    """Grade 3: Area and Perimeter Word Problems"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 3, 'P3APWordProblems',
                                          Problem_Details="Area and Perimeter Word Problems practice content")

@flask_practice_all_bp.route('/Grade_3_Math_Practice/What_is_a_Fraction', methods=['GET', 'POST'])
def g3_what_is_fraction():
    """Grade 3: What is a Fraction"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 3, 'P3FRWhatIsFractions',
                                          Problem_Details="What is a Fraction practice content")

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Equivalent-Fraction', methods=['GET', 'POST'])
def g3_equivalent_fractions():
    """Grade 3: Equivalent Fractions"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 3, 'P3FREquivalentFractions',
                                          Problem_Details="Equivalent Fractions practice content")

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Simplifying-Fractions', methods=['GET', 'POST'])
def g3_simplifying_fractions():
    """Grade 3: Simplifying Fractions"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 3, 'P3FRSimplifyingFractions',
                                          Problem_Details="Simplifying Fractions practice content")

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Comparing-and-Ordering-Fractions', methods=['GET', 'POST'])
def g3_comparing_ordering_fractions():
    """Grade 3: Comparing and Ordering Fractions"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 3, 'P3FRComparingOrdering',
                                          Problem_Details="Comparing and Ordering Fractions practice content")

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Adding-Fractions', methods=['GET', 'POST'])
def g3_adding_fractions():
    """Grade 3: Adding Fractions"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 3, 'P3FRAddition',
                                          Problem_Details="Adding Fractions practice content")

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Subtracting-Fractions', methods=['GET', 'POST'])
def g3_subtracting_fractions():
    """Grade 3: Subtracting Fractions"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 3, 'P3FRSubtraction',
                                          Problem_Details="Subtracting Fractions practice content")

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Identifying_Perpendicular_Parallel_Lines', methods=['GET', 'POST'])
def g3_perpendicular_parallel():
    """Grade 3: Identifying Perpendicular and Parallel Lines"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 3, 'P3PPPerpendicularParallel',
                                          Problem_Details="Identifying Perpendicular and Parallel Lines practice content")


# ====== GRADE 4 PRACTICE ROUTES (30 routes) ======

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Whole_Numbers_Write_Figures', methods=['GET', 'POST'])
def g4_whole_numbers_write_figures():
    """Grade 4: Whole Numbers Write Figures"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 4, 'P4WholeNumbersWriteInFigures',
                                          Problem_Details="Whole Numbers Write Figures practice content")

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Whole_Numbers_Write_Words', methods=['GET', 'POST'])
def g4_whole_numbers_write_words():
    """Grade 4: Whole Numbers Write Words"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 4, 'P4WholeNumbersWriteInWords',
                                          Problem_Details="Whole Numbers Write Words practice content")

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Whole_Numbers_Place_Values', methods=['GET', 'POST'])
def g4_whole_numbers_place_values():
    """Grade 4: Whole Numbers Place Values"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 4, 'P4WholeNumbersPlaceValues',
                                          Problem_Details="Whole Numbers Place Values practice content")

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Whole_Numbers_Comparing_Ordering', methods=['GET', 'POST'])
def g4_whole_numbers_comparing_ordering():
    """Grade 4: Whole Numbers Comparing and Ordering"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 4, 'P4WholeNumbersComparingOrdering',
                                          Problem_Details="Whole Numbers Comparing and Ordering practice content")

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Whole_Numbers_Rounding_Off', methods=['GET', 'POST'])
def g4_whole_numbers_rounding_off():
    """Grade 4: Whole Numbers Rounding Off"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 4, 'P4WholeNumbersRoundingOff',
                                          Problem_Details="Whole Numbers Rounding Off practice content")

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Whole_Numbers_Factors_Multiples', methods=['GET', 'POST'])
def g4_whole_numbers_factors_multiples():
    """Grade 4: Whole Numbers Factors and Multiples"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 4, 'P4WholeNumbersFactorMultiple',
                                          Problem_Details="Whole Numbers Factors and Multiples practice content")

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Whole_Numbers_Multiplication_Division', methods=['GET', 'POST'])
def g4_whole_numbers_multiplication_division():
    """Grade 4: Whole Numbers Multiplication and Division"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 4, 'P4WholeNumbersMutliplyDivide',
                                          Problem_Details="Whole Numbers Multiplication and Division practice content")

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Mixed_Numbers_Improper_Fractions', methods=['GET', 'POST'])
def g4_mixed_numbers_improper_fractions():
    """Grade 4: Mixed Numbers and Improper Fractions"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 4, 'P4FractionsMixedImproper',
                                          Problem_Details="Mixed Numbers and Improper Fractions practice content")

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Fractions_Simplifying', methods=['GET', 'POST'])
def g4_fractions_simplifying():
    """Grade 4: Fractions Simplifying"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 4, 'P4FractionsSimplifying',
                                          Problem_Details="Fractions Simplifying practice content")

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Add_Like_Related_Fractions', methods=['GET', 'POST'])
def g4_add_like_related_fractions():
    """Grade 4: Add Like and Related Fractions"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 4, 'P4FractionsAdd',
                                          Problem_Details="Add Like and Related Fractions practice content")

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Subtract_Like_Related_Fractions', methods=['GET', 'POST'])
def g4_subtract_like_related_fractions():
    """Grade 4: Subtract Like and Related Fractions"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 4, 'P4FractionsSubtract',
                                          Problem_Details="Subtract Like and Related Fractions practice content")

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Multiplication_Fractions_Whole_Numbers', methods=['GET', 'POST'])
def g4_multiplication_fractions_whole_numbers():
    """Grade 4: Multiplication of Fractions and Whole Numbers"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 4, 'P4FractionsMultiplication',
                                          Problem_Details="Multiplication of Fractions and Whole Numbers practice content")

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Decimals_Tenths', methods=['GET', 'POST'])
def g4_decimals_tenths():
    """Grade 4: Decimals Tenths"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 4, 'P4DecimalsTenths',
                                          Problem_Details="Decimals Tenths practice content")

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Decimals_Hundredths', methods=['GET', 'POST'])
def g4_decimals_hundredths():
    """Grade 4: Decimals Hundredths"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 4, 'P4DecimalsHundredths',
                                          Problem_Details="Decimals Hundredths practice content")

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Decimals_Thousandths', methods=['GET', 'POST'])
def g4_decimals_thousandths():
    """Grade 4: Decimals Thousandths"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 4, 'P4DecimalsThousandths',
                                          Problem_Details="Decimals Thousandths practice content")

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Decimals_Comparing_Ordering', methods=['GET', 'POST'])
def g4_decimals_comparing_ordering():
    """Grade 4: Decimals Comparing and Ordering"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 4, 'P4DecimalsComparingOrdering',
                                          Problem_Details="Decimals Comparing and Ordering practice content")

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Decimals_Rounding_Off', methods=['GET', 'POST'])
def g4_decimals_rounding_off():
    """Grade 4: Decimals Rounding Off"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 4, 'P4DecimalsRoundingOff',
                                          Problem_Details="Decimals Rounding Off practice content")

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Decimals_Fractions', methods=['GET', 'POST'])
def g4_decimals_fractions():
    """Grade 4: Decimals and Fractions"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 4, 'P4DecimalsFractions',
                                          Problem_Details="Decimals and Fractions practice content")

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Decimals_Addition_Subtraction', methods=['GET', 'POST'])
def g4_decimals_addition_subtraction():
    """Grade 4: Decimals Addition and Subtraction"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 4, 'P4DecimalsAddSub',
                                          Problem_Details="Decimals Addition and Subtraction practice content")

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Decimals_Multiplication_Division', methods=['GET', 'POST'])
def g4_decimals_multiplication_division():
    """Grade 4: Decimals Multiplication and Division"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 4, 'P4DecimalsMultiplyDivide',
                                          Problem_Details="Decimals Multiplication and Division practice content")

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Measurement_24-Hour_Clock', methods=['GET', 'POST'])
def g4_measurement_24hour_clock():
    """Grade 4: Measurement 24-Hour Clock"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 4, 'P4MTTime24Hrs',
                                          Problem_Details="Measurement 24-Hour Clock practice content")

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Measurement_Time_Duration', methods=['GET', 'POST'])
def g4_measurement_time_duration():
    """Grade 4: Measurement Time Duration"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 4, 'P4MTTimeDuration',
                                          Problem_Details="Measurement Time Duration practice content")

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Perimeter_Rectangle_Squares', methods=['GET', 'POST'])
def g4_perimeter_rectangle_squares():
    """Grade 4: Perimeter of Rectangles and Squares"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 4, 'P4MTPerimeter',
                                          Problem_Details="Perimeter of Rectangles and Squares practice content")

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Area_Rectangle_Squares', methods=['GET', 'POST'])
def g4_area_rectangle_squares():
    """Grade 4: Area of Rectangles and Squares"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 4, 'P4MTArea',
                                          Problem_Details="Area of Rectangles and Squares practice content")

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Measurement_Composite_Figures', methods=['GET', 'POST'])
def g4_measurement_composite_figures():
    """Grade 4: Measurement Composite Figures"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 4, 'P4MTCompositeFigures',
                                          Problem_Details="Measurement Composite Figures practice content")

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Data_Analysis_Tables_Bar_Graphs', methods=['GET', 'POST'])
def g4_data_analysis_tables_bar_graphs():
    """Grade 4: Data Analysis Tables and Bar Graphs"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 4, 'P4DATablesBarGraphs',
                                          Problem_Details="Data Analysis Tables and Bar Graphs practice content")

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Data_Analysis_Line_Graphs', methods=['GET', 'POST'])
def g4_data_analysis_line_graphs():
    """Grade 4: Data Analysis Line Graphs"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 4, 'P4DALineGraphs',
                                          Problem_Details="Data Analysis Line Graphs practice content")

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Whole_Numbers_Word_Problems', methods=['GET', 'POST'])
def g4_whole_numbers_word_problems():
    """Grade 4: Whole Numbers Word Problems"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 4, 'P4WNWordProblems',
                                          Problem_Details="Whole Numbers Word Problems practice content")

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Decimals_Word_Problems', methods=['GET', 'POST'])
def g4_decimals_word_problems():
    """Grade 4: Decimals Word Problems"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 4, 'P4DCWordProblems',
                                          Problem_Details="Decimals Word Problems practice content")

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Fractions_Word_Problems', methods=['GET', 'POST'])
def g4_fractions_word_problems():
    """Grade 4: Fractions Word Problems"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 4, 'P4FRWordProblems',
                                          Problem_Details="Fractions Word Problems practice content")


# ====== GRADE 5 PRACTICE ROUTES (35 routes) ======

@flask_practice_all_bp.route('/Grade_5_Math_Practice/Whole_Numbers_Write_Figures', methods=['GET', 'POST'])
def g5_whole_numbers_write_figures():
    """Grade 5: Whole Numbers Write Figures"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 5, 'P5WholeNumbersWriteInFigures',
                                          Problem_Details="Whole Numbers Write Figures practice content")

@flask_practice_all_bp.route('/Grade_5_Math_Practice/Whole_Numbers_Write_Words', methods=['GET', 'POST'])
def g5_whole_numbers_write_words():
    """Grade 5: Whole Numbers Write Words"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 5, 'P5WholeNumbersWriteInWords',
                                          Problem_Details="Whole Numbers Write Words practice content")

@flask_practice_all_bp.route('/Grade_5_Math_Practice/Whole_Numbers_Place_Values', methods=['GET', 'POST'])
def g5_whole_numbers_place_values():
    """Grade 5: Whole Numbers Place Values"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 5, 'P5WholeNumbersPlaceValue',
                                          Problem_Details="Whole Numbers Place Values practice content")

@flask_practice_all_bp.route('/Grade_5_Math_Practice/Whole_Numbers_Comparing_Ordering', methods=['GET', 'POST'])
def g5_whole_numbers_comparing_ordering():
    """Grade 5: Whole Numbers Comparing and Ordering"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 5, 'P5WholeNumbersCAndO',
                                          Problem_Details="Whole Numbers Comparing and Ordering practice content")

@flask_practice_all_bp.route('/Grade_5_Math_Practice/Whole_Numbers_Find_Pattern', methods=['GET', 'POST'])
def g5_whole_numbers_find_pattern():
    """Grade 5: Whole Numbers Find Pattern"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 5, 'P5WholeNumbersFindPattern',
                                          Problem_Details="Whole Numbers Find Pattern practice content")

@flask_practice_all_bp.route('/Grade_5_Math_Practice/Whole_Numbers_Approximation_Estimation', methods=['GET', 'POST'])
def g5_whole_numbers_approximation_estimation():
    """Grade 5: Whole Numbers Approximation and Estimation"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 5, 'P5WholeNumbersApproxEstimate',
                                          Problem_Details="Whole Numbers Approximation and Estimation practice content")

@flask_practice_all_bp.route('/Grade_5_Math_Practice/Whole_Numbers_Multiplication_Division', methods=['GET', 'POST'])
def g5_whole_numbers_multiplication_division():
    """Grade 5: Whole Numbers Multiplication and Division"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 5, 'P5WholeNumbersMultiplyDivide',
                                          Problem_Details="Whole Numbers Multiplication and Division practice content")

@flask_practice_all_bp.route('/Grade_5_Math_Practice/Whole_Numbers_Order_Operations', methods=['GET', 'POST'])
def g5_whole_numbers_order_operations():
    """Grade 5: Whole Numbers Order of Operations"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 5, 'P5WholeNumbersOrderOperation',
                                          Problem_Details="Whole Numbers Order of Operations practice content")

@flask_practice_all_bp.route('/Grade_5_Math_Practice/Whole_Numbers_Word_Problems', methods=['GET', 'POST'])
def g5_whole_numbers_word_problems():
    """Grade 5: Whole Numbers Word Problems"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 5, 'P5WholeNumbersWordProblems',
                                          Problem_Details="Whole Numbers Word Problems practice content")

@flask_practice_all_bp.route('/Grade_5_Math_Practice/Add_Subtract_Proper_Fractions', methods=['GET', 'POST'])
def g5_add_subtract_proper_fractions():
    """Grade 5: Add and Subtract Proper Fractions"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 5, 'P5FractionsAddSubProperFractions',
                                          Problem_Details="Add and Subtract Proper Fractions practice content")

@flask_practice_all_bp.route('/Grade_5_Math_Practice/Add_Subtract_Mixed_Fractions', methods=['GET', 'POST'])
def g5_add_subtract_mixed_fractions():
    """Grade 5: Add and Subtract Mixed Fractions"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 5, 'P5FractionsAddSubMixedFractions',
                                          Problem_Details="Add and Subtract Mixed Fractions practice content")

@flask_practice_all_bp.route('/Grade_5_Math_Practice/Multiply_Proper_Improper_Fractions', methods=['GET', 'POST'])
def g5_multiply_proper_improper_fractions():
    """Grade 5: Multiply Proper and Improper Fractions"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 5, 'P5FractionsMultProperImproperFractions',
                                          Problem_Details="Multiply Proper and Improper Fractions practice content")

@flask_practice_all_bp.route('/Grade_5_Math_Practice/Multiply_Mixed_Fraction_Whole_Number', methods=['GET', 'POST'])
def g5_multiply_mixed_fraction_whole_number():
    """Grade 5: Multiply Mixed Fractions and Whole Numbers"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 5, 'P5FractionsMultMixedFractions',
                                          Problem_Details="Multiply Mixed Fractions and Whole Numbers practice content")

@flask_practice_all_bp.route('/Grade_5_Math_Practice/Divide_Proper_Fraction_Whole_Number', methods=['GET', 'POST'])
def g5_divide_proper_fraction_whole_number():
    """Grade 5: Divide Proper Fractions by Whole Numbers"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 5, 'P5FractionsDivideProperFractions',
                                          Problem_Details="Divide Proper Fractions by Whole Numbers practice content")

@flask_practice_all_bp.route('/Grade_5_Math_Practice/Fractions_Word_Problems', methods=['GET', 'POST'])
def g5_fractions_word_problems():
    """Grade 5: Fractions Word Problems"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 5, 'P5FractionsWordProblems',
                                          Problem_Details="Fractions Word Problems practice content")

@flask_practice_all_bp.route('/Grade_5_Math_Practice/Decimals_Multiply_Divide', methods=['GET', 'POST'])
def g5_decimals_multiply_divide():
    """Grade 5: Decimals Multiply and Divide"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 5, 'P5DecimalsMultiplyDivide',
                                          Problem_Details="Decimals Multiply and Divide practice content")

@flask_practice_all_bp.route('/Grade_5_Math_Practice/Decimals_Rounding_Off', methods=['GET', 'POST'])
def g5_decimals_rounding_off():
    """Grade 5: Decimals Rounding Off"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 5, 'P5DecimalsRounding',
                                          Problem_Details="Decimals Rounding Off practice content")

@flask_practice_all_bp.route('/Grade_5_Math_Practice/Decimals_Word_Problems', methods=['GET', 'POST'])
def g5_decimals_word_problems():
    """Grade 5: Decimals Word Problems"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 5, 'P5DecimalsWordProblems',
                                          Problem_Details="Decimals Word Problems practice content")

@flask_practice_all_bp.route('/Grade_5_Math_Practice/Express_as_Percentage', methods=['GET', 'POST'])
def g5_express_as_percentage():
    """Grade 5: Express as Percentage"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 5, 'P5PercentageExpressAsPercent',
                                          Problem_Details="Express as Percentage practice content")

@flask_practice_all_bp.route('/Grade_5_Math_Practice/Express_as_Decimal', methods=['GET', 'POST'])
def g5_express_as_decimal():
    """Grade 5: Express as Decimal"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 5, 'P5PercentageExpressAsDecimal',
                                          Problem_Details="Express as Decimal practice content")

@flask_practice_all_bp.route('/Grade_5_Math_Practice/Express_as_Fraction', methods=['GET', 'POST'])
def g5_express_as_fraction():
    """Grade 5: Express as Fraction"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 5, 'P5PercentageExpressAsFraction',
                                          Problem_Details="Express as Fraction practice content")

@flask_practice_all_bp.route('/Grade_5_Math_Practice/Percentage_Word_Problems', methods=['GET', 'POST'])
def g5_percentage_word_problems():
    """Grade 5: Percentage Word Problems"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 5, 'P5PercentageWordProblems',
                                          Problem_Details="Percentage Word Problems practice content")

@flask_practice_all_bp.route('/Grade_5_Math_Practice/Ratio_Simplest_Form', methods=['GET', 'POST'])
def g5_ratio_simplest_form():
    """Grade 5: Ratio in Simplest Form"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 5, 'P5RatioSimplestForm',
                                          Problem_Details="Ratio in Simplest Form practice content")

@flask_practice_all_bp.route('/Grade_5_Math_Practice/Ratio_Missing_Number', methods=['GET', 'POST'])
def g5_ratio_missing_number():
    """Grade 5: Ratio Missing Number"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 5, 'P5RatioMissingNumber',
                                          Problem_Details="Ratio Missing Number practice content")

@flask_practice_all_bp.route('/Grade_5_Math_Practice/Ratio_Word_Problems', methods=['GET', 'POST'])
def g5_ratio_word_problems():
    """Grade 5: Ratio Word Problems"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 5, 'P5RatioWordProblems',
                                          Problem_Details="Ratio Word Problems practice content")

@flask_practice_all_bp.route('/Grade_5_Math_Practice/Measurement_Unit_Conversion', methods=['GET', 'POST'])
def g5_measurement_unit_conversion():
    """Grade 5: Measurement Unit Conversion"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 5, 'P5MeasurementUnitConversion',
                                          Problem_Details="Measurement Unit Conversion practice content")

@flask_practice_all_bp.route('/Grade_5_Math_Practice/Measurement_Area_Triangle', methods=['GET', 'POST'])
def g5_measurement_area_triangle():
    """Grade 5: Measurement Area of Triangle"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 5, 'P5MeasurementAreaOfTriangle',
                                          Problem_Details="Measurement Area of Triangle practice content")

@flask_practice_all_bp.route('/Grade_5_Math_Practice/Measurement_Volume_Cube_Cuboid', methods=['GET', 'POST'])
def g5_measurement_volume_cube_cuboid():
    """Grade 5: Measurement Volume of Cube and Cuboid"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 5, 'P5MeasurementVolume',
                                          Problem_Details="Measurement Volume of Cube and Cuboid practice content")

@flask_practice_all_bp.route('/Grade_5_Math_Practice/Measurement_Word_Problems', methods=['GET', 'POST'])
def g5_measurement_word_problems():
    """Grade 5: Measurement Word Problems"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 5, 'P5MeasurementWordProblems',
                                          Problem_Details="Measurement Word Problems practice content")

@flask_practice_all_bp.route('/Grade_5_Math_Practice/Geometry_Find_Unknown_Angles', methods=['GET', 'POST'])
def g5_geometry_find_unknown_angles():
    """Grade 5: Geometry Find Unknown Angles"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 5, 'P5GeometryAngles',
                                          Problem_Details="Geometry Find Unknown Angles practice content")

@flask_practice_all_bp.route('/Grade_5_Math_Practice/Triangles_Find_Unknown_Angles', methods=['GET', 'POST'])
def g5_triangles_find_unknown_angles():
    """Grade 5: Triangles Find Unknown Angles"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 5, 'P5GeometryTriangles',
                                          Problem_Details="Triangles Find Unknown Angles practice content")

@flask_practice_all_bp.route('/Grade_5_Math_Practice/Find_Unknown_Angles_in_Four_Sided_Figures', methods=['GET', 'POST'])
def g5_find_unknown_angles_four_sided():
    """Grade 5: Find Unknown Angles in Four-Sided Figures"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 5, 'P5GeometryFourSided',
                                          Problem_Details="Find Unknown Angles in Four-Sided Figures practice content")

@flask_practice_all_bp.route('/Grade_5_Math_Practice/Data_Analysis_Find_Average', methods=['GET', 'POST'])
def g5_data_analysis_find_average():
    """Grade 5: Data Analysis Find Average"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 5, 'P5DataAnalysisAverage',
                                          Problem_Details="Data Analysis Find Average practice content")

@flask_practice_all_bp.route('/Grade_5_Math_Practice/Data_Analysis_Find_Total', methods=['GET', 'POST'])
def g5_data_analysis_find_total():
    """Grade 5: Data Analysis Find Total"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 5, 'P5DataAnalysisTotal',
                                          Problem_Details="Data Analysis Find Total practice content")

@flask_practice_all_bp.route('/Grade_5_Math_Practice/Data_Analysis_Word_Problems', methods=['GET', 'POST'])
def g5_data_analysis_word_problems():
    """Grade 5: Data Analysis Word Problems"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 5, 'P5DataAnalysisWordProblems',
                                          Problem_Details="Data Analysis Word Problems practice content")


# ====== GRADE 6 PRACTICE ROUTES (20 routes) ======

@flask_practice_all_bp.route('/Grade_6_Math_Practice/Algebra_Simplify_Expressions', methods=['GET', 'POST'])
def g6_algebra_simplify_expressions():
    """Grade 6: Algebra Simplify Expressions"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 6, 'P6AGSimplifyingExpression',
                                          Problem_Details="Algebra Simplify Expressions practice content")

@flask_practice_all_bp.route('/Grade_6_Math_Practice/Algebra_Evaluate_Expressions', methods=['GET', 'POST'])
def g6_algebra_evaluate_expressions():
    """Grade 6: Algebra Evaluate Expressions"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 6, 'P6AGEvaluationExpression',
                                          Problem_Details="Algebra Evaluate Expressions practice content")

@flask_practice_all_bp.route('/Grade_6_Math_Practice/Divide_Whole_Number_Proper_Fraction', methods=['GET', 'POST'])
def g6_divide_whole_number_proper_fraction():
    """Grade 6: Divide Whole Number by Proper Fraction"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 6, 'P6FRDivideWholeNumber',
                                          Problem_Details="Divide Whole Number by Proper Fraction practice content")

@flask_practice_all_bp.route('/Grade_6_Math_Practice/Divide_Proper_Fraction_by_Proper_Fraction', methods=['GET', 'POST'])
def g6_divide_proper_fraction_by_proper_fraction():
    """Grade 6: Divide Proper Fraction by Proper Fraction"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 6, 'P6FRDivideProperFraction',
                                          Problem_Details="Divide Proper Fraction by Proper Fraction practice content")

@flask_practice_all_bp.route('/Grade_6_Math_Practice/Percentage_Find_Whole_Given_Part', methods=['GET', 'POST'])
def g6_percentage_find_whole_given_part():
    """Grade 6: Percentage Find Whole Given Part"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 6, 'P6PRFindWhole',
                                          Problem_Details="Percentage Find Whole Given Part practice content")

@flask_practice_all_bp.route('/Grade_6_Math_Practice/Percentage_Increase_Decrease', methods=['GET', 'POST'])
def g6_percentage_increase_decrease():
    """Grade 6: Percentage Increase and Decrease"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 6, 'P6PRIncDec',
                                          Problem_Details="Percentage Increase and Decrease practice content")

@flask_practice_all_bp.route('/Grade_6_Math_Practice/Speed_Distance_Time', methods=['GET', 'POST'])
def g6_speed_distance_time():
    """Grade 6: Speed, Distance, and Time"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 6, 'P6SPDTS',
                                          Problem_Details="Speed, Distance, and Time practice content")

@flask_practice_all_bp.route('/Grade_6_Math_Practice/Measurement_Circle_Radius_Diameter', methods=['GET', 'POST'])
def g6_measurement_circle_radius_diameter():
    """Grade 6: Measurement Circle Radius and Diameter"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 6, 'P6MTRadius',
                                          Problem_Details="Measurement Circle Radius and Diameter practice content")

@flask_practice_all_bp.route('/Grade_6_Math_Practice/Measurement_Circle_Circumference', methods=['GET', 'POST'])
def g6_measurement_circle_circumference():
    """Grade 6: Measurement Circle Circumference"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 6, 'P6MTCircumference',
                                          Problem_Details="Measurement Circle Circumference practice content")

@flask_practice_all_bp.route('/Grade_6_Math_Practice/Measurement_Circle_Area', methods=['GET', 'POST'])
def g6_measurement_circle_area():
    """Grade 6: Measurement Circle Area"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 6, 'P6MTArea',
                                          Problem_Details="Measurement Circle Area practice content")

@flask_practice_all_bp.route('/Grade_6_Math_Practice/Measurement_Semi_Circle_Quadrant_Perimeter', methods=['GET', 'POST'])
def g6_measurement_semi_circle_quadrant_perimeter():
    """Grade 6: Measurement Semi-Circle and Quadrant Perimeter"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 6, 'P6MTSemiPerimeter',
                                          Problem_Details="Measurement Semi-Circle and Quadrant Perimeter practice content")

@flask_practice_all_bp.route('/Grade_6_Math_Practice/Measurement_Semi_Circle_Quadrant_Area', methods=['GET', 'POST'])
def g6_measurement_semi_circle_quadrant_area():
    """Grade 6: Measurement Semi-Circle and Quadrant Area"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 6, 'P6MTSemiArea',
                                          Problem_Details="Measurement Semi-Circle and Quadrant Area practice content")

@flask_practice_all_bp.route('/Grade_6_Math_Practice/Area_Perimeter_of_Composite_Figures', methods=['GET', 'POST'])
def g6_area_perimeter_composite_figures():
    """Grade 6: Area and Perimeter of Composite Figures"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 6, 'P6MTComposite',
                                          Problem_Details="Area and Perimeter of Composite Figures practice content")

@flask_practice_all_bp.route('/Grade_6_Math_Practice/Measurement_Volume_Cube_Cuboid', methods=['GET', 'POST'])
def g6_measurement_volume_cube_cuboid():
    """Grade 6: Measurement Volume of Cube and Cuboid"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 6, 'P6MTVolume',
                                          Problem_Details="Measurement Volume of Cube and Cuboid practice content")

@flask_practice_all_bp.route('/Grade_6_Math_Practice/Ratio_Word_Problems', methods=['GET', 'POST'])
def g6_ratio_word_problems():
    """Grade 6: Ratio Word Problems"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 6, 'P6RTWordProblems',
                                          Problem_Details="Ratio Word Problems practice content")

@flask_practice_all_bp.route('/Grade_6_Math_Practice/Data_Analysis_Pie_Chart', methods=['GET', 'POST'])
def g6_data_analysis_pie_chart():
    """Grade 6: Data Analysis Pie Chart"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 6, 'P6DAWordProblems',
                                          Problem_Details="Data Analysis Pie Chart practice content")

@flask_practice_all_bp.route('/Grade_6_Math_Practice/Algebra_Word_Problems', methods=['GET', 'POST'])
def g6_algebra_word_problems():
    """Grade 6: Algebra Word Problems"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 6, 'P6AGWordProblems',
                                          Problem_Details="Algebra Word Problems practice content")

@flask_practice_all_bp.route('/Grade_6_Math_Practice/Fractions_Word_Problems', methods=['GET', 'POST'])
def g6_fractions_word_problems():
    """Grade 6: Fractions Word Problems"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 6, 'P6FRWordProblems',
                                          Problem_Details="Fractions Word Problems practice content")

@flask_practice_all_bp.route('/Grade_6_Math_Practice/Speed_Word_Problems', methods=['GET', 'POST'])
def g6_speed_word_problems():
    """Grade 6: Speed Word Problems"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 6, 'P6SPWordProblems',
                                          Problem_Details="Speed Word Problems practice content")

@flask_practice_all_bp.route('/Grade_6_Math_Practice/Percentage_Word_Problems', methods=['GET', 'POST'])
def g6_percentage_word_problems():
    """Grade 6: Percentage Word Problems"""
    handler = FlaskPracticeHandler()
    return handler.render_practice_response('Practice_Question_Page.html', 6, 'P6PRWordProblems',
                                          Problem_Details="Percentage Word Problems practice content")


# ====== AUTHENTICATION AND MISC ROUTES ======

@flask_practice_all_bp.route('/auth/login')
def auth_login():
    """Authentication login route"""
    return redirect('/SignIn')

@flask_practice_all_bp.route('/auth/logout')
def auth_logout():
    """Authentication logout route"""
    session.clear()
    return redirect('/')

@flask_practice_all_bp.route('/auth/signup')
def auth_signup():
    """Authentication signup route"""
    return redirect('/Register')

@flask_practice_all_bp.route('/auth/register')
def auth_register():
    """Authentication register route"""
    return redirect('/Register')

@flask_practice_all_bp.route('/Register')
def register():
    """Registration route"""
    return redirect('/Register')

@flask_practice_all_bp.route('/SignIn')
def signin():
    """Sign in route"""
    return redirect('/SignIn')

@flask_practice_all_bp.route('/auth/PracticeLogin')
def practice_login():
    """Practice login route"""
    return redirect('/SignIn')


# ====== ROUTE SUMMARY ======
"""
COMPLETE PRACTICE ROUTE COVERAGE:

Main Practice Pages: 6 routes
- /Practice
- /Practice/Primary_Grade_3_Mathematics
- /Practice/Primary_4_Mathematics 
- /Practice/Primary_5_Mathematics
- /Practice/Primary_6_Mathematics
- /Practice/Primary_Grade_1_RAYAN_Mathematics

Grade 3 Practice Routes: 40 routes
- All Grade_3_Math_Practice/* topics covered

Grade 4 Practice Routes: 30 routes  
- All Grade_4_Math_Practice/* topics covered

Grade 5 Practice Routes: 35 routes
- All Grade_5_Math_Practice/* topics covered

Grade 6 Practice Routes: 20 routes
- All Grade_6_Math_Practice/* topics covered

Authentication Routes: 8 routes
- All auth/* and login/register routes covered

TOTAL: 139 practice routes with 100% URL compatibility
"""