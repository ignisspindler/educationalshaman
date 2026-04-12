// EducationalShaman.com - Main JavaScript

document.addEventListener('DOMContentLoaded', () => {
  initNavigation();
  initScrollEffects();
  initTestimonials();
  initContactForm();
});

// Navigation
function initNavigation() {
  const nav = document.getElementById('nav');
  const navToggle = document.getElementById('navToggle');
  const navLinks = document.getElementById('navLinks');
  
  // Scroll effect
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      nav.classList.add('scrolled');
    } else {
      nav.classList.remove('scrolled');
    }
  });
  
  // Mobile toggle
  navToggle.addEventListener('click', () => {
    navLinks.classList.toggle('active');
  });
  
  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        const offsetTop = target.offsetTop - 80;
        window.scrollTo({
          top: offsetTop,
          behavior: 'smooth'
        });
        // Close mobile menu
        navLinks.classList.remove('active');
      }
    });
  });
}

// Scroll animations
function initScrollEffects() {
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };
  
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, index) => {
      if (entry.isIntersecting) {
        setTimeout(() => {
          entry.target.classList.add('visible');
        }, index * 80);
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);
  
  // Observe elements
  document.querySelectorAll('.journey-step, .service-card, .testimonial').forEach(el => {
    el.classList.add('fade-up');
    observer.observe(el);
  });
}

// Testimonials carousel
function initTestimonials() {
  const track = document.getElementById('testimonialTrack');
  const dotsContainer = document.getElementById('testimonialDots');
  const testimonials = track.querySelectorAll('.testimonial');
  
  if (!testimonials.length) return;
  
  // Create dots
  testimonials.forEach((_, index) => {
    const dot = document.createElement('button');
    dot.setAttribute('aria-label', `Go to testimonial ${index + 1}`);
    if (index === 0) dot.classList.add('active');
    dot.addEventListener('click', () => goToSlide(index));
    dotsContainer.appendChild(dot);
  });
  
  let currentIndex = 0;
  let autoplayInterval;
  
  function goToSlide(index) {
    currentIndex = index;
    track.style.transform = `translateX(-${index * 100}%)`;
    
    // Update dots
    dotsContainer.querySelectorAll('button').forEach((dot, i) => {
      dot.classList.toggle('active', i === index);
    });
  }
  
  function nextSlide() {
    const next = (currentIndex + 1) % testimonials.length;
    goToSlide(next);
  }
  
  // Autoplay
  function startAutoplay() {
    autoplayInterval = setInterval(nextSlide, 5000);
  }
  
  function stopAutoplay() {
    clearInterval(autoplayInterval);
  }
  
  track.addEventListener('mouseenter', stopAutoplay);
  track.addEventListener('mouseleave', startAutoplay);
  
  startAutoplay();
}

// Contact form
function initContactForm() {
  const form = document.getElementById('contactForm');
  const success = document.getElementById('formSuccess');
  
  if (!form) return;
  
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    
    // Collect form data
    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());
    
    // Log for now (in production, send to backend/email service)
    console.log('Form submitted:', data);
    
    // Show success
    form.style.display = 'none';
    success.style.display = 'block';
    
    // Reset for new submissions
    form.reset();
  });
}

// Smooth reveal on page load
window.addEventListener('load', () => {
  document.body.classList.add('loaded');
});

// Add loaded class for entrance animations
document.body.classList.add('loading');