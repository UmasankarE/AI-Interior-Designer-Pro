from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash
from flask_login import login_required, current_user
from database.db import db
from database.models import Design, Recommendation, Category
from ai.recommendation_engine import RecommendationEngine

bp = Blueprint('recommendations', __name__, url_prefix='/recommendations')

@bp.route('/')
@login_required
def index():
    """AI Recommendations"""
    return render_template('recommendations/index.html')

@bp.route('/get-recommendations', methods=['POST'])
@login_required
def get_recommendations():
    """Get AI recommendations"""
    room_type = request.form.get('room_type', '').strip()
    budget = request.form.get('budget', type=float)
    colour = request.form.get('colour', '').strip()
    style = request.form.get('style', '').strip()
    furniture_type = request.form.get('furniture_type', '').strip()
    
    if not all([room_type, budget, style]):
        return jsonify({'error': 'Missing required fields'}), 400
    
    # Get recommendations using AI engine
    engine = RecommendationEngine()
    recommendations = engine.get_recommendations(
        room_type=room_type,
        budget=budget,
        colour=colour,
        style=style,
        furniture_type=furniture_type
    )
    
    # Save recommendations
    for rec in recommendations:
        recommendation = Recommendation(
            user_id=current_user.id,
            design_id=rec['design_id'],
            room_type=room_type,
            style=style,
            budget=budget,
            colour_preference=colour,
            furniture_type=furniture_type,
            score=rec['score'],
            reason=rec['reason']
        )
        db.session.add(recommendation)
    
    db.session.commit()
    
    return render_template('recommendations/results.html', recommendations=recommendations)

@bp.route('/cost-estimation', methods=['GET', 'POST'])
@login_required
def cost_estimation():
    """AI Cost Estimation"""
    if request.method == 'POST':
        room_size = request.form.get('room_size', type=float)
        material = request.form.get('material', '').strip()
        furniture = request.form.get('furniture', '').strip()
        electrical = request.form.get('electrical', type=float)
        painting = request.form.get('painting', type=float)
        labour = request.form.get('labour', type=float)
        tax = request.form.get('tax', type=float)
        discount = request.form.get('discount', type=float)
        
        # Calculate total cost
        total = (room_size or 0) + (electrical or 0) + (painting or 0) + (labour or 0)
        total = total * (1 + (tax or 0) / 100)
        total = total * (1 - (discount or 0) / 100)
        
        return jsonify({
            'total_cost': total,
            'breakdown': {
                'material': room_size or 0,
                'electrical': electrical or 0,
                'painting': painting or 0,
                'labour': labour or 0,
                'tax': (total - (total / (1 + (tax or 0) / 100))) if tax else 0,
                'discount': (total / (1 - (discount or 0) / 100) - total) if discount else 0
            }
        })
    
    return render_template('recommendations/cost_estimation.html')
