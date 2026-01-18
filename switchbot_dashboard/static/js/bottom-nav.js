/**
 * Bottom Navigation Bar functionality
 * Handles mobile navigation interactions and scroll-based hiding/showing
 */
(function() {
  'use strict';
  
  class BottomNavigation {
    constructor() {
      this.nav = document.querySelector('.sb-bottom-nav');
      this.lastScrollY = window.scrollY;
      this.scrollThreshold = 100;
      this.isTicking = false;
      
      if (this.nav) {
        this.init();
      }
    }
    
    init() {
      this.bindEvents();
      this.updateActiveState();
      this.setupPerformanceOptimizations();
    }
    
    bindEvents() {
      // Handle scroll events with throttling
      let scrollTimer;
      window.addEventListener('scroll', () => {
        if (!scrollTimer) {
          scrollTimer = setTimeout(() => {
            this.handleScroll();
            scrollTimer = null;
          }, 16); // ~60fps
        }
      }, { passive: true });
      
      // Handle navigation clicks
      this.nav.addEventListener('click', (e) => {
        const link = e.target.closest('.sb-bottom-nav-item');
        if (link) {
          this.handleNavClick(link, e);
        }
      });
      
      // Handle resize events
      window.addEventListener('resize', this.debounce(() => {
        this.updateActiveState();
      }, 250));
    }
    
    handleScroll() {
      const currentScrollY = window.scrollY;
      const scrollDelta = Math.abs(currentScrollY - this.lastScrollY);
      
      if (scrollDelta > this.scrollThreshold) {
        if (currentScrollY > this.lastScrollY && currentScrollY > 100) {
          // Scrolling down - hide nav
          this.hideNav();
        } else {
          // Scrolling up - show nav
          this.showNav();
        }
        this.lastScrollY = currentScrollY;
      }
    }
    
    handleNavClick(link, event) {
      // Add visual feedback
      link.style.transform = 'scale(0.95)';
      setTimeout(() => {
        link.style.transform = '';
      }, 150);
      
      // Update active state immediately for better UX
      this.updateActiveState(link);
    }
    
    hideNav() {
      if (!this.nav.classList.contains('sb-bottom-nav--hidden')) {
        this.nav.classList.add('sb-bottom-nav--hidden');
      }
    }
    
    showNav() {
      if (this.nav.classList.contains('sb-bottom-nav--hidden')) {
        this.nav.classList.remove('sb-bottom-nav--hidden');
      }
    }
    
    updateActiveState(clickedLink = null) {
      const currentPath = window.location.pathname;
      const links = this.nav.querySelectorAll('.sb-bottom-nav-item');
      
      links.forEach(link => {
        const href = link.getAttribute('href');
        const isActive = clickedLink === link || 
                       (href === currentPath) ||
                       (href === '/' && currentPath === '/');
        
        if (isActive) {
          link.classList.add('sb-bottom-nav-item--active');
          link.setAttribute('aria-current', 'page');
        } else {
          link.classList.remove('sb-bottom-nav-item--active');
          link.removeAttribute('aria-current');
        }
      });
    }
    
    setupPerformanceOptimizations() {
      // Add will-change for smooth animations
      this.nav.style.willChange = 'transform';
      
      // Enable GPU acceleration
      this.nav.style.transform = 'translateZ(0)';
      
      // Use Intersection Observer for lazy loading if needed
      if ('IntersectionObserver' in window) {
        const observer = new IntersectionObserver((entries) => {
          entries.forEach(entry => {
            if (entry.isIntersecting) {
              this.nav.style.opacity = '1';
            }
          });
        }, { threshold: 0.1 });
        
        observer.observe(this.nav);
      }
    }
    
    debounce(func, wait) {
      let timeout;
      return function executedFunction(...args) {
        const later = () => {
          clearTimeout(timeout);
          func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
      };
    }
  }
  
  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
      new BottomNavigation();
    });
  } else {
    new BottomNavigation();
  }
})();
