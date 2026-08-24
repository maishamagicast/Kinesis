from flask import Blueprint, jsonify, request
from app.services import load_settings, save_settings

settings_bp=Blueprint('settings',__name__)

@settings_bp.route('/settings',methods=['GET'])
def get_user_settings():
    settings=load_settings()
    return jsonify(settings), 200

@settings_bp.route('/settings', methods=['POST'])
def update_user_settings():
    data=request.get_json()
    if not data or not isinstance(data,dict): #isInstance checks if data is a dict
        return jsonify(
            {"error":"Invalid response. Expected JSON Object"}
            )

    updated_settings=save_settings(data)
    return jsonify(
        {
            "message":"Settings updated successfully",
            "settings":updated_settings
        }
    ),200