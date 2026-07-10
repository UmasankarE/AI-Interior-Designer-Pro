from database.models import Design, Review
from database.db import db
from sqlalchemy import func

class RecommendationEngine:
    def __init__(self):
        pass
    
    def get_recommendations(self, room_type="", budget=0, colour="", style="", furniture_type=""):
        """Get design recommendations based on user preferences"""
        query = Design.query.filter_by(is_active=True)
        
        if room_type:
            query = query.filter_by(room_type=room_type)
        
        if style:
            query = query.filter_by(style=style)
        
        if budget > 0:
            query = query.filter(Design.price <= budget)
        
        if colour:
            query = query.filter(Design.wall_colour.ilike(f'%{colour}%'))
        
        designs = query.all()
        
        # Score designs
        recommendations = []
        for design in designs:
            score = self.calculate_score(design, budget, colour, style)
            
            # Get average rating
            avg_rating = db.session.query(func.avg(Review.rating)).filter_by(design_id=design.id).scalar() or 0
            score += avg_rating * 0.2  # Add 20% weight to rating
            
            recommendations.append({
                'design_id': design.id,
                'title': design.title,
                'image_url': design.image_url,
                'price': design.price,
                'score': round(score, 2),
                'reason': self.get_reason(design, budget, colour, style)
            })
        
        # Sort by score
        recommendations.sort(key=lambda x: x['score'], reverse=True)
        
        return recommendations[:6]  # Return top 6 recommendations
    
    def calculate_score(self, design, budget=0, colour="", style=""):
        """Calculate recommendation score"""
        score = 0.0
        
        # Budget matching
        if budget > 0 and design.price:
            if design.price <= budget:
                score += (1 - (design.price / budget)) * 40
            else:
                score -= 20
        
        # Style matching
        if style and design.style and design.style.lower() == style.lower():
            score += 30
        
        # Colour matching
        if colour and design.wall_colour and colour.lower() in design.wall_colour.lower():
            score += 20
        
        # Popularity
        score += min(design.views_count / 100, 10)
        
        return score
    
    def get_reason(self, design, budget=0, colour="", style=""):
        """Generate recommendation reason"""
        reasons = []
        
        if style and design.style:
            reasons.append(f"Matches your {design.style} style preference")
        
        if budget > 0 and design.price and design.price <= budget:
            reasons.append(f"Within your budget of ₹{budget:,.0f}")
        
        if colour and design.wall_colour:
            reasons.append(f"Features {design.wall_colour} wall colour you like")
        
        if design.views_count > 100:
            reasons.append("Popular with other users")
        
        return ". ".join(reasons) if reasons else "Recommended for you"
