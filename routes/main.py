from flask import Blueprint, render_template
from database.models import Design, Category, Review

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    """Home page"""
    featured_designs = Design.query.filter_by(is_featured=True, is_active=True).limit(6).all()
    categories = Category.query.filter_by(is_active=True).all()
    recent_designs = Design.query.filter_by(is_active=True).order_by(Design.created_at.desc()).limit(8).all()
    
    return render_template('index.html', 
                         featured_designs=featured_designs,
                         categories=categories,
                         recent_designs=recent_designs)

@bp.route('/about')
def about():
    """About page"""
    return render_template('about.html')

@bp.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page"""
    if request.method == 'POST':
        # Handle contact form
        pass
    return render_template('contact.html')

@bp.route('/features')
def features():
    """Features page"""
    return render_template('features.html')
