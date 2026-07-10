// Initialize AOS
AOS.init({
    duration: 1000,
    once: true,
    offset: 100
});

// Smooth scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});

// Add active class to navbar links on scroll
const navbarLinks = document.querySelectorAll('.navbar-nav .nav-link');

window.addEventListener('scroll', () => {
    let current = '';
    const sections = document.querySelectorAll('section');
    
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        if (pageYOffset >= sectionTop - 200) {
            current = section.getAttribute('id');
        }
    });
    
    navbarLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href').slice(1) === current) {
            link.classList.add('active');
        }
    });
});

// Scroll to top button
const scrollButton = document.createElement('button');
scrollButton.innerHTML = '<i class="fas fa-arrow-up"></i>';
scrollButton.className = 'btn btn-primary rounded-circle';
scrollButton.style.cssText = 'position: fixed; bottom: 20px; right: 20px; display: none; z-index: 99; width: 50px; height: 50px; padding: 0;';
scrollButton.id = 'scrollTop';
document.body.appendChild(scrollButton);

window.addEventListener('scroll', () => {
    if (window.pageYOffset > 300) {
        scrollButton.style.display = 'flex';
        scrollButton.style.alignItems = 'center';
        scrollButton.style.justifyContent = 'center';
    } else {
        scrollButton.style.display = 'none';
    }
});

scrollButton.addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});

// Form validation
const forms = document.querySelectorAll('form');
forms.forEach(form => {
    form.addEventListener('submit', function(e) {
        if (!this.checkValidity()) {
            e.preventDefault();
            e.stopPropagation();
        }
        this.classList.add('was-validated');
    });
});

// Counter animation
function animateCounter(element, target, duration = 2000) {
    let current = 0;
    const increment = target / (duration / 16);
    const timer = setInterval(() => {
        current += increment;
        if (current >= target) {
            element.textContent = target.toLocaleString();
            clearInterval(timer);
        } else {
            element.textContent = Math.floor(current).toLocaleString();
        }
    }, 16);
}

// Intersection Observer for counter animation
const observerOptions = {
    threshold: 0.5
};

const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting && !entry.target.dataset.animated) {
            const counters = entry.target.querySelectorAll('[data-count-up]');
            counters.forEach(counter => {
                const target = parseInt(counter.getAttribute('data-count-up'));
                animateCounter(counter, target);
            });
            entry.target.dataset.animated = 'true';
        }
    });
}, observerOptions);

const statisticsSection = document.querySelector('.statistics-section');
if (statisticsSection) {
    observer.observe(statisticsSection);
}

// Toast notifications
function showToast(message, type = 'info') {
    const toast = document.createElement('div');
    toast.className = `alert alert-${type} alert-dismissible fade show`;
    toast.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    document.body.insertBefore(toast, document.body.firstChild);
    
    setTimeout(() => {
        toast.remove();
    }, 3000);
}

// AJAX form submission
const ajaxForms = document.querySelectorAll('[data-ajax]');
ajaxForms.forEach(form => {
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        const formData = new FormData(this);
        const url = this.getAttribute('action');
        const method = this.getAttribute('method') || 'POST';
        
        try {
            const response = await fetch(url, {
                method: method,
                body: formData
            });
            
            if (response.ok) {
                showToast('Success!', 'success');
                this.reset();
                if (this.hasAttribute('data-redirect')) {
                    window.location.href = this.getAttribute('data-redirect');
                }
            } else {
                showToast('Error occurred', 'danger');
            }
        } catch (error) {
            console.error('Error:', error);
            showToast('Error occurred', 'danger');
        }
    });
});

// Lazy loading images
if ('IntersectionObserver' in window) {
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });
    
    document.querySelectorAll('img.lazy').forEach(img => imageObserver.observe(img));
}
