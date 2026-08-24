from flask import Blueprint, jsonify
from app.services import get_available_media

media_bp=Blueprint('media',__name__)

@media_bp.route('/media', methods=['GET'])
def list_media():
    media_data=get_available_media()
    return jsonify(media_data), 200