"""
Comprehensive Template Fix for ALL Learn Routes
Maps generated route template paths to actual existing templates
"""

import os
import re

def get_existing_templates():
    """Get all existing template files"""
    templates = []
    template_dir = '/Users/farhat/Documents/AI Systems/homecampus/src/templates/Notes'
    
    for root, dirs, files in os.walk(template_dir):
        for file in files:
            if file.endswith('.html'):
                # Get relative path from Notes/
                rel_path = os.path.relpath(os.path.join(root, file), template_dir)
                templates.append(f'Notes/{rel_path}')
    
    return templates

def create_template_mapping():
    """Create mapping from generated paths to existing templates"""
    
    existing = get_existing_templates()
    
    # Create mapping dictionary
    mapping = {}
    
    for template in existing:
        # Convert from actual template path to what generated route would try to load
        
        # Primary5/WholeNumbers/ -> Primary-Grade-5/Whole-Numbers/
        if 'Primary5/' in template:
            generated_path = template.replace('Primary5/', 'Primary-Grade-5/')
            generated_path = generated_path.replace('WholeNumbers/', 'Whole-Numbers/')
            generated_path = generated_path.replace('DataAnalysis/', 'Data-Analysis/')
            mapping[generated_path] = template
        
        # Primary4/ -> Primary-Grade-4/  
        elif 'Primary4/' in template:
            generated_path = template.replace('Primary4/', 'Primary-Grade-4/')
            generated_path = generated_path.replace('WholeNumbers/', 'Whole-Numbers/')
            generated_path = generated_path.replace('DataAnalysis/', 'Data-Analysis/')
            mapping[generated_path] = template
            
        # Primary3/ -> Primary-Grade-3/
        elif 'Primary3/' in template:
            generated_path = template.replace('Primary3/', 'Primary-Grade-3/')
            generated_path = generated_path.replace('WholeNumbers/', 'Whole-Numbers/')
            generated_path = generated_path.replace('AreaPerimeter/', 'Area-Perimeter/')
            generated_path = generated_path.replace('BarGraphs/', 'Bar-Graphs/')
            generated_path = generated_path.replace('LengthMassVolume/', 'Length-Mass-Volume/')
            generated_path = generated_path.replace('PerpendicularParallel/', 'Perpendicular-Parallel/')
            mapping[generated_path] = template
            
        # Primary6/ -> Primary-Grade-6/
        elif 'Primary6/' in template:
            generated_path = template.replace('Primary6/', 'Primary-Grade-6/')
            generated_path = generated_path.replace('DataAnalysis/', 'Data-Analysis/')
            mapping[generated_path] = template
    
    return mapping

def apply_comprehensive_fixes():
    """Apply all template fixes"""
    
    print("🔍 Analyzing existing templates...")
    existing_templates = get_existing_templates()
    print(f"Found {len(existing_templates)} existing templates")
    
    print("🗺️  Creating template mapping...")
    mapping = create_template_mapping()
    print(f"Created {len(mapping)} template mappings")
    
    # Read the generated routes file
    with open('/Users/farhat/Documents/AI Systems/homecampus/src/flask_learn_all_generated.py', 'r') as f:
        content = f.read()
    
    # Apply all mappings
    fixes_applied = 0
    for generated_path, actual_path in mapping.items():
        if f"'{generated_path}'" in content:
            content = content.replace(f"'{generated_path}'", f"'{actual_path}'")
            fixes_applied += 1
    
    # Write the fixed content
    with open('/Users/farhat/Documents/AI Systems/homecampus/src/flask_learn_all_generated.py', 'w') as f:
        f.write(content)
    
    print(f"✅ Applied {fixes_applied} comprehensive template fixes")
    
    # Print some examples of what was fixed
    print("\n📝 Example fixes applied:")
    for i, (generated, actual) in enumerate(list(mapping.items())[:5]):
        print(f"  {generated}")
        print(f"  -> {actual}")
        print()
    
    return fixes_applied

if __name__ == '__main__':
    fixes_applied = apply_comprehensive_fixes()
    print(f"🎉 Comprehensive template fix complete! Applied {fixes_applied} fixes.")
    print("🚀 Most Learn routes should now load actual content instead of 'Content updating...'")