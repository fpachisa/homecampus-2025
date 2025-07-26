"""
Add this cleanup route to your Flask app temporarily
"""

from flask import Blueprint, jsonify
from google.cloud import ndb
from flask_models import FlaskHomeCampusUser
import logging

cleanup_bp = Blueprint('cleanup', __name__)

@cleanup_bp.route('/admin/cleanup-database', methods=['POST'])
def cleanup_database():
    """
    DANGER: This will delete ALL user data!
    Only use in development.
    """
    try:
        deleted_counts = {}
        
        # Delete FlaskHomeCampusUser entities
        users = FlaskHomeCampusUser.query()
        user_keys = users.fetch(keys_only=True)
        if user_keys:
            ndb.delete_multi(user_keys)
            deleted_counts['FlaskHomeCampusUser'] = len(user_keys)
        else:
            deleted_counts['FlaskHomeCampusUser'] = 0
        
        # Try to delete other entities by kind
        entity_kinds = [
            'HomeCampusUser',  # Original users
            'HCStudents',
            'ProblemsTable', 
            'TestProblems',
            'HCGoals',
            'HCSubscription',
            'HCPayment'
        ]
        
        for kind in entity_kinds:
            try:
                query = ndb.Query(kind=kind)
                keys = query.fetch(keys_only=True)
                if keys:
                    ndb.delete_multi(keys)
                    deleted_counts[kind] = len(keys)
                else:
                    deleted_counts[kind] = 0
            except Exception as e:
                logging.warning(f"Could not delete {kind}: {e}")
                deleted_counts[kind] = f"Error: {e}"
        
        return jsonify({
            'success': True,
            'message': 'Database cleanup completed',
            'deleted_counts': deleted_counts
        })
        
    except Exception as e:
        logging.error(f"Cleanup error: {e}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@cleanup_bp.route('/admin/list-entities', methods=['GET']) 
def list_entities():
    """List all entities to see what exists"""
    try:
        entity_info = {}
        
        # Count FlaskHomeCampusUser
        users = FlaskHomeCampusUser.query()
        user_count = len(users.fetch(keys_only=True))
        entity_info['FlaskHomeCampusUser'] = user_count
        
        return jsonify({
            'success': True,
            'entities': entity_info
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500