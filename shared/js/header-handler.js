/**
 * Header and navigation handler
 * Handles sticky header, mobile menu toggle, and dropdown menus
 * Optimized for performance and SEO
 */
(function() {
  'use strict';

  // --- Sticky header shadow on scroll ---
  var header = document.getElementById('site-header');
  if (header) {
    window.addEventListener('scroll', function() {
      header.classList.toggle('scrolled', window.scrollY > 10);
    }, { passive: true });
  }

  // --- Mobile nav toggle ---
  var hamburger = document.getElementById('hamburger');
  var mobileNav = document.getElementById('mobile-nav');
  var mobileNavClose = document.getElementById('mobile-nav-close');

  function closeMobileNav() {
    hamburger.classList.remove('active');
    hamburger.setAttribute('aria-expanded', 'false');
    mobileNav.hidden = true;
    mobileNav.classList.remove('open');
    document.body.style.overflow = '';
  }

  if (hamburger && mobileNav) {
    hamburger.addEventListener('click', function() {
      var isOpen = hamburger.classList.toggle('active');
      hamburger.setAttribute('aria-expanded', isOpen);
      mobileNav.hidden = !isOpen;
      mobileNav.classList.toggle('open', isOpen);
      document.body.style.overflow = isOpen ? 'hidden' : '';
    });

    // Close mobile nav on link click
    mobileNav.querySelectorAll('a').forEach(function(link) {
      link.addEventListener('click', function() {
        closeMobileNav();
      });
    });

    // Close mobile nav on close button click
    if (mobileNavClose) {
      mobileNavClose.addEventListener('click', function() {
        closeMobileNav();
      });
    }
  }

  // --- Dropdown menu management with hover delay ---
  var navItems = document.querySelectorAll('.nav-item');
  navItems.forEach(function(item) {
    var dropdownMenu = item.querySelector('.dropdown-menu');
    if (!dropdownMenu) return;

    // Store timeout per nav-item
    item.dropdownTimeout = null;

    item.addEventListener('mouseenter', function() {
      // Clear this item's close timeout
      if (item.dropdownTimeout) {
        clearTimeout(item.dropdownTimeout);
        item.dropdownTimeout = null;
      }

      // Close all other open menus
      navItems.forEach(function(otherItem) {
        if (otherItem !== item && otherItem.dropdownTimeout === null) {
          var otherMenu = otherItem.querySelector('.dropdown-menu');
          if (otherMenu && otherMenu.style.display === 'block') {
            otherMenu.style.display = 'none';
            otherMenu.style.opacity = '0';
            otherMenu.style.pointerEvents = 'none';
          }
        }
      });

      // Show this menu
      dropdownMenu.style.display = 'block';
      dropdownMenu.style.opacity = '1';
      dropdownMenu.style.pointerEvents = 'auto';
    });

    item.addEventListener('mouseleave', function() {
      item.dropdownTimeout = setTimeout(function() {
        dropdownMenu.style.display = 'none';
        dropdownMenu.style.opacity = '0';
        dropdownMenu.style.pointerEvents = 'none';
        item.dropdownTimeout = null;
      }, 150);
    });
  });

  // --- Scroll fade-in animations ---
  if ('IntersectionObserver' in window) {
    var observer = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('in-view');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

    document.querySelectorAll('.fade-up').forEach(function(el) {
      observer.observe(el);
    });
  } else {
    // Fallback for older browsers
    document.querySelectorAll('.fade-up').forEach(function(el) {
      el.classList.add('in-view');
    });
  }
})();
