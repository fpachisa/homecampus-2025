"""
Complete Flask Practice System - ALL Practice Routes
AUTO-GENERATED from Primary3Problems.py, Primary4Problems.py, Primary5Problems.py, Primary6Problems.py analysis
Comprehensive Practice route coverage for Grades 3-6 Mathematics
"""

from flask import Blueprint, render_template, request, session, redirect, url_for
import logging
from flask_models import get_flask_auth_context

flask_practice_all_bp = Blueprint('flask_practice_all', __name__)

def normalize_fraction_answer(answer):
    """Normalize fraction answers to handle 1/2 vs 1.0/2.0 equivalence"""
    if not answer or '/' not in answer:
        return answer.strip()
    
    try:
        # Split by / and normalize each part
        parts = answer.split('/')
        if len(parts) == 2:
            numerator = parts[0].strip()
            denominator = parts[1].strip()
            
            # Convert decimal strings to integers if they represent whole numbers
            try:
                num_float = float(numerator)
                if num_float.is_integer():
                    numerator = str(int(num_float))
            except:
                pass
                
            try:
                den_float = float(denominator)
                if den_float.is_integer():
                    denominator = str(int(den_float))
            except:
                pass
                
            return f"{numerator}/{denominator}"
    except:
        pass
    
    return answer.strip()

class FlaskPracticeHandler:
    def __init__(self):
        # Initialize practice-specific context - will get real auth context
        pass
        
    def get_template_context(self, grade=3, concept="", practice_page=""):
        """Get base template context for practice pages"""
        # Get real authentication context like homepage does
        context = get_flask_auth_context(session)
        
        # Add practice-specific context
        context.update({
            'current_url': request.url,
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
        })
        
        return context

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
    # Detect if this is an AJAX request for problem content only
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return g3_whole_numbers_place_values_content(full_page=not is_ajax)

def create_grade3_problem_content(concept_id, concept_display, generator_module, generator_class, full_page=True):
    """Generic helper function to create Grade 3 problem content"""
    logging.error(f"=== CREATE_GRADE3_PROBLEM_CONTENT CALLED FOR {concept_id} ===")
    try:
        logging.info(f"Generating {concept_id} problem, full_page={full_page}, method={request.method}")
        logging.info(f"Current session keys for {concept_id}: {[k for k in session.keys() if concept_id in k]}")
        
        # Import the problem generator dynamically
        try:
            module = __import__(generator_module, fromlist=[generator_class])
            GeneratorClass = getattr(module, generator_class)
            logging.info(f"Successfully imported {generator_class} from {generator_module}")
        except ImportError as e:
            logging.error(f"Import error for {generator_module}: {e}")
            raise
        except AttributeError as e:
            logging.error(f"Class {generator_class} not found in {generator_module}: {e}")
            raise
        
        # Get last problem type from session (mimicking memcache)
        problem_type_number = session.get(f'{concept_id}_problem_type', 0)
        
        # Convert numeric problem type to the string format expected by GenerateProblemSequential
        # For first time (0), pass 0. For subsequent calls, pass the last problem type string
        last_problem_type_string = session.get(f'{concept_id}_last_problem_type_string', None)
        
        logging.info(f"PROBLEM GENERATION DEBUG for {concept_id}:")
        logging.info(f"  problem_type_number: {problem_type_number}")
        logging.info(f"  last_problem_type_string: {last_problem_type_string}")
        logging.info(f"  Will call GenerateProblemSequential with: {0 if problem_type_number == 0 or last_problem_type_string is None else last_problem_type_string}")
        
        # Generate the problem
        try:
            generator = GeneratorClass()
            if problem_type_number == 0 or last_problem_type_string is None:
                # First time generation
                template_values = generator.GenerateProblemSequential(0)
            else:
                # Use the last generated problem type string for sequential generation
                template_values = generator.GenerateProblemSequential(last_problem_type_string)
            template_values["concept"] = concept_id
            
            # Store the maximum number of problem types for this concept
            if hasattr(generator, 'ProblemType') and generator.ProblemType:
                max_types = max(generator.ProblemType.keys())
                session[f'{concept_id}_max_problem_types'] = max_types
                logging.info(f"Stored max problem types for {concept_id}: {max_types}")
            else:
                # Fallback: try to count ProblemTypes list if available
                if hasattr(generator, 'ProblemTypes') and generator.ProblemTypes:
                    max_types = len(generator.ProblemTypes)
                    session[f'{concept_id}_max_problem_types'] = max_types
                    logging.info(f"Stored max problem types from ProblemTypes for {concept_id}: {max_types}")
            
            logging.info(f"Successfully generated problem for {concept_id}, problem_type_number={problem_type_number}")
        except Exception as e:
            logging.error(f"Error generating problem for {concept_id}: {e}")
            raise
        
        # DEBUG: Check what template_values contains
        logging.error(f"TEMPLATE_VALUES DEBUG for {concept_id}: keys={list(template_values.keys())}")
        logging.error(f"TEMPLATE_VALUES answer: {template_values.get('answer', 'NOT_FOUND')}")
        logging.error(f"TEMPLATE_VALUES problem_type: {template_values.get('problem_type', 'NOT_FOUND')}")
        
        # Store current problem info in session for answer checking
        current_answer = template_values.get('answer', '')
        current_explanation = template_values.get('explain', {}).get('explain_text', '')
        current_problem_type_string = template_values.get('problem_type', 'ProblemType1')
        
        logging.info(f"PROBLEM GENERATED for {concept_id}: type='{current_problem_type_string}', answer='{current_answer}'")
        
        session[f'{concept_id}_current_answer'] = current_answer
        session[f'{concept_id}_current_problem_type'] = problem_type_number
        session[f'{concept_id}_current_explanation'] = current_explanation
        session[f'{concept_id}_problem_type'] = problem_type_number
        session[f'{concept_id}_last_problem_type_string'] = current_problem_type_string
        
        logging.info(f"Stored session data for {concept_id}: answer='{current_answer}', type_number={problem_type_number}, type_string='{current_problem_type_string}', explanation_length={len(current_explanation) if current_explanation else 0}")
        
        # Ensure session changes are saved
        session.permanent = True
        session.modified = True
        
        # Create a temporary current_user for the problem template (needs to be compatible)
        temp_user = {
            'username': session.get('student_id', 'guest'),
            'IsParent': session.get('IsParent', False),
            'IsTeacher': session.get('IsTeacher', False),
            'authorized': session.get('authorized', True)
        }
        
        # Add required template context variables for the problem template
        template_values.update({
            'current_user': temp_user,  # Problem template needs this
            'grade': 3,
            'problems_attempted': session.get('problems_attempted', 1),
            'ConceptID': concept_id,
            'test_id': session.get('test_id', ''),
            'counter': session.get('counter', 1),
            'from_test': session.get('from_test', 'N'),
            'concept_display_full': f'Grade 3 - {concept_display}',
            'concept_display': concept_display,
            'Concept_HCScore': session.get('Concept_HCScore', 0),
            'correct_problems': session.get('correct_problems', 0),
            'Ninja_title': 'White Belt',
            'Ninja_Percentage': 10,
            'Ninja_Start': 0,
            'Ninja_End': 100,
            'SubscribeMessage': 'N',
            'practice_page': f'/Grade_3_Math_Practice/{concept_id.replace("P3", "").replace("WN", "Whole_Numbers_").replace("MO", "Money_").replace("TI", "Time_").replace("AN", "Angles_").replace("BG", "Bar_").replace("AP", "Area_").replace("FR", "Fraction_").replace("LM", "Length_Mass_Volume_").replace("PP", "Perpendicular_Parallel_")}'
        })
        
        # Get the specific template for this problem
        problem_template = template_values["template"]
        
        # Render the problem using its specific template
        problem_details = render_template(problem_template, **template_values)
        
        # Create context for the main practice page
        handler = FlaskPracticeHandler()
        practice_context = handler.get_template_context(3, concept_id, "/Practice/Primary_Grade_3_Mathematics")
        practice_context['Problem_Details'] = problem_details
        
        # Ensure current_user is properly set in practice context for consistency
        # Use the same temp_user structure for both problem and practice templates
        if not practice_context.get('current_user') or practice_context.get('current_user') is None:
            practice_context['current_user'] = temp_user
        
        # Add JavaScript variable for concept using consistent user data
        current_user = practice_context.get('current_user')
        if current_user and hasattr(current_user, 'username'):
            user_name = current_user.username
            is_parent = current_user.IsParent if hasattr(current_user, 'IsParent') else False
        elif current_user and isinstance(current_user, dict):
            user_name = current_user.get('username', 'guest')
            is_parent = current_user.get('IsParent', False)
        else:
            # Final fallback for guest users or when no user is logged in
            user_name = 'guest'
            is_parent = False
        
        concept_script = f"""<script type="text/javascript">
            var actualConcept = '{concept_id}';
            var _data = {{
                student_id: '{user_name}',
                IsParent: {str(is_parent).lower()},
                grade: {template_values.get('grade', 3)},
                complexity_level: '{template_values.get('complexity_level', 'medium')}',
                HCScore: {template_values.get('HCScore', 5)}
            }};
            console.log('Debug: actualConcept set to:', actualConcept);
            console.log('Debug: _data set to:', _data);
        </script>"""
        practice_context['Problem_Details'] = concept_script + problem_details
        
        if full_page:
            # Return full page for initial GET requests
            return render_template('Practice_Question_Page.html', **practice_context)
        else:
            # Return only problem content for AJAX requests (to avoid duplicate headers/footers)
            return concept_script + problem_details
        
    except Exception as e:
        logging.error(f"Error generating {concept_id} problem: {e}")
        import traceback
        logging.error(f"Full traceback: {traceback.format_exc()}")
        # Fallback to skeleton
        if full_page:
            handler = FlaskPracticeHandler()
            return handler.render_practice_response('Practice_Question_Page.html', 3, concept_id, 
                                                  Problem_Details=f"Error generating problem: {e}<br>Check server logs for details.")
        else:
            return f"Error generating problem: {e}. Please refresh the page."

def create_grade4_problem_content(concept_id, concept_display, generator_module, generator_class, full_page=True):
    """Generic helper function to create Grade 4 problem content"""
    logging.error(f"=== CREATE_GRADE4_PROBLEM_CONTENT CALLED FOR {concept_id} ===")
    logging.error(f"=== PARAMETERS: display='{concept_display}', module='{generator_module}', class='{generator_class}', full_page={full_page} ===")
    try:
        logging.info(f"Generating {concept_id} problem, full_page={full_page}, method={request.method}")
        logging.info(f"Current session keys for {concept_id}: {[k for k in session.keys() if concept_id in k]}")
        
        # Import the problem generator dynamically
        try:
            module = __import__(generator_module, fromlist=[generator_class])
            GeneratorClass = getattr(module, generator_class)
            logging.info(f"Successfully imported {generator_class} from {generator_module}")
        except ImportError as e:
            logging.error(f"Import error for {generator_module}: {e}")
            raise
        except AttributeError as e:
            logging.error(f"Class {generator_class} not found in {generator_module}: {e}")
            raise
        
        # Get last problem type from session (mimicking memcache)
        problem_type_number = session.get(f'{concept_id}_problem_type', 0)
        
        # Convert numeric problem type to the string format expected by GenerateProblemSequential
        # For first time (0), pass 0. For subsequent calls, pass the last problem type string
        last_problem_type_string = session.get(f'{concept_id}_last_problem_type_string', None)
        
        logging.info(f"PROBLEM GENERATION DEBUG for {concept_id}:")
        logging.info(f"  problem_type_number: {problem_type_number}")
        logging.info(f"  last_problem_type_string: {last_problem_type_string}")
        logging.info(f"  Will call GenerateProblemSequential with: {0 if problem_type_number == 0 or last_problem_type_string is None else last_problem_type_string}")
        
        # Generate the problem
        try:
            generator = GeneratorClass()
            if problem_type_number == 0 or last_problem_type_string is None:
                # First time generation
                template_values = generator.GenerateProblemSequential(0)
            else:
                # Use the last generated problem type string for sequential generation
                template_values = generator.GenerateProblemSequential(last_problem_type_string)
            template_values["concept"] = concept_id
            
            # Store the maximum number of problem types for this concept
            if hasattr(generator, 'ProblemType') and generator.ProblemType:
                max_types = max(generator.ProblemType.keys())
                session[f'{concept_id}_max_problem_types'] = max_types
                logging.info(f"Stored max problem types for {concept_id}: {max_types}")
                
            # Store the new problem type string for next sequential generation
            if template_values.get('problem_type'):
                session[f'{concept_id}_last_problem_type_string'] = template_values['problem_type']
                logging.info(f"Stored last problem type string for {concept_id}: {template_values['problem_type']}")
            
            # Update the problem type number (used for progress tracking)
            new_problem_type_number = (problem_type_number + 1)
            session[f'{concept_id}_problem_type'] = new_problem_type_number
            logging.info(f"Updated problem_type_number for {concept_id}: {new_problem_type_number}")
            
        except Exception as e:
            logging.error(f"Error calling GenerateProblemSequential for {concept_id}: {e}")
            import traceback
            logging.error(f"Full traceback: {traceback.format_exc()}")
            raise
        
        logging.info(f"Generated template values keys for {concept_id}: {list(template_values.keys())}")
        
        # DEBUG: Check what template_values contains
        logging.error(f"TEMPLATE_VALUES DEBUG for {concept_id}: keys={list(template_values.keys())}")
        logging.error(f"TEMPLATE_VALUES answer: {template_values.get('answer', 'NOT_FOUND')}")
        logging.error(f"TEMPLATE_VALUES problem_type: {template_values.get('problem_type', 'NOT_FOUND')}")
        
        # Store current problem info in session for answer checking
        current_answer = template_values.get('answer', '')
        current_explanation = template_values.get('explain', {}).get('explain_text', '')
        current_problem_type_string = template_values.get('problem_type', 'ProblemType1')
        
        logging.info(f"PROBLEM GENERATED for {concept_id}: type='{current_problem_type_string}', answer='{current_answer}'")
        
        session[f'{concept_id}_current_answer'] = current_answer
        session[f'{concept_id}_current_problem_type'] = problem_type_number
        session[f'{concept_id}_current_explanation'] = current_explanation
        session[f'{concept_id}_problem_type'] = problem_type_number
        session[f'{concept_id}_last_problem_type_string'] = current_problem_type_string
        
        logging.info(f"Stored session data for {concept_id}: answer='{current_answer}', type_number={problem_type_number}, type_string='{current_problem_type_string}', explanation_length={len(current_explanation) if current_explanation else 0}")
        
        # Store the maximum number of problem types for this concept
        if hasattr(generator, 'ProblemType') and generator.ProblemType:
            max_types = max(generator.ProblemType.keys())
            session[f'{concept_id}_max_problem_types'] = max_types
            logging.info(f"Stored max problem types for {concept_id}: {max_types}")
        else:
            # Fallback: try to count ProblemTypes list if available
            if hasattr(generator, 'ProblemTypes') and generator.ProblemTypes:
                max_types = len(generator.ProblemTypes)
                session[f'{concept_id}_max_problem_types'] = max_types
                logging.info(f"Stored max problem types from ProblemTypes for {concept_id}: {max_types}")
        
        # Ensure session changes are saved
        session.permanent = True
        session.modified = True
        
        # Create a temporary user object for the template context
        temp_user = type('TempUser', (), {
            'username': session.get('current_user', {}).get('username', 'guest'),
            'IsParent': session.get('current_user', {}).get('IsParent', False),
            'IsTeacher': session.get('current_user', {}).get('IsTeacher', False),
        })()
        
        # Add required template context
        template_values.update({
            'current_user': temp_user,  # Problem template needs this
            'grade': 4,
            'problems_attempted': session.get('problems_attempted', 1),
            'ConceptID': concept_id,
            'test_id': session.get('test_id', ''),
            'counter': session.get('counter', 1),
            'from_test': session.get('from_test', 'N'),
            'concept_display_full': f'Grade 4 - {concept_display}',
            'concept_display': concept_display,
            'Concept_HCScore': session.get('Concept_HCScore', 0),
            'correct_problems': session.get('correct_problems', 0),
            'Ninja_title': 'White Belt',
            'Ninja_Percentage': 10,
            'Ninja_Start': 0,
            'Ninja_End': 100,
            'SubscribeMessage': 'N',
            'practice_page': f'/Grade_4_Math_Practice/{concept_id.replace("P4", "").replace("WN", "Whole_Numbers_").replace("MO", "Money_").replace("TI", "Time_").replace("DC", "Decimals_").replace("FR", "Fractions_").replace("MT", "Measurement_").replace("DA", "Data_Analysis_")}'
        })
        
        # Get the specific template for this problem
        problem_template = template_values["template"]
        
        # Render the problem using its specific template
        problem_details = render_template(problem_template, **template_values)
        
        # Create context for the main practice page
        handler = FlaskPracticeHandler()
        practice_context = handler.get_template_context(4, concept_id, "/Practice/Primary_Grade_4_Mathematics")
        practice_context['Problem_Details'] = problem_details
        practice_context['problem'] = problem_details  # PracticePageSkeleton.html expects 'problem' variable
        
        # Ensure current_user is properly set in practice context for consistency
        # Use the same temp_user structure for both problem and practice templates
        if not practice_context.get('current_user') or practice_context.get('current_user') is None:
            practice_context['current_user'] = temp_user
        
        # Add JavaScript variable for concept using consistent user data
        current_user = practice_context.get('current_user')
        if current_user and hasattr(current_user, 'username'):
            user_name = current_user.username
            is_parent = current_user.IsParent if hasattr(current_user, 'IsParent') else False
        elif current_user and isinstance(current_user, dict):
            user_name = current_user.get('username', 'guest')
            is_parent = current_user.get('IsParent', False)
        else:
            # Final fallback for guest users or when no user is logged in
            user_name = 'guest'
            is_parent = False
        
        concept_script = f"""<script type="text/javascript">
            var actualConcept = '{concept_id}';
            var _data = {{
                student_id: '{user_name}',
                IsParent: {str(is_parent).lower()},
                grade: {template_values.get('grade', 4)},
                complexity_level: '{template_values.get('complexity_level', 'medium')}',
                HCScore: {template_values.get('HCScore', 5)}
            }};
            console.log('Debug: actualConcept set to:', actualConcept);
            console.log('Debug: _data set to:', _data);
        </script>"""
        
        practice_context['concept_script'] = concept_script
        
        # Return the appropriate response
        if full_page:
            # Use the same template as Grade 3 for consistent styling
            return render_template('Practice_Question_Page.html', **practice_context)
        else:
            # AJAX request - return only the problem details
            return problem_details
            
    except Exception as e:
        logging.error(f"Error generating {concept_id} problem: {e}")
        import traceback
        logging.error(f"Full traceback: {traceback.format_exc()}")
        # Fallback to skeleton
        if full_page:
            handler = FlaskPracticeHandler()
            return handler.render_practice_response('Practice_Question_Page.html', 4, concept_id, 
                                                  Problem_Details=f"Error generating problem: {e}<br>Check server logs for details.")
        else:
            return f"Error generating problem: {e}. Please refresh the page."

def g3_whole_numbers_place_values_content(full_page=True):
    """Grade 3: Whole Numbers Place Values"""
    return create_grade3_problem_content(
        'P3WNPlaceValues',
        'Place Values',
        'Problems.Primary3.WholeNumbers.P3WNPlaceValue',
        'P3WNPlaceValue',
        full_page
    )

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Whole_Numbers_Figures_to_Words', methods=['GET', 'POST'])
def g3_whole_numbers_figures_to_words():
    """Grade 3: Whole Numbers Figures to Words"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade3_problem_content(
        'P3WNFiguresToWords',
        'Figures to Words',
        'Problems.Primary3.WholeNumbers.P3WNFiguresToWords',
        'P3WNFiguresToWords',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Whole_Numbers_Words_to_Figures', methods=['GET', 'POST'])
def g3_whole_numbers_words_to_figures():
    """Grade 3: Whole Numbers Words to Figures"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade3_problem_content(
        'P3WNWordsToFigures',
        'Words to Figures',
        'Problems.Primary3.WholeNumbers.P3WNWordsToFigures',
        'P3WNWordsToFigures',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Whole_Numbers_Comparing_Ordering', methods=['GET', 'POST'])
def g3_whole_numbers_comparing_ordering():
    """Grade 3: Whole Numbers Comparing and Ordering"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade3_problem_content(
        'P3WNComparingOrdering',
        'Comparing and Ordering',
        'Problems.Primary3.WholeNumbers.P3WNComparingOrdering',
        'P3WNComparingOrdering',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Whole_Numbers_Patterns', methods=['GET', 'POST'])
def g3_whole_numbers_patterns():
    """Grade 3: Whole Numbers Patterns"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade3_problem_content(
        'P3WNNumberPatterns',
        'Number Patterns',
        'Problems.Primary3.WholeNumbers.P3WNNumberPatterns',
        'P3WNNumberPatterns',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Whole_Numbers_Addition', methods=['GET', 'POST'])
def g3_whole_numbers_addition():
    """Grade 3: Whole Numbers Addition"""
    # logging.error("FLASK ROUTE CALLED: Grade_3_Math_Practice/Whole_Numbers_Addition")
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade3_problem_content(
        'P3WNAddition',
        'Addition',
        'Problems.Primary3.WholeNumbers.P3WNAddition',
        'P3WNAddition',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Whole_Numbers_Subtraction', methods=['GET', 'POST'])
def g3_whole_numbers_subtraction():
    """Grade 3: Whole Numbers Subtraction"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade3_problem_content(
        'P3WNSubtraction',
        'Subtraction',
        'Problems.Primary3.WholeNumbers.P3WNSubtraction',
        'P3WNSubtraction',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Whole_Numbers_Multiplication', methods=['GET', 'POST'])
def g3_whole_numbers_multiplication():
    """Grade 3: Whole Numbers Multiplication"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade3_problem_content(
        'P3WNMultiplication',
        'Multiplication',
        'Problems.Primary3.WholeNumbers.P3WNMultiplication',
        'P3WNMultiplication',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Whole_Numbers_Division', methods=['GET', 'POST'])
def g3_whole_numbers_division():
    """Grade 3: Whole Numbers Division"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade3_problem_content(
        'P3WNDivision',
        'Division',
        'Problems.Primary3.WholeNumbers.P3WNDivision',
        'P3WNDivision',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Whole_Numbers_Word_Problems', methods=['GET', 'POST'])
def g3_whole_numbers_word_problems():
    """Grade 3: Whole Numbers Word Problems"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade3_problem_content(
        'P3WNWordProblems',
        'Word Problems',
        'Problems.Primary3.WholeNumbers.P3WNWordProblems',
        'P3WNWordProblems',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Money_Addition', methods=['GET', 'POST'])
def g3_money_addition():
    """Grade 3: Money Addition"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade3_problem_content(
        'P3MOAddition',
        'Money Addition',
        'Problems.Primary3.Money.P3MOAddition',
        'P3MOAddition',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Money_Subtraction', methods=['GET', 'POST'])
def g3_money_subtraction():
    """Grade 3: Money Subtraction"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade3_problem_content(
        'P3MOSubtraction',
        'Money Subtraction',
        'Problems.Primary3.Money.P3MOSubtraction',
        'P3MOSubtraction',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Money_Word_Problems', methods=['GET', 'POST'])
def g3_money_word_problems():
    """Grade 3: Money Word Problems"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade3_problem_content(
        'P3MOWordProblems',
        'Money Word Problems',
        'Problems.Primary3.Money.P3MOWordProblems',
        'P3MOWordProblems',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Metres_Centimetres', methods=['GET', 'POST'])
def g3_metres_centimetres():
    """Grade 3: Metres and Centimetres"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade3_problem_content(
        'P3LMMetreCentiMetre',
        'Metres and Centimetres',
        'Problems.Primary3.LengthMassVolume.P3LMMetreCentiMetre',
        'P3LMMetreCentiMetre',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Kilometres_Metres', methods=['GET', 'POST'])
def g3_kilometres_metres():
    """Grade 3: Kilometres and Metres"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade3_problem_content(
        'P3LMKiloMetre',
        'Kilometres and Metres',
        'Problems.Primary3.LengthMassVolume.P3LMKiloMetre',
        'P3LMKiloMetre',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Kilograms_Grams', methods=['GET', 'POST'])
def g3_kilograms_grams():
    """Grade 3: Kilograms and Grams"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade3_problem_content(
        'P3LMKiloGram',
        'Kilograms and Grams',
        'Problems.Primary3.LengthMassVolume.P3LMKiloGram',
        'P3LMKiloGram',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Litres_Millilitres', methods=['GET', 'POST'])
def g3_litres_millilitres():
    """Grade 3: Litres and Millilitres"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade3_problem_content(
        'P3LMLitresMilli',
        'Litres and Millilitres',
        'Problems.Primary3.LengthMassVolume.P3LMLitresMilli',
        'P3LMLitresMilli',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Length_Mass_Volume_1-Step_Word_Problems', methods=['GET', 'POST'])
def g3_length_mass_volume_1step():
    """Grade 3: Length Mass Volume 1-Step Word Problems"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade3_problem_content(
        'P3LMWordProblems',
        'Length Mass Volume 1-Step Word Problems',
        'Problems.Primary3.LengthMassVolume.P3LMWordProblems',
        'P3LMWordProblems',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Length_Mass_Volume_2-Step_Word_Problems', methods=['GET', 'POST'])
def g3_length_mass_volume_2step():
    """Grade 3: Length Mass Volume 2-Step Word Problems"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade3_problem_content(
        'P3LMWordProblems_2Steps',
        'Length Mass Volume 2-Step Word Problems',
        'Problems.Primary3.LengthMassVolume.P3LMWordProblems_2Steps',
        'P3LMWordProblems_2Steps',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Telling_Time', methods=['GET', 'POST'])
def g3_telling_time():
    """Grade 3: Telling Time"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade3_problem_content(
        'P3TITellingTime',
        'Telling Time',
        'Problems.Primary3.Time.P3TITellingTime',
        'P3TITellingTime',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Time_Conversion_Hours_Minutes', methods=['GET', 'POST'])
def g3_time_conversion():
    """Grade 3: Time Conversion Hours and Minutes"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade3_problem_content(
        'P3TIConversionTime',
        'Time Conversion',
        'Problems.Primary3.Time.P3TIConversionTime',
        'P3TIConversionTime',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Time_Finding_Duration_Start_Finish', methods=['GET', 'POST'])
def g3_time_duration():
    """Grade 3: Time Finding Duration Start and Finish"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade3_problem_content(
        'P3TIDuration',
        'Time Duration',
        'Problems.Primary3.Time.P3TIDuration',
        'P3TIDuration',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Time_Addition', methods=['GET', 'POST'])
def g3_time_addition():
    """Grade 3: Time Addition"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade3_problem_content(
        'P3TIAddition',
        'Time Addition',
        'Problems.Primary3.Time.P3TIAddition',
        'P3TIAddition',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Time_Subtraction', methods=['GET', 'POST'])
def g3_time_subtraction():
    """Grade 3: Time Subtraction"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade3_problem_content(
        'P3TISubtraction',
        'Time Subtraction',
        'Problems.Primary3.Time.P3TISubtraction',
        'P3TISubtraction',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Time_Word_Problems', methods=['GET', 'POST'])
def g3_time_word_problems():
    """Grade 3: Time Word Problems"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade3_problem_content(
        'P3TIWordProblems',
        'Time Word Problems',
        'Problems.Primary3.Time.P3TIWordProblems',
        'P3TIWordProblems',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Identifying_Angles_in_Figures', methods=['GET', 'POST'])
def g3_identifying_angles():
    """Grade 3: Identifying Angles in Figures"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade3_problem_content(
        'P3ANIdentifying',
        'Identifying Angles in Figures',
        'Problems.Primary3.Angles.P3ANIdentifying',
        'P3ANIdentifying',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Right_Angles', methods=['GET', 'POST'])
def g3_right_angles():
    """Grade 3: Right Angles"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade3_problem_content(
        'P3ANRightAngle',
        'Right Angles',
        'Problems.Primary3.Angles.P3ANRightAngle',
        'P3ANRightAngle',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Bar_Graphs', methods=['GET', 'POST'])
def g3_bar_graphs():
    """Grade 3: Bar Graphs"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade3_problem_content(
        'P3BGBarGraphs',
        'Bar Graphs',
        'Problems.Primary3.BarGraphs.P3BGBarGraphs',
        'P3BGBarGraphs',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Area_in_Square_Units', methods=['GET', 'POST'])
def g3_area_square_units():
    """Grade 3: Area in Square Units"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade3_problem_content(
        'P3APSquareUnits',
        'Area in Square Units',
        'Problems.Primary3.AreaPerimeter.P3APSquareUnits',
        'P3APSquareUnits',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Area_in_Square_cm_Square_m', methods=['GET', 'POST'])
def g3_area_square_cm_m():
    """Grade 3: Area in Square cm and Square m"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade3_problem_content(
        'P3APSquareCmM',
        'Area in Square cm and Square m',
        'Problems.Primary3.AreaPerimeter.P3APSquareCmM',
        'P3APSquareCmM',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Perimeter_of_Squares_Rectangles', methods=['GET', 'POST'])
def g3_perimeter():
    """Grade 3: Perimeter of Squares and Rectangles"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade3_problem_content(
        'P3APPerimeter',
        'Perimeter of Squares and Rectangles',
        'Problems.Primary3.AreaPerimeter.P3APPerimeter',
        'P3APPerimeter',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Area_of_Squares_Rectangles', methods=['GET', 'POST'])
def g3_area():
    """Grade 3: Area of Squares and Rectangles"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade3_problem_content(
        'P3APArea',
        'Area of Squares and Rectangles',
        'Problems.Primary3.AreaPerimeter.P3APArea',
        'P3APArea',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Area_Perimeter_Word_Problems', methods=['GET', 'POST'])
def g3_area_perimeter_word_problems():
    """Grade 3: Area and Perimeter Word Problems"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade3_problem_content(
        'P3APWordProblems',
        'Area and Perimeter Word Problems',
        'Problems.Primary3.AreaPerimeter.P3APWordProblems',
        'P3APWordProblems',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_3_Math_Practice/What_is_a_Fraction', methods=['GET', 'POST'])
def g3_what_is_fraction():
    """Grade 3: What is a Fraction"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade3_problem_content(
        'P3FRWhatIsFractions',
        'What is a Fraction',
        'Problems.Primary3.Fractions.P3FRWhatIsFractions',
        'P3FRWhatIsFractions',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Equivalent-Fraction', methods=['GET', 'POST'])
def g3_equivalent_fractions():
    """Grade 3: Equivalent Fractions"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade3_problem_content(
        'P3FREquivalentFractions',
        'Equivalent Fractions',
        'Problems.Primary3.Fractions.P3FREquivalentFractions',
        'P3FREquivalentFractions',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Simplifying-Fractions', methods=['GET', 'POST'])
def g3_simplifying_fractions():
    """Grade 3: Simplifying Fractions"""
    # logging.error("FLASK ROUTE CALLED: Grade_3_Math_Practice/Simplifying-Fractions")
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade3_problem_content(
        'P3FRSimplifyingFractions',
        'Simplifying Fractions',
        'Problems.Primary3.Fractions.P3FRSimplifyingFractions',
        'P3FRSimplifyingFractions',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Comparing-and-Ordering-Fractions', methods=['GET', 'POST'])
def g3_comparing_ordering_fractions():
    """Grade 3: Comparing and Ordering Fractions"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade3_problem_content(
        'P3FRComparingOrdering',
        'Comparing and Ordering Fractions',
        'Problems.Primary3.Fractions.P3FRComparingOrdering',
        'P3FRComparingOrdering',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Adding-Fractions', methods=['GET', 'POST'])
def g3_adding_fractions():
    """Grade 3: Adding Fractions"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade3_problem_content(
        'P3FRAddition',
        'Adding Fractions',
        'Problems.Primary3.Fractions.P3FRAddition',
        'P3FRAddition',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Subtracting-Fractions', methods=['GET', 'POST'])
def g3_subtracting_fractions():
    """Grade 3: Subtracting Fractions"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade3_problem_content(
        'P3FRSubtraction',
        'Subtracting Fractions',
        'Problems.Primary3.Fractions.P3FRSubtraction',
        'P3FRSubtraction',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_3_Math_Practice/Identifying_Perpendicular_Parallel_Lines', methods=['GET', 'POST'])
def g3_perpendicular_parallel():
    """Grade 3: Identifying Perpendicular and Parallel Lines"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade3_problem_content(
        'P3PPPerpendicularParallel',
        'Identifying Perpendicular and Parallel Lines',
        'Problems.Primary3.PerpendicularParallel.P3PPPerpendicularParallel',
        'P3PPPerpendicularParallel',
        full_page=not is_ajax
    )


# ====== GRADE 4 PRACTICE ROUTES (30 routes) ======

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Whole_Numbers_Write_Figures', methods=['GET', 'POST'])
def g4_whole_numbers_write_figures():
    """Grade 4: Whole Numbers Write Figures"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade4_problem_content(
        'P4WholeNumbersWriteInFigures',
        'Write in Figures',
        'Problems.Primary4.WholeNumbers.WriteInFigures',
        'WriteInFigures',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Whole_Numbers_Write_Words', methods=['GET', 'POST'])
def g4_whole_numbers_write_words():
    """Grade 4: Whole Numbers Write Words"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade4_problem_content(
        'P4WholeNumbersWriteInWords',
        'Write in Words',
        'Problems.Primary4.WholeNumbers.WriteInWords',
        'WriteInWords',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Whole_Numbers_Place_Values', methods=['GET', 'POST'])
def g4_whole_numbers_place_values():
    """Grade 4: Whole Numbers Place Values"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade4_problem_content(
        'P4WholeNumbersPlaceValues',
        'Place Values',
        'Problems.Primary4.WholeNumbers.PlaceValue',
        'PlaceValue',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Whole_Numbers_Comparing_Ordering', methods=['GET', 'POST'])
def g4_whole_numbers_comparing_ordering():
    """Grade 4: Whole Numbers Comparing and Ordering"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade4_problem_content(
        'P4WholeNumbersComparingOrdering',
        'Comparing and Ordering',
        'Problems.Primary4.WholeNumbers.ComparingAndOrdering',
        'ComparingAndOrdering',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Whole_Numbers_Rounding_Off', methods=['GET', 'POST'])
def g4_whole_numbers_rounding_off():
    """Grade 4: Whole Numbers Rounding Off"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade4_problem_content(
        'P4WholeNumbersRoundingOff',
        'Rounding Off',
        'Problems.Primary4.WholeNumbers.RoundingOff',
        'RoundingOff',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Whole_Numbers_Factors_Multiples', methods=['GET', 'POST'])
def g4_whole_numbers_factors_multiples():
    """Grade 4: Whole Numbers Factors and Multiples"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade4_problem_content(
        'P4WholeNumbersFactorMultiple',
        'Factors and Multiples',
        'Problems.Primary4.WholeNumbers.FactorMultiple',
        'FactorMultiple',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Whole_Numbers_Multiplication_Division', methods=['GET', 'POST'])
def g4_whole_numbers_multiplication_division():
    """Grade 4: Whole Numbers Multiplication and Division"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade4_problem_content(
        'P4WholeNumbersMutliplyDivide',
        'Multiplication and Division',
        'Problems.Primary4.WholeNumbers.MultiplicationDivision',
        'MultiplicationDivision',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Mixed_Numbers_Improper_Fractions', methods=['GET', 'POST'])
def g4_mixed_numbers_improper_fractions():
    """Grade 4: Mixed Numbers and Improper Fractions"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade4_problem_content(
        'P4FractionsMixedImproper',
        'Mixed Numbers and Improper Fractions',
        'Problems.Primary4.Fractions.MixedNumbersImproperFractions',
        'MixedNumbersImproperFractions',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Fractions_Simplifying', methods=['GET', 'POST'])
def g4_fractions_simplifying():
    """Grade 4: Fractions Simplifying"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade4_problem_content(
        'P4FractionsSimplifying',
        'Fractions Simplifying',
        'Problems.Primary4.Fractions.SimplifyingFractions',
        'SimplifyingFractions',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Add_Like_Related_Fractions', methods=['GET', 'POST'])
def g4_add_like_related_fractions():
    """Grade 4: Add Like and Related Fractions"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade4_problem_content(
        'P4FractionsAdd',
        'Add Like and Related Fractions',
        'Problems.Primary4.Fractions.AddLikeRelatedFractions',
        'AddLikeRelatedFractions',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Subtract_Like_Related_Fractions', methods=['GET', 'POST'])
def g4_subtract_like_related_fractions():
    """Grade 4: Subtract Like and Related Fractions"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade4_problem_content(
        'P4FractionsSubtract',
        'Subtract Like and Related Fractions',
        'Problems.Primary4.Fractions.SubtractLikeRelatedFractions',
        'SubtractLikeRelatedFractions',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Multiplication_Fractions_Whole_Numbers', methods=['GET', 'POST'])
def g4_multiplication_fractions_whole_numbers():
    """Grade 4: Multiplication of Fractions and Whole Numbers"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade4_problem_content(
        'P4FractionsMultiplication',
        'Multiplication of Fractions and Whole Numbers',
        'Problems.Primary4.Fractions.MultiplyProperImproperFractions',
        'MultiplyProperImproperFractions',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Decimals_Tenths', methods=['GET', 'POST'])
def g4_decimals_tenths():
    """Grade 4: Decimals Tenths"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade4_problem_content(
        'P4DecimalsTenths',
        'Decimals Tenths',
        'Problems.Primary4.Decimals.DecimalsTenths',
        'DecimalsTenths',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Decimals_Hundredths', methods=['GET', 'POST'])
def g4_decimals_hundredths():
    """Grade 4: Decimals Hundredths"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade4_problem_content(
        'P4DecimalsHundredths',
        'Decimals Hundredths',
        'Problems.Primary4.Decimals.DecimalsHundredths',
        'DecimalsHundredths',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Decimals_Thousandths', methods=['GET', 'POST'])
def g4_decimals_thousandths():
    """Grade 4: Decimals Thousandths"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade4_problem_content(
        'P4DecimalsThousandths',
        'Decimals Thousandths',
        'Problems.Primary4.Decimals.DecimalsThousandths',
        'DecimalsThousandths',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Decimals_Comparing_Ordering', methods=['GET', 'POST'])
def g4_decimals_comparing_ordering():
    """Grade 4: Decimals Comparing and Ordering"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade4_problem_content(
        'P4DecimalsComparingOrdering',
        'Decimals Comparing and Ordering',
        'Problems.Primary4.Decimals.DecimalsComparingOrdering',
        'DecimalsComparingOrdering',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Decimals_Rounding_Off', methods=['GET', 'POST'])
def g4_decimals_rounding_off():
    """Grade 4: Decimals Rounding Off"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade4_problem_content(
        'P4DecimalsRoundingOff',
        'Decimals Rounding Off',
        'Problems.Primary4.Decimals.DecimalsRoundingOff',
        'DecimalsRoundingOff',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Decimals_Fractions', methods=['GET', 'POST'])
def g4_decimals_fractions():
    """Grade 4: Decimals and Fractions"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade4_problem_content(
        'P4DecimalsFractions',
        'Decimals and Fractions',
        'Problems.Primary4.Decimals.DecimalsFractions',
        'DecimalsFractions',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Decimals_Addition_Subtraction', methods=['GET', 'POST'])
def g4_decimals_addition_subtraction():
    """Grade 4: Decimals Addition and Subtraction"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade4_problem_content(
        'P4DecimalsAddSub',
        'Decimals Addition and Subtraction',
        'Problems.Primary4.Decimals.DecimalsAddSub',
        'DecimalsAddSub',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Decimals_Multiplication_Division', methods=['GET', 'POST'])
def g4_decimals_multiplication_division():
    """Grade 4: Decimals Multiplication and Division"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade4_problem_content(
        'P4DecimalsMultiplyDivide',
        'Decimals Multiplication and Division',
        'Problems.Primary4.Decimals.DecimalsMultiplyDivide',
        'DecimalsMultiplyDivide',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Measurement_24-Hour_Clock', methods=['GET', 'POST'])
def g4_measurement_24hour_clock():
    """Grade 4: Measurement 24-Hour Clock"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade4_problem_content(
        'P4MTTime24Hrs',
        'Measurement 24-Hour Clock',
        'Problems.Primary4.Measurement.MTTime24Hrs',
        'MTTime24Hrs',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Measurement_Time_Duration', methods=['GET', 'POST'])
def g4_measurement_time_duration():
    """Grade 4: Measurement Time Duration"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade4_problem_content(
        'P4MTTimeDuration',
        'Measurement Time Duration',
        'Problems.Primary4.Measurement.MTTimeDuration',
        'MTTimeDuration',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Perimeter_Rectangle_Squares', methods=['GET', 'POST'])
def g4_perimeter_rectangle_squares():
    """Grade 4: Perimeter of Rectangles and Squares"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade4_problem_content(
        'P4MTPerimeter',
        'Perimeter of Rectangles and Squares',
        'Problems.Primary4.Measurement.MTPerimeter',
        'MTPerimeter',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Area_Rectangle_Squares', methods=['GET', 'POST'])
def g4_area_rectangle_squares():
    """Grade 4: Area of Rectangles and Squares"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade4_problem_content(
        'P4MTArea',
        'Area of Rectangles and Squares',
        'Problems.Primary4.Measurement.MTArea',
        'MTArea',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Measurement_Composite_Figures', methods=['GET', 'POST'])
def g4_measurement_composite_figures():
    """Grade 4: Measurement Composite Figures"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade4_problem_content(
        'P4MTCompositeFigures',
        'Measurement Composite Figures',
        'Problems.Primary4.Measurement.MTCompositeFigures',
        'MTCompositeFigures',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Data_Analysis_Tables_Bar_Graphs', methods=['GET', 'POST'])
def g4_data_analysis_tables_bar_graphs():
    """Grade 4: Data Analysis Tables and Bar Graphs"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade4_problem_content(
        'P4DATablesBarGraphs',
        'Data Analysis Tables and Bar Graphs',
        'Problems.Primary4.DataAnalysis.P4DATablesBarGraphs',
        'P4DATablesBarGraphs',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Data_Analysis_Line_Graphs', methods=['GET', 'POST'])
def g4_data_analysis_line_graphs():
    """Grade 4: Data Analysis Line Graphs"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade4_problem_content(
        'P4DALineGraphs',
        'Data Analysis Line Graphs',
        'Problems.Primary4.DataAnalysis.P4DALineGraphs',
        'P4DALineGraphs',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Whole_Numbers_Word_Problems', methods=['GET', 'POST'])
def g4_whole_numbers_word_problems():
    """Grade 4: Whole Numbers Word Problems"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade4_problem_content(
        'P4WNWordProblems',
        'Whole Numbers Word Problems',
        'Problems.Primary4.WholeNumbers.P4WNWordProblems',
        'P4WNWordProblems',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Decimals_Word_Problems', methods=['GET', 'POST'])
def g4_decimals_word_problems():
    """Grade 4: Decimals Word Problems"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade4_problem_content(
        'P4DCWordProblems',
        'Decimals Word Problems',
        'Problems.Primary4.Decimals.P4DCWordProblems',
        'P4DCWordProblems',
        full_page=not is_ajax
    )

@flask_practice_all_bp.route('/Grade_4_Math_Practice/Fractions_Word_Problems', methods=['GET', 'POST'])
def g4_fractions_word_problems():
    """Grade 4: Fractions Word Problems"""
    is_ajax = request.method == 'POST' and not request.form.get('answer')
    return create_grade4_problem_content(
        'P4FRWordProblems',
        'Fractions Word Problems',
        'Problems.Primary4.Fractions.P4FRWordProblems',
        'P4FRWordProblems',
        full_page=not is_ajax
    )


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

# Practice Answer Submission Endpoint
@flask_practice_all_bp.route('/submit', methods=['POST'])
def submit_practice_answer():
    """Handle practice problem answer submission"""
    logging.error(f"=== SUBMIT_PRACTICE_ANSWER CALLED ===")
    try:
        # Get form data
        answer = request.form.get('answer', '').strip()
        student_id = request.form.get('student_id', 'guest')
        grade = int(request.form.get('grade', 3))
        time_taken = request.form.get('time_taken', '0')
        complexity_level = request.form.get('complexity_level', 'medium')
        hc_score = int(request.form.get('HCScore', 5))
        concept = request.form.get('concept', '')
        
        logging.error(f"SUBMIT DEBUG: answer='{answer}', concept='{concept}'")
        logging.error(f"ALL SESSION KEYS: {list(session.keys())}")
        logging.error(f"SESSION KEYS CONTAINING {concept}: {[k for k in session.keys() if concept in k]}")
        logging.error(f"SESSION VALUE current_answer: {session.get(f'{concept}_current_answer')}")
        logging.error(f"SESSION VALUE current_explanation: {session.get(f'{concept}_current_explanation')}")
        logging.error(f"SESSION VALUE current_problem_type: {session.get(f'{concept}_current_problem_type')}")
        
        logging.info(f"Submit answer: {answer} for concept: {concept} by student: {student_id}")
        logging.info(f"Session keys: {list(session.keys())}")
        logging.info(f"Session current_answer for {concept}: {session.get(f'{concept}_current_answer')}")
        logging.info(f"Session current_explanation available for {concept}: {bool(session.get(f'{concept}_current_explanation'))}")
        logging.info(f"All session keys starting with {concept}: {[k for k in session.keys() if k.startswith(concept)]}")
        
        # Get current problem from session to check answer - handle all Grade 3 and Grade 4 concepts generically
        if concept.startswith('P3') or concept.startswith('P4'):
            # Get the CURRENT displayed problem's answer and explanation from session
            current_problem_answer = session.get(f'{concept}_current_answer')
            current_problem_type = session.get(f'{concept}_current_problem_type')
            current_explanation = session.get(f'{concept}_current_explanation')
            
            if current_problem_answer is None:
                # No current problem in session - return error
                logging.error(f"No current problem data found in session for concept: {concept}")
                logging.error(f"Available session keys: {list(session.keys())}")
                correct_answer = ''
                problem_text = f"{concept} problem"
                explanation_text = f'No problem data found in session for {concept}. Please refresh the page.'
            else:
                # Handle different answer formats: string, list (MCQ), etc.
                if isinstance(current_problem_answer, list):
                    # MCQ format - check if it's [index, num, den] format for fractions
                    if len(current_problem_answer) >= 3:
                        # Format: [index, numerator, denominator] -> convert to fraction string
                        correct_answer = f"{current_problem_answer[1]}/{current_problem_answer[2]}"
                        logging.error(f"MCQ FORMAT DETECTED: {current_problem_answer} -> converted to '{correct_answer}'")
                    else:
                        # Other list format - use as string
                        correct_answer = str(current_problem_answer)
                else:
                    correct_answer = str(current_problem_answer)
                problem_text = f"{concept} problem"
                explanation_text = current_explanation or 'No explanation available'
            
            # Check for empty submitted answer first
            if not answer.strip():
                is_correct = False
                normalized_submitted = ""
                normalized_correct = normalize_fraction_answer(correct_answer.lower().strip())
                logging.error(f"ANSWER COMPARISON DEBUG: Empty answer submitted")
            else:
                # Normalize both answers for comparison (handle 1/2 vs 1.0/2.0)
                normalized_submitted = normalize_fraction_answer(answer.lower().strip())
                normalized_correct = normalize_fraction_answer(correct_answer.lower().strip())
                is_correct = normalized_submitted == normalized_correct
            
            logging.error(f"ANSWER COMPARISON DEBUG: submitted='{answer}' -> normalized='{normalized_submitted}'")
            logging.error(f"ANSWER COMPARISON DEBUG: correct='{correct_answer}' -> normalized='{normalized_correct}'")
            logging.error(f"ANSWER COMPARISON DEBUG: is_correct={is_correct}")
            logging.info(f"Answer comparison: '{answer}' vs '{correct_answer}' -> {is_correct}")
            
            if is_correct:
                # Correct answer response
                correctness = "Correct"
                concept_id = concept
                answer_text = f"Great job! The correct answer is {str(correct_answer)}."
                
                # For correct answers, use the detailed explanation from the second part
                if explanation_text and 'ANSWERSEPARATOR' in explanation_text:
                    parts = explanation_text.split('ANSWERSEPARATOR')
                    explanation = parts[1] if len(parts) > 1 else explanation_text
                else:
                    explanation = explanation_text or 'Well done!'
                
                # Update session with incremented problem type for next problem
                # Use the persistent problem_type, not the current_problem_type that gets cleared
                current_type = session.get(f'{concept}_problem_type', 0)
                
                # Get the maximum problem types for this concept (stored when problem was first generated)
                max_problem_types = session.get(f'{concept}_max_problem_types', 8)  # 8 as fallback
                
                logging.error(f"SUBMIT DEBUG for {concept}: current_type={current_type}, max_types={max_problem_types}")
                
                # Cycle through problem types dynamically based on actual available types
                # Ensure we cycle from 1 to max_problem_types, never 0
                next_type = (int(current_type) % max_problem_types) + 1
                session[f'{concept}_problem_type'] = next_type
                logging.error(f"SUBMIT DEBUG: Updated problem type from {current_type} to {next_type} for {concept}")
                session['problems_attempted'] = int(session.get('problems_attempted', 0)) + 1
                session['correct_problems'] = int(session.get('correct_problems', 0)) + 1
                
                # Clear current problem from session so a new one is generated
                session.pop(f'{concept}_current_answer', None)
                session.pop(f'{concept}_current_problem_type', None)
                session.pop(f'{concept}_current_explanation', None)
                # Keep the last_problem_type_string for sequential generation
                
                # Ensure session changes are saved
                session.modified = True
                logging.info(f"Cleared session data for {concept} after correct answer")
                
            else:
                # Incorrect answer response  
                correctness = "InCorrect"
                concept_id = concept
                
                # Split the explanation_text which contains "answer_text + ANSWERSEPARATOR + solution_text"
                if explanation_text and 'ANSWERSEPARATOR' in explanation_text:
                    parts = explanation_text.split('ANSWERSEPARATOR')
                    # answer_text = Simple message shown immediately when wrong (first part)
                    answer_text = parts[0] if len(parts) > 0 else f"The correct answer is:<br>{correct_answer}"
                    # explanation = Detailed explanation shown when "Explanation" button is clicked (second part)
                    explanation = parts[1] if len(parts) > 1 else explanation_text
                else:
                    # Fallback if no separator found
                    answer_text = f"The correct answer is:<br>{correct_answer}"
                    explanation = explanation_text or 'No detailed explanation available'
                
                # Update session
                session['problems_attempted'] = int(session.get('problems_attempted', 0)) + 1
            
            # Format response as expected by JavaScript
            response = f"{correctness}ANSWERSEPARATOR{concept_id}ANSWERSEPARATOR{answer_text}ANSWERSEPARATOR{explanation}"
            return response
            
        else:
            # Default response for unknown concepts
            return "InCorrectANSWERSEPARATORUnknownConceptANSWERSEPARATORSorry, this concept is not yet supported.ANSWERSEPARATORPlease try a different problem type."
            
    except Exception as e:
        logging.error(f"Error in submit_practice_answer: {e}")
        return "Show error message"