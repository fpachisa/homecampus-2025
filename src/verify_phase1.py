#!/usr/bin/env python3
"""
Phase 1 Verification Script
HomeCampus Python 3 Migration

This script verifies that Phase 1 setup is complete without requiring
Flask dependencies to be installed yet.
"""

import os
import sys

def check_python_version():
    """Check if Python 3 is being used"""
    version = sys.version_info
    if version.major >= 3:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} detected")
        return True
    else:
        print(f"❌ Python 2 detected: {version.major}.{version.minor}")
        return False

def check_files_exist():
    """Check if all Phase 1 files were created"""
    required_files = [
        'main.py',
        'flask_config.py', 
        'requirements.txt',
        'app_python3.yaml'
    ]
    
    missing_files = []
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file} exists")
        else:
            print(f"❌ {file} missing")
            missing_files.append(file)
    
    return len(missing_files) == 0

def check_syntax():
    """Check if Python files have valid syntax"""
    python_files = ['main.py', 'flask_config.py']
    
    for file in python_files:
        try:
            with open(file, 'r') as f:
                compile(f.read(), file, 'exec')
            print(f"✅ {file} syntax valid")
        except SyntaxError as e:
            print(f"❌ {file} syntax error: {e}")
            return False
        except FileNotFoundError:
            print(f"❌ {file} not found")
            return False
    
    return True

def check_config_compatibility():
    """Check if new Flask config can access old Tipfy config"""
    try:
        # This should work even without Flask installed
        import Config
        print("✅ Original Config.py accessible")
        
        # Check if flask_config can import it
        import flask_config
        print("✅ Flask config compatibility layer working")
        
        # Check if we can access the Tipfy config through Flask config
        config_class = flask_config.FlaskConfig
        secret_key = config_class.SECRET_KEY
        print(f"✅ Secret key accessible: {secret_key[:10]}...")
        return True
    except Exception as e:
        print(f"❌ Config compatibility issue: {e}")
        return False

def main():
    """Run all Phase 1 verification checks"""
    print("HomeCampus Python 3 Migration - Phase 1 Verification")
    print("=" * 50)
    
    checks = [
        ("Python Version", check_python_version),
        ("Required Files", check_files_exist),
        ("Python Syntax", check_syntax),
        ("Config Compatibility", check_config_compatibility)
    ]
    
    passed = 0
    total = len(checks)
    
    for name, check_func in checks:
        print(f"\n{name}:")
        if check_func():
            passed += 1
        
    print("\n" + "=" * 50)
    print(f"Phase 1 Verification: {passed}/{total} checks passed")
    
    if passed == total:
        print("🎉 Phase 1 setup is COMPLETE!")
        print("\nNext steps:")
        print("1. Install dependencies: pip install -r requirements.txt")
        print("2. Test Flask app: python main.py")
        print("3. Begin Phase 2: Framework migration")
    else:
        print("⚠️  Phase 1 setup needs attention")
        print("Please fix the issues above before proceeding to Phase 2")

if __name__ == '__main__':
    main()