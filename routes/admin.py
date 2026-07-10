from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from database.db import db
from database.models import User, Design, Category, Review, Booking, Admin
from functools import wraps

bp = Blueprint('admin', __name__, url_prefix='/admin')

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not isinstance(current_user, Admin):
            flash('Access denied', 'danger')
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    return decorated_function

@bp.route('/')
@login_required
@admin_required
def dashboard():
    """Admin dashboard"""
    total_users = User.query.count()
    total_designs = Design.query.count()
    total_bookings = Booking.query.count()
    total_reviews = Review.query.count()
    
    return render_template('admin/dashboard.html',
                         total_users=total_users,
                         total_designs=total_designs,
                         total_bookings=total_bookings,
                         total_reviews=total_reviews)

@bp.route('/users')
@login_required
@admin_required
def manage_users():
    """Manage users"""
    page = request.args.get('page', 1, type=int)
    users = User.query.paginate(page=page, per_page=20)
    return render_template('admin/manage_users.html', users=users)

@bp.route('/designs')
@login_required
@admin_required
def manage_designs():
    """Manage designs"""
    page = request.args.get('page', 1, type=int)
    designs = Design.query.paginate(page=page, per_page=20)
    return render_template('admin/manage_designs.html', designs=designs)

@bp.route('/categories')
@login_required
@admin_required
def manage_categories():
    """Manage categories"""
    page = request.args.get('page', 1, type=int)
    categories = Category.query.paginate(page=page, per_page=20)
    return render_template('admin/manage_categories.html', categories=categories)

@bp.route('/reviews')
@login_required
@admin_required
def manage_reviews():
    """Manage reviews"""
    page = request.args.get('page', 1, type=int)
    reviews = Review.query.paginate(page=page, per_page=20)
    return render_template('admin/manage_reviews.html', reviews=reviews)

@bp.route('/bookings')
@login_required
@admin_required
def manage_bookings():
    """Manage bookings"""
    page = request.args.get('page', 1, type=int)
    bookings = Booking.query.paginate(page=page, per_page=20)
    return render_template('admin/manage_bookings.html', bookings=bookings)
