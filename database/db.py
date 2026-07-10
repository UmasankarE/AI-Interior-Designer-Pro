from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db():
    """Initialize database"""
    from database.models import User, Admin, Design, Category, Booking, Recommendation, ChatHistory, GeneratedImage, Wishlist, Review, Notification
    db.create_all()
    print("Database initialized successfully!")
