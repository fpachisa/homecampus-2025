#!/usr/bin/env python3
"""
Quick fix for missing pkg_resources dependency
"""

import subprocess
import sys

def install_missing_packages():
    """Install missing packages that are needed"""
    packages_to_install = [
        'setuptools',  # Provides pkg_resources
        'wheel',       # Modern Python packaging
        'pip',         # Ensure pip is up to date
    ]
    
    for package in packages_to_install:
        try:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', package])
            print(f"✅ {package} installed successfully")
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install {package}: {e}")
            return False
    
    return True

def test_imports():
    """Test if the problematic imports now work"""
    try:
        import pkg_resources
        print("✅ pkg_resources import successful")
        
        from google.cloud import ndb
        print("✅ google.cloud.ndb import successful")
        
        return True
    except ImportError as e:
        print(f"❌ Import still failing: {e}")
        return False

if __name__ == '__main__':
    print("Fixing missing dependencies...")
    
    if install_missing_packages():
        print("\nTesting imports...")
        if test_imports():
            print("\n🎉 Dependencies fixed! Try running 'python main.py' again")
        else:
            print("\n⚠️ Some imports still failing. You may need to reinstall google-cloud-ndb")
    else:
        print("\n❌ Failed to install required packages")