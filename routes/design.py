from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash
from flask_login import login_required, current_user
from database.db import db
from database.models import Design, Review, Wishlist, Booking

bp = Blueprint('design', __name__, url_prefix='/design')

@bp.route('/<int:design_id>')
def detail(design_id):
    """Design detail page"""
    design = Design.query.get_or_404(design_id)
    
    # Increment views
    design.views_count += 1
    db.session.commit()
    
    # Get reviews
    reviews = Review.query.filter_by(design_id=design_id).order_by(Review.created_at.desc()).all()
    avg_rating = db.session.query(db.func.avg(Review.rating)).filter_by(design_id=design_id).scalar() or 0
    review_count = len(reviews)
    
    is_liked = False
    user_review = None
    if current_user.is_authenticated:
        is_liked = Wishlist.query.filter_by(user_id=current_user.id, design_id=design_id).first() is not None
        user_review = Review.query.filter_by(user_id=current_user.id, design_id=design_id).first()
    
    # Related designs
    related = Design.query.filter_by(
        category_id=design.category_id,
        is_active=True
    ).filter(Design.id != design_id).limit(4).all()
    
    return render_template('design/detail.html',
                         design=design,
                         reviews=reviews,
                         avg_rating=avg_rating,
                         review_count=review_count,
                         is_liked=is_liked,
                         user_review=user_review,
                         related=related)

@bp.route('/<int:design_id>/review', methods=['POST'])
@login_required
def add_review(design_id):
    """Add review to design"""
    design = Design.query.get_or_404(design_id)
    
    rating = request.form.get('rating', type=int)
    comment = request.form.get('comment', '').strip()
    
    if not rating or rating < 1 or rating > 5:
        flash('Invalid rating', 'danger')
        return redirect(url_for('design.detail', design_id=design_id))
    
    # Check if review exists
    review = Review.query.filter_by(user_id=current_user.id, design_id=design_id).first()
    
    if review:
        review.rating = rating
        review.comment = comment
    else:
        review = Review(
            user_id=current_user.id,
            design_id=design_id,
            rating=rating,
            comment=comment
        )
        db.session.add(review)
    
    db.session.commit()
    flash('Review submitted successfully', 'success')
    return redirect(url_for('design.detail', design_id=design_id))

@bp.route('/<int:design_id>/booking', methods=['GET', 'POST'])
@login_required
def create_booking(design_id):
    """Create booking"""
    design = Design.query.get_or_404(design_id)
    
    if request.method == 'POST':
        booking_date = request.form.get('booking_date')
        description = request.form.get('description', '').strip()
        
        if not booking_date:
            flash('Booking date is required', 'danger')
            return redirect(url_for('design.create_booking', design_id=design_id))
        
        booking = Booking(
            user_id=current_user.id,
            design_id=design_id,
            booking_date=booking_date,
            description=description,
            total_cost=design.price
        )
        db.session.add(booking)
        db.session.commit()
        
        flash('Booking created successfully', 'success')
        return redirect(url_for('dashboard.bookings'))
    
    return render_template('design/booking.html', design=design)

@bp.route('/<int:design_id>/download')
@login_required
def download_design(design_id):
    """Download design details as PDF"""
    design = Design.query.get_or_404(design_id)
    # PDF generation logic
    flash('Download started', 'success')
    return redirect(url_for('design.detail', design_id=design_id))
