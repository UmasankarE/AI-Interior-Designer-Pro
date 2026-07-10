# AI Interior Designer Pro

## Overview

**AI Interior Designer Pro** is a production-ready Full Stack web application that leverages Artificial Intelligence to provide personalized interior design recommendations, cost estimations, and AI-generated design visualizations.

## 🎯 Key Features

### Phase 1: Frontend
- ✅ Modern responsive HTML5/CSS3 UI
- ✅ Bootstrap 5 framework
- ✅ Glassmorphism design elements
- ✅ Dark mode toggle
- ✅ Smooth animations (AOS, Swiper.js)
- ✅ Fully functional dashboard
- ✅ Design gallery with filters
- ✅ User wishlist system
- ✅ Booking management
- ✅ Admin panel

### Phase 2: Backend
- ✅ Flask framework with Blueprints
- ✅ SQLAlchemy ORM
- ✅ MySQL database
- ✅ User authentication
- ✅ Session management
- ✅ Password hashing (bcrypt)
- ✅ Email verification
- ✅ REST API
- ✅ Admin panel

### Phase 3: AI Integration
- ✅ OpenAI/Gemini API chatbot
- ✅ AI-powered recommendations
- ✅ Cost estimation engine
- ✅ Stable Diffusion image generation
- ✅ Prompt engineering
- ✅ ML recommendation system

### Phase 4: Deployment
- ✅ Docker containerization
- ✅ Deployment-ready configuration
- ✅ Comprehensive documentation
- ✅ Installation guide
- ✅ User manual

## 📁 Project Structure

```
AI-Interior-Designer-Pro/
├── app.py                      # Main Flask application
├── config.py                   # Configuration settings
├── requirements.txt            # Python dependencies
├── .env.example               # Environment variables template
├── Dockerfile                 # Docker configuration
├── setup.sh                   # Setup script
├── README.md                  # Project documentation
│
├── database/
│   ├── __init__.py
│   ├── db.py                 # Database initialization
│   ├── models.py             # SQLAlchemy models
│   ├── schema.sql            # MySQL schema
│   └── sample_data.sql       # Sample data
│
├── routes/
│   ├── __init__.py
│   ├── main.py               # Home and main routes
│   ├── auth.py               # Authentication routes
│   ├── dashboard.py          # User dashboard
│   ├── gallery.py            # Design gallery
│   ├── design.py             # Design details
│   ├── recommendations.py    # AI recommendations
│   ├── admin.py              # Admin panel
│   └── api.py                # REST API endpoints
│
├── ai/
│   ├── __init__.py
│   ├── chatbot.py            # AI chatbot
│   ├── recommendation_engine.py
│   ├── cost_estimator.py
│   └── image_generator.py
│
├── static/
│   ├── css/
│   │   ├── style.css         # Main styles
│   │   └── dark-mode.css     # Dark mode styles
│   ├── js/
│   │   ├── main.js           # Main JavaScript
│   │   └── dark-mode.js      # Dark mode toggle
│   ├── images/               # Static images
│   └── uploads/              # User uploads
│
├── templates/
│   ├── base.html             # Base template
│   ├── index.html            # Home page
│   ├── auth/
│   │   ├── login.html
│   │   ├── register.html
│   │   └── forgot_password.html
│   ├── dashboard/
│   │   ├── index.html
│   │   ├── profile.html
│   │   ├── wishlist.html
│   │   └── bookings.html
│   ��── gallery/
│   │   ├── index.html
│   │   └── view.html
│   ├── design/
│   │   ├── detail.html
│   │   └── booking.html
│   ├── recommendations/
│   │   ├── index.html
│   │   ├── results.html
│   │   └── cost_estimation.html
│   ├── admin/
│   │   ├── dashboard.html
│   │   ├── manage_users.html
│   │   └── manage_designs.html
│   └── errors/
│       ├── 404.html
│       └── 500.html
│
├── docs/
│   ├── API_DOCUMENTATION.md
│   ├── INSTALLATION_GUIDE.md
│   ├── USER_MANUAL.md
│   └── DEPLOYMENT.md
│
└── presentation/
    └── project_presentation.pptx
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- MySQL 5.7+
- pip package manager
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/UmasankarE/AI-Interior-Designer-Pro.git
   cd AI-Interior-Designer-Pro
   ```

2. **Run setup script**
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

3. **Configure environment**
   ```bash
   nano .env
   ```
   Add your API keys and database configuration

4. **Setup database**
   ```bash
   mysql -u root -p < database/schema.sql
   mysql -u root -p ai_interior_designer < database/sample_data.sql
   ```

5. **Run application**
   ```bash
   python app.py
   ```

   Access at `http://localhost:5000`

## 🔧 Technology Stack

### Frontend
- HTML5, CSS3, JavaScript ES6
- Bootstrap 5
- AOS (Animate On Scroll)
- Swiper.js
- Font Awesome

### Backend
- Python 3
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Flask-Mail

### Database
- MySQL
- SQLAlchemy ORM

### AI/ML
- OpenAI API / Google Gemini
- Stable Diffusion API
- HuggingFace API

### Deployment
- Docker
- Render / Railway
- GitHub

## 📖 Documentation

Detailed documentation is available in the `docs/` folder:

- [API Documentation](docs/API_DOCUMENTATION.md)
- [Installation Guide](docs/INSTALLATION_GUIDE.md)
- [User Manual](docs/USER_MANUAL.md)
- [Deployment Guide](docs/DEPLOYMENT.md)

## 🔐 Security Features

- Password hashing with bcrypt
- Session management
- CSRF protection
- Input validation
- SQL injection prevention (SQLAlchemy ORM)
- XSS protection
- Email verification
- Forgot password with OTP

## 📊 Database Schema

- **users**: User accounts
- **admins**: Admin accounts
- **categories**: Design categories
- **designs**: Interior designs
- **wishlists**: User wishlists
- **reviews**: Design reviews
- **bookings**: Booking requests
- **recommendations**: AI recommendations
- **chat_histories**: AI chatbot history
- **generated_images**: AI generated images
- **notifications**: User notifications

## 🤖 AI Features

### AI Chatbot
- Interior design advice
- Decoration tips
- Furniture suggestions
- Color recommendations
- Natural language processing

### AI Recommendations
- Personalized design suggestions
- Budget analysis
- Style matching
- Color recommendations
- Material suggestions

### Cost Estimation
- Material cost calculation
- Labor estimation
- Tax calculation
- Discount application
- PDF report generation

### Image Generation
- Text-to-image generation
- Style-based variations
- Room type customization
- Download capability

## 📝 Modules Overview

### Phase 1: Frontend (Modules 1-6)
1. **Module 1**: Modern home page with hero section, features, gallery
2. **Module 2**: Login & Registration with glassmorphism
3. **Module 3**: User dashboard with statistics
4. **Module 4**: Design gallery with search & filters
5. **Module 5**: Design details page with reviews
6. **Module 6**: AI recommendation interface

### Phase 2: Backend (Modules 7-10)
7. **Module 7**: Flask setup with MVC architecture
8. **Module 8**: MySQL database with relationships
9. **Module 9**: Authentication system
10. **Module 10**: Admin panel

### Phase 3: AI Integration (Modules 11-14)
11. **Module 11**: AI Chatbot
12. **Module 12**: AI Recommendation Engine
13. **Module 13**: AI Cost Estimation
14. **Module 14**: AI Image Generator

### Phase 4: Deployment (Modules 15-17)
15. **Module 15**: Docker & Deployment
16. **Module 16**: Documentation
17. **Module 17**: Final Testing & Optimization

## 🧪 Testing

The application includes:
- Form validation
- Input sanitization
- Error handling
- API testing

## 📱 Responsive Design

Fully responsive across:
- Desktop (1920px and above)
- Laptop (1024px - 1919px)
- Tablet (768px - 1023px)
- Mobile (320px - 767px)

## 🎨 UI/UX Features

- Glassmorphism cards
- Gradient backgrounds
- Smooth animations
- Dark mode support
- Intuitive navigation
- Professional icons
- Interactive charts
- Loading states

## 🚢 Deployment Options

### Render
```bash
railway link
railway up
```

### Railway
```bash
railway login
railway up
```

### Docker
```bash
docker build -t ai-interior-designer .
docker run -p 5000:5000 ai-interior-designer
```

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📞 Support

For support, email support@aiinteriordesigner.com or create an issue on GitHub.

## 👨‍💻 Author

**Umasankar E**
- GitHub: [@UmasankarE](https://github.com/UmasankarE)
- Portfolio: [Your Portfolio]

## 🙏 Acknowledgments

- Bootstrap for CSS framework
- OpenAI for AI capabilities
- Flask community for excellent documentation
- All contributors and testers

---

**Built with ❤️ by Umasankar E**

Made with AI-powered interior design solutions for modern homes and businesses.
