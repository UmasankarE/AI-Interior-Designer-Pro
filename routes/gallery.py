from flask import Blueprint, render_template, request, jsonify
from flask_login import current_user, login_required
from database.db import db
from database.models import Design, Category, Wishlist, Review
from sqlalchemy import or_, and_

bp = Blueprint('gallery', __name__, url_prefix='/gallery')

@bp.route('/')
def index():
    """Design gallery"""
    page = request.args.get('page', 1, type=int)
    category_id = request.args.get('category')
    search = request.args.get('search', '').strip()
    style = request.args.get('style')
    room_type = request.args.get('room_type')
    sort_by = request.args.get('sort', 'recent')
    
    # Build query
    query = Design.query.filter_by(is_active=True)
    
    if category_id:
        query = query.filter_by(category_id=category_id)
    
    if search:
        query = query.filter(or_(
            Design.title.ilike(f'%{search}%'),
            Design.description.ilike(f'%{search}%')
        ))
    
    if style:
        query = query.filter_by(style=style)
    
    if room_type:
        query = query.filter_by(room_type=room_type)
    
    # Sort
    if sort_by == 'popular':
        query = query.order_by(Design.views_count.desc())
    elif sort_by == 'rating':
        # Join with reviews and sort by average rating
        query = query.outerjoin(Review).group_by(Design.id).order_by(
            db.func.avg(Review.rating).desc()
        )
    elif sort_by == 'price_low':
        query = query.order_by(Design.price.asc())
    elif sort_by == 'price_high':
        query = query.order_by(Design.price.desc())
    else:  # recent
        query = query.order_by(Design.created_at.desc())
    
    designs = query.paginate(page=page, per_page=12)
    categories = Category.query.filter_by(is_active=True).all()
    styles = Design.query.filter_by(is_active=True).with_entities(Design.style).distinct().all()
    room_types = Design.query.filter_by(is_active=True).with_entities(Design.room_type).distinct().all()
    
    return render_template('gallery/index.html',
                         designs=designs,
                         categories=categories,
                         styles=[s[0] for s in styles if s[0]],
                         room_types=[r[0] for r in room_types if r[0]],
                         current_category=category_id,
                         current_search=search,
                         current_style=style,
                         current_room_type=room_type,
                         current_sort=sort_by)

@bp.route('/<int:design_id>/like', methods=['POST'])
@login_required
def like_design(design_id):
    """Like design"""
    design = Design.query.get_or_404(design_id)
    
    wishlist = Wishlist.query.filter_by(user_id=current_user.id, design_id=design_id).first()
    
    if wishlist:
        db.session.delete(wishlist)
        is_liked = False
    else:
        wishlist = Wishlist(user_id=current_user.id, design_id=design_id)
        db.session.add(wishlist)
        is_liked = True
    
    db.session.commit()
    
    return jsonify({'success': True, 'is_liked': is_liked})

@bp.route('/<int:design_id>/view')
def view_design(design_id):
    """View design details"""
    design = Design.query.get_or_404(design_id)
    
    # Increment views
    design.views_count += 1
    db.session.commit()
    
    # Get reviews
    reviews = Review.query.filter_by(design_id=design_id).order_by(Review.created_at.desc()).all()
    avg_rating = db.session.query(db.func.avg(Review.rating)).filter_by(design_id=design_id).scalar() or 0
    
    is_liked = False
    if current_user.is_authenticated:
        is_liked = Wishlist.query.filter_by(user_id=current_user.id, design_id=design_id).first() is not None
    
    return render_template('gallery/view.html',
                         design=design,
                         reviews=reviews,
                         avg_rating=avg_rating,
                         is_liked=is_liked)
