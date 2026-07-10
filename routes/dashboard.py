from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash
from flask_login import login_required, current_user
from database.db import db
from database.models import Design, Wishlist, Review, Notification, ChatHistory, GeneratedImage, Recommendation, Booking
from sqlalchemy import func

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('/')
@login_required
def index():
    """User dashboard"""
    # Statistics
    wishlist_count = Wishlist.query.filter_by(user_id=current_user.id).count()
    bookings_count = Booking.query.filter_by(user_id=current_user.id).count()
    generated_images_count = GeneratedImage.query.filter_by(user_id=current_user.id).count()
    
    # Recent activities
    recent_wishlists = Wishlist.query.filter_by(user_id=current_user.id).order_by(Wishlist.created_at.desc()).limit(5).all()
    recent_generated = GeneratedImage.query.filter_by(user_id=current_user.id).order_by(GeneratedImage.created_at.desc()).limit(5).all()
    recent_bookings = Booking.query.filter_by(user_id=current_user.id).order_by(Booking.created_at.desc()).limit(5).all()
    
    # Notifications
    notifications = Notification.query.filter_by(user_id=current_user.id, is_read=False).order_by(Notification.created_at.desc()).limit(10).all()
    
    return render_template('dashboard/index.html',
                         wishlist_count=wishlist_count,
                         bookings_count=bookings_count,
                         generated_images_count=generated_images_count,
                         recent_wishlists=recent_wishlists,
                         recent_generated=recent_generated,
                         recent_bookings=recent_bookings,
                         notifications=notifications)

@bp.route('/profile')
@login_required
def profile():
    """User profile"""
    return render_template('dashboard/profile.html', user=current_user)

@bp.route('/profile/update', methods=['POST'])
@login_required
def update_profile():
    """Update user profile"""
    current_user.first_name = request.form.get('first_name', '').strip()
    current_user.last_name = request.form.get('last_name', '').strip()
    current_user.phone = request.form.get('phone', '').strip()
    current_user.bio = request.form.get('bio', '').strip()
    current_user.address = request.form.get('address', '').strip()
    current_user.city = request.form.get('city', '').strip()
    current_user.state = request.form.get('state', '').strip()
    current_user.country = request.form.get('country', '').strip()
    current_user.zip_code = request.form.get('zip_code', '').strip()
    
    db.session.commit()
    flash('Profile updated successfully', 'success')
    return redirect(url_for('dashboard.profile'))

@bp.route('/wishlist')
@login_required
def wishlist():
    """User wishlist"""
    page = request.args.get('page', 1, type=int)
    wishlists = Wishlist.query.filter_by(user_id=current_user.id).paginate(page=page, per_page=12)
    return render_template('dashboard/wishlist.html', wishlists=wishlists)

@bp.route('/bookings')
@login_required
def bookings():
    """User bookings"""
    page = request.args.get('page', 1, type=int)
    bookings = Booking.query.filter_by(user_id=current_user.id).order_by(Booking.created_at.desc()).paginate(page=page, per_page=10)
    return render_template('dashboard/bookings.html', bookings=bookings)

@bp.route('/generated-images')
@login_required
def generated_images():
    """User generated images"""
    page = request.args.get('page', 1, type=int)
    images = GeneratedImage.query.filter_by(user_id=current_user.id).order_by(GeneratedImage.created_at.desc()).paginate(page=page, per_page=12)
    return render_template('dashboard/generated_images.html', images=images)

@bp.route('/recommendations')
@login_required
def recommendations():
    """User recommendations"""
    page = request.args.get('page', 1, type=int)
    recommendations = Recommendation.query.filter_by(user_id=current_user.id).order_by(Recommendation.created_at.desc()).paginate(page=page, per_page=12)
    return render_template('dashboard/recommendations.html', recommendations=recommendations)

@bp.route('/notifications')
@login_required
def notifications():
    """User notifications"""
    page = request.args.get('page', 1, type=int)
    notifications = Notification.query.filter_by(user_id=current_user.id).order_by(Notification.created_at.desc()).paginate(page=page, per_page=20)
    return render_template('dashboard/notifications.html', notifications=notifications)

@bp.route('/chat-history')
@login_required
def chat_history():
    """Chat history"""
    page = request.args.get('page', 1, type=int)
    chats = ChatHistory.query.filter_by(user_id=current_user.id).order_by(ChatHistory.created_at.desc()).paginate(page=page, per_page=20)
    return render_template('dashboard/chat_history.html', chats=chats)
