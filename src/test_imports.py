#!/usr/bin/env python3
"""
Test script to verify Python 2 library conflicts are resolved
"""

import sys
import os

def test_import_paths():
    """Test that we're not importing Python 2 libraries"""
    print("Python version:", sys.version)
    print("Python path:")
    for i, path in enumerate(sys.path):
        print(f"  {i}: {path}")
    
    # Test that we don't import the old libraries
    old_libs = ['werkzeug', 'jinja2', 'wtforms', 'tipfy', 'babel', 'blinker', 'simplejson', 'pytz']
    
    print("\nTesting import conflicts:")
    for lib in old_libs:
        try:
            if lib == 'tipfy':
                # We expect Tipfy to fail (it's Python 2 only)
                print(f"  {lib}: Expected to fail (Python 2 only)")
                continue
                
            module = __import__(lib)
            module_file = getattr(module, '__file__', 'unknown')
            
            if 'python2_libs_backup' in module_file:
                print(f"  ❌ {lib}: Still importing from backup directory")
            elif 'site-packages' in module_file or 'venv' in module_file:
                print(f"  ✅ {lib}: Importing from virtual environment")
            else:
                print(f"  ⚠️ {lib}: Importing from {module_file}")
                
        except ImportError as e:
            if lib in ['wtforms', 'babel', 'blinker', 'simplejson', 'pytz']:
                print(f"  ⚠️ {lib}: Not installed in venv ({e})")
            else:
                print(f"  ✅ {lib}: Import blocked (expected)")
        except Exception as e:
            print(f"  ❌ {lib}: Error - {e}")

def test_config_import():
    """Test that our Config import still works"""
    try:
        import Config
        print(f"\n✅ Config.py import successful")
        print(f"   Config keys: {list(Config.config.keys())}")
    except Exception as e:
        print(f"\n❌ Config.py import failed: {e}")

if __name__ == '__main__':
    test_import_paths()
    test_config_import()
    
    print("\n" + "="*50)
    print("To test Flask app:")
    print("1. Activate your virtual environment: source venv/bin/activate")
    print("2. Install missing dependencies if needed: pip install Flask Flask-WTF")
    print("3. Run: python main.py")