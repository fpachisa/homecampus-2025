"""
Fix all Learn route template paths
Convert URL-based paths to actual template file paths
"""

def fix_template_path(url_path):
    """Convert URL path to actual template path"""
    
    # Remove /Learn/ prefix
    if url_path.startswith('/Learn/'):
        url_path = url_path[7:]
    
    # Convert Primary-Grade-X to PrimaryX
    url_path = url_path.replace('Primary-Grade-3', 'Primary3')
    url_path = url_path.replace('Primary-Grade-4', 'Primary4') 
    url_path = url_path.replace('Primary-Grade-5', 'Primary5')
    url_path = url_path.replace('Primary-Grade-6', 'Primary6')
    
    # Convert Whole-Numbers to WholeNumbers
    url_path = url_path.replace('Whole-Numbers', 'WholeNumbers')
    
    # Convert other dashed paths to camelCase
    url_path = url_path.replace('Data-Analysis', 'DataAnalysis')
    url_path = url_path.replace('Length-Mass-Volume', 'LengthMassVolume')
    url_path = url_path.replace('Perpendicular-Parallel', 'PerpendicularParallel')
    url_path = url_path.replace('Bar-Graphs', 'BarGraphs')
    
    return f'Notes/{url_path}.html'

def create_fixed_routes():
    """Create the fixed Learn routes with correct template paths"""
    
    # Read the generated routes file
    with open('/Users/farhat/Documents/AI Systems/homecampus/src/flask_learn_all_generated.py', 'r') as f:
        content = f.read()
    
    # Template path fixes for specific known issues
    template_fixes = {
        # Primary 5 specific fixes
        'Notes/Primary-Grade-5/Whole-Numbers/Word-Problems-Solving-Model-Method.html': 'Notes/Primary5/WholeNumbers/Word-Problems.html',
        'Notes/Primary-Grade-5/Whole-Numbers/Figures-to-Words.html': 'Notes/Primary5/WholeNumbers/Figures-to-Words.html',
        'Notes/Primary-Grade-5/Whole-Numbers/Words-to-Figures.html': 'Notes/Primary5/WholeNumbers/Words-to-Figures.html',
        'Notes/Primary-Grade-5/Whole-Numbers/Place-Values.html': 'Notes/Primary5/WholeNumbers/Place-Value.html',
        'Notes/Primary-Grade-5/Whole-Numbers/Comparison-Ordering-Pattern.html': 'Notes/Primary5/WholeNumbers/Comparison-Ordering-Pattern.html',
        'Notes/Primary-Grade-5/Whole-Numbers/Approximation-Estimation-Part-1.html': 'Notes/Primary5/WholeNumbers/Approximation-Estimation-Part-1.html',
        'Notes/Primary-Grade-5/Whole-Numbers/Approximation-Estimation-Part-2.html': 'Notes/Primary5/WholeNumbers/Approximation-Estimation-Part-2.html',
        'Notes/Primary-Grade-5/Whole-Numbers/Multiply-by-10-100-1000.html': 'Notes/Primary5/WholeNumbers/Multiply-by-10-100-1000.html',
        'Notes/Primary-Grade-5/Whole-Numbers/Divide-by-10-100-1000.html': 'Notes/Primary5/WholeNumbers/Divide-by-10-100-1000.html',
        'Notes/Primary-Grade-5/Whole-Numbers/Order-of-Operations.html': 'Notes/Primary5/WholeNumbers/Order-of-Operations.html',
        
        # Primary 5 Fractions
        'Notes/Primary-Grade-5/Fractions/What-Is-a-Fraction.html': 'Notes/Primary5/Fractions/What-Is-a-Fraction.html',
        'Notes/Primary-Grade-5/Fractions/Types-of-Fractions.html': 'Notes/Primary5/Fractions/Types-of-Fractions.html',
        'Notes/Primary-Grade-5/Fractions/Improper-Mixed-Fractions.html': 'Notes/Primary5/Fractions/Improper-Mixed-Fractions.html',
        'Notes/Primary-Grade-5/Fractions/Addition-Proper-Fractions.html': 'Notes/Primary5/Fractions/Addition-Proper-Fractions.html',
        'Notes/Primary-Grade-5/Fractions/Addition-Mixed-Fractions.html': 'Notes/Primary5/Fractions/Addition-Mixed-Fractions.html',
        'Notes/Primary-Grade-5/Fractions/Subtraction-Proper-Fractions.html': 'Notes/Primary5/Fractions/Subtraction-Proper-Fractions.html',
        'Notes/Primary-Grade-5/Fractions/Subtraction-Mixed-Fractions.html': 'Notes/Primary5/Fractions/Subtraction-Mixed-Fractions.html',
        'Notes/Primary-Grade-5/Fractions/Multiplication-Fractions.html': 'Notes/Primary5/Fractions/Multiplication-Fractions.html',
        'Notes/Primary-Grade-5/Fractions/Multiplication-Mixed-Fractions.html': 'Notes/Primary5/Fractions/Multiplication-Mixed-Fractions.html',
        'Notes/Primary-Grade-5/Fractions/Division-Proper-Fraction.html': 'Notes/Primary5/Fractions/Division-Proper-Fraction.html',
        
        # Primary 5 Decimals
        'Notes/Primary-Grade-5/Decimal/Multiplying-Decimal-Numbers-by-10s-100s-1000s.html': 'Notes/Primary5/Decimal/multiplying-decimal-numbers-by-10s-100s-1000s.html',
        'Notes/Primary-Grade-5/Decimal/Dividing-Decimal-Numbers-by-10s-100s-1000s.html': 'Notes/Primary5/Decimal/dividing-decimal-numbers-by-10s-100s-1000s.html',
        'Notes/Primary-Grade-5/Decimal/Rounding-Off-Decimal-Numbers.html': 'Notes/Primary5/Decimal/rounding-off-decimal-numbers.html',
        'Notes/Primary-Grade-5/Decimal/Estimation-in-Calculations-with-Decimal-Numbers.html': 'Notes/Primary5/Decimal/estimation-in-calculations-with-decimal-numbers.html',
        
        # Primary 5 Percentage  
        'Notes/Primary-Grade-5/Percentage/Introduction-to-Percentage.html': 'Notes/Primary5/Percentage/introduction-to-percentage.html',
        'Notes/Primary-Grade-5/Percentage/Percentage-and-Fraction.html': 'Notes/Primary5/Percentage/percentage-and-fraction.html',
        'Notes/Primary-Grade-5/Percentage/Percentage-and-Decimals.html': 'Notes/Primary5/Percentage/percentage-and-decimals.html',
        
        # Primary 5 Ratio
        'Notes/Primary-Grade-5/Ratio/Introduction-to-Ratio.html': 'Notes/Primary5/Ratio/introduction-to-ratio.html',
        'Notes/Primary-Grade-5/Ratio/Equivalent-Ratios.html': 'Notes/Primary5/Ratio/equivalent-ratios.html',
        'Notes/Primary-Grade-5/Ratio/Simplifying-Ratios.html': 'Notes/Primary5/Ratio/simplifying-ratios.html',
    }
    
    # Apply all template path fixes
    for old_path, new_path in template_fixes.items():
        content = content.replace(f"'{old_path}'", f"'{new_path}'")
    
    # Write the fixed content
    with open('/Users/farhat/Documents/AI Systems/homecampus/src/flask_learn_all_generated.py', 'w') as f:
        f.write(content)
    
    print(f"✅ Applied {len(template_fixes)} template path fixes")
    print("🔧 Fixed primary Learn route template paths")

if __name__ == '__main__':
    create_fixed_routes()