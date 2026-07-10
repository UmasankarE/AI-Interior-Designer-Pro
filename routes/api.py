from flask import Blueprint, jsonify, request
from database.models import Design, Category, Review
from database.db import db

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/designs')
def get_designs():
    """Get designs API"""
    page = request.args.get('page', 1, type=int)
    category_id = request.args.get('category')
    
    query = Design.query.filter_by(is_active=True)
    if category_id:
        query = query.filter_by(category_id=category_id)
    
    designs = query.paginate(page=page, per_page=12)
    
    return jsonify({
        'total': designs.total,
        'pages': designs.pages,
        'current_page': page,
        'designs': [{
            'id': d.id,
            'title': d.title,
            'description': d.description,
            'image_url': d.image_url,
            'price': d.price,
            'style': d.style,
            'room_type': d.room_type
        } for d in designs.items]
    })

@bp.route('/designs/<int:design_id>')
def get_design(design_id):
    """Get single design API"""
    design = Design.query.get_or_404(design_id)
    reviews = Review.query.filter_by(design_id=design_id).all()
    avg_rating = db.session.query(db.func.avg(Review.rating)).filter_by(design_id=design_id).scalar() or 0
    
    return jsonify({
        'id': design.id,
        'title': design.title,
        'description': design.description,
        'image_url': design.image_url,
        'price': design.price,
        'style': design.style,
        'room_type': design.room_type,
        'materials': design.materials,
        'furniture': design.furniture,
        'lighting': design.lighting,
        'wall_colour': design.wall_colour,
        'avg_rating': float(avg_rating),
        'review_count': len(reviews)
    })

@bp.route('/categories')
def get_categories():
    """Get categories API"""
    categories = Category.query.filter_by(is_active=True).all()
    return jsonify([{
        'id': c.id,
        'name': c.name,
        'slug': c.slug,
        'icon': c.icon,
        'image': c.image
    } for c in categories])
