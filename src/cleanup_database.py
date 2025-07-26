#!/usr/bin/env python3
"""
Database Cleanup Script
Deletes all users and data from the datastore using same config as Flask app
"""

import os
import sys
from google.cloud import ndb

# Add the current directory to the Python path
sys.path.insert(0, os.path.dirname(__file__))

from flask_models import FlaskHomeCampusUser
from flask_config import get_config

def cleanup_all_data():
    """Delete all entities using the same configuration as the Flask app"""
    
    # Use the same configuration as the Flask app
    config = get_config()
    project = config.GOOGLE_CLOUD_PROJECT
    
    # Initialize NDB client the same way as main.py
    if not os.getenv('GAE_ENV', '').startswith('standard'):
        # Local development - same as Flask app
        client = ndb.Client(project=project)
    else:
        # Production GAE
        client = ndb.Client()
    
    print("🧹 Starting database cleanup...")
    
    with client.context():
        try:
            # Delete all FlaskHomeCampusUser entities
            print("Deleting FlaskHomeCampusUser entities...")
            users = FlaskHomeCampusUser.query()
            user_keys = users.fetch(keys_only=True)
            if user_keys:
                ndb.delete_multi(user_keys)
                print(f"✅ Deleted {len(user_keys)} user records")
            else:
                print("ℹ️  No FlaskHomeCampusUser records found")
            
            # Try to delete other common entities by kind name
            entity_kinds = [
                'HomeCampusUser',  # Original Tipfy users
                'HCStudents',
                'ProblemsTable', 
                'TestProblems',
                'HCGoals',
                'HCSubscription',
                'HCPayment',
                'HCClass',
                'HCBooks',
                'HCCommunication',
                'HCSchoolInfo',
                'HCGrade7Questions',
                'HCGrade7TestQuestions', 
                'HCGrade7TestMaster',
                'TestsMasterTable',
                'HCResetPassword'
            ]
            
            for kind in entity_kinds:
                try:
                    query = ndb.Query(kind=kind)
                    keys = query.fetch(keys_only=True)
                    if keys:
                        ndb.delete_multi(keys)
                        print(f"✅ Deleted {len(keys)} {kind} records")
                    else:
                        print(f"ℹ️  No {kind} records found")
                except Exception as e:
                    print(f"⚠️  Could not delete {kind}: {e}")
            
            print("🎉 Database cleanup completed!")
            print("💡 You can now create fresh user accounts.")
            
        except Exception as e:
            print(f"❌ Error during cleanup: {e}")
            return False
    
    return True

if __name__ == '__main__':
    print("HomeCampus Database Cleanup")
    print("=" * 40)
    
    response = input("⚠️  This will delete ALL users and data. Continue? (y/N): ")
    if response.lower() not in ['y', 'yes']:
        print("Cleanup cancelled.")
        sys.exit(0)
    
    success = cleanup_all_data()
    
    if success:
        print("\n🚀 Cleanup complete! Restart your Flask server to begin with fresh data.")
    else:
        print("\n❌ Cleanup failed. Check the error messages above.")